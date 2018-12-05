import glob
import re

txt_files = glob.glob("../../Papers/*.txt")
directory = "../../Paperstext/"

for file in txt_files:
    filename = file.split("/")
    path = directory + filename[len(filename)-1]
    openFile = open(path, "w")

    # nom du fichier d' origine
    openFile.write(filename[len(filename)-1].replace(".txt", ".pdf"))
    openFile.write("\n\n")


    sequence = ""
    write = False
    with open(file) as mytxt:
        #txt = mytxt.read()
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
    openFile.write(title)
    openFile.write("\n\n")

    # abstract ou resume
    #found = re.search('(Abstract|ABSTRCAT)[^1]+', txt).group
    #for line in found:
    #    print line
    openFile.write(sequence)

    openFile.close() 


    