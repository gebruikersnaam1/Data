from Converter import CsvConvertToDB #import 

while True:
    print("What do you want do? \n \n ")
    result = int(input("1) Import database \n 2) show database "))
    if result == 1:
        query = CsvConvertToDB.RunConvertor('Applicants.csv',';','Jeugdfonds', 'applicant')
    else:
        print("...")