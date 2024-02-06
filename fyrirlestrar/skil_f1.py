import re

class Skil(object):
    """Fyrirlestrardaemi 1 f. REI

    """

    #Daemi 1
    def fun1(self,n):
        # Skrifa fall sem skilar ollum slettum tolum fra 0
        # uppi ef n er slett og ollum oddatolum fra n nidri 1 ef 
        # n er oddatala. Skila sem lista.

        if(n % 2 == 0):
            ls = list(range(0,n+1,2))
        else:
            ls = list(range(n,0,-2))
        
        return ls







if __name__ == '__main__':
    skil = Skil()
