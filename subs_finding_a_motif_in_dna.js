let sequence = 'CAGAAGTGATTGAAGTGAGCGGTGAAGTGACTCGAAGTGAGAACGCACGAACGGGAAGTGAGAAGTGACGGAAGTGACGAAGTGATTGAAGTGAGAAGTGATGTGAAGTGAAGGGAAGTGAGAAGTGATGGAAGTGATCCTGAAGTGAGGAAGTGAGATGAAGTGAGAAGTGAGAGCAGAAGTGAGGAAGTGACGAAGTGAGAAGTGATACGAAGTGAAGGAAGTGATGAACGCGGGAAGTGATTGGAGAAGTGATGACTTGAAGAAGTGAAAATCGAAGTGAGGCGCGAAGAAGTGAGAAGTGATGGAAGTGATCTGGAAGTGACAGAAGTGACGAAGTGAGAAGTGAACAAGGAAGTGACGACAAGGCTAGAAGTGAGGAAGTGAGAAGTGATGAAGTGAGAAGTGACGAAGTGAGAAGTGAAGAAGTGAGGGTGTGAAGTGACGAAGTGAGGAACATCGAAGTGAAGAAGTGAGAAGTGAGCGAAGTGAACAGAAGTGAGAAGTGAGAAGTGATTGCGAAGTGACACGAAGTGAGCTGGAAGTGACGAAGTGAGCGAAGTGAGAAGTGAAAGAAGTGAGGGAAGTGAGAAGTGAGAAGTGAGATGTCGAAGTGAGAAGTGATGAAGTGAAGAAGTGACTGAAGTGATTCGTCCCCGAAGTGAATTGGAAGTGACCAGAAGTGACGAAGTGATAGAAGTGAGGAAGTGAGAAGTGAGGAAGTGATAGAAGTGACTGAAACTGAGAAGTGAAAGAGAAGTGACGGAAGTGATGAAGTGAGGAAGTGACGAAGTGA';
let needle = 'GAAGTGAGA';
let match = [];

for (let x = 0; x < sequence.length; x++) {
  if (sequence.indexOf(needle) === 0) {
    match.push(x + 1);
  }
  sequence = sequence.slice(1);
}

console.log(match.join(' '));
