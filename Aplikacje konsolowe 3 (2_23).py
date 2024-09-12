class Notatka:
    liczbaNotatek = 0
    def __init__(self, tytul="", tresc=""):
        self._tytul = tytul
        self._tresc = tresc
        Notatka.liczbaNotatek += 1
        self.__id = Notatka.liczbaNotatek

    def getTytulTresc(self):
        return f"Tytuł: {self._tytul}, treść {self._tresc}"

    def metodaDiagnostyczna(self):
        return f"{self.__id};{self._tytul};{self._tresc}"

notatka1 = Notatka("Siema", "elo zero")
print(notatka1.getTytulTresc())
print(notatka1.metodaDiagnostyczna())

notatka2 = Notatka("Cos tam", "elo dwa zera")
print(notatka2.getTytulTresc())
print(notatka2.metodaDiagnostyczna())

