from jeugdfonds.controllers.components.Deelgemeente import Deelgemeente

class MapItem:

    def __init__(self, listOrder : int, className : str, deelgemeente : Deelgemeente):
        self.listOrder = listOrder
        self.className = className
        self.deelgemeente = deelgemeente
