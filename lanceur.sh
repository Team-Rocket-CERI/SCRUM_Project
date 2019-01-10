#!/bin/bash

rm -r papersTXT/
rm -r papersXML/

./parser/target/release/parser $1
mkdir papersTXT
mv $1/*.txt papersTXT/
mkdir papersXML
python parser/script/parser.py

echo 'parsing complete'