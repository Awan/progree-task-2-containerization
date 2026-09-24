const button = document.querySelector("#health");
const result = document.querySelector("#result");

button.addEventListener("click", async () => {
  result.textContent = "Checking backend...";

  try {
    const response = await fetch("/api");
    const data = await response.json();
    result.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    result.textContent = `Backend request failed: ${error}`;
  }
});
