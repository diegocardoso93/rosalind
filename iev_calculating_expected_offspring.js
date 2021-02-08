function calculateExpectedOffspring(couples) {
  return [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
    .map((k, i) => k * couples[i])
    .reduce((a, v) => a + v, 0) * 2;
}

console.log(calculateExpectedOffspring([19958, 17359, 19189, 18623, 16368, 18144]));

