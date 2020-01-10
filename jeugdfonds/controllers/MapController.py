from jeugdfonds.controllers.components.MapItem import MapItem

class MapController:
    areaNames = ["Overschie","Hillegersberg-Schiebroek","Prins Alexander","Noord","Kralingen-Crooswijk",
                      "Delfshaven","Centrum","Charlois","Feijenoord","Ijsselmonde","Rozenburg","Hoogvliet","Pernis","Hoek van Holland"]
    listGemeentes = []

    def __init__(self, gemeentes):
        self.listGemeentes = gemeentes
    
    def GetMapItems(self):
        mapItems = []
        for g in self.listGemeentes:
            try:
                indexValue = self.areaNames.index(g.areaName)
                mapItems.append(MapItem(indexValue,((g.areaName.replace(" ",""))+"style"),g))
            except:
                print("Area not found in list")
        return sorted(mapItems, key = lambda i: i.listOrder) 
    