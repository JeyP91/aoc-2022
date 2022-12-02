use input::*;
use mr_kaffee_aoc::{Puzzle, Star};

/// the puzzle
pub fn puzzle() -> Puzzle<'static, PuzzleData, usize, usize, usize, usize> {
    Puzzle {
        year: 2022,
        day: 1,
        input: include_str!("../input.txt"),
        star1: Some(Star {
            name: "Star 1",
            f: &star_1,
            exp: Some(67_658),
        }),
        star2: Some(Star {
            name: "Star 2",
            f: &star_2,
            exp: Some(200_158),
        }),
    }
}

// tag::input[]
pub mod input {
    use std::num::ParseIntError;

    #[derive(Debug)]
    pub struct PuzzleData {
        pub calories: Vec<usize>,
    }

    impl TryFrom<&'static str> for PuzzleData {
        type Error = ParseIntError;

        /// parse the puzzle input
        fn try_from(s: &'static str) -> Result<Self, Self::Error> {
            s.split("\n\n")
                .map(|elf| elf.lines().map(|l| l.parse::<usize>()).sum())
                .collect::<Result<Vec<_>, _>>()
                .map(|calories| Self { calories })
        }
    }
}
// end::input[]

// tag::star_1[]
pub fn star_1(data: &PuzzleData) -> usize {
    data.calories.iter().fold(0, |mx, &cal| mx.max(cal))
}
// end::star_1[]

// tag::star_2[]
pub fn star_2(data: &PuzzleData) -> usize {
    data.calories
        .iter()
        .fold([0; 3], |mut mx, &cal| {
            if cal > mx[0] {
                mx[2] = mx[1];
                mx[1] = mx[0];
                mx[0] = cal;
            } else if cal > mx[1] {
                mx[2] = mx[1];
                mx[1] = cal;
            } else if cal > mx[2] {
                mx[2] = cal;
            }
            mx
        })
        .iter()
        .sum()
}
// end::star_2[]
