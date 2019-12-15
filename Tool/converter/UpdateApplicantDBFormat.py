####################
#   @content this class is to create the model
####################
from converter.Database import Database
import datetime
from random import randint

class UpdateApplicantDBFormat: #TODO shorter name
    oldColumnsName = ['rowid','Applicant','DateOfBirth','Zipcode','Gender','DateOfApproval']
    amountIntermediaries = 20 #there are 14 areas ('deelgemeentes'), so this ensures that all get one and some get more
    IntermediariesZipCodes = [3013,3071,3021,3042,3033,3045,3031,3071,3081,3044,3029,3087,3047,3065]

    def GetData(dbName, tableName):
        db = Database(dbName)
        query = "SELECT "
        count = 0
        for n in UpdateApplicantDBFormat.oldColumnsName:
            count += 1
            query += n 
            if count < (len(UpdateApplicantDBFormat.oldColumnsName)): #check if , is needed
                query += ","
            
        query += ' FROM ' + tableName
        return db.GetQuery(query)

    def SpecificFormat(RawData): #this will only work in the specfic format
        rowsApplicants = []
        rowsProjects = []
        try:      
            for r in RawData:
                rowsAp = []
                rowsPro = []
                rowsAp.append(r[0]) #rowID
                #name
                name = r[1].split(" ")
                del name[-1] #remove the date behind a name
                rowsAp.append(name[0]) #firstname
                #affix
                affix = " ".join(name[1:-1])
                rowsAp.append(affix) 
                rowsAp.append(name[-1])
                rowsAp.append(r[2]) #date of birth
                rowsAp.append(r[3]) #zip code
                rowsAp.append(r[4]) #gender

                rowsPro.append(r[0]) #userID
                if r[5].strip() == "":
                    rowsPro.append(False)
                else:
                    rowsPro.append(True)
                rowsPro.append(randint(1, UpdateApplicantDBFormat.amountIntermediaries)) #there are 14 'deelgemeentes' so lets create 20 intermediairs (so all areas have one and some have more)
                if len(rowsApplicants) > 0: #remove the dupples
                    if rowsAp[1:] == rowsApplicants[-1][1:]:
                        continue
                rowsApplicants.append(rowsAp)
                rowsProjects.append(rowsPro)
            return rowsApplicants, rowsProjects
        except:
            print("Data needs to exact to make it work, please alter the format!") 

    def DropOldTable(dbName,tableName):
        db = Database(dbName)
        query = "DROP TABLE " + tableName
        db.RunCreateQuery(query)

    def ExplainClass():
        #explain how the code word
        print("Running the creator: the SQLite file should have being given a table name with the columns")
        for n in UpdateApplicantDBFormat.oldColumnsName:
            print("-" + n )

    def CreateApplicantsTable(dbName,tableName):
        #headers 
        query = "CREATE TABLE " + tableName + "(ID int, FirstName VARCHAR(100), Affix VARCHAR (100), Lastname VARCHAR (100), DateOfBirth DATE, ZipCode int(4), Gender VARCHAR(6) )"
        db = Database(dbName)
        db.RunCreateQuery(query)

    def CreateProjectsTable(dbName,tableName):
        #headers 
        query = "CREATE TABLE " + tableName + "( ApplicantsID int, Approved BOOL, Intermediair int)"
        db = Database(dbName)
        db.RunCreateQuery(query)
    
    def CreateIntermediairTable(dbName,tableName):
        #headers 
        query = "CREATE TABLE  " + tableName + "(Intermediair int, Zipcode int(4))"
        db = Database(dbName)
        db.RunCreateQuery(query)
    
    def InsertIntermediairs(dbName, tableName):
        db = Database(dbName)
        for i in range(UpdateApplicantDBFormat.amountIntermediaries):
            value = int(randint(0, (len(UpdateApplicantDBFormat.IntermediariesZipCodes)-1)))
            zipCode = str(UpdateApplicantDBFormat.IntermediariesZipCodes[value])
            id = str(i)
            query = "insert into " + tableName + " values(" + id + ", " + zipCode + ");"
            db.RunCreateQuery(query)

    def InsertRows(dbName, rows, tableName): #TODO same method in Converter (so, should be made one)
        database = Database(dbName)
        for row in rows:
            query = "insert into " + tableName + " values ("
            for c in range(len(row)): #for loop to get all the column names into the query
                query +=  "'" + str(row[c]).strip() + "'"
                if c < (len(row)-1):
                    query += ","
                else:
                    query += ")"
            database.RunCreateQuery(query)
    
    def RunCreator(dbName,applicantName,projectName,intermediairsName): #TODO make the method shorter/ 
        UpdateApplicantDBFormat.ExplainClass()
        
        #note: this code is not flexible and needs to be changed if the format changes
        rawData = UpdateApplicantDBFormat.GetData(dbName, applicantName) #get the SQLite data and converts it two tables
        ApplicantRows, ProjectRows = UpdateApplicantDBFormat.SpecificFormat(rawData) #TODO: make the code more flexible
    
        #DROP old tables (to create the new once)
        UpdateApplicantDBFormat.DropOldTable(dbName,applicantName)
        UpdateApplicantDBFormat.DropOldTable(dbName ,projectName)
        
        #insert the new tables
        UpdateApplicantDBFormat.CreateIntermediairTable(dbName,intermediairsName)
        UpdateApplicantDBFormat.CreateApplicantsTable(dbName,applicantName)
        UpdateApplicantDBFormat.CreateProjectsTable(dbName,projectName)

        #insert the values
        UpdateApplicantDBFormat.InsertRows(dbName,ApplicantRows,applicantName)
        UpdateApplicantDBFormat.InsertRows(dbName,ProjectRows,projectName)
        UpdateApplicantDBFormat.InsertIntermediairs(dbName,intermediairsName)