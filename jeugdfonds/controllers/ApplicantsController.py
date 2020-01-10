from jeugdfonds.controllers.components.Deelgemeente import Deelgemeente
from jeugdfonds.models.ApplicantsModel import ApplicantsModel
import datetime
from flask import request

class ApplicantsController:
    minAge = 4
    maxAge = 18
    gender = "%%" #gender 

    def GetAllApplicants(self):
        a = ApplicantsModel()
        applicants = a.GetUnhelpedApplicantsInfo()
        return self.GetDeelgemeentesArray(applicants)

    def GetGenderValue(self):
        try: 
            if request.form['gender'] == "Vrouw" or request.form['gender'] == "Man":
                return request.form['gender']
            else:
                return "%%"
        except:
            return "%%"

    def GetBirthOfAge(self,age : int, month : str, day : str):
        year = (str(datetime.datetime.now().year - int(age)))
        birth = "{y}-{m}-{d}".format(y=year,m=month,d=day)
        return birth

    def GetPostValues(self): 
        try:
            gender = self.GetGenderValue()  
            minAge = self.GetBirthOfAge(request.form['minAge'],"01","01")
            maxAge = self.GetBirthOfAge(request.form['maxAge'],"12","31")
            return gender,minAge,maxAge
        except:
            return "%%","1900-01-01","3000-01-01"

    def GetFilterdApplicants(self):
        a = ApplicantsModel()
        gender, minAge, maxAge = self.GetPostValues()
        applicants = a.GetUnhelpedApplicantsWithSearchTerms(gender, minAge, maxAge)
        return self.GetDeelgemeentesArray(applicants)
    
    def GetDeelgemeentesArray(self,applicants):
        Deelgemeentes = []
        for a in applicants:
            Deelgemeentes.append(Deelgemeente(a[0],(a[3],a[4]),a[1],a[2]))
        return Deelgemeentes

    def GetRequestedApplicants(self):
        if request.method == "POST":
            return self.GetFilterdApplicants() 
        else:
            return self.GetAllApplicants()
