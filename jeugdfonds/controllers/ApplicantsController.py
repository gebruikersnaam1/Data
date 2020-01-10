from jeugdfonds.controllers.components.Deelgemeente import Deelgemeente
from jeugdfonds.models.ApplicantsModel import ApplicantsModel
from flask import request

class ApplicantsController:
    minAge = 4
    maxAge = 18
    gender = "%%" #gender 

    def GetAllApplicants(self):
        a = ApplicantsModel()
        applicants = a.GetApplicantsInfo()
        return self.GetDeelgemeentesArray(applicants)

    def GetPostValues(self):
        return self.GetAllApplicants()

    def GetFilterdApplicants(self):
        return self.GetAllApplicants()
    
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
