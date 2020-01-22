import json
from flask import request

class ChartController:
    

    def __init__(self, gemeentes):
        self.listGemeentes = gemeentes

    #json.dumps doesn't give the correct format, hence replace is needed
    def ConvertListToJSON(self,lst):
        lst = str(json.dumps(lst))
        lst = lst.replace("{", "' { ")
        lst = lst.replace("'", "")
        return lst
    
    def GetApplicantsList(self,breakpoint):
        lst = []
        for g in self.listGemeentes:
            row = {"applicants": g.applicants, "deelgemeente" : g.areaName}
            lst.append(row)
            if len(lst) == breakpoint:
                break
        return lst

    def GetBreakPoint(self):
        try:
            breakpoint = int(request.args.get('breakpoint'))
            return breakpoint
        except:
            return 5
    
    def GetApplicantsCountJSON(self):
        lst = self.GetApplicantsList(self.GetBreakPoint())
        return self.ConvertListToJSON(lst)
    