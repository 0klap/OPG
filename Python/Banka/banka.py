
import mysql.connector

class Ucet:
    def __init__(self, majitel, cislo, zostatok, urok):
        self.majitel = majitel
        self.cislo = cislo
        self.setZostatok(zostatok)
        self.urok = urok
    
    def setZostatok(self, zostatok):
        if zostatok >= 0: self.zostatok = zostatok
        else:
            try: self.zostatok = self.zostatok
            except: self.zostatok = 0

    def __str__(self):
        return f"Ucet(majitel={self.majitel}, cislo={self.cislo}, zostatok={self.zostatok}, urok={self.urok})"

class UcetdoMinusu(Ucet):
    def __init__(self, majitel, cislo, zostatok, urok, limitPrecerpania, urokDoMinusu):
        super().__init__(majitel, cislo, zostatok, urok)
        self.limitPrecerpania = limitPrecerpania
        self.urokDoMinusu = urokDoMinusu


    def __str__(self):
        return f"UcetDoMinusu(majitel={self.majitel}, cislo={self.cislo}, zostatok={self.zostatok}, urok={self.urok}, limit_precerpania={self.limitPrecerpania}, urok_do_minusu={self.urokDoMinusu})"

ucet = Ucet("Janko Hrasko", 123, 300.53, 1.2)
print(ucet)
ucet.setZostatok(-5.77)
print(ucet)




ucet = UcetdoMinusu("Janko Hrasko", 123, 300.53, 1.2, 100, 1.1)
print(ucet)
ucet.setZostatok(-5.77)
print(ucet)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="4SB_banka"
)

cursor = connection.cursor()
cursor.execute("CREATE TABLE users(majitel varchar(30), cislo int unique, zostatok decimal(10,2), urok decimal(3,2));")
cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)

connection.close()