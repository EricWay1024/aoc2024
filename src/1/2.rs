use std::fs::File;
use std::io::{self, BufReader, BufRead};
use std::collections::HashMap;

fn main() -> io::Result<()> {
    // Open the file
    let file = File::open("in")?;
    
    // Create a BufReader for efficient reading line by line
    let reader = BufReader::new(file);

    let mut numbers_1: Vec<i32> = Vec::new();

    let mut map: HashMap<i32, i32> = HashMap::new();
    
    // Iterate over each line in the file
    for line in reader.lines() {
        match line {
            Ok(line_content) => {
                let parts: Vec<i32> = line_content
                    .split_whitespace() // Split the line into parts based on spaces
                    .filter_map(|s| s.parse::<i32>().ok()) // Try to parse each part as an i32, skipping invalid ones
                    .collect();
                
                numbers_1.push(parts[0]);

                *map.entry(parts[1]).or_insert(0) += 1;
                
            }
            Err(e) => {
                eprintln!("Error reading line: {}", e);
            }
        }
    }


    let mut ans = 0;

    for a in numbers_1 {
        ans += a * (*map.entry(a).or_insert(0));
    }

    println!("{}", ans);
    
    Ok(())
}
