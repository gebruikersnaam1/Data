import datetime

class Applicant:
    FirstName = "Piet"
    Affix = "van der"
    LastName = "Melkboer"
    Gender = "Man"
    ZipCode = "3085"
    DateOfBirth = "2010-01-01"

    def SetValues(self,firstName : str,affix : str,lastname : str,gender :str,zipCode : int, dateOfBirth):
        self.FirstName = self.FilterName(firstName)
        if affix != "":
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
        try:
            z = int(zipCode)
            if z > 999 and z < 10000:
                return z
            else:
                return None
        except:
            return None
    
    def FilterDateOfBirth(self,birthDate):
        try:
            year,month,day = birthDate.split('-')
            nBirthDate = datetime.datetime(int(year),int(month),int(day))
            print(nBirthDate)
            if (nBirthDate.year > datetime.datetime.now().year - int(18)):
                return birthDate
            else:
                return None
        except:
            return None
        