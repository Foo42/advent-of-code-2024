use crate::input::{BlockChunk, FileId};

pub type DiskMap = Vec<Option<FileId>>;

#[derive(Debug, PartialEq)]
pub struct DiskBlockMap {
    blocks: Vec<Option<FileId>>,
    compacted_lower_bound: usize,
}

impl DiskBlockMap {
    pub fn new(blocks: Vec<Option<FileId>>) -> Self {
        DiskBlockMap {
            blocks,
            compacted_lower_bound: 0,
        }
    }
    pub fn blocks(&self) -> &[Option<FileId>] {
        &self.blocks
    }
    pub fn compact_once(&mut self) -> bool {
        let first_gap_index: Option<usize> = self.blocks()[self.compacted_lower_bound..]
            .iter()
            .enumerate()
            .find(|(_counter, item)| Option::is_none(item))
            .map(|(counter, _item)| counter + self.compacted_lower_bound);

        let last_file_index: Option<usize> = self
            .blocks
            .iter()
            .enumerate()
            .rev()
            .find(|(_index, item)| Option::is_some(item))
            .map(|(index, _item)| index);

        match (first_gap_index, last_file_index) {
            (Some(a), Some(b)) if a < b => {
                self.blocks.swap(a, b);
                self.compacted_lower_bound = a;
                true
            }
            _ => false,
        }
    }
}

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
        let mut disk_map = DiskBlockMap::new(vec![
            Some(FileId(0)),
            None,
            Some(FileId(1)),
            Some(FileId(1)),
        ]);
        let did_compact = disk_map.compact_once();
        assert!(did_compact);
        assert_eq!(
            disk_map.blocks(),
            DiskBlockMap::new(vec![
                Some(FileId(0)),
                Some(FileId(1)),
                Some(FileId(1)),
                None
            ])
            .blocks()
        );

        assert_eq!(disk_map.compact_once(), false);
    }
}

pub fn block_chunks_to_blocks(chunks: &[BlockChunk]) -> DiskMap {
    chunks.iter().flat_map(|chunk| chunk.blocks()).collect()
}
