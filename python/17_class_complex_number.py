# Q17 Complex number operator overloading - @JIYO P V 2026-07-13
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __str__(self):
        return str(self.real) + "+" + str(self.imag) + "i"


c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
print("Sum:", c1 + c2)
print("Equal:", c1 == c2)
