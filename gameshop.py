import random

import colorama
from colorama import Fore

colorama.init()

from pyfiglet import Figlet

figlet = Figlet(font="Starwars")
print(figlet.renderText("Hra"))


money = 699
inventory = []


def CheckIfinInventory(item):
    for _item in inventory:
        if isinstance(_item, item):
            return True
        return False


def getValueFromList(message: str, list: list):
    while True:
        value = input(message)

        if value in list:
            return value

        print(Fore.RED + " ❌ Musíš zadat Správny Vstup!" + "\033[39m")

def AdvancedSellingSystem(inventory, item):
    item: str

    inventory = [item]

    if item in inventory:
        if inventory.count(item) == 0:
            return
        if inventory.count(item) == 1:
            return
        if inventory.count(item) > 1:
            print("Nalezl jsem vícekrát stejny predmet")

            for index in item:
                print(f"{index + 1}. {item}")
                prodavani = input("Co Chces prodat? ")
            
    
class Zbroj:
    defense: int
    price: int
    name: str
    health: int

    def __init__(
        self,
        defense,
        price,
        name,
    ):
        self.defense = defense
        self.price = price
        self.name = name

    def dejDamage(self, enemy):
        enemy.hp -= self.defense

    def nabrousit(self):
        self.defense += 0


class HusitskaZbroj(Zbroj):

    def __init__(self):
        super().__init__(defense=30, price=400, name="Husitska Zbroj")

    def HusitskaZbrojInformace(self):
        print("")
        print("Informace o" + str(self.name))
        print("Defense:" + str(self.defense))
        print("Cena:" + str(self.price))
        print("")

    def __str__(self) -> str:
        return self.name


class RimskaZbroj(Zbroj):

    def __init__(self):
        super().__init__(defense=50, price=800, name="Rimska Zbroj")

    def RimskaZbrojInformace(self):
        print("")
        print("Informace o" + str(self.name))
        print("Defense: " + str(self.defense))
        print("Cena: " + str(self.price))
        print("")

    def __str__(self) -> str:
        return self.name


class KumanskaZbroj(Zbroj):

    def __init__(self):
        super().__init__(defense=70, price=1200, name="Kumanska Zbroj")

    def KumanskaZbrojInformace(self):
        print("")
        print("informace o" + str(self.name))
        print("Defense: " + str(self.defense))
        print("Cena: " + str(self.price))
        print("")

    def __str__(self) -> str:
        return self.name


class GermanskaZbroj(Zbroj):

    def __init__(self):
        super().__init__(defense=100, price=1600, name="Germanska Zbroj")

    def GermanskaZbrojInformace(self):
        print("")
        print("Informace o" + str(self.name))
        print("Defense: " + str(self.defense))
        print("Cena: " + str(self.price))
        print("")

    def __str__(self) -> str:
        return self.name


class VelkoMoravskaZbroj(Zbroj):

    def __init__(self):
        super().__init__(defense=130, price=2000, name="VelkoMoravska Zbroj")

    def VelkoMoravskaZbrojinformace(self):
        print("")
        print("Informace o " + str(self.name))
        print("Defense: " + str(self.defense))
        print("Cena: " + str(self.price))
        print("")

    def __str__(self) -> str:
        return self.name


def Kupbrneni():
    print("")
    print("✅ Uspesne si zavítal do obchodu s brnenim")
    print("Vyber Brneni")
    print("1) Husitska Zbroj - 400$")
    print("2) Rimska Zbroj - 800$")
    print("3) Kumanska Zbroj - 1200$")
    print("4) Germanska Zbroj - 1600$")
    print("5) VelkoMoravska Zbroj - 2000$")
    print("")
    print("Z) Zpet")

    def really():
        return (
            getValueFromList("Opravdu chces koupit Tuto Zbroj? (A/N): ", ["A", "N"])
            == "A".upper()
        )

    while True:
        val = getValueFromList("Vyber mecu: ", ["1", "2", "3", "4", "5", "Z"]).upper()

        if val == "Z":
            return None

        if val == "1":
            husitskejzbroj = HusitskaZbroj()
            husitskejzbroj.HusitskaZbrojInformace()
            if CheckIfinInventory(HusitskaZbroj):
                print(Fore.RED + " ❌ Nemuzes si tuto zbroj koupit nebot ji jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 400:
                    return HusitskaZbroj()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

        elif val == "2":
            rimskejzbroj = RimskaZbroj()
            rimskejzbroj.RimskaZbrojInformace
            if CheckIfinInventory(RimskaZbroj):
                print(Fore.RED + " ❌ Nemuzes si tuto zbroj koupit nebot ji jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 800:
                    return RimskaZbroj()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

        elif val == "3":
            kumanskejzbroj = KumanskaZbroj()
            kumanskejzbroj.KumanskaZbrojInformace()
            if CheckIfinInventory(KumanskaZbroj):
                print(Fore.RED + " ❌ Nemuzes si tuto zbroj koupit nebot ji jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 1200:
                    return KumanskaZbroj()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

        elif val == "4":
            germanskozbroj = GermanskaZbroj()
            germanskozbroj.GermanskaZbrojInformace()
            if CheckIfinInventory(GermanskaZbroj):
                print(Fore.RED + " ❌ Nemuzes si tuto zbroj koupit nebot ji jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 1600:
                    return GermanskaZbroj()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

        elif val == "5":
            velkomoravskebroj = VelkoMoravskaZbroj()
            velkomoravskebroj.VelkoMoravskaZbrojinformace()
            if CheckIfinInventory(VelkoMoravskaZbroj):
                print(Fore.RED + " ❌ Nemuzes si tuto zbroj koupit nebot ji jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 2000:
                    return VelkoMoravskaZbroj()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

# Mece
class Mec:
    damage: int
    price: int
    name: str

    def __init__(self, damage: int, price: int, name: str, health_sword: int):
        self.damage = damage
        self.price = price
        self.name = name
        self.health_sword = health_sword

    def dejDamage(self, enemy):
        enemy.hp -= self.damage

    def nabrousit(self):
        self.damage += 5


class TupyMec(Mec):
    def __init__(self):
        super().__init__(damage=10, price=200, name="Tupy Mec", health_sword=150)

    def TupyMecInformace(self):
        print("")
        print("Informace o " + self.name)
        print("Útok: " + Fore.RED + str(self.damage) + "\033[39m")
        print("Poškození: " + str(self.health_sword))
        print("Cena: " + Fore.LIGHTYELLOW_EX + str(self.price) + "$" + "\033[39m")
        print("")

    def __str__(self) -> str:
        return self.name + " " + str(self.damage)


class TureckaSavle(Mec):
    def __init__(self):
        super().__init__(damage=20, price=400, name="Turecka Savle", health_sword=200)

    def TureckaSavleInformace(self):
        print("")
        print("Informace o" + str(self.name))
        print("Útok: " + Fore.RED + str(self.damage) + "\033[39m")
        print("Poškození: " + str(self.health_sword))
        print("Cena: " + Fore.YELLOW + str(self.price) + "$" + "\033[39m")
        print("")

    def __str__(self) -> str:
        return self.name + " " + str(self.damage)


class NemeckyMec(Mec):
    def __init__(self):
        super().__init__(damage=30, price=700, name="Nemecky Mec", health_sword=250)

    def NemeckyMecInformace(self):
        print("")
        print("Informace o " + str(self.name))
        print("Utok: " + Fore.RED + str(self.damage) + "\033[39m")
        print("Poskozeni: " + str(self.health_sword))
        print("Cena: " + Fore.YELLOW + str(self.price) + "$" + "\033[39m")
        print("")

    def __str__(self) -> str:
        return self.name + " " + str(self.damage)


class CeskyMec(Mec):
    def __init__(self):
        super().__init__(damage=40, price=1000, name="Cesky Mec", health_sword=400)

    def CeskyMecInformace(self):
        print("")
        print("Informace o " + self.name)
        print("Utok: " + Fore.RED + str(self.damage) + "\033[39m")
        print("Poskozeni: " + str(self.health_sword))
        print("Cena: " + Fore.YELLOW + str(self.price) + "$" + "\033[39m")
        print("")

    def __str__(self) -> str:
        return self.name + " " + str(self.damage)


class MadarskyMec(Mec):
    def __init__(self):
        super().__init__(damage=50, price=1250, name="Madarskem Meci", health_sword=450)

    def MadarskyMecInformace(self):
        print("")
        print("Informace o " + self.name)
        print("Utok: " + Fore.RED + str(self.damage) + "\033[39m")
        print("Poskozeni: " + str(self.health_sword))
        print("Cena: " + Fore.YELLOW + str(self.price) + "$" + "\033[39m")
        print("")

    def __str__(self) -> str:
        return self.name + " " + str(self.damage)


def kupMec():
    print("")
    print("✅ Uspesne si zavítal do obchodu s meci")
    print("Vyber mecu")
    print("1) Mec Tupy - 200$")
    print("2) Turecka Savle - 400$")
    print("3) Nemecky Mec - 700$")
    print("4) Cesky Mec - 1000$")
    print("5) Madarsky mec - 1250$")
    print("")
    print("Z) Zpet")

    def really():
        return (
            getValueFromList("Opravdu chces koupit tento mec? (A/N): ", ["A", "N"])
            == "A".upper()
        )

    while True:
        val = getValueFromList("Vyber mecu: ", ["1", "2", "3", "4", "5", "Z"]).upper()

        if val == "Z":
            return None

        if val == "1":
            tupickejmec = TupyMec()
            tupickejmec.TupyMecInformace()
            if CheckIfinInventory(TupyMec):
                print(Fore.RED + " ❌ Nemuzes si tento mec koupit nebot ho jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 200:
                    return TupyMec()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

        elif val == "2":
            tureckejsavlec = TureckaSavle()
            tureckejsavlec.TureckaSavleInformace()
            if CheckIfinInventory(TupyMec):
                print(Fore.RED + " ❌ Nemuzes si tento mec koupit nebot ho jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 400:
                    return TureckaSavle()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

        elif val == "3":
            nemeckejmec = NemeckyMec()
            nemeckejmec.NemeckyMecInformace()
            if CheckIfinInventory(TupyMec):
                print(Fore.RED + " ❌ Nemuzes si tento mec koupit nebot ho jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 700:
                    return NemeckyMec()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

        elif val == "4":
            ceskejmec = CeskyMec()
            ceskejmec.CeskyMecInformace()
            if CheckIfinInventory(TupyMec):
                print(Fore.RED + " ❌ Nemuzes si tento mec koupit nebot ho jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 1000:
                    return CeskyMec()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")

        elif val == "5":
            madarskejmec = MadarskyMec()
            madarskejmec.MadarskyMecInformace()
            if CheckIfinInventory(TupyMec):
                print(Fore.RED + " ❌ Nemuzes si tento mec koupit nebot ho jiz mas v inventari" + "\033[39m")
                return None
            if really():
                if money >= 1250:
                    return MadarskyMec()
                else:
                    print(Fore.RED + " ❌ Nemas Dostatek Penez!" + "\033[39m")




def obchodnik():
    print(f"Vitej v obchode, mas {money} peněz")

    while True:
        val = getValueFromList(
            "1) Mece 2) Brneni 3) Prodej 4) Oprava 5) Konec: ",
            ["1", "2", "3", "4", "5"],
        )
        koupeno = None

        if val == "1":
            koupeno = kupMec()

        if val == "2":
            koupeno = Kupbrneni()

        if val == "3":
            Prodej().Prodavani()

        if val == "4":
            pass
        
        if val == "5":
            break
        
        if koupeno is not None:
            inventory.append(koupeno)
            print(f"Koupil jsi {koupeno}")
            koupeno = None


class Prodej:

    def __str__(self) -> str:
        return self.name 

    def Prodavani(self):
        print("Vítej v prodejne!")
                #Prodavani Mece
        print("")
        print("Mece")
        print("1) TupyMec - 100$")
        print("2) Turecka Savle - 200$")
        print("3) Nemecky Mec - 350$")
        print("4) Cesky Mec - 500$")
        print("5) Madarky mec - 625$")
        print("")
        print("Brneni")
        print("6) Husitská Zbroj - 200$")
        print("7) Rimska Zbroj - 400$")
        print("8) Kumanska Zbroj - 600$ ")
        print("9) Germánská Zbroj - 800$ ")
        print("10) Velkomoravská Zbroj - 1000$")
        print("")
        print("=====================================")
        print("Tvuj Inventar")
        print("")
        print("Mece: ")
        if CheckIfinInventory(TupyMec):
            print("Tupy Mec")
        if CheckIfinInventory(TureckaSavle):
            print("Turecka Savle")
        if CheckIfinInventory(NemeckyMec):
            print("Nemecky Mec")
        if CheckIfinInventory(MadarskyMec):
            print("Madarsky mec")
        print("")
        print("Brneni: ")
        if CheckIfinInventory(HusitskaZbroj):
            print("Husistka Zbroj")
        if CheckIfinInventory(RimskaZbroj):
            print("Rimska Zbroj")
        if CheckIfinInventory(KumanskaZbroj):
            print("Kumanska Zbroj")
        if CheckIfinInventory(GermanskaZbroj):
            print("Germánská Zbroj")
        if CheckIfinInventory(VelkoMoravskaZbroj):
            print("Velkomoravska zbroj")
        print("=====================================")

    

        
        while True:
                
            val = getValueFromList("Vyber mecu: ", ["1", "2", "3", "4", "5", "6", "7" , "8" , "9" , "10" ,"Z"]).upper()

            print("Tvuj inventar mecu")
            if CheckIfinInventory(TupyMec):
                if val == "1":
                    print("Uspesne prodano")
                    inventory.remove(TupyMec)
                    money + 100
                    print("Tvuj aktualni zustatek na ucte je: " + str(money) + str(100))

            if CheckIfinInventory(TureckaSavle):
                if val == "2":
                    print("Uspesne prodano!")
                    for item in inventory:
                        if isinstance(item, TureckaSavle):
                            inventory.remove(item)
                            break
                    money + 200
                    print("Tvuj aktualni zustatek na ucte je: " + str(money) + str(200))

            if CheckIfinInventory(NemeckyMec):
                if val == "3":
                    print("Uspesne prodano")
                    inventory.remove(NemeckyMec)
                    money + 350
                    print("Tvuj aktualni zustatek na ucte je: " + str(money) + str(350))

            if CheckIfinInventory(CeskyMec):
                if val == "4":
                    print("Uspesne prodano")
                    inventory.remove(CeskyMec)
                    money + 500
                    print("Tvuj aktualni zustatek na ucte je: " + str(money) + str(500))

            if CheckIfinInventory(MadarskyMec):
                if val == "5":
                    print("Uspesne prodano!")
                    inventory.remove(MadarskyMec)
                    money + 625
                    print("Tvuj aktualni zustatek na ucte je: " + str(money) + str(625))
            

            print("")
            print("Tvuj inventar Brneni: ")
            if CheckIfinInventory(HusitskaZbroj):
                if val == "6":
                    print("Uspesne Prodano")
                    husitskeeejzbroj = HusitskaZbroj()
                    inventory.remove(husitskeeejzbroj)
                    money + 200
                    print("Tvuj aktualni zustatek na ucte je: " + str(money))

            if CheckIfinInventory(RimskaZbroj):
                if val == "7":
                    print("Uspesne Prodano")
                    rimskeojzbroj = RimskaZbroj()
                    inventory.remove(rimskeojzbroj)
                    money + 400
                    print("Tvuj aktualni zustatek na ucte je: " + str(money))

            if CheckIfinInventory(KumanskaZbroj):
                if val == "8":
                    print("Uspesne Prodano")
                    kumanskeozbroj = KumanskaZbroj()
                    inventory.remove(kumanskeozbroj)
                    money + 600
                    print("Tvuj aktualni zustatek na ucte je: " + str(money))

            if CheckIfinInventory(GermanskaZbroj):
                if val == "9":
                    print("Uspesne Prodano")
                    germanskoezbroj = GermanskaZbroj()
                    inventory.remove(germanskoezbroj)
                    money + 800
                    print("Tvuj aktualni zustatek na ucte je: " + str(money))

            if CheckIfinInventory(VelkoMoravskaZbroj):
                if val == "10":
                    print("Uspesne Prodano")
                    velkomoravskebrojj = VelkoMoravskaZbroj()
                    inventory.remove(velkomoravskebrojj)
                    money + 1000
                    print("Tvuj aktualni zustatek na ucte je: " + str(money))

class Oprava():

    def systemOpravy():
        pass

obchodnik()


class Zombie:
    hp: int

    def __init__(self, hp: int) -> None:
        self.hp = hp


print("=====================================")
print("V inventáří máš:")
for item in inventory:
    print(item)

print("=====================================")

zombik = Zombie(100)

print("Zadacek:", zombik.hp)

for item in inventory:
    item.dejDamage(zombik)

print("Potom:", zombik.hp)


for item in inventory:
    item.nabrousit()

for item in inventory:
    print(item.damage)

for item in inventory:
    item.dejDamage(zombik)

print("Potom:", zombik.hp)


print("=====================================")
print("V inventáří máš:")
for item in inventory:
    print(item)

print("=====================================")
