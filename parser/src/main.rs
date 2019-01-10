/**

Program who lunch pdf_to_text on the directory in param

**/


//import
use std::fs;
use std::path::Path;
use std::process::Command;
use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io;

fn main() {




    // get args
    let args: Vec<String> = env::args().collect();
    //println!("{:?}", args);


    let mut dir_name = String::from(args[1].clone());
    //println!("{:?}", dir_name);
    //create_directory(&dir_name);


    let path = Path::new(&args[1]);
    for entry in fs::read_dir(path).expect("Unable to list") {
        let entry = entry.expect("unable to get entry");

        println!("{:?}", entry.path());
        
        let input: String = get_input("Parser ce fichier y/n ? ");

        if (input == "n") {
            continue;
        }
        
        let path = entry.path().into_os_string();
        //println!("{:?}", path);
        
        pdf_to_txt(&path.clone().into_string().unwrap());

        //dir_name.push_str("text");

    }

}


// create directory
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

// lunch pdftotext
fn pdf_to_txt(path: &String) {

    let filename = path.split(".").next();

    let output = Command::new("pdftotext")
                    //.arg("-enc UTF-8")
                    .arg(path)
                    .output()
                    .expect("failed to execute process");

    let s = String::from_utf8_lossy(&output.stdout);
    println!("{}", s);
}

// read a file
fn read_file(filename: &String) {
    let mut f = File::open(Path::new(filename)).expect("file not found");
    let mut contents = String::new();

    f.read_to_string(&mut contents)
        .expect("something went wrong reading the file");
}


// get user input
pub fn get_input(prompt: &str) -> String{
    println!("{}",prompt);
    let mut input = String::new();
    match io::stdin().read_line(&mut input) {
        Ok(_goes_into_input_above) => {},
        Err(_no_updates_is_fine) => {},
    }
    input.trim().to_string()
}
