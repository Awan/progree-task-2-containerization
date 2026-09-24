import os
import pwd
import shutil
import sys

SECRET_SOURCE = "/run/secrets/postgres_password"
SECRET_DEST = "/run/progree-secrets/postgres_password"
APP_USER = "appuser"


def main():
    if not os.path.isfile(SECRET_SOURCE):
        raise RuntimeError(f"Secret not found: {SECRET_SOURCE}")

    user = pwd.getpwnam(APP_USER)
    os.makedirs("/run/progree-secrets", mode=0o700, exist_ok=True)
    os.chown("/run/progree-secrets", user.pw_uid, user.pw_gid)

    shutil.copyfile(SECRET_SOURCE, SECRET_DEST)
    os.chown(SECRET_DEST, user.pw_uid, user.pw_gid)
    os.chmod(SECRET_DEST, 0o400)

    os.initgroups(APP_USER, user.pw_gid)
    os.setgid(user.pw_gid)
    os.setuid(user.pw_uid)

    os.execvp(sys.argv[1], sys.argv[1:])


if __name__ == "__main__":
    main()
