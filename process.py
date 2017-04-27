import sys

working_dir = str(sys.argv[1])

phppass_filename = str(sys.argv[2])


file = working_dir+phppass_filename




#Librarys

classId_lib = {
    '3 Hour NY SAFE CE - 2017 Online': '6925',
    '1 Hour SAFE CE Elective - 2017 Online': '6924',
    '7 Hour SAFE Core CE 2017 - Online': '6915',
    '1 Hour ID SAFE CE - 2017 Online': '6914',
    '1 Hour MO SAFE CE - 2017 Online': '6913',
    '3 Hour NV SAFE CE - 2017 Online': '6912',
    '1 Hour KY SAFE CE - 2017 Online': '6901',
    '2 Hour OR SAFE CE - 2017 Online': '6900',
    '1 Hour WV SAFE CE - 2017 Online': '6887',
    '1 Hour NM SAFE CE - 2017 Online': '6886',
    '2 Hour NJ SAFE CE - 2017 Online': '6885',
    '1 Hour MD SAFE CE - 2017 Online': '6884',
    '1 Hour MA SAFE CE - 2017 Online': '6883',
    '1 Hour RI SAFE CE - 2017 Online': '6882',
    '1 Hour PA SAFE CE - 2017 Online': '6863',
    '1 Hour NC SAFE CE - 2017 Online': '6862',
    '1 Hour GA SAFE CE - 2017 Online': '6861',
    '1 Hour DC SAFE CE - 2017 Online': '6860',
    '1 Hour CT SAFE CE - 2017 Online': '6852',
    '1 Hour CO SAFE CE - 2017 Online': '6850',
    '1 Hour HI SAFE CE - 2017 Online': '6849',
    '1 Hour AZ SAFE CE - 2017 Online': '6848',
    '1 Hour CA-DBO SAFE CE - 2017 Online': '6847',
    '1 Hour WA SAFE CE - 2017 Online': '6846',
    '8 Hour SAFE Comprehensive Live 2017': '6759',


    '1 Hour WA SAFE CE 2017 Online':'6846', #Lookup
    '2 Hour OR SAFE CE 2017 Online':'6900',
    '1 Hour CA-DBO SAFE CE 2017 Online':'6847',
    '1 Hour AZ SAFE CE 2017 Online':'6848',
    '1 Hour CO SAFE CE 2017 Online':'6850',
    '1 Hour GA SAFE CE 2017 Online':'6861',
    '1 Hour MD SAFE CE 2017 Online':'6884',
    '1 Hour NC SAFE CE 2017 Online': '6862',
    '1 Hour PA SAFE CE 2017 Online': '6863',
    '2017 7 Hour SAFE CE Core Online': '6915',
    '2017 8 Hour SAFE CE (7 Hour Core + 1 Hour Elective) Online': '6759',
    '3 Hour NV SAFE CE 2017 Online': '6117',

    '1 Hour SAFE CE Elective 2017 Online':'6924',
    '1 Hour CT SAFE CE 2017 Online':'6852',
    '1 Hour DC SAFE CE 2017 Online': '6860',
    '1 Hour HI SAFE CE 2017 Online': '6849',
    '1 Hour ID SAFE CE 2017 Online': '6914',
    '1 Hour KY SAFE CE 2017 Online': '6901',
    '1 Hour MA SAFE CE 2017 Online': '6883',
    '1 Hour MO SAFE CE 2017 Online': '6913',
    '2 Hour NJ SAFE CE 2017 Online': '6885',
    '1 Hour NM SAFE CE 2017 Online': '6886',
    '3 Hour NY SAFE CE 2017 Online': '6925',
    '1 Hour RI DBR CE – 2017 Online': '6882',
    '2 Hour UT SAFE Online CE 2017':'N/A',
    '1 Hour WV SAFE CE 2017 Online': '6887',
}


Offering_lib = {
    '3 Hour NY SAFE CE - 2017 Online': '293528',
    '1 Hour SAFE CE Elective - 2017 Online': '293550',
    '7 Hour SAFE Core CE 2017 - Online': '293551',
    '1 Hour ID SAFE CE - 2017 Online': '293532',
    '1 Hour MO SAFE CE - 2017 Online': '293533',
    '3 Hour NV SAFE CE - 2017 Online': '293552',
    '1 Hour KY SAFE CE - 2017 Online': '293534',
    '2 Hour OR SAFE CE - 2017 Online': '293553',
    '1 Hour WV SAFE CE - 2017 Online': '293535',
    '1 Hour NM SAFE CE - 2017 Online': '293538',
    '2 Hour NJ SAFE CE - 2017 Online': '293544',
    '1 Hour MD SAFE CE - 2017 Online': '293554',
    '1 Hour MA SAFE CE - 2017 Online': '293545',
    '1 Hour RI SAFE CE - 2017 Online': '293546',
    '1 Hour PA SAFE CE - 2017 Online': '293556',
    '1 Hour NC SAFE CE - 2017 Online': '293557',
    '1 Hour GA SAFE CE - 2017 Online': '293558',
    '1 Hour DC SAFE CE - 2017 Online': '293547',
    '1 Hour CT SAFE CE - 2017 Online': '293559',
    '1 Hour CO SAFE CE - 2017 Online': '293560',
    '1 Hour HI SAFE CE - 2017 Online': '293561',
    '1 Hour AZ SAFE CE - 2017 Online': '293564',
    '1 Hour CA-DBO SAFE CE - 2017 Online': '293567',
    '1 Hour WA SAFE CE - 2017 Online': '293581',
    '8 Hour SAFE Comprehensive Live 2017': 'N/A',
    '1 Hour KY SAFE CE - 2016 Online': '293534',
    '1 Hour CO SAFE CE 2016 Online': '293560',
    '3 Hour NV SAFE CE 2016 Online': '293552',



    '1 Hour WA SAFE CE 2017 Online':'293581', #Lookup
    '2 Hour OR SAFE CE 2017 Online':'293553',
    '1 Hour CA-DBO SAFE CE 2017 Online':'293567',
    '1 Hour AZ SAFE CE 2017 Online':'293564',
    '1 Hour CO SAFE CE 2017 Online':'293560',
    '1 Hour GA SAFE CE 2017 Online':'293558',
    '1 Hour MD SAFE CE 2017 Online':'293554',
    '1 Hour NC SAFE CE 2017 Online': '293557',
    '1 Hour PA SAFE CE 2017 Online': '293556',
    '2017 7 Hour SAFE CE Core Online': '293551',
    '2017 8 Hour SAFE CE (7 Hour Core + 1 Hour Elective) Online': 'N/A',
    '3 Hour NV SAFE CE 2017 Online': '293552',

    '1 Hour SAFE CE Elective 2017 Online':'293550',
    '1 Hour CT SAFE CE 2017 Online':'293559',
    '1 Hour DC SAFE CE 2017 Online': '293547',
    '1 Hour HI SAFE CE 2017 Online': '293561',
    '1 Hour ID SAFE CE 2017 Online': '293532',
    '1 Hour KY SAFE CE 2017 Online': '293534',
    '1 Hour MA SAFE CE 2017 Online': '293545',
    '1 Hour MO SAFE CE 2017 Online': '293533',
    '2 Hour NJ SAFE CE 2017 Online': '293544',
    '1 Hour NM SAFE CE 2017 Online': '293538',
    '3 Hour NY SAFE CE 2017 Online': '293528',
    '1 Hour RI DBR CE – 2017 Online': '293546',
    '2 Hour UT SAFE Online CE 2017':'N/A',
    '1 Hour WV SAFE CE 2017 Online': '293535',
}





# Import
import os
import pandas as pd
import numpy
import csv
import dateparser
import re
import shutil



import pprint
pp = pprint.PrettyPrinter(indent=4)



# #Functions

def move(src, dest):
    shutil.move(src, dest)


def num_only(a_input):
     a_input=re.sub("[^0-9]", "", a_input)
     return a_input

def timestamp_fix(i):
    i = i.date()
    i = i.strftime("%m/%d/%Y")
    return i


def split(filehandler, delimiter=',', row_limit=99, output_name_template='output_%s.csv', output_path='.', keep_headers=True):
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    print(current_out_path)
    current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = reader.__next__()
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)


#End_Functions


#Pull Data From File
xl = pd.ExcelFile(file)
sheet1 = xl.parse(0,skiprows=2)
lastname = sheet1['Last Name']
CourseName = sheet1['Course Name']
compleated_Date = sheet1['Completed On']
compleation_per = sheet1['Completion %']
nmls_ids = sheet1['NMLS ID']
out_data = [['Last Name','Course Name', 'Compleated Date','Compleation Per','nmls ids']]
for i, item in enumerate(nmls_ids):
    nmls = nmls_ids[i]
    out_data.append([lastname[i],CourseName[i],compleated_Date[i],compleation_per[i],nmls])
#END###Pull Data From File

#Remove all non 100%
out_data.pop(0)
students_compleation=[]
for x in out_data:
    compleation_data = num_only(str(x[3]))
    if compleation_data == "100":
        students_compleation.append(x)
#End -- Remove all non 100%


#Organise into Classrooms
classrooms = {}
for i in students_compleation:
    key = i[1]
    classrooms.setdefault(key, [])
    email =i[0]
    classrooms[key].append(i)
#End Organise into Classrooms


#Save Class into Files
for i in classrooms: # Grabbing Classrooms -- i = Key
    course_id = classId_lib[i]
    offering_id = Offering_lib[i]

    class_room = [['Course_Num','Offering_Num','NMLS_ID','Last_Name', 'Completion_Date','Inst']]
    for student in classrooms[i]: # Iterating through students in  classroom.
        class_room.append([course_id,offering_id,student[4],student[0],timestamp_fix(student[2])])

    #Output to CSV
    # Write to new file
    out = open(working_dir+"/"+i+'-NMLSbanking.csv', 'w', newline='', encoding='utf-8')
    output = csv.writer(out)
    for row in class_room:
        #print(row)
        output.writerow(row)
    out.close()
#End_#Save Class into Files


os.chdir(working_dir)
files_in_dir = os.listdir()
files_to_check = []
for x in files_in_dir:
    file_extension = os.path.splitext(x)
    #print(file_extension[1])
    if file_extension[1] == ".csv":
        files_to_check.append(x)

#check length of files and grab ones with greater than 100
files_to_breakup =[]
for x in files_to_check:
    with open(x, "r") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)
        row_count = len(data)
    if row_count > 99:
        files_to_breakup.append(x)


for x in files_to_breakup:
    print(x)
    outputfilename = str(x) + '_%s.csv'
    split(open(files_to_breakup[0], 'r'), delimiter=',', row_limit=99, output_name_template=outputfilename);
    os.remove(x)

os.chdir('/var/www/html/')
#Zip files
output_filename ="output-"+phppass_filename
dir_name = working_dir
shutil.make_archive(output_filename, 'zip', dir_name)
#End Zip files


#Move File to Destination
src = output_filename+".zip"
dest ="output/"+src
move(src, dest)
#End #Move File to Destination
