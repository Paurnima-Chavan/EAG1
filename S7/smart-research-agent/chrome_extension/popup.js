document.getElementById("searchBtn").addEventListener("click", async () => {
  const query = document.getElementById("query").value;
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // Wait 500ms before sending the query
  setTimeout(() => {
    chrome.runtime.sendMessage({ type: "search_query", query }, (response) => {
      document.getElementById("result").textContent = response?.message || "No match found.";
    });
  }, 500);
});
