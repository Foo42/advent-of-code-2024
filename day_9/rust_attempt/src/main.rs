mod checksum;
mod disk_map;
mod input;

use crate::{
    checksum::calculate_checksum,
    disk_map::{block_chunks_to_blocks, compact_once},
    input::load_chunk_list_from_file,
};

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_exercise_1_example() {
        let input_path = "../input/example.txt";
        let checksum = exercise_1(input_path);
        assert_eq!(checksum, 1928);
    }
}

fn exercise_1(input_path: &str) -> usize {
    let chunks = load_chunk_list_from_file(input_path).unwrap();
    let mut blocks = block_chunks_to_blocks(&chunks);
    while compact_once(&mut blocks) {}
    calculate_checksum(&blocks)
}

fn main() {
    println!("Exercise 1: {}", exercise_1("../input/exercise.txt"));
}
