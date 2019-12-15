#quick code
from converter.Database import Database

class CreateZipcodes:
    ZipCodes = [
        {'area' : "Centrum", "min" : 3011, "max":3016},
        {'area' : "Charlois", "min" : 3081, "max":3089},
        {'area' : "Delfshaven", "min" : 3021, "max":3029},
        {'area' : "Feijnoord", "min" : 3071, "max":3075},
        {'area' : "Hillegersberg-Schiebroek", "min" : 3051, "max":3056},
        {'area' : "Hoek van Holland", "min" : 3151, "max":3151},
        {'area' : "Hoogvliet", "min" : 3191, "max":3194},
        {'area' : "IJsselmonde", "min" : 3076, "max":3079},
        {'area' : "Kralingen-Crooswijk", "min" : 3031, "max":3031},
        {'area' : "Noord", "min" : 3032, "max":3041},
        {'area' : "Overschie", "min" : 3042, "max":3047},
        {'area' : "Prins Alexander", "min" : 3059, "max":3068},
        {'area' : "Rozenburg", "min" : 3181, "max":3181},
        {'area' : "Pernis", "min" : 3195, "max":3195},
    ]

    def IsZipcodeRangeValid(min,zipCode):
        for zp in zipCode:
            minCheck = int(zp["min"])
            maxCheck = int(zp["max"])
            if minCheck <= min and maxCheck >= min: #if there is is overlap between zip codes
                return False
        return True

    def CheckIfZipCodesOverlap():
        for zp in range(len(CreateZipcodes.ZipCodes)):
            zips = CreateZipcodes.ZipCodes.copy()
            min = int(zips[zp]["min"])
            del zips[zp]
            rs = CreateZipcodes.IsZipcodeRangeValid(min,zips)
            if rs == False:
                print("Error: Zip codes overlap")
                return False
        return True

    def CreateZipCodeTable(dbName, tableName):
        query = "CREATE TABLE " + tableName +  "(area STRING, minValue INT, maxValue INT)"
        db = Database(dbName)
        db.RunCreateQuery(query)

    def InsertAreas(dbName,tableName):
        db = Database(dbName)
        for i in CreateZipcodes.ZipCodes:
            query = "insert into " + tableName + " values ("
            query += "'" + i['area'] + "'" + "," + str(i['min']) + "," + str(i['max']) + ")"
            db.RunCreateQuery(query)

    def InitZipcodes(dbName, tableName):
        if CreateZipcodes.CheckIfZipCodesOverlap() == False:
            return False
        CreateZipcodes.CreateZipCodeTable(dbName,tableName)
        CreateZipcodes.InsertAreas(dbName,tableName)