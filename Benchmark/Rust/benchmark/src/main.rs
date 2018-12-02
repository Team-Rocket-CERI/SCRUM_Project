use std::time::{Instant};

fn main() {
    let start = Instant::now();
    let mut _count = 0;

    for _i in 0..10000 {
        for _j in 0..10000 {
            _count += 1;
        }
    }

    println!("{:?}", start.elapsed());
}
