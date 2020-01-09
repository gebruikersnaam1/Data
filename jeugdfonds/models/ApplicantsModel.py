from jeugdfonds.models.Connector import Connector

class ApplicantsModel(Connector):

    def GetApplicantsPerArea(self):
        query = "SELECT z.Area, (SELECT COUNT(*) FROM Applicant as A WHERE z.MinValue <= a.Zipcode and z.MaxValue >= a.Zipcode) as applicants, z.MinValue, z.MaxValue FROM ZipCode as Z ORDER BY applicants DESC"
        return self.GetQuery(query)
    
    def GetApplicantsInfo(self):
        query = "SELECT z.Area, (SELECT COUNT(*) FROM Applicant as A WHERE z.MinValue <= a.Zipcode and z.MaxValue >= a.Zipcode) as applicants,(SELECT COUNT(*) FROM Intermediair as i WHERE z.MinValue <= i.Zipcode and z.MaxValue >= i.Zipcode) as intermediairs, z.MinValue, z.MaxValue FROM ZipCode as Z ORDER BY applicants DESC"
        return self.GetQuery(query)