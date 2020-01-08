##################################################
    # @note that this is just experment, hence SQL-injection is not done in best practisch!
    #       just trying stuff
##################################################

#import files
import sqlite3 #to work with SQLlite

class Database:
    conn = None

    def __init__(self, fileName):
        self.conn = sqlite3.connect("./output/" + fileName + ".sql")  # loading the database (creating if name isn't found)
    
    def GetQuery(self,query):
        c = self.conn.cursor()
        c.execute(query)
        return c.fetchall()
        try:
            c = self.conn.cursor()
            c.execute(query)
            return c.fetchall()
        except:
            print("Row insert rejected")

    def RunCreateQuery(self,query):
        try:
            c = self.conn.cursor() #return the connector to insert,select, delete and update the database
            c.execute(query) #execute query
            self.conn.commit() #commit
        except:
            print("Row rejected")