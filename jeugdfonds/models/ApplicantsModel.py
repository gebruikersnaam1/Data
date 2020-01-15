from jeugdfonds.models.Connector import Connector
from datetime import date

class ApplicantsModel(Connector):
    
    def GetUnhelpedApplicantsInfo(self,endYear):
        query = '''
                SELECT z.Area, count(*) as applicants,
                (SELECT COUNT(*) FROM Intermediair as i WHERE z.MinValue <= i.Zipcode and z.MaxValue >= i.Zipcode) as intermediairs, 
                z.MinValue, z.MaxValue 
                FROM Applicant as a INNER JOIN Zipcode as z ON (z.MinValue <= a.Zipcode and z.MaxValue >= a.Zipcode)
                INNER JOIN Project as P ON p.ApplicantsID = a.ID AND p.Approved = 'False' 
                WHERE a.DateOfBirth > '{qDate}'
                GROUP BY z.Area ORDER BY count(*) DESC
                '''.format(qDate=endYear)
        return self.GetQuery(query)

    def GetUnhelpedApplicantsWithSearchTerms(self, gender : str, minAge : date, maxAge : date, approved : bool):
        query = '''
                SELECT z.Area, count(*) as applicants,(SELECT COUNT(*) FROM Intermediair as i WHERE z.MinValue <= i.Zipcode and z.MaxValue >= i.Zipcode) as intermediairs, 
                z.MinValue, z.MaxValue FROM Applicant as a INNER JOIN Zipcode as z ON (z.MinValue <= a.Zipcode and z.MaxValue >= a.Zipcode) 
                INNER JOIN Project as P ON p.ApplicantsID = a.ID AND p.Approved = '{qApproved}' 
                WHERE a.Gender like '{qGender}' AND a.DateOfBirth > '{qMaxAge}' AND a.DateOfBirth < '{qMinAge}'  
                GROUP BY z.Area ORDER BY count(*) DESC 
                '''.format(qGender=gender, qMinAge=minAge,qMaxAge=maxAge,qApproved = approved)
        return self.GetQuery(query)

    def InsertApplicant(self,firstname: str,affix:str,lastname:str,gender:str,zipcode:int,birthDate : date):
        query = '''
            INSERT INTO Applicant (ID,FirstName,Affix,lastname,DateOfBirth,ZipCode,Gender) 
            VALUES((SELECT (ID+1) FROM Applicant ORDER BY ID DESC LIMIT 1),'{qFirstName}','{qAffix}','{qLastname}','{qDate}','{qZipCode}','{qGender}');
            '''.format(qFirstName=firstname,qAffix=affix,qLastname=lastname,qDate = birthDate, qZipCode = zipcode,qGender = gender)
        return self.RunCreateQuery(query)
