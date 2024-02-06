import re

class Skil(object):
    """Skiladaemi 1 f. REI

    """

    #Daemi 1
    def fun1(self,c):
    # Skrifa fall sem skilar reiknar hitastig i f gefid hitastig i c.

        f = 9/5 * c + 32

        return f


    #Daemi 2
    def fun2(self):
    #skila uppflettitoflu

        d = {"a":1,"b":2,"c":[1,2]}

        return d

    #Daemi 3
    def fun3(self,l):
    #skila fyrsta og sidasta staki i l sem lista k 

        k = [l[n] for n in (0,-1)]
    
        return k




if __name__ == '__main__':
    skil = Skil()
