from jeugdfonds.controllers.components.Deelgemeente import Deelgemeente
import os.path

class MapItem:

    def __init__(self, listOrder : int, className : str, deelgemeente : Deelgemeente):
        self.listOrder = listOrder
        self.className = className
        self.deelgemeente = deelgemeente

    def GetImage(self):
        if self.deelgemeente.applicants < 500:
            return "static/img/map/"+self.deelgemeente.areaName+"-GREEN.png"
        elif self.deelgemeente.applicants < 1500:
            return "static/img/map/"+self.deelgemeente.areaName+"-ORANGE.png"
        else:
            return "static/img/map/"+self.deelgemeente.areaName+"-RED.png"
