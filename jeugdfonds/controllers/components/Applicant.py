class Applicant:
    FirstName = ""
    Affix = ""
    LastName = ""
    Gender = ""
    ZipCode = ""
    DateOfBirth = ""

    def SetValues(self,firstName : str,affix : str,lastname : str,gender :str,zipCode : int, dateOfBirth):
        if self.AreValuesValid(firstName,affix,lastname,gender,zipCode,dateOfBirth):
            self.FirstName = firstName
            self.Affix = affix
            self.LastName = lastname
            self.Gender = gender
            self.ZipCode = zipCode
            self.DateOfBirth = dateOfBirth
    
    def AreValuesValid(self,firstName : str,affix : str,lastname : str,gender :str,zipCode : int, dateOfBirth):
        errors = []
        errors.append(self.ValidateName(firstName))
        if affix == "":
            errors.append(self.ValidateName(affix))
        errors.append(self.ValidateName(lastname))
        errors.append(self.ValidateGender(gender))
        errors.append(self.ValidateZipCode(zipCode))
        errors.append(self.ValidateDateOfBirth(dateOfBirth))
        if False in errors:
            return False
        return True

    def ValidateName(self,name):
        if(name.replace(" ", "").isalpha()):
            return True
        return False
    
    def ValidateGender(self,gender):
        if gender == "Man" or gender == "Vrouw":
            return True
        return False
    
    def ValidateZipCode(self):
        if (isinstance(zipCode),int):
            return True
        return False
    
    def ValidateDateOfBirth(self,birthDate):
        try:
            day,month,year = birthDate.split('-')
            nBirthDate = datetime.datetime(int(year),int(month),int(day))
            if (nBirthDate.year > datetime.datetime.now().year - int(10)):
                return True
            else:
                return False
        except:
            return False
        