# coding: utf-8

import glob
import re
from lxml import etree


# creation du xml
page = etree.Element('xml')
doc = etree.ElementTree(page)

article = etree.SubElement(page, 'article')
preambule = etree.SubElement(article, 'preambule')
titre = etree.SubElement(article, 'titre')
auteur = etree.SubElement(article, 'auteur')
abstract = etree.SubElement(article, 'abstract')
biblio = etree.SubElement(article, 'biblio')

# chemin fichiers
txt_files = glob.glob("papersTXT/*.txt")
directory = "papersXML/"

for file in txt_files:
    filename = file.split("/")
    path = directory + filename[len(filename)-1].replace(".txt", ".xml")
    outFile = open(path, "w")

    # nom du fichier d' origine
    preambule.text = filename[len(filename)-1].replace(".txt", ".pdf")

    # auteur
    aut = filename[len(filename)-1].split('_')
    aut = aut[0]
    auteur.text = aut


    sequence = ""
    write = False
    with open(file) as mytxt:
        for line in mytxt:
            if 'Abstract' in line:
                write = True
            if write:
                sequence += line
            if not line.strip():
                write = False



    # titre de l' article
    title = filename[len(filename)-1].replace(".txt", "")
    title = title.split("_")
    title = title[len(title)-1]

    titre.text = title

    # abstract ou resume
    #found = re.search('(Abstract|ABSTRCAT)[^1]+', txt).group
    #for line in found:
    #    print line
    try:
        
        abstract.text = sequence
    except:
        #print "Unexpected error"
        abstract.text = sequence.decode('utf-8')


    # bibliographie 

    sequence = ""
    write = False
    with open(file) as mytxt:
        for line in mytxt:
            if "References\n" == line:
                write = True
            if write:
                sequence += line
            if not line.strip():
                write = False    

    try:    
        biblio.text = sequence
    except:
        #print "Unexpected error"
        sequence = sequence.decode('utf-8')
        biblio.text = unicode(sequence)

    doc.write(outFile)


    