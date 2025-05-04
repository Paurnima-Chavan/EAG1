function analyzeQuery(query) {
  return {
    intent: query.includes("where") ? "find_location" : "search_info",
    keywords: query.toLowerCase().split(" "),
  };
}
