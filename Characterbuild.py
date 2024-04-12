class character:
    def __init__(self):
        self.setAttributes()
        self.initSkills()
        self.setSkils()
        self.health = self.level * (self.hpAveage + self.getBonus(self.con))
        

    def setAttributes(self):
        self.speed = int(input("Input character Speed: "))
        self.level = int(input("Input character level: "))
        self.hpAveage = int(input("Input character Average level-up HP: "))
        

        self.str = int(input("Input character STR: "))
        self.dex = int(input("Input character Dex: "))
        self.con = int(input("Input character Con: "))
        self.int = int(input("Input character Int: "))
        self.wis = int(input("Input character Wis: "))
        self.cha = int(input("Input character Cha: "))
        self.ProficiencyBonus = int(input("Input character Proficiency Bonus: "))


        self.name = str(input("Input character Name :"))
        self.race = str(input("Input character race: "))
        self.characterClass = str(input("Input character Class: "))
        

    def initSkills(self):
        strSkills = {"Athletics": self.getBonus(self.str)}
        dexSkills = {"Acrobatics": self.getBonus(self.dex), "Sleight of Hand": self.getBonus(self.dex), "Stealth" : self.getBonus(self.dex)}
        intSkills = {"Arcana" : self.getBonus(self.int), "History" : self.getBonus(self.int),"Investigation" : self.getBonus(self.int),"Nature" : self.getBonus(self.int), "Religion" : self.getBonus(self.int)}
        wisSkills = {"Animal Handling" : self.getBonus(self.wis), "Insight" : self.getBonus(self.wis), "Medicine" : self.getBonus(self.wis), "Perception" : self.getBonus(self.wis), "Survival" : self.getBonus(self.wis)}
        chaSkils = {"Deception" : self.getBonus(self.cha), "Performance" : self.getBonus(self.cha), "Intimidation" : self.getBonus(self.cha), "Persuasion" : self.getBonus(self.cha)}

        self.skills = strSkills | dexSkills | intSkills | wisSkills | chaSkils
        self.savingThrows = {"Strength": self.getBonus(self.str), "Dexterity": self.getBonus(self.dex), "Constitution": self.getBonus(self.con), "Intelligence" : self.getBonus(self.int), "Wisdom": self.getBonus(self.wis), "Charisma": self.getBonus(self.cha)}



    def getBonus(self, skill):
        return (skill//2) - 5

    def setSkils(self):
        inp = ""
        while inp != "quit":
            inp = str(input("Please enter skill: "))
            if inp in self.skills.keys():
                self.skills[inp] += self.ProficiencyBonus
            else: 
                print("Error | Invalid skill.")

        inp = ""
        while inp != "quit":
            inp = str(input("Please enter Saving Throw: "))
            if inp in self.savingThrows.keys():
                self.savingThrows[inp] += self.ProficiencyBonus
            else: 
                print("Error | Invalid saving throw.")

    def writeStats(self):
        fp = open(self.name + "CharacterSheet.txt", "w")
        savingThrows = ["Strength", "Dexterity","Constitution", "Intelligence", "Wisdom","Charisma"]
        skills = ["Athletics", "Acrobatics", "Sleight of Hand", "Stealth", "Arcana", "History", "Investigation", "Nature", "Religion",  "Animal Handling",  "Insight", "Medicine", "Perception", "Survival",
        "Deception", "Intimidation", "Performance", "Persuasion"]
        wrString = "{}\n{}\n{}\n".format(self.name, self.characterClass, self.race)
        wrString += "------------------------------------------------------------\n"
        wrString += "Armor Class: \nSpeed: {}\nInitiative: \nHealth: {}\nCurrent Health: \n".format(self.speed, self.health)
        wrString += "------------------------------------------------------------\n"
        wrString += "Str: {}\nDex: {}\nCon: {}\nInt: {}\nWis {}\nCha {}\n".format(self.str, self.dex, self.con, self.int, self.wis, self.cha)
        wrString += "------------------------------------------------------------\n"
        wrString += "Saving Throws\n--\n"

        for val in savingThrows:
            wrString += "{}: {}\n".format(val, self.savingThrows[val])

        wrString += "------------------------------------------------------------\nSkills\n--\n"

        for val in self.skills.keys():
            wrString += "{}: {}\n".format(val, self.skills[val])

        wrString += "------------------------------------------------------------\n"
        wrString += "Attacks\n"
        wrString += "--\n"
        wrString += "Attack Type: \n"
        wrString += "Attack Bonus: \n"
        wrString += "Damage:\n"
        wrString += "Description\n\n\n"
        wrString += "--\n"
        wrString += "------------------------------------------------------------\n"

        wrString += "Misc Proficiencies\n--\n"
        wrString += "Proficiency: \n"
        wrString += "--\n------------------------------------------------------------\n"


        wrString += "Traits\n------------------------------------------------------------\nTrait: \n--\nDescription\n\n\n--\n------------------------------------------------------------\n"

        wrString += "Equipment\n------------------------------------------------------------\nItem: \n--\nDescription\n\n\n--\n------------------------------------------------------------\n"

        wrString += "------------------------------------------------------------\n"
        wrString += "Spells\n"
        wrString += "--\n"
        wrString += "-\n"
        wrString += "Spell: \n"
        wrString += "Description:\n\n\n"
        wrString += "-\n"
        wrString += "--\n"
        wrString += "------------------------------------------------------------\n"

        wrString +="Spell slots:\n1: \n2: \n3: \n4: \n5: \n6: \n7: \n8: \n9: \n"

        wrString +="Used Spell slots:\n1: \n2: \n3: \n4: \n5: \n6: \n7: \n8: \n9: \n"

        fp.write(wrString)
        fp.close()





        


def main():
    z = character()
    z.writeStats()
    pass


if __name__ == "__main__":
    main()