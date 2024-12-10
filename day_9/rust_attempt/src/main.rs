mod checksum;
mod disk_map;
mod input;

use disk_map::DiskBlockMap;

use crate::{
    checksum::calculate_checksum, disk_map::block_chunks_to_blocks,
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
    let blocks = block_chunks_to_blocks(&chunks);
    let mut disk_map = DiskBlockMap::new(blocks);
    while disk_map.compact_once() {}
    calculate_checksum(disk_map.blocks())
}

fn main() {
    println!("Exercise 1: {}", exercise_1("../input/exercise.txt"));
}
