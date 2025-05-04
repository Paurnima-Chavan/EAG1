importScripts("memory.js", "perception.js", "decision.js");

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === "search_query") {
    const query = request.query;
    const perception = analyzeQuery(query); // optional NLP-like analysis
    const candidates = retrieveChunks(query); // from memory.js
    const best = decideMatch(query, candidates); // from decision.js

    // Only proceed if we found a good match
    if (best) {
      chrome.tabs.create({ url: best.url }, (newTab) => {
        // Wait until tab is ready, then send highlight text
        const sendHighlight = () => {
          chrome.tabs.sendMessage(newTab.id, {
            type: "highlight",
            text: best.text
          }, (response) => {
            // Retry if content script hasn't loaded yet
            if (chrome.runtime.lastError) {
              setTimeout(sendHighlight, 500);
            }
          });
        };

        // Initial delay before first attempt
        setTimeout(sendHighlight, 1500);
      });

      sendResponse({ message: `Found in ${best.url}` });

    } else {
      sendResponse({ message: "No match found." });
    }

    return true; // async response
  }
});
