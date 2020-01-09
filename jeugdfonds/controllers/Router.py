from jeugdfonds.controllers.ApplicantsController import ApplicantsController
from jeugdfonds.controllers.MapController import MapController


class Router:

    def GetController(name):
        if name == "map":
            c = ApplicantsController()
            return MapController(c.GetAllApplicants())
        else:
            return None
            