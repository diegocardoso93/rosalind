// Enumerating k-mers Lexicographically
// https://rosalind.info/problems/lexf/

pub fn lexf(input: &str) -> String {
    let lines = input.lines().collect::<Vec<&str>>();
    let mut symbols = lines[0]
        .split_whitespace()
        .collect::<String>()
        .chars()
        .collect::<Vec<char>>();
    symbols.sort();
    let length = lines[1].parse::<u32>().unwrap();
    let combs = symbols.len().pow(length) as u32;

    let mut result = vec![];
    for i in 0..combs {
        result.push(encode(i, symbols.len() as u32, length, &symbols));
    }

    result.join("\n")
}

fn encode(mut num: u32, radix: u32, decimals: u32, symbols: &[char]) -> String {
    let mut result = String::new();
    loop {
        let i = (num % radix) as usize;
        result.insert(0, symbols[i]);
        num /= radix;
        if num == 0 && result.len() == decimals as usize {
            break;
        }
    }
    result
}
