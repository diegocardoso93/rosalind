// RNA Splicing
// https://rosalind.info/problems/splc/

pub fn splc(fasta: &str) -> String {
    let seqs = fasta
        .lines()
        .filter(|l| !l.starts_with('>'))
        .collect::<Vec<_>>();

    let dna_str = seqs[0];
    let substrs = &seqs[1..];

    let mut dna_str = dna_str.to_string();
    for substr in substrs.iter() {
        dna_str = dna_str.replace(substr, "");
    }

    let mut protein_result = String::from("");
    for i in (0..dna_str.len()).step_by(3) {
        match get_amino_acid(&dna_str[i..i + 3]) {
            Some("Stop") => break,
            Some(amino_acid) => protein_result += amino_acid,
            None => (),
        }
    }

    protein_result
}

fn get_amino_acid(codon: &str) -> Option<&str> {
    match codon {
        "TTT" => Some("F"),
        "TTC" => Some("F"),
        "TTA" => Some("L"),
        "TTG" => Some("L"),
        "TCT" => Some("S"),
        "TCC" => Some("S"),
        "TCA" => Some("S"),
        "TCG" => Some("S"),
        "TAT" => Some("Y"),
        "TAC" => Some("Y"),
        "TAA" => Some("Stop"),
        "TAG" => Some("Stop"),
        "TGT" => Some("C"),
        "TGC" => Some("C"),
        "TGA" => Some("Stop"),
        "TGG" => Some("W"),
        "CTT" => Some("L"),
        "CTC" => Some("L"),
        "CTA" => Some("L"),
        "CTG" => Some("L"),
        "CCT" => Some("P"),
        "CCC" => Some("P"),
        "CCA" => Some("P"),
        "CCG" => Some("P"),
        "CAT" => Some("H"),
        "CAC" => Some("H"),
        "CAA" => Some("Q"),
        "CAG" => Some("Q"),
        "CGT" => Some("R"),
        "CGC" => Some("R"),
        "CGA" => Some("R"),
        "CGG" => Some("R"),
        "ATT" => Some("I"),
        "ATC" => Some("I"),
        "ATA" => Some("I"),
        "ATG" => Some("M"),
        "ACT" => Some("T"),
        "ACC" => Some("T"),
        "ACA" => Some("T"),
        "ACG" => Some("T"),
        "AAT" => Some("N"),
        "AAC" => Some("N"),
        "AAA" => Some("K"),
        "AAG" => Some("K"),
        "AGT" => Some("S"),
        "AGC" => Some("S"),
        "AGA" => Some("R"),
        "AGG" => Some("R"),
        "GTT" => Some("V"),
        "GTC" => Some("V"),
        "GTA" => Some("V"),
        "GTG" => Some("V"),
        "GCT" => Some("A"),
        "GCC" => Some("A"),
        "GCA" => Some("A"),
        "GCG" => Some("A"),
        "GAT" => Some("D"),
        "GAC" => Some("D"),
        "GAA" => Some("E"),
        "GAG" => Some("E"),
        "GGT" => Some("G"),
        "GGC" => Some("G"),
        "GGA" => Some("G"),
        "GGG" => Some("G"),
        _ => None,
    }
}
