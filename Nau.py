class Nau:

    def __init__(self,x,y):        
        self.x=x
        self.y=y
        self.v=1
    
    def moure_dreta(self):
        self.x+=self.v
        
    def moure_esquerre(self):
        self.x+=self.v

    def moure_amunt(self):
        self.y+=self.v
        
    def moure_avall(self):
        self.y-=self.v
        
    def mostrar(self):
        print(f"[{self.x},{self.y}]")
