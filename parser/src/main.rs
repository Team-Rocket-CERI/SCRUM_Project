use std::fs;
use std::path::Path;
use std::process::Command;


fn main() {

    let output = Command::new("ls")
                    .arg("-l")
                    .output()
                    .expect("failed to execute process");

    let s = String::from_utf8_lossy(&output.stdout);
    println!("{}", s);

    let path = Path::new("../Papers/");
    //create_directory("lel".to_string());
    for entry in fs::read_dir(path).expect("Unable to list") {
        let entry = entry.expect("unable to get entry");
        
        println!("{:?}", entry.file_name());
        let mut test =  entry.file_name().into_string().expect("failed");

        //let mut iter = test.split_whitespace();
        let mut iter = test.split(".");
        println!("{:?}", iter.next());

    }
}


fn create_directory(path: &String) -> std::io::Result<()> {
    match fs::create_dir(path) {
        Ok(r) => println!("{} created", path),
        Err(e) => {
            println!("{}", e);
            fs::remove_dir_all(path);
            fs::create_dir(path);
        }
    };
    Ok(())
}