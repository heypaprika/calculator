import math as m

class exponential:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        if self.num1 == 'e' or self.num1 == 'E':
            self.num1 = 'e'
            self.result = m.exp(num2)
        else: self.result = num1**num2

    def __str__(self):
        return '{}^{}'.format(self.num1, self.num2)

    def __add__(self, other):
        return self.result + other

    def __radd__(self, other):
        return self.result + other

    def __sub__(self, other):
        return self.result - other

    def __rsub__(self, other):
        return self.result - other

    def __mul__(self, other):
        if type(other) == exponential:
            if self.num1 == other.num1:
                num2 = self.num2 + other.num2
                return exponential(self.num1, num2)
        if self.num1 == other:
            return exponential(self.num1, self.num2+1)
        return self.result * other

    def __rmul__(self, other):
        if type(other) == exponential:
            if self.num1 == other.num1:
                num2 = self.num2 + other.num2
                return exponential(self.num1, num2)
        if self.num1 == other:
            return exponential(self.num1, self.num2+1)
        return self.result * other

    def __floordiv__(self, other):
        if type(other) == exponential:
            if self.num1 == other.num1:
                num2 = self.num2 - other.num2
                return exponential(self.num1, num2)
        if self.num1 == other:
            return exponential(self.num1, self.num2 - 1)
        return self.result // other

    def __rfloordiv__(self, other):
        if type(other) == exponential:
            if self.num1 == other.num1:
                num2 = other.num2 - self.num2
                return exponential(self.num1, num2)
        if self.num1 == other:
            return exponential(self.num1, 1-self.num2)
        return other // self.result

    def __truediv__(self, other):
        if type(other) == exponential:
            if self.num1 == other.num1:
                num2 = self.num2 - other.num2
                return exponential(self.num1, num2)
        if self.num1 == other:
            return exponential(self.num1, self.num2-1)
        return self.result / other

    def __rtruediv__(self, other):
        if type(other) == exponential:
            if self.num1 == other.num1:
                num2 = other.num2 - self.num2
                return exponential(self.num1, num2)
        if self.num1 == other:
            return exponential(self.num1, 1-self.num2)
        return other / self.result

    def __mod__(self, other):
        return self.result % other

    def __rmod__(self, other):
        return other % self.result

    def __pow__(self, power, modulo=None):
        return exponential(self.num1, self.num2*power)

    def __neg__(self):
        return -self.result

    def __pos__(self):
        return +self.result

    def __abs__(self):
        return abs(self.result)

    def __lt__(self, other):
        if self.result < other:
            return True
        return False

    def __le__(self, other):
        if self.result <= other:
            return True
        return False

    def __gt__(self, other):
        if self.result > other:
            return True
        return False

    def __ge__(self, other):
        if self.result >= other:
            return True
        return False

    def __eq__(self, other):
        if self.result == other:
            return True
        return False

    def __ne__(self, other):
        if self.result != other:
            return True
        return False

    def __int__(self):
        return int(self.result)

    def __float__(self):
        return float(self.result)

    def __complex__(self):
        return complex(self.result)