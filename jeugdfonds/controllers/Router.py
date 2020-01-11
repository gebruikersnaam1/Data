from jeugdfonds.controllers.ApplicantsController import ApplicantsController
from jeugdfonds.controllers.MapController import MapController
from jeugdfonds.controllers.ChartController import ChartController

class Router:

    def GetController(name):
        c = ApplicantsController() 
        if name == "map":
            return MapController(c.GetRequestedApplicants())
        elif name == "chart":
            return ChartController(c.GetRequestedApplicants())
        else:
            return None
            