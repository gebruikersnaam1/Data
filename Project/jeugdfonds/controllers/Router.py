from jeugdfonds.controllers.ApplicantsController import ApplicantsController
from jeugdfonds.controllers.MapController import MapController
from jeugdfonds.controllers.ChartController import ChartController
from jeugdfonds.controllers.FormController import FormController

class Router:

    def GetController(name):
        c = ApplicantsController() 
        if name == "map":
            return MapController(c.GetRequestedApplicants())
        elif name == "form":
            return FormController()
        elif name == "chart":
            return ChartController(c.GetRequestedApplicants())
        else:
            return None
            