// Inferring mRNA from Protein
// https://rosalind.info/problems/mrna/

use std::collections::HashMap;

pub fn mrna(rna_seq: String) -> u64 {
    let qty_rna_aa = HashMap::from([
        ('F', 2),
        ('L', 6),
        ('S', 6),
        ('Y', 2),
        ('C', 2),
        ('W', 1),
        ('P', 4),
        ('H', 2),
        ('Q', 2),
        ('R', 6),
        ('I', 3),
        ('M', 1),
        ('T', 4),
        ('N', 2),
        ('K', 2),
        ('V', 4),
        ('A', 4),
        ('D', 2),
        ('E', 2),
        ('G', 4),
    ]);

    let mut total: u64 = 3; // 3 Stop codons

    for c in rna_seq.chars() {
        total = (total * qty_rna_aa.get(&c).unwrap_or(&1)) % 1_000_000;
    }

    total
}
