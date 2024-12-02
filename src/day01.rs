use std::collections::HashMap;
use std::fs;

pub fn solve_part1() {
    // Open the file
    let file = fs::read_to_string("input/1.in").expect("Failed to read input file");

    let mut numbers_1: Vec<i32> = Vec::new();
    let mut numbers_2: Vec<i32> = Vec::new();

    // Iterate over each line in the file
    for line in file.lines() {
        let parts: Vec<i32> = line
            .split_whitespace() // Split the line into parts based on spaces
            .filter_map(|s| s.parse::<i32>().ok()) // Try to parse each part as an i32, skipping invalid ones
            .collect();
        numbers_1.push(parts[0]);
        numbers_2.push(parts[1]);
    }

    numbers_1.sort();
    numbers_2.sort();

    let mut ans = 0;

    for (a, b) in numbers_1.iter().zip(numbers_2.iter()) {
        ans += (a - b).abs();
    }

    println!("{}", ans);
}

pub fn solve_part2() {
    // Open the file
    let file = fs::read_to_string("input/1.in").expect("Failed to read input file");

    let mut numbers_1: Vec<i32> = Vec::new();

    let mut map: HashMap<i32, i32> = HashMap::new();

    // Iterate over each line in the file
    for line in file.lines() {
        let parts: Vec<i32> = line
            .split_whitespace() // Split the line into parts based on spaces
            .filter_map(|s| s.parse::<i32>().ok()) // Try to parse each part as an i32, skipping invalid ones
            .collect();
        numbers_1.push(parts[0]);
        *map.entry(parts[1]).or_insert(0) += 1;
    }

    let mut ans = 0;
    for a in numbers_1 {
        ans += a * (*map.entry(a).or_insert(0));
    }

    println!("{}", ans);
}
