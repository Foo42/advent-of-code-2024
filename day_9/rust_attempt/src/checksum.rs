use crate::input::FileId;

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate_checksum() {
        assert_eq!(calculate_checksum(&[]), 0);
        assert_eq!(
            calculate_checksum(&vec![
                Some(FileId(1)),
                Some(FileId(0)),
                Some(FileId(2)),
                None
            ]),
            4
        );
    }
}

pub fn calculate_checksum(blocks: &[Option<FileId>]) -> usize {
    blocks
        .iter()
        .enumerate()
        .flat_map(|(position, block)| block.map(|FileId(id)| id * position))
        .sum()
}
