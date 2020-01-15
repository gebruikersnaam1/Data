from jeugdfonds.controllers.components.Applicant import Applicant
from jeugdfonds.models.ApplicantsModel import ApplicantsModel
from flask import request, Markup, redirect

class FormController:
    Message = ""
    entered = False

    def __init__(self):
        self.Applicant = Applicant()
        if request.method == "POST":
            self.SetPostValues()

    def SetPostValues(self):
        p = [request.form['firstname'],request.form['affix'],request.form['lastname'],request.form['gender'],request.form['zipcode'],request.form['dateofbirth']]
        self.Applicant.SetValues(p[0],p[1],p[2],p[3],p[4],p[5])
        
        if self.IsSendValuesValid() == True:
            self.InsertFormData()
        else:
            self.Message = Markup(self.Message)
    
    def InsertFormData(self):
        a = ApplicantsModel()
        a.InsertApplicant(self.Applicant.FirstName, self.Applicant.Affix, self.Applicant.LastName,self.Applicant.Gender,self.Applicant.ZipCode, self.Applicant.DateOfBirth)
        self.Message = "Applicant inserted!"
        self.entered = True

        #if redirect fails, pressing the send button won't work (crtl+r will work)
        self.Applicant = Applicant()
        self.Message = "A new applicant has been entered"


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
