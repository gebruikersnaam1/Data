from jeugdfonds.controllers.components.Deelgemeente import Deelgemeente
from jeugdfonds.models.ApplicantsModel import ApplicantsModel

class ApplicantsController:

    def GetApplicants(self):
        a = ApplicantsModel()
        return a.GetApplicantsAreaInfo()

    def GetDeelgemeentesArray(self):
        applicants = self.GetApplicants()
        Deelgemeentes = []
        for a in applicants:
            Deelgemeentes.append(Deelgemeente(a[0],(a[1],a[2]),a[3],a[4]))
        return Deelgemeentes
