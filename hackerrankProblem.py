#python 3

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imag + no.imag)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imag - no.imag)
        
    def __mul__(self, no):
        realPart = (self.real * no.real) + (self.imag * no.imag * -1)
        imagPart = (self.real * no.imag) + (no.real * self.imag)
        return Complex(realPart, imagPart)


    def __truediv__(self, no):
        numeratorComplex = self * Complex(no.real,-1*no.imag)    #get numerator complex number by multiplying with conjugate
        denominator = no.real**2 + no.imag**2                    #denominator is sqaured mod of second number
        return Complex(numeratorComplex.real/denominator, numeratorComplex.imag/denominator)
        
    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imag**2),0)

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
