use std::fs;

extern crate regex;

use regex::Regex;


pub fn solve_part1() {
    let file = fs::read_to_string("input/3.in").expect("Failed to read input file");

    // Define the regex pattern to match mul(x, y) where x and y are 1-3 digit numbers
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();

    let mut ans = 0;
    for line in file.lines() {
        // Find all matches
        for cap in re.captures_iter(line) {
            let x: i32 = cap[1].parse().unwrap(); // This is the first capture group (x)
            let y: i32 = cap[2].parse().unwrap(); // This is the second capture group (y)

            ans += x * y;

        }
    }

    println!("{}", ans);
}

pub fn solve_part2() {
    let file = fs::read_to_string("input/3.in").expect("Failed to read input file");

    // Define the regex pattern to match mul(x, y), don't(), or do()
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)").unwrap();

    let mut ans = 0;
    let mut is_enabled: bool = true;
    for line in file.lines() {
        // Find all matches
        for cap in re.captures_iter(line) {
            if let Some(mul_match) = cap.get(0) {
                if mul_match.as_str().starts_with("mul") {
                    // If the match is of the form "mul(x, y)", parse x and y
                    let x: i32 = cap[1].parse().unwrap();
                    let y: i32 = cap[2].parse().unwrap();
                    if is_enabled {
                        ans += x * y;
                    }
                } else if mul_match.as_str() == "don't()" {
                    // Handle the "don't()" match
                    is_enabled = false;
                } else if mul_match.as_str() == "do()" {
                    // Handle the "do()" match
                    is_enabled = true;
                }
            }
        }
    }

    println!("{}", ans);
}