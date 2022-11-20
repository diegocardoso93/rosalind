// Introduction to the Bioinformatics Armory
// https://rosalind.info/problems/ini/

use std::collections::BTreeMap;

pub fn ini(seq: &str) -> String {
    let mut count = BTreeMap::from([('A', 0), ('C', 0), ('G', 0), ('T', 0)]);

    for c in seq.chars() {
        *count.entry(c).or_insert(0) += 1;
    }

    count
        .values()
        .map(|v| v.to_string())
        .collect::<Vec<String>>()
        .join(" ")
}
