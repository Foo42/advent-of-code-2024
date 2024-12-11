use std::iter;

use input::load_from_file;

mod input;

#[cfg(test)]
mod test {
    use std::iter;

    use input::{load_from_file, load_from_string};

    use super::*;

    #[test]
    fn test_evolve_0() {
        assert_eq!(evolve_stone(0), (1, None))
    }
    #[test]
    fn test_evolve_even_digits() {
        assert_eq!(evolve_stone(8119), (81, Some(19)))
    }
    #[test]
    fn test_evolve_default_rule() {
        assert_eq!(evolve_stone(100), (202400, None))
    }
    #[test]
    fn test_evolve_row() {
        let original = vec![125, 17];
        let evolved = vec![253000, 1, 7];
        assert_eq!(evolve_row(&original), evolved)
    }

    #[test]
    fn test_example_1() {
        let input = load_from_file("../input/example.txt").unwrap();
        let v = iter::successors(Some(input), |stones| Some(evolve_row(stones)))
            .nth(6)
            .unwrap();
        assert_eq!(
            v,
            load_from_string(
                "2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2"
            )
        )
    }
}

fn evolve_stone(stone_value: usize) -> (usize, Option<usize>) {
    if stone_value == 0 {
        return (1, None);
    }
    let string_value = stone_value.to_string();
    if string_value.len() % 2 == 0 {
        let split_point = string_value.len() / 2;
        let left: usize = (&string_value[0..split_point]).parse().unwrap();
        let right: usize = (&string_value[split_point..]).parse().unwrap();
        return (left, Some(right));
    }

    (stone_value * 2024, None)
}

fn evolve_row(stones: &[usize]) -> Vec<usize> {
    stones
        .iter()
        .flat_map(|stone| {
            let evolved = evolve_stone(*stone);
            if let (left, Some(right)) = evolved {
                vec![left, right]
            } else {
                vec![evolved.0]
            }
        })
        .collect()
}

fn exercise_1() -> usize {
    let input = load_from_file("../input/exercise.txt").unwrap();
    let v = iter::successors(Some(input), |stones| Some(evolve_row(stones)))
        .nth(25)
        .unwrap();
    v.len()
}

fn main() {
    println!("Exercise 1: {}", exercise_1());
}
