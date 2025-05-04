const stopWords = new Set([
  "is", "the", "a", "an", "where", "what", "when", "how", "does", "do", "to", "of", "in", "on", "at", "by", "for", "and", "or"
]);

function decideMatch(query, candidates) {
  if (!candidates || candidates.length === 0) return null;

  const queryWords = query
    .toLowerCase()
    .split(/\W+/)
    .filter(word => !stopWords.has(word) && word.length > 2);

  const scored = candidates.map(c => {
    const text = c.text.toLowerCase();
    const wordMatches = queryWords.filter(qw => text.includes(qw)).length;
    const phraseMatch = text.includes(query.toLowerCase().trim());
    const score = wordMatches + (phraseMatch ? 5 : 0);
    return { ...c, score };
  });

  scored.sort((a, b) => b.score - a.score);

  // Reject if no meaningful match
  if (scored[0].score < 2) return null;

  return scored[0];
}
