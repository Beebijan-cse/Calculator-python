class calculator:
    def add(self,a,b):
        return a+b
    def substract(self,a,b):
        return a-b
    def Multiplication(self,a,b):
        return a*b
    def Division(self,a,b):
        return a/b
    def floor_division(self,a,b):
        return a // b
    def Modulus(self,a,b):
        return a % b
    def Exponent(self,a,b):
        return a ** b
c=calculator()
a=int(int(input("enter the element:")))
b=int(int(input("enter the element:")))

print("Addition is",c.add(a,b))
print("substraction is",c.substract(a,b))
print("Multiplication is",c.Multiplication(a,b))
print("Division is ",c.Division(a,b))
print("floor_division is",c.floor_division(a,b))
print("Modulus is ",c.Modulus(a,b))
