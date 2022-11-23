class calc:
    a=0
    b=0

    @staticmethod
    def getvalue(self):
        self.a=int(input("Enter A:"))
        self.b=int(input("Enter B:"))
    
    def add(self):
        print("Sum:",self.a+self.b)
    
    def sub(self):
        print("Sub:",self.a-self.b)
    
    def myl(self):
        print("Mul:",self.a*self.b)
    
    def div(self):
        print("Div:",self.a/self.b)
