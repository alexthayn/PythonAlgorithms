class Polynomial:

    def __init__(self, cs):
        """
        initialize polynomial with coefficients: cs
        """
        self.coefficients = cs

    @staticmethod
    def pad(a, m=0):
        """
        returns a new list with the elements of a padded out to size m
        with 0
        """
        return list(a) + [0] * (m-len(a))

    def __call__(self, x):
        """
        returns p(x) where p is this polynomial
        """
        return sum(c*x**i for i, c in enumerate(self.coefficients))

    def __len__(self):
        #simple way to call length of polynomial
        return len(self.coefficients)

    def __add__(self, rhs):
        if len(self.coefficients) > len(rhs):
            rhsPadded = self.pad(rhs, len(self.coefficients))
        else:
            rhsPadded = rhs.coefficients
            lhsPadded = self.pad(self.coefficients, len(rhs))
            
        addedCoef = [0]*len(rhsPadded)
        for i in range(len(rhsPadded)):
            #add the coefficients together
            addedCoef[i] = lhsPadded[i] + rhsPadded[i]
            
        return Polynomial(addedCoef)

    def __mul__(self, rhs):
        multipliedCoef = [0] * (len(self)+len(rhs)-1)
        for lh in range(len(self)):
            for rh in range(len(rhs)):
                #add exponents and multiply coefficients
                multipliedCoef[lh+rh] += self.coefficients[lh] * rhs.coefficients[rh]
        return Polynomial(multipliedCoef)


def test_add0():
    p1 = Polynomial([2])
    p2 = Polynomial([3])
    assert (p1+p2).coefficients == [5]

def test_add1():
    p1 = Polynomial([0,5])
    p2 = Polynomial([6,5])
    assert (p1+p2).coefficients == [6,10]

    p1 = Polynomial([3])
    assert (p1+p2).coefficients == [9,5]

def test_mul0():
    p1 = Polynomial([2])
    p2 = Polynomial([3])
    assert (p1*p2).coefficients == [6]

def test_mul1():
    p1 = Polynomial([3,2])
    p2 = Polynomial([1])
    assert (p1*p2).coefficients == [3,2]

    p2 = Polynomial([20,100])
    assert (p1*p2).coefficients == [60,340,200]

def test_mul2():
    p1 = Polynomial([2,8,7])
    p2 = Polynomial([5,6,8])

    assert (p1*p2).coefficients == [10,52,99,106,56]

    p1 = Polynomial([3,0,2])
    p2 = Polynomial([20,0,100])
    assert (p1*p2).coefficients == [60,0,340,0,200]

def test_call():
    p = Polynomial([1])
    assert p(1) == 1
    assert p(12332) == 1

    p1 = Polynomial([300, 2])
    assert p1(1) == 302
    assert p1(300) == 900

    p3 = Polynomial([0,0,4])
    assert p3(3) == 36
    assert p3(42390) == 4*42390**2

if __name__ == '__main__':
    p = Polynomial([1,5,6])
    p2 = p + p
    p3 = p * p2
    v = p3(45.8)
    print(p.coefficients)
    print(p2.coefficients)
    print(p3.coefficients)

    print(v)