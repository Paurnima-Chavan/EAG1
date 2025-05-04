let metadata = [];
let metadataLoaded = false;

fetch(chrome.runtime.getURL("metadata.json"))
  .then((res) => res.json())
  .then((data) => {
    metadata = data;
    metadataLoaded = true;
  });

function retrieveChunks(query) {
  if (!metadataLoaded) {
    console.warn("Metadata not loaded yet.");
    return [];
  }

  const words = query.toLowerCase().split(" ");
  return metadata.filter((m) => {
    const text = m.text.toLowerCase();
    return words.some((word) => text.includes(word));
  });
}
