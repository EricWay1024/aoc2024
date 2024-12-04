// src/main.rs
mod day01;
mod day02; 
mod day03;
mod day04;

fn main() {
    // Call the solution for both parts of Day 1
    println!("Advent of Code 2024 - Day 1");
    day01::solve_part1(); // Part 1
    day01::solve_part2(); // Part 2
    
    // // Call the solution for both parts of Day 2 (if you have implemented it)
    println!("Advent of Code 2024 - Day 2");
    day02::solve_part1(); // Part 1
    day02::solve_part2(); // Part 2

    println!("Advent of Code 2024 - Day 3");
    day03::solve_part1(); // Part 1
    day03::solve_part2(); // Part 2

    println!("Advent of Code 2024 - Day 4");
    day04::solve_part1(); // Part 1
    day04::solve_part2(); // Part 2
}
