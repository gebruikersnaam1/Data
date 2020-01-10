from jeugdfonds.models.Connector import Connector

class ApplicantsModel(Connector):
    
    def GetApplicantsInfo(self):
        query = "SELECT z.Area, count(*) as applicants,(SELECT COUNT(*) FROM Intermediair as i WHERE z.MinValue <= i.Zipcode and z.MaxValue >= i.Zipcode) as intermediairs, z.MinValue, z.MaxValue FROM Applicant as a INNER JOIN Zipcode as z ON (z.MinValue <= a.Zipcode and z.MaxValue >= a.Zipcode) INNER JOIN Project as P ON p.ApplicantsID = a.ID AND p.Approved = 'True' GROUP BY z.Area ORDER BY count(*) DESC"
        return self.GetQuery(query)