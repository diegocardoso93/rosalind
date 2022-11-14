// Enumerating Oriented Gene Orderings
// https://rosalind.info/problems/sign/

use std::io::Write;

pub fn sign(input: &str) -> String {
    let num = input.parse::<i64>().unwrap();
    let mut result = vec![];
    let symbols = (-num..=num).filter(|n| n != &0i64).collect::<Vec<_>>();

    let nx = input.parse::<u64>().unwrap();
    let max = (2u64.pow(nx as u32) * (1..=nx).product::<u64>()) as usize;
    for i in 0..i64::MAX {
        if let Some(x) = encode(i, num * 2, num, &symbols) {
            result.push(
                x.iter()
                    .map(|i| i.to_string())
                    .collect::<Vec<_>>()
                    .join(" "),
            );
        }
        if result.len() == max {
            break;
        }
    }

    result.insert(0, result.len().to_string());

    let mut file = std::fs::File::create("result.txt").expect("create failed");
    file.write_all(result.join("\n").as_bytes())
        .expect("write failed");

    result.join("\n")
}

fn encode(mut num: i64, radix: i64, places: i64, symbols: &[i64]) -> Option<Vec<i64>> {
    let mut result = vec![];
    loop {
        let i = (num % radix) as usize;
        if result.contains(&symbols[i]) || result.contains(&(-symbols[i])) {
            return None;
        }
        result.insert(0, symbols[i]);
        num /= radix;
        if result.len() == places as usize {
            break;
        }
    }
    Some(result)
}
