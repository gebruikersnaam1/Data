class Applicant:
    FirstName = ""
    Affix = ""
    LastName = ""
    Gender = ""
    ZipCode = ""
    DateOfBirth = ""

    def SetValues(self,firstName : str,affix : str,lastname : str,gender :str,zipCode : int, dateOfBirth):
        self.FirstName = self.FilterName(firstName)
        if affix == "":
            self.Affix = self.FilterName(affix)
        self.LastName = self.FilterName(lastname)
        self.Gender = self.FilterGender(gender)
        self.ZipCode = self.FilterZipCode(zipCode)
        self.DateOfBirth = self.FilterDateOfBirth(dateOfBirth)

    def FilterName(self,name):
        if(name.replace(" ", "").isalpha()):
            return name
        return None
    
    def FilterGender(self,gender):
        if gender == "Man" or gender == "Vrouw":
            return gender
        return None
    
    def FilterZipCode(self,zipCode):
        if type(zipCode) == int:
            return zipCode
        return None
    
    def FilterDateOfBirth(self,birthDate):
        try:
            day,month,year = birthDate.split('-')
            nBirthDate = datetime.datetime(int(year),int(month),int(day))
            if (nBirthDate.year > datetime.datetime.now().year - int(18)):
                return birthDate
            else:
                return None
        except:
            return None
        