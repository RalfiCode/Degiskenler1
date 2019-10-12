personeller = [
    {"ID": 1,
     "FirstName": "Ralfi",
     "LastName": "Bahar",
     "Phone": "05399125147",
     "Mail": "ralficode@hotmail.com"
     },
    {
        "ID": 2,
        "FirstName": "Meri",
        "LastName": "Istiroti",
        "Phone": "05325487653",
        "Mail": "meri@meriistiroti.com"
    }
]
#print(personeller[0])
#print(personeller[1])
#print(personeller[:])
#print(personeller[0:])
#print(personeller[0:2])
#print(personeller[0]["FirstName"])
yeniPersonel ={
        "ID" : 3,
        "FirstName": "Ahmet",
        "LastName": "Akın",
        "Phone": "05325487654",
        "Mail": "ahmet.şahin@gmail.com"
   }

personeller.append(yeniPersonel)
print(personeller[len(personeller)-1])
print("Personelin Adı: {}\nPersonal Soyadı: {}\nPersonelin Telefon:{}\nPersonel Mail: {}".format(personeller[0]["FirstName"], personeller[0]["LastName"], personeller[0]["Phone"], personeller[0]["Mail"]))
