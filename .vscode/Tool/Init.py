#################
    # note: this is a quick tool to work with data
#################
from converter.Converter import CsvConvertToDB 
from converter.UpdateApplicantDBFormat import UpdateApplicantDBFormat
from converter.Zipcodes import CreateZipcodes
import os

def init():
    tableName = 'Applicant'
    databaseName = 'Jeugdfonds.sql'

    #explaining whats happening
    print("\n =======================================================================================================\n")
    print("step One: getting the data 'Applicant' of the to the SQLlite format (database shouldn't exist)")
    print("NOTE: because of the data format, some rows may be rejected")
    CsvConvertToDB.RunConvertor('Applicants.csv',';',databaseName, tableName) #import the database

    print("\n =======================================================================================================\n")
    print("step 2: transforming the SQL-data to the new format")
    print("NOTE: because of the data format, some rows may be rejected")
    UpdateApplicantDBFormat.RunCreator(databaseName,tableName,"Project","Intermediair")

    print("\n =======================================================================================================\n")
    print("step 3: create the Zip code table")
    CreateZipcodes.InitZipcodes(databaseName,'ZipCode')

#intro text, just because...
print("This application is made to convert de CSV of Jeugdfonds to a data format that is usable for Jeugdfonds project of InCubeData \n")
#result = input("Press 'Y' to complete the database!")
result = 'Y'
if result == "Y" or result == "y":
    init()
else:
    exit()