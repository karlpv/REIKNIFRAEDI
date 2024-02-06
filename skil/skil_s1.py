import re
import math

class Skil(object):
    """Skiladaemi 1 f. REI

    """

    #Daemi 1
    def fun1(self,x):
    # Skrifa fall sem skilar reiknar x^3 - 5x^2 + x/2 - (1/13)

        fx = math.pow(x,3) - 5 * math.pow(x,2) + x/2 - (1/13) 

    

        return fx

    #Daemi 2
    def fun2(self,l):
    #Skila summu allra staka i lista l sem er tekið inn i inntaki, nota for lykkju
        summa = sum(l)
        return summa

    #Daemi 3
    def fun3(self):
    #Skila naturulega logra talnanna 1 - 10 sem lista
    # möo skila [ln(1)... ln(10)]


        l = [math.log(n) for n in range (1,11)]

        return l

    #Daemi 4
    def fun4(self,r):
    #Skila rummal kulu med radius r

        rummal = (4 / 3) * math.pi * math.pow(r,3)
        return rummal


    #Daemi 5
    def fun5(self,u):
    #Skila radius hrings med ummal u

        radius = u / (2 * math.pi)
        return radius




if __name__ == '__main__':
    skil = Skil()
