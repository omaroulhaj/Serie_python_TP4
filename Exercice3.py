class Employe:
    def __init__(self,nom,prenom):
        self.__nom=nom
        self.__prenom=prenom
    def get_nom(self):
        return self.__nom
    def get_prenom(self):
        return self.__prenom
    def set_nom(self,nom):
        self.__nom=nom
    def set_prenom(self,prenom):
        self.__prenom=prenom
    def gains(self):
        pass
    def __str__(self):
        return "Nom : {}, Prenom : {})".format(self.__nom,self.__prenom)
class Patron(Employe):
    def __init__(self,nom,prenom,salaire):
        super().__init__(nom,prenom)
        self.__salaire=salaire
    def get_salaire(self):
        return self.__salaire
    def set_salaire(self,salaire):
        self.__salaire=salaire
    def gains(self):
        return self.__salaire
    def __str__(self):
        return "Patron : {} , salaire : {}".format(super().__str__(),self.__salaire)
    

    
class TravailleurCommission(Employe):
    def __init__(self,nom,prenom,salaire,commission,quantite):
        super().__init__(nom,prenom)
        self.__salaire=salaire
        self.__commission=commission
        self.__quantite=quantite
    def get_commission(self):
        return self.__commission
    def set_commission(self,commission):
        self.__commission=commission
    def get_quantite(self):
        return self.__quantite
    def set_quantite(self,quantite):
        self.__quantite=quantite
    def gains(self):
        return self.__salaire+(self.__commission*self.__quantite)
    def __str__(self):
        return "Travailleur Commission : {} , salaire mensuel : {} , Montant de la commission par article vendus : {} , Nombre d'articles vendus par mois : {}".format(super().__str__(),self.__salaire,self.__commission,self.__quantite)
    

    
class TravailleurHoraire(Employe):
    def __init__(self,nom,prenom,retribution,heures):
        super().__init__(nom,prenom)
        self.__retribution=retribution
        self.__heures=heures
    def get_heures(self):
        return self.__heures
    def set_heures(self,heures):
        self.__heures=heures
    def get_retribution(self):
        return self.__retribution
    def set_retribution(self,retribution):
        self.__retribution=retribution
    def gains(self):
        return (self.__heures*self.__retribution)
    def __str__(self):
        return "Travailleur heures : {} , retribution horaire : {} ,Nombre d'heures de travail par mois  : {} ".format(super().__str__(),self.__retribution,self.__heures)
    

patron = Patron("Ali", "ait flan", 5000)
travailleur_commission = TravailleurCommission("Mohamed", "FOlani", 2000, 0.5, 100)
travailleur_horaire = TravailleurHoraire("Said", "Ben flan", 20, 120)

employes = [patron, travailleur_commission, travailleur_horaire]

for i in employes:
    print(i)
    print(f"Gains : {i.gains()}")
    print("-----------------------------")
