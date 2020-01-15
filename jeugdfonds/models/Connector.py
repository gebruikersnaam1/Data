##################################################
    # @note that this is just experment, hence SQL-injection is not done in best practisch!
    #       just trying stuff
##################################################

#import files
import sqlite3 #to work with SQLlite

class Connector:

    def GetCon(self):
        return sqlite3.connect("jeugdfonds/models/Jeugdfonds.sql")

    def GetQuery(self,query):
        conn = self.GetCon()
        c = conn.cursor()
        c.execute(query)
        return c.fetchall()
        try:
            c = self.conn.cursor()
            c.execute(query)
            return c.fetchall()
        except:
            print("Row insert rejected")
        c.close()


    def RunCreateQuery(self,query):
        c = self.GetCon()
        c.execute(query) #execute query
        c.commit() #commit
        c.close()
        