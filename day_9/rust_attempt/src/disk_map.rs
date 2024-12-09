use crate::input::{BlockChunk, FileId};

pub type DiskMap = Vec<Option<FileId>>;

#[cfg(test)]
mod tests {
    use super::*;
    use crate::input::load_chunk_list;

    #[test]
    fn test_block_chunks_to_blocks() {
        assert_eq!(
            block_chunks_to_blocks(&load_chunk_list("112")),
            vec![Some(FileId(0)), None, Some(FileId(1)), Some(FileId(1))]
        );
    }

    #[test]
    fn test_compact_once() {
        let mut blocks = vec![Some(FileId(0)), None, Some(FileId(1)), Some(FileId(1))];
        let did_compact = compact_once(&mut blocks);
        assert!(did_compact);
        assert_eq!(
            blocks,
            vec![Some(FileId(0)), Some(FileId(1)), Some(FileId(1)), None]
        );

        assert_eq!(compact_once(&mut blocks), false);
    }
}

pub fn block_chunks_to_blocks(chunks: &[BlockChunk]) -> DiskMap {
    chunks
        .iter()
        .flat_map(|chunk| (0..chunk.length).map(|_| chunk.file_id).collect::<Vec<_>>())
        .collect()
}

pub fn compact_once(blocks: &mut DiskMap) -> bool {
    let first_gap_index: Option<usize> = blocks
        .iter()
        .enumerate()
        .find(|(_index, item)| Option::is_none(item))
        .map(|(index, _item)| index);

    let last_file_index: Option<usize> = blocks
        .iter()
        .enumerate()
        .rev()
        .find(|(_index, item)| Option::is_some(item))
        .map(|(index, _item)| index);

    match (first_gap_index, last_file_index) {
        (Some(a), Some(b)) if a < b => {
            blocks.swap(a, b);
            true
        }
        _ => false,
    }
}
