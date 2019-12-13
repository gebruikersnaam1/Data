import csv #to get code that allows CSV file import
from Database import Database

class CsvConvertToDB: #TODO think of a better name

    #import the CSV file
    def ImportFile(fileName): 
        try:
           return open(fileName, mode='r')
        except:
            print ("File couldn't be found! Did you include an extension (e.g. .CSV) to the file? ")
            exit()
    
    #get column names
    def GetHeaders(rawDataFile,splitCharacter):
        try:
            return (next(iter(rawDataFile))).split(splitCharacter)
        except:
            print ("File couldn't be seperate! Maybe the file or split character is wrong")

    #get rows
    def CreateRows(rawDataFile,splitCharacter):
        try:
            newList = []
            for i in rawDataFile:
                newList.append(i.split(splitCharacter))
            return newList
        except:
            print('')

    #create table 
    def CreateTable(database, nameColumns, tablename): #TODO re-factor in best practisch
        query = '''CREATE TABLE ''' + tablename + '''(''' #star the creation of the query
        for c in range(len(nameColumns)): #for loop to get all the column names into the query
            query += "[" + str(nameColumns[c]).strip() + "] text"
            if nameColumns[c] != nameColumns[-1]:
                query += ","
            else:
                query += ")"
        database.RunCreateQuery(query)
    
    #insert DATA
    def InsertRows(database, rows, tablename):
        for row in rows:
            query = "insert into " + tablename + " values ("
            for c in range(len(row)): #for loop to get all the column names into the query
                query +=  "'" + str(row[c]).strip() + "'"
                if row[c] != row[-1]:
                    query += ","
                else:
                    query += ")"
            database.RunCreateQuery(query)

    #Run the class
    def RunConvertor(fileName,splitCharacter,dbName,tableName):
        print("Start converting... file must have a header and be in the right format (one table)!\n\n")
        
        #convert CSV to data that can be used 
        rawDataFile = CsvConvertToDB.ImportFile(fileName) #import
        nameColumns = CsvConvertToDB.GetHeaders(rawDataFile,splitCharacter) #headers, that is going to be used for creating the table
        rows = CsvConvertToDB.CreateRows(rawDataFile,splitCharacter) #rows, that contains the data for the giving table
        #create database object to create the tables and rows
        database = Database(dbName) 

        #create table
        CsvConvertToDB.CreateTable(database,nameColumns, tableName)
        #insert data
        CsvConvertToDB.InsertRows(database,rows,tableName)

        print ("done with converting")