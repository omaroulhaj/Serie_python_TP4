class point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def set_x(self,x):
        self.__x=x
    def set_y(self,y):
        self.__y=y
    def __str__(self):
        return "Point({},{})".format(self.__x,self.__y)
class rectangle(point):
    def __init__(self,x,y,largeur,longeur):
        super().__init__(x,y)
        self.__largeur=largeur
        self.__longeur=longeur
    def get_largeur(self):
        return self.__largeur
    def get_longeur(self):
        return self.__longeur
    def set_longeur(self,longeur):
        self.__longeur=longeur
    def set_largeur(self,largeur):
        self.__largeur=largeur
    def aire(self):
        return self.__largeur*self.__longeur
    def __str__(self):
        return "Rectangle en point ({},{}) avec largeur = {} longeur = {} Son aire = {} metre au carre".format(self.get_x(),self.get_y(),self.__largeur,self.__longeur,self.aire())
    

    
class parallelepipede(rectangle):
    def __init__(self,x,y,largeur,longeur,hauteur):
        super().__init__(x,y,largeur,longeur)
        self.__hauteur=hauteur
    def get_hauteur(self):
        return self.__hauteur
    def set_hauteur(self,hauteur):
        self.__hauteur=hauteur
    def aire(self):
        return 2*self.__hauteur*(self.get_longeur()+self.get_longeur())+2*self.get_longeur()*self.get_largeur()
    def volume(self):
        return self.__hauteur*self.get_longeur()*self.get_longeur()
    def __str__(self):
        return "parallélépipède en point ({},{}) avec largeur = {} ; longeur = {} ; hauteur={}  ; Son aire = {} metre au carre ; Son volume = {} au cube".format(self.get_x(),self.get_y(),self.get_largeur(),self.get_longeur(),self.__hauteur,self.aire(),self.volume())
    
R=parallelepipede(10,20,5,2,5)
print(R.__str__())
    
