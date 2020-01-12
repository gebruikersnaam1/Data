from jeugdfonds.controllers.components.Applicant import Applicant
from flask import request

class FormController:
    message = ""

    def __init__(self):
        self.Applicant = Applicant()
        if request.method == "POST":
            self.InsertApplicant()

    def InsertApplicant(self):
        return True
