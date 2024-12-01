use std::fs::File;
use std::io::{self, BufReader, BufRead};

fn main() -> io::Result<()> {
    // Open the file
    let file = File::open("in")?;
    
    // Create a BufReader for efficient reading line by line
    let reader = BufReader::new(file);

    let mut numbers_1: Vec<i32> = Vec::new();
    let mut numbers_2: Vec<i32> = Vec::new();
    
    // Iterate over each line in the file
    for line in reader.lines() {
        match line {
            Ok(line_content) => {
                let parts: Vec<i32> = line_content
                    .split_whitespace() // Split the line into parts based on spaces
                    .filter_map(|s| s.parse::<i32>().ok()) // Try to parse each part as an i32, skipping invalid ones
                    .collect();
                
                numbers_1.push(parts[0]);
                numbers_2.push(parts[1]);
                
                // Print the parts as integers (or process them as needed)
                // println!("{:?}", parts);
            }
            Err(e) => {
                eprintln!("Error reading line: {}", e);
            }
        }
    }

    numbers_1.sort();
    numbers_2.sort();

    let mut ans = 0;

    for (a, b) in numbers_1.iter().zip(numbers_2.iter()) {
        ans += (a - b).abs();
    }

    println!("{}", ans);
    
    Ok(())
}
