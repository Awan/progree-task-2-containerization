# syntax=docker/dockerfile:1
FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build


FROM nginx:alpine AS runtime

LABEL org.opencontainers.image.title="Progree Task 2 Frontend" \
      org.opencontainers.image.description="Production frontend for the Progree Internship Task 2 application containerization and asset optimization project." \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.authors="Muhammad Abdullah Khabir <abdullah@abdullah.support>" \
      org.opencontainers.image.url="https://github.com/Awan/progree-task-2-containerization" \
      org.opencontainers.image.source="https://github.com/Awan/progree-task-2-containerization" \
      org.opencontainers.image.documentation="https://github.com/Awan/progree-task-2-containerization/blob/main/README.md"

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
