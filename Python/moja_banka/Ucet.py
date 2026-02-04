class Ucet:

    def __init__(self, majitel: str, cislo: int, zostatok: float):
        self.majitel = majitel
        self.cislo = cislo
        self.zostatok = zostatok
    
    def toString(self):
        return f"{self.majitel}\t{self.cislo}\t{self.zostatok}"
    
    def vklad(self, suma):
        if suma < 0:
            print("Chybná banková operácia - záporný vklad")
        else: self.zostatok += suma

    def vyber(self, suma):
        if suma < 0:
            print("Chybná banková operácia - záporný výber")
        elif self.zostatok < suma: print("Chybná banková operácia - výber prevyšuje zostatok!");
        else: self.zostatok -= suma
    