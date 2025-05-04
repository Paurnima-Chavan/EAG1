function normalizeQuotes(str) {
  return str
    .replace(/[‘’´`]/g, "'")
    .replace(/[“”]/g, '"');
}

function highlightText(textToFind) {
  const body = document.body;
  const walker = document.createTreeWalker(body, NodeFilter.SHOW_TEXT);

  const matchWords = normalizeQuotes(textToFind.trim().toLowerCase().split(" "));
  const firstFew = matchWords.slice(0, 5).join(" ");

  let node;
  while ((node = walker.nextNode())) {
    const nodeText = normalizeQuotes(node.nodeValue.toLowerCase());

    if (nodeText.includes(firstFew)) {
      const range = document.createRange();
      const startIndex = nodeText.indexOf(firstFew);
      range.setStart(node, startIndex);
      range.setEnd(node, startIndex + firstFew.length);

      const highlight = document.createElement("span");
      highlight.style.backgroundColor = "yellow";
      highlight.style.fontWeight = "bold";
      range.surroundContents(highlight);

      // ✅ Smooth scroll into view
      highlight.scrollIntoView({ behavior: "smooth", block: "center" });

      console.log("✅ Highlighted:", firstFew);
      return;
    }
  }

  console.warn("❌ Text not found:", firstFew);
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === "highlight") {
    highlightText(request.text);
  }
});
