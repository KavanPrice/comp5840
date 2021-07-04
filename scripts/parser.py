"""
parser.py

This parser uses the csv package to write csv data - gathered from all 6 corpora - to an arff file type. This file is
then converted to arff file format automatically when read into WEKA.
"""


import csv
import os
import re

#Get file paths
PATH = os.getcwd()
RESOURCE_PATH = PATH + '/resources'

# Open arff file and create writer
write_file = open('dialect_data.arff', 'w', encoding='utf-8', newline='')
writer = csv.writer(write_file)

#Write attributes
writer.writerow(['line', 'class'])


#Loop over corpora
for file in os.listdir(RESOURCE_PATH):
    current_file = open(os.path.join(RESOURCE_PATH, file), 'r', encoding='utf-8')
    lines = []
    parsed_lines = []


    #Read all lines from file into array
    while True:
        line = current_file.readline()
        if not line:
            break
        #Strip trailing whitespace
        lines.append(line.strip())

    current_file.close()


    #Parse lines for writing
    for line in lines:
        #'if' condition removes all lines with <doc> tags
        if '<doc ' not in line and '</doc>' not in line:

            #Remove <p> tags
            parsed_line = line.replace('<p> ', '')
            parsed_line = parsed_line.replace('</p>', '')

            #Remove non-letters and convert to lower case
            parsed_line = re.sub('[^A-Za-z\sáéíñóúüÁÉÍÑÓÊÚÜ]+', '', parsed_line).lower()[:-1]

            #Get rid of empty lines
            if parsed_line != '' and parsed_line != '\n':
                parsed_lines.append(parsed_line)


    #Prepare data to write to csv
    data_to_write = []

    if file == 'spanishPH.txt':
        spanish_class = 'philippines'
    else:
        spanish_class = 'not_philippines'

    for line in parsed_lines:
        data_to_write.append([line, spanish_class])

    #Write data
    writer.writerows(data_to_write)


write_file.close()
