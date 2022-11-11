// Finding a Shared Motif
// https://rosalind.info/problems/lcsm/

pub fn lcsm(input: &str) -> String {
    let words = input
        .lines()
        .filter(|l| !l.starts_with('>'))
        .collect::<Vec<_>>();

    let minseq = words
        .iter()
        .min_by(|x, y| x.len().cmp(&y.len()))
        .unwrap()
        .to_string();

    for s in (1..=minseq.len()).rev() {
        let series = all_series(minseq.to_string(), s);

        for seq in series {
            if words.iter().skip(1).all(|w| w.contains(&seq)) {
                return seq;
            }
        }
    }

    String::from("")
}

fn all_series(word: String, size: usize) -> Vec<String> {
    let mut series = vec![];
    for i in 0..=word.len() {
        series.push(word.get(i..i + size).unwrap().to_string());
        if i + size == word.len() {
            break;
        }
    }
    series
}
