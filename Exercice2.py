class Batiment:
    def __init__(self,adress_bat):
        self.__adress_bat=adress_bat
    def get_adress_bat(self):
        return self.__adress_bat
    def get_adress_bat(self):
        return self.__adress_bat
    def __str__(self):
        return "Batiment dont son adresse : {}".format(self.__adress_bat)
class Maison(Batiment):
    def __init__(self,adress_bat,nbPieces):
        super().__init__(adress_bat)
        self.__nbPieces=nbPieces
    def get_nbPieces(self):
        return self.__nbPieces
    def get_nbPieces(self):
        return self.__nbPieces
    def __str__(self):
        return "Maison est dans le {} Nombre de pieces est : {}".format(super().__str__(),self.__nbPieces)
    
        
class Immeuble(Batiment):
    def __init__(self,adress_bat,nbAppart):
        super().__init__(adress_bat)
        self.__nbAppart=nbAppart
    def get_nbAppart(self):
        return self.__nbAppart
    def get_nbAppart(self):
        return self.__nbAppart
    def __str__(self):
        return "Maison est dans le {} Nombre de pieces est : {}".format(super().__str__(),self.__nbAppart)
    
a=Immeuble("Ksar taguelgoult ",12)
print(a.__str__())