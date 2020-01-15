from jeugdfonds.controllers.components.Applicant import Applicant
from flask import request

class FormController:
    message = ""

    def __init__(self):
        self.Applicant = Applicant()
        if request.method == "POST":
            self.SetPostValues()
    
    def SetPostValues(self):
        p = [request.form['firstname'],request.form['affix'],request.form['lastname'],request.form['gender'],request.form['zipcode'],request.form['dateofbirth']]
        self.Applicant.SetValues(p[0],p[1],p[2],p[3],p[4],p[5])
        
    def AreTheFormValues(self):
        return
    def InsertApplicant(self):
        return True
