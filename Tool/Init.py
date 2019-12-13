#################
    # note: this is a quick tool to work with data
#################
from Converter import CsvConvertToDB 
from UpdateApplicantDBFormat import UpdateApplicantDBFormat
import os

def init():
    tableName = 'applicant'
    databaseName = 'Jeugdfonds.sql'

    #explaining whats happening
    print("\n =======================================================================================================\n")
    print("step One: getting the data 'Applicant' of the to the SQLlite format (database shouldn't exist)")
    CsvConvertToDB.RunConvertor('Applicants.csv',';',databaseName, tableName) #import the database

    print("\n =======================================================================================================\n")
    print("step 2: transforming the SQL-data to the exit form")
    UpdateApplicantDBFormat.RunCreator(databaseName,tableName,"Project","Intermediairs")

#intro text, just because...
print("This application is made to convert de CSV of Jeugdfonds to a data format that is usable for Jeugdfonds project of InCubeData \n")
#result = input("Press 'Y' to complete the database!")
result = 'Y'
if result == "Y" or result == "y":
    init()
else:
    exit()