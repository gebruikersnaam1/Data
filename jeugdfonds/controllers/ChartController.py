import json

class ChartController:
    

    def __init__(self, gemeentes):
        self.listGemeentes = gemeentes

    def ConvertListToJSON(self,lst):
        lst = str(json.dumps(lst))
        lst = lst.replace("{", "' { ")
        lst = lst.replace("'", "")
        return lst
    def GetApplicantsCountJSON(self):
        lst = []
        for g in self.listGemeentes:
            row = {"applicants": g.applicants, "deelgemeente" : g.areaName}
            lst.append(row)
        return self.ConvertListToJSON(lst)