use std::fs;

fn count(s: Vec<String>) -> i32 {
    let mut ans: i32 = 0;
    for line in s {
        ans += line.matches("XMAS").count() as i32;
        ans += line.matches("SAMX").count() as i32;
    }
    return ans;
}

pub fn solve_part1() {
    let file = fs::read_to_string("input/4.in").expect("Failed to read input file");

    let lines: Vec<String> = file.lines().map(|s| s.to_string()).collect();

    // Get the number of rows and columns (assuming a square matrix)
    let num_rows = lines.len();
    let num_cols = lines[0].len();

    let columns: Vec<String> = (0..num_cols)
        .map(|col_idx| {
            lines
                .iter()
                .map(|line| line.chars().nth(col_idx).unwrap())
                .collect::<String>()
        })
        .collect();

    // Collect all diagonals starting from the first row
    let diagonals: Vec<String> = (0..num_cols) // Starting from each character in the first row
        .map(|start_col| {
            let mut diagonal = String::new();
            let mut r = 0;
            let mut c = start_col;
            while r < num_rows && c < num_cols {
                diagonal.push(lines[r].chars().nth(c).unwrap());
                r += 1;
                c += 1;
            }
            diagonal
        })
        .chain(
            (1..num_rows) // Starting from each character in the first column (excluding the top-left)
                .map(|start_row| {
                    let mut diagonal = String::new();
                    let mut r = start_row;
                    let mut c = 0;
                    while r < num_rows && c < num_cols {
                        diagonal.push(lines[r].chars().nth(c).unwrap());
                        r += 1;
                        c += 1;
                    }
                    diagonal
                }),
        )
        .collect();

    // Collect all anti-diagonals (down-left)
    let anti_diagonals: Vec<String> = (0..num_cols) // Starting from each character in the first row (top-right)
        .map(|start_col| {
            let mut diagonal = String::new();
            let mut r = 0;
            let mut c = start_col;
            while r < num_rows {
                diagonal.push(lines[r].chars().nth(c).unwrap());
                r += 1;

                if c == 0 {
                    break;
                } else {
                    c -= 1;
                }
            }
            diagonal
        })
        .chain(
            (1..num_rows) // Starting from each character in the last column (excluding (0,0))
                .map(|start_row| {
                    let mut diagonal = String::new();
                    let mut r = start_row;
                    let mut c: usize = num_cols - 1;
                    while r < num_rows {
                        diagonal.push(lines[r].chars().nth(c).unwrap());
                        r += 1;
                        if c == 0 {
                            break;
                        } else {
                            c -= 1;
                        }
                    }
                    diagonal
                }),
        )
        .collect();

    let mut ans: i32 = 0;
    ans += count(columns);
    ans += count(lines);
    ans += count(diagonals);
    ans += count(anti_diagonals);

    println!("{}", ans);
}

fn check(a: char, b: char) -> bool {
    return (a == 'M' && b == 'S') || (a == 'S' && b == 'M');
}

pub fn solve_part2() {
    let file = fs::read_to_string("input/4.in").expect("Failed to read input file");

    let lines: Vec<String> = file.lines().map(|s| s.to_string()).collect();

    // Get the number of rows and columns (assuming a square matrix)
    let num_rows = lines.len();
    let num_cols = lines[0].len();

    let mut ans = 0;

    for i in 0..(num_rows - 2) {
        for j in 0..(num_cols - 2) {
            if lines[i + 1].chars().nth(j + 1).unwrap() != 'A' {
                continue;
            }
            let a = lines[i].chars().nth(j).unwrap();
            let b = lines[i + 2].chars().nth(j + 2).unwrap();
            let c = lines[i + 2].chars().nth(j).unwrap();
            let d = lines[i].chars().nth(j + 2).unwrap();

            if check(a, b) && check(c, d) {
                ans += 1;
            }
        }
    }

    println!("{}", ans);

}
