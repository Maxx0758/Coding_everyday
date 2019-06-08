import math

class trekant():
    
    def __init__(self, g, h):  
        self.g = g
        self.h = h
    
    @classmethod
    def areal(cls, g, h):
        '''
        Beregner areal af en trekant (wow amazing)
        '''
        return (g * h) / 2
    '''
    En @classmethod der returnerer cls() bruges til at returnere noget, 
    på samme format som i __init__()
    Her er formatet, g, h, altså to forskellige objekter.
    '''
    @classmethod
    def skalering(cls, g, h, s):
        return cls(g*s, h*s)

    def kræver_ikke_noget(self):
        '''
        en_trekant.kræver_ikke_noget()
        >>> en_trekant
        '''
        return print(self)

    def __str__(self):
        return 'Højden er {} & grundlinjen {}'.format(self.h, self.g)
