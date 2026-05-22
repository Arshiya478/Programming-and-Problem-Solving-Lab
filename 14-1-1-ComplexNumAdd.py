#Complex Number Addition using Class

class Complex:
    def __init__(self):
        self.real = 0
        self.imag = 0

    def initComplex(self):
        values = input().split()
        self.real = int(values[0])
        self.imag = int(values[1])

    def sum(self, c1, c2):
        self.real = c1.real + c2.real
        self.imag = c1.imag + c2.imag

    def display(self):
        if self.imag >= 0:
            print(str(self.real) + " + " + str(self.imag) + "i")
        else:
            print(str(self.real) + " - " + str(abs(self.imag)) + "i")

# Create three instances
c1 = Complex()
c2 = Complex()
c3 = Complex()

# Initialize two complex numbers
c1.initComplex()
c2.initComplex()

# Compute and display sum
c3.sum(c1, c2)
c3.display()