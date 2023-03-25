use std::fs; // for reading file contents from file system (fs)

/**
 * Rust solution to Advent of Code 2021 - Day 1: Sonar Sweep
 */
fn main() {
    let file_input_path = "./../../input_files/day_01/input.txt";
    // open file for reading
    let file_contents = fs::read_to_string(file_input_path).expect("Unable to open file");
    // vector to store values from lines in file
    let mut values: Vec<i32> = Vec::new();
    // start at 1 because first value is always increased
    let mut depth_counter: i32 = 0;

    /* loop through lines in file */
    file_contents.lines().for_each(|line| {
        values.push(line.parse::<i32>().unwrap());
    });

    /*
    loop through vector values and compare to next value in
    vector to see if it increased, decreased or stayed the same (no change)
    - We use `-1` because we are comparing to next value in vector
    - 0..values.len() loops through a vector (0..5 = 0, 1, 2, 3, 4)
     */
    for i in 0..values.len() - 1 {
        let next_sweep: i32 = values[i + 1];
        println!("Current depth: {}", depth_counter);
        if next_sweep > values[i] {
            println!("{} > {} : Increased", next_sweep, values[i]);
            depth_counter += 1;
        } else if next_sweep < values[i] {
            println!("{} < {} : Decreased", next_sweep, values[i]);
        } else {
            println!("{} = {} : Same - no change", next_sweep, values[i]);
        }
    }

    println!(
        "There are {} measurements that are larger than the previous measurement",
        depth_counter
    );
}
