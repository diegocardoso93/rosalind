// Enumerating Gene Orders
// https://rosalind.info/problems/perm/

pub fn perm(input: &str) -> String {
    let num = input.parse::<u32>().unwrap();
    let mut result = vec![];
    for i in 0..num.pow(num) {
        if let Some(x) = encode(i, num, num) {
            result.push(x);
        }
    }
    result.insert(0, result.len().to_string());
    result.join("\n")
}

fn encode(mut num: u32, radix: u32, decimals: u32) -> Option<String> {
    let mut result = vec![];
    loop {
        let i = (num % radix) + 1;
        let c = char::from_digit(i, 10).unwrap().to_string();
        if result.contains(&c) {
            return None;
        }
        result.insert(0, c);
        num /= radix;
        if result.len() == decimals as usize {
            break;
        }
    }
    Some(result.join(" "))
}
