// Disclaimer: I hate my code today

use std::fs;

fn read() -> (Vec<(i32, i32)>, Vec<Vec<i32>>) {
    let mut requirements: Vec<(i32, i32)> = Vec::new();
    let mut sequences: Vec<Vec<i32>> = Vec::new();

    let file = fs::read_to_string("input/5.in").expect("Failed to read input file");

    let lines: Vec<String> = file.lines().map(|s| s.to_string()).collect();

    for line in lines {
        if line.contains("|") {
            let parts: Vec<i32> = line.split('|').map(|s| s.parse::<i32>().unwrap()).collect();
            requirements.push((parts[0], parts[1]));
        } else if line.contains(",") {
            let parts: Vec<i32> = line.split(',').map(|s| s.parse::<i32>().unwrap()).collect();
            sequences.push(parts);
        }
    }

    return (requirements, sequences);
}

fn check_valid(seq: &Vec<i32>, requirements: &Vec<(i32, i32)>) -> bool {
    let len_seq = seq.len();
    for i in 0..len_seq {
        for j in 0..i {
            // j < i
            let a = seq[j];
            let b = seq[i];

            for (x, y) in requirements.iter() {
                if (*x == b) && (*y == a) {
                    return false;
                }
            }
        }
    }
    return true;
}

fn try_fix(seq: &Vec<i32>, requirements: &Vec<(i32, i32)>) -> Vec<i32> {
    let mut ans = seq.clone();
    let len_seq = seq.len();
    for i in 0..len_seq {
        for j in 0..i {
            // j < i
            let a = ans[j];
            let b = ans[i];

            for (x, y) in requirements.iter() {
                if (*x == b) && (*y == a) {
                    let temp = ans[i];
                    ans[i] = ans[j];
                    ans[j] = temp;
                }
            }
        }
    }
    return ans;
}

pub fn solve_part1() {
    let (requirements, sequences) = read();
    let mut ans = 0;
    for seq in sequences {
        if check_valid(&seq, &requirements) {
            let l = seq.len();
            ans += seq[l / 2];
        }
    }
    println!("{}", ans);
}

pub fn solve_part2() {
    let (requirements, sequences) = read();
    let mut ans = 0;
    for seq in sequences {
        if !check_valid(&seq, &requirements) {
            let mut temp = seq.clone();
            while !check_valid(&temp, &requirements) {
                temp = try_fix(&temp, &requirements);
            }
            let l = seq.len();
            ans += temp[l / 2];
        }
    }
    println!("{}", ans);
}


