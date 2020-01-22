from jeugdfonds.controllers.components.MapItem import MapItem
from jeugdfonds.controllers.components.Deelgemeente import Deelgemeente
from flask import request

class MapController:
    areaNames = ["Overschie","Hillegersberg-Schiebroek","Prins Alexander","Noord","Kralingen-Crooswijk",
                      "Delfshaven","Centrum","Charlois","Feijenoord","Ijsselmonde","Rozenburg","Hoogvliet","Pernis","Hoek van Holland"]
    listGemeentes = []
    MapItems = []
    MinAge = 4
    MaxAge = 18
    SelectedValues = {"minAge" : MinAge, "maxAge" : MaxAge, "gender": "%%", "status": "False"}
    totalPeople = {"intermediaries": 0,"applicants": 0}

    def __init__(self, gemeentes):
        self.listGemeentes = gemeentes
        self.SetSelectedValues()
        self.MapItems = self.CreateMapItems()
        
    def SetSelectedValues(self): 
        try:
            self.SelectedValues['minAge'] = int(request.form['minAge'])
            self.SelectedValues['maxAge'] = int(request.form['maxAge'])
            self.SelectedValues['gender'] = str(request.form['gender'])
            self.SelectedValues['status'] = str(request.form['status'])
        except:
            self.SelectedValues['minAge'] = self.MinAge
            self.SelectedValues['maxAge'] = self.MaxAge
            self.SelectedValues['gender'] = "%%"
            self.SelectedValues['status'] = "False"

            
    def CreateMapItems(self):
        mapItems = []
        areasFound = []
        for g in self.listGemeentes:
            try:
                indexValue = self.areaNames.index(g.areaName)
                areasFound.append(indexValue)
                mapItems.append(MapItem(indexValue,((g.areaName.replace(" ",""))+"style"),g))
            except:
                print("Area not found in list")
        return self.CreatePlaceholders(mapItems,areasFound)
    
    #if an area has no applicants then the area won't show up
    #hence a placeholder will be created
    def CreatePlaceholders(self,mapItems,areasFound):
        for i in range(0,len(self.areaNames)):
            if i not in areasFound:
                g = Deelgemeente(self.areaNames[i],(0,0),0,0)
                mapItems.append(MapItem(i,((g.areaName.replace(" ",""))+"style"),g))
        return mapItems

    def GetMapItems(self):
        return sorted(self.MapItems, key = lambda i: i.listOrder) 
    