function calculateProbability(k, m, n) {
    const total_population = k + m + n;
    return ((k ** 2 - k) + (2 * k * m) + (3 / 4 * (m ** 2 - m)) + (2* k * n) + (m * n))
    	/ (total_population ** 2 - total_population)
}

console.log(calculateProbability(2, 2, 2));

