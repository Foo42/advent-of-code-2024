use std::io;
use std::{fs, path::Path, usize};

#[derive(Debug, PartialEq, Clone, Copy)]
pub struct FileId(pub usize);

#[derive(Debug, PartialEq)]
pub struct BlockChunk {
    pub file_id: Option<FileId>,
    pub start_position: usize,
    pub length: usize,
}

impl BlockChunk {
    pub fn blocks(&self) -> Vec<Option<FileId>> {
        (0..self.length).map(|_| self.file_id).collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_load_chunk_list() {
        assert_eq!(load_chunk_list(""), vec![]);
        assert_eq!(
            load_chunk_list("1"),
            vec![BlockChunk {
                file_id: Some(FileId(0)),
                start_position: 0,
                length: 1
            }]
        );
        assert_eq!(
            load_chunk_list("124"),
            vec![
                BlockChunk {
                    file_id: Some(FileId(0)),
                    start_position: 0,
                    length: 1
                },
                BlockChunk {
                    file_id: None,
                    start_position: 1,
                    length: 2
                },
                BlockChunk {
                    file_id: Some(FileId(1)),
                    start_position: 3,
                    length: 4
                },
            ]
        );
    }
}

pub fn load_chunk_list_from_file(path: &str) -> io::Result<Vec<BlockChunk>> {
    let contents = fs::read_to_string(path)?;
    io::Result::Ok(load_chunk_list(contents.trim()))
}

pub fn load_chunk_list(s: &str) -> Vec<BlockChunk> {
    s.chars()
        .map(|char| usize::try_from(char.to_digit(10).unwrap()).unwrap())
        .enumerate()
        .fold(
            (0, vec![]),
            |(position, mut chunks): (usize, Vec<BlockChunk>), (i, length)| {
                let start_position = position;
                let file_id = if i % 2 == 0 {
                    Some(FileId(i / 2))
                } else {
                    None
                };
                let chunk = BlockChunk {
                    file_id,
                    start_position,
                    length,
                };
                chunks.push(chunk);
                (position + length, chunks)
            },
        )
        .1
}
