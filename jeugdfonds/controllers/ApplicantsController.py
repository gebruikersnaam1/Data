from jeugdfonds.controllers.components.Deelgemeente import Deelgemeente
from jeugdfonds.models.ApplicantsModel import ApplicantsModel

class ApplicantsController:

    def GetAllApplicants(self):
        a = ApplicantsModel()
        applicants = a.GetApplicantsInfo()
        return self.GetDeelgemeentesArray(applicants)

    def GetDeelgemeentesArray(self,applicants):
        Deelgemeentes = []
        for a in applicants:
            Deelgemeentes.append(Deelgemeente(a[0],(a[3],a[4]),a[1],a[2]))
        return Deelgemeentes
