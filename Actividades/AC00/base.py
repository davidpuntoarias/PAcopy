# Seccion para importar liberías
def side(x,y):
    return (((x[0]-y[0])**2)+((x[1]-y[1]))**2)**(1/2)
# Las coordenadas deben ser ingresadas de la forma [x,y]
class Cuadrado(object):
    def __init__(self,v1,v2,v3,v4):
        self.A=v1
        self.B=v2
        self.C=v3
        self.D=v4
        self.side=side(self.A,self.B)
    def obtener_area(self):
        return self.side**2
    def obtener_perimetro(self):
        return self.side*4
    def __str__(self):
        return "Cuadrado de coordenadas A="+str(self.A)+" B="+str(self.B)+" C="+str(self.C)+" D="+str(self.D)+"\n Longitud de lados "+str(self.side)

class Triangulo(object):
    def __init__(self,v1,v2,v3):
        self.A=v1
        self.B=v2
        self.C=v3
        self.a=side(self.B,self.C)
        self.b=side(self.A,self.C)
        self.c=side(self.A,self.B)
    def obtener_area(self):
        sp=self.obtener_perimetro()/2
        return ((sp-self.a)*(sp-self.b)*(sp-self.c))**(1/2)
    def obtener_perimetro(self):
        return self.a+self.b+self.c
    def es_equilatero(self):
        if self.a==self.b and self.b==self.c:
            return True
        else:
            return False
    def __str__(self):
        return "Triángulo de coordenadas A="+str(self.A)+" B="+str(self.B)+" C="+str(self.C)+"\n Longitud de lados a="+str(self.a)+" b="+str(self.b)+" c="+str(self.c)
		
		
if __name__ == '__main__':
    P1=Triangulo([0,0],[3,(3**(1/2))*3],[6,0])
    P2=Cuadrado([1,2],[2,2],[2,3],[1,3])