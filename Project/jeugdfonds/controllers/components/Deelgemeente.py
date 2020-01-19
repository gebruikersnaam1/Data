class Deelgemeente:
    areaName = ""
    zipCodeRange = tuple()
    applicants = 0
    intermediary = 0 

    def __init__(self,areaName : str, zipCodeRange : tuple, applicants : int, intermediary : int):
        self.areaName = areaName
        self.zipCodeRange = zipCodeRange
        self.applicants = applicants
        self.intermediary = intermediary