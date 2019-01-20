#!/usr/bin/env python2
# coding: utf-8


## XML PARSER ###


import glob
import re
from lxml import etree


# creation du xml
page = etree.Element('xml')
doc = etree.ElementTree(page)

# structure du fichier
article = etree.SubElement(page, 'article')
preambule = etree.SubElement(article, 'preambule')
titre = etree.SubElement(article, 'titre')
auteur = etree.SubElement(article, 'auteur')
abstract = etree.SubElement(article, 'abstract')
introduction = etree.SubElement(article, 'introduction')
corps = etree.SubElement(article, 'corps')
conclusion = etree.SubElement(article, 'conclusion')
discussion = etree.SubElement(article, 'discussion')
biblio = etree.SubElement(article, 'biblio')

# chemin fichiers
txt_files = glob.glob("papersTXT/*.txt")
directory = "papersXML/"


# extract the biblio of the article
def parseBiblio(file):
	content = ""
	write = False

	with open(file) as mytxt:
		for line in mytxt:
			if "REFERENCES" in line or "References\n" in line or "References" in line:
				write = True

			if write:
				content += line

	try:	
		biblio.text = transform(content)
	except:
		# print "Unexpected error"
		content = transform2(content)
		biblio.text = unicode(content)
		#introduction.text = content.decode('utf-8')


# extract the discussion of the article
def parseDiscussion(file):
	content = ""
	write = False
	end = False

	with open(file) as mytxt:
		for line in mytxt:
			if ". Discussion" in line:
				write = True
			if "Conclusion" in line or "CONCLUSION" in line or "Conclusions" in line or "CONCLUSIONS" in line:
				end = True
			if end:
				break
			elif write and line != "\n":
				content += line

	try:	
		discussion.text = transform(content)
	except:
		# print "Unexpected error"
		content = transform2(content)
		discussion.text = unicode(content)
		#introduction.text = content.decode('utf-8')


# extract the conclusion of the article
def parseConclusion(file):
	content = ""
	write = False

	with open(file) as mytxt:
		for line in mytxt:
			if "Conclusion" in line or "CONCLUSION" in line or "Conclusions" in line or "CONCLUSIONS" in line:
				for i in range(0,6):
					if line[i] == "C":
						write = True

					if write and "REFERENCES" in line or "References" in line:
						break

			if write and line != "\n":
				content += line
	try:	
		conclusion.text = transform(content)
	except:
		# print "Unexpected error"
		content = transform2(content)
		conclusion.text = unicode(content)
		#introduction.text = content.decode('utf-8')


# extract the corps of the article
def parseCorps(file):
	content = ""									
							 
	jump = False							
	numeric = False
	string = False
	discus = False
	end = False
	write = False


	with open(file) as mytxt:
		for line in mytxt:
			if "Abstract" in line or "ABSTRACT" in line:
				write = True
				
			if write:
				if not jump and not numeric and not string:
					if line == "1\n" or line == "1 Introduction\n":
						jump = True
					elif line[0] == "1" and line[1] == ".":
						numeric = True
					elif line[0] == "I" and line[1] == ".":
						string = True

			if jump and line == "2\n" or line == "2\n" or line[0] == "2" and line[1] == " ":
				discus = True
			elif numeric and line[0] == "2" and line[1] == ".":
				discus = True
			elif string and line[0] == "I" and line[1] == "I":
				discus = True

			if "Conclusion" in line or "CONCLUSION" in line or "Conclusions" in line or "CONCLUSIONS" in line:
				for i in range(0,6):
					if line[i] == "C":
						end = True
			if end:
				break
			elif ". Discussion" in line:
				break
			elif discus and line != "\n":
				content += line

	try:	
		corps.text = transform(content)
	except:
		# print "Unexpected error"
		content = transform2(content)
		corps.text = unicode(content)
		#introduction.text = content.decode('utf-8')



# extract the introduction of the article
def parseIntroduction(file):
	content = ""
	jump = False
	numeric = False
	string = False
	write = False

	with open(file) as mytxt:
		for line in mytxt:
			if "Abstract" in line or "ABSTRACT" in line:
				write = True
			
			if write:
				if not jump and not numeric and not string:
					if line == "1\n" or line == "1 Introduction\n":
						jump = True
					elif line[0] == "1" and line[1] == ".":
						numeric = True
					elif line[0] == "I" and line[1] == ".":
						string = True
				
				if jump and line == "2\n" or line == "2\n" or line[0] == "2" and line[1] == " ":
					break
				elif numeric and line[0] == "2" and line[1] == ".":
					break
				elif string and line[0] == "I" and line[1] == "I":
					break
				
				if jump or numeric or string:
					content += line

	try:	
		introduction.text = transform(content)
	except:
		# print "Unexpected error"
		content = transform2(content)
		introduction.text = unicode(content)
		#introduction.text = content.decode('utf-8')


# extract the abstract of the article
def parseAbstract(file):
	content = ""
	write = False

	with open(file) as mytxt:
			for line in mytxt:
				if "Abstract" in line or "ABSTRACT" in line:
					write = True;
				elif "Introduction" in line or "INTRODUCTION" in line:
					break;
				
				if write:
					content += line

				if not line.strip():
					write = False

	try:		
		abstract.text = transform(content)
	except:
		# print "Unexpected error"
		abstract.text = content.decode('utf-8')


# extract the author of the article
def parseAuthor(file):
	filename = file.split("/")
	aut = filename[len(filename)-1].split('_')
	aut = aut[0]
	test = aut.replace('.', '-').replace('-', ' ')
	test = test.split(" ")
	author = test[0]

	content = ""

	with open(file) as mytxt:
			for line in mytxt:							
				if author in line:
					content += line
					break

	try:		
		auteur.text = transform(content)
	except:
		# print "Unexpected error"
		auteur.text = content.decode('utf-8')


# extract the title of the article
def parseTitle(file):
	content = ""
	write = True

	with open(file) as mytxt:
			for line in mytxt:
							
				if write:
					content += line
				if line.strip():
					write = False


	try:		
		titre.text = transform(content)
	except:
		# print "Unexpected error"
		titre.text = content.decode('utf-8')


# encode / replace / decode
def transform(string):
	string.replace("\n"," ")
	string.replace("\f"," ")
	string.replace("&",  "&amp;")
	string.replace("\ ", "&quot;")
	string.replace("'",  "&apos;")
	string.replace("<",  "&lt;")
	string.replace(">",  "&gt;")
	string.replace("\r", "&#xD;")
	string.replace("\0", '')
	unexpected ="\x0c"
	string = string.encode('string_escape')
	string = string.replace( unexpected.encode('string_escape') , "" )
	string = string.decode('string_escape')
	
	return string


# encode / replace / decode
def transform2(string):
	string.replace("\n"," ")
	string.replace("\f"," ")
	string.replace("&",  "&amp;")
	string.replace("\ ", "&quot;")
	string.replace("'",  "&apos;")
	string.replace("<",  "&lt;")
	string.replace(">",  "&gt;")
	string.replace("\r", "&#xD;")
	string.replace("\0", '')
	
	stripped = lambda s: "".join(i for i in s if 31 < ord(i) < 127)

	return stripped(string)


if __name__ == '__main__':
	for file in txt_files:
		filename = file.split("/")
		path = directory + filename[len(filename)-1].replace(".txt", ".xml")
		outFile = open(path, "w")

		# nom du fichier d' origine
		preambule.text = filename[len(filename)-1].replace(".txt", ".pdf")

		parseTitle(file)
		parseAuthor(file)
		parseAbstract(file)
		parseIntroduction(file)
		parseCorps(file)
		parseConclusion(file)
		parseDiscussion(file)
		parseBiblio(file)

		doc.write(outFile)