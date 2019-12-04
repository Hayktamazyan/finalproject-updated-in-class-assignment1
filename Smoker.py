import os.path
import json
import os
class Smoker(object):
    def __init__(self):
        if(os.path.exists('./data.json')):
            with open('data.json') as data_file:
                data = json.load(data_file)
            self.smokerData = data["smoked_packs"]
            user_info= data["user_info"]
            asciihash=user_info["name"]
            name=""
            for i in asciihash:
                name+=chr(int(i))
            self.smokerName=name
        else:
            self.createNewSmokerProfile()

    def saveData(self):
        file = open("data.json", "w")
        file.write(json.dumps({
                "smoked_packs" : self.smokerData,
                "user_info" : self.smokerAscii
            }))
        file.close()

    def getTotalStatistics(self):
        total_money = 0.0
        total_nicotine = 0.0
        total_packs_count = 0
        for cigarette in self.smokerData:
            total_money += float(cigarette["price"]) * int(cigarette["count"])
            total_nicotine += float(cigarette["nicotine"]) * int(cigarette["count"])
            total_packs_count += int(cigarette["count"])
        return (total_money,total_nicotine,total_packs_count)

    def addPacksCount(self, count):
        self.smokerData[len(self.smokerData) - 1]["count"] += count
        self.saveData()
    
    def addCiggaretType(self,price,nicotine):
        self.smokerData.append({
            "price": price,
            "nicotine": nicotine,
            "count": 0
        })
        self.saveData()

    def deleteData(self):
        os.remove("data.json")
    def getName(self):
        return self.smokerName
    def createNewSmokerProfile(self):
        if(os.path.exists('./data.json')):
            os.remove("data.json")
            
        price = float (input ("     Input you cigarette price in drams: "))
        nicotine = float (input ("     Input you cigarette nicotine in milligrams: "))
        name = str (input ("     Input Name: "))
        asciihash=[]
        for i in range(len(name)):
            asciihash+=[(str(ord(name[i])))]
        self.smokerData = [{"price": price, "nicotine": nicotine, "count": 0}]
        self.smokerAscii ={"name": asciihash}
        self.smokerName=name
        self.saveData()