##################################################
    # @note that this is just experment, hence SQL-injection is not done in best practisch!
    #       just trying stuff
##################################################

#import files
import sqlite3 #to work with SQLlite

class Connector:
    conn = None

    def __init__(self):
        self.conn = sqlite3.connect("jeugdfonds/models/Jeugdfonds.sql")  # loading the database (creating if name isn't found)
    
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
        c = self.conn.cursor() #return the connector to insert,select, delete and update the database
        c.execute(query) #execute query
        self.conn.commit() #commit
        