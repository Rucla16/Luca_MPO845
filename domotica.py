# NOM DEL FITXER: domotica.py
from abc import ABC, abstractmethod

class DispositiuInteligent(ABC):
    
    def __init__(self, nom):
        self.nom = nom
        self.estat = "OFF"

    @abstractmethod
    def activar(self):
        pass

    def apagar(self):
        self.estat = "OFF"
        return f"{self.nom} s'ha APAGAT."


class Bombeta(DispositiuInteligent):

    def activar(self):
        
        self.estat = "ON"
        return f"Llum {self.nom} ENCÈS amb color blanc."


class Altaveu(DispositiuInteligent):
    
    def activar(self):
        self.estat = "ON"
        return f"Altaveu {self.nom} REPRODUINT música."
    
class Persiana(DispositiuInteligent):
    pass