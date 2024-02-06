import re
import math
class Skil(object):
    """Timadaemi 2 f. REI

    """
    def asj(self,a,b,c):
        discriminant = (b**2) - (4*a*c)
        if discriminant > 0:
            root1 = (-b+math.sqrt(discriminant))/(2*a)
            root2 = (-b-math.sqrt(discriminant))/(2*a)
            return root1,root2
        elif discriminant == 0:
            root = -b / (2*a)
            return root
        else:
            return None


    def trap(self,f,a,b,n):
        deltax = (b-a)/n
        summa = 0
        for i in range(1,n):
            summa += f(a + i * deltax)
        heild_gildi = deltax *(0.5 *   (f(a) + f(b)) + summa )
        
        return heild_gildi
    

    def krot(self,a):
        x = 1 
        epsilon = 1e-4
        while True:
            print(x)    
            y = (x+a/x) / 2
            if abs(y-x) < epsilon:
                return y
            x=y
    
        
