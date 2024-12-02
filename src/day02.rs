use std::fs;

fn check_report(parts: Vec<i32>) -> bool {
    if parts[0] == parts[1] {
        return false;
    }

    let is_increasing = parts[0] < parts[1];

    for (i, value) in parts.iter().enumerate() {
        if i == 0 {
            continue;
        }

        let pre_value = parts[i - 1];

        if pre_value == *value {
            return false;
        }

        if (pre_value < *value) != is_increasing {
            return false;
        }

        if (pre_value - *value).abs() > 3 {
            return false;
        }
    }

    return true;
}

pub fn solve_part1() {
    let file = fs::read_to_string("input/2.in").expect("Failed to read input file");

    let mut ans = 0;
    for line in file.lines() {
        let parts: Vec<i32> = line
            .split_whitespace() // Split the line into parts based on spaces
            .filter_map(|s| s.parse::<i32>().ok()) // Try to parse each part as an i32, skipping invalid ones
            .collect();

        if check_report(parts) {
            ans += 1;
        }
    }

    println!("{}", ans);
}

pub fn solve_part2() {
    let file = fs::read_to_string("input/2.in").expect("Failed to read input file");

    let mut ans = 0;
    for line in file.lines() {
        let parts: Vec<i32> = line
            .split_whitespace() // Split the line into parts based on spaces
            .filter_map(|s| s.parse::<i32>().ok()) // Try to parse each part as an i32, skipping invalid ones
            .collect();

        let candidates: Vec<Vec<i32>> = (0..parts.len()) // Iterate over indices (0 to len-1)
            .map(|i| {
                parts
                    .iter()
                    .enumerate() // Add index to each element
                    .filter(|(index, _)| *index != i) // Filter out the i-th element
                    .map(|(_, &value)| value) // Get the value (dereference the reference)
                    .collect::<Vec<i32>>() // Collect into a new vector
            })
            .collect(); // Collect all the vectors into a Vec<Vec<i32>>
        for candidate in candidates {
            if check_report(candidate) {
                ans += 1;
                break;
            }
        }
    }

    println!("{}", ans);
}
