import glob


txt_files = glob.glob("../../Papers/*.txt")

for file in txt_files:
    with open(file) as mytxt:
        for line in mytxt:
            print (line)