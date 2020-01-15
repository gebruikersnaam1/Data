from jeugdfonds.controllers.components.Applicant import Applicant
from jeugdfonds.models.ApplicantsModel import ApplicantsModel
from flask import request, Markup

class FormController:
    Message = ""
    FirstName = ""
    Affix = ""
    LastName = ""
    Gender = ""
    ZipCode = ""
    DateOfBirth = ""

    def __init__(self):
        self.Applicant = Applicant()
        if request.method == "POST":
            self.SetPostValues()
    
    def SetPostValues(self):
        p = [request.form['firstname'],request.form['affix'],request.form['lastname'],request.form['gender'],request.form['zipcode'],request.form['dateofbirth']]
        self.Applicant.SetValues(p[0],p[1],p[2],p[3],p[4],p[5])
        
        if self.IsSendValuesValid() == True:
            a = ApplicantsModel()
            self.Message = a.InsertApplicant(self.FirstName, self.Affix, self.LastName,self.Gender,self.ZipCode, self.DateOfBirth)
        else:
            self.Message = Markup(self.Message)
    
    def IsSendValuesValid(self):
        noErrors = True
        self.Message = ""

        if self.Applicant.FirstName == None:
            noErrors, self.Applicant.FirstName = self.ErrorChecking("Firstname")
        if self.Applicant.LastName == None:
            noErrors, self.Applicant.LastName = self.ErrorChecking("Lastname")
        if self.Applicant.Gender == None:
            noErrors, self.Applicant.Gender = self.ErrorChecking("Gender")
        if self.Applicant.ZipCode == None:
            noErrors, self.Applicant.ZipCode = self.ErrorChecking("Zipcode")
        if self.Applicant.DateOfBirth == None:
            noErrors, self.Applicant.DateOfBirth = self.ErrorChecking("Date of birth")
        return noErrors

    def ErrorChecking(self, fieldName):
        self.Message += self.ErrorMessages(fieldName)
        return False, ""

    def ErrorMessages(self, field):
        return "The inserted value of field '" + field + "' is invalid<br/>"

    def InsertApplicant(self):
        return True
