from jeugdfonds.controllers.components.MapItem import MapItem
from flask import request

class MapController:
    areaNames = ["Overschie","Hillegersberg-Schiebroek","Prins Alexander","Noord","Kralingen-Crooswijk",
                      "Delfshaven","Centrum","Charlois","Feijenoord","Ijsselmonde","Rozenburg","Hoogvliet","Pernis","Hoek van Holland"]
    listGemeentes = []
    MinAge = 4
    MaxAge = 18
    SelectedValues = {"minAge" : MinAge, "maxAge" : MaxAge, "gender": "%%"}

    def __init__(self, gemeentes):
        self.listGemeentes = gemeentes
        self.SetSelectedValues()
    
    def SetSelectedValues(self): 
        try:
            self.SelectedValues['minAge'] = int(request.form['minAge'])
            self.SelectedValues['maxAge'] = int(request.form['maxAge'])
            self.SelectedValues['gender'] = str(request.form['gender'])
        except:
            self.SelectedValues['minAge'] = self.MinAge
            self.SelectedValues['maxAge'] = self.MaxAge
            self.SelectedValues['gender'] = "%%"
    
    def GetMapItems(self):
        mapItems = []
        for g in self.listGemeentes:
            try:
                indexValue = self.areaNames.index(g.areaName)
                mapItems.append(MapItem(indexValue,((g.areaName.replace(" ",""))+"style"),g))
            except:
                print("Area not found in list")
        return sorted(mapItems, key = lambda i: i.listOrder) 
    