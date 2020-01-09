class Deelgemeente:
    areaName = ""
    zipCodeRange = tuple()
    applicants = 0
    intermediair = 0 

    def __init__(self,areaName : str, zipCodeRange : tuple, applicants : int, intermediair : int):
        self.areaName = areaName
        self.zipCodeRange = zipCodeRange
        self.applicants = applicants
        self.intermediair : int