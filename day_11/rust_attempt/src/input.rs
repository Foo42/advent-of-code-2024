use std::fs;
use std::io;

pub fn load_from_file(path: &str) -> io::Result<Vec<usize>> {
    let s = fs::read_to_string(path)?;
    Ok(load_from_string(&s))
}

pub fn load_from_string(input: &str) -> Vec<usize> {
    input
        .trim()
        .split_whitespace()
        .map(|word| word.parse().unwrap())
        .collect::<Vec<_>>()
}
