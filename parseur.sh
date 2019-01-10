#!/bin/bash


if [ "$#" -ne 2 ]
then
 echo "Le nombre d'arguments est invalide"
else

    rm -r papersTXT/
    rm -r papersXML/

    ./parser/target/release/parser $2
    mkdir papersTXT
    mv $2/*.txt papersTXT/

    if [ "$1" = "-t"  ]
    then
        echo "txt output"
        python2 parser/script/parserTXT.py
    elif [ "$1" = "-x" ]
    then
        mkdir papersXML
        echo "xml output"
        python2 parser/script/parserXML.py
    fi


    echo 'parsing complete'
fi
