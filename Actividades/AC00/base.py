# Seccion para importar liberías

class Cuadrado(object):
	def __init__(self,v1,v2,v3,v4):
        self.A=v1
        self.B=v2
        self.C=v3
		self.D=v4
		self.side=side(self.A,self.B)
    def area(self):
        return self.side**2
    def peri(self):
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
    def area(self):
        sp=self.peri()/2
        return ((sp-self.a)*(sp-self.b)*(sp-self.c))**(1/2)
    def peri(self):
        return self.a+self.b+self.c
    def equi(self):
        if self.a==self.b and self.b==self.c:
            return True
        else:
            return False
    def __str__(self):
        return "Triángulo de coordenadas A="+str(self.A)+" B="+str(self.B)+" C="+str(self.C)+"\n Longitud de lados a="+str(self.a)+" b="+str(self.b)+" c="+str(self.c)
		
		
if __name__ == '__main__':
	# Crear instancias aquí
