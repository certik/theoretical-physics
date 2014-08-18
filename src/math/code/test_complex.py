def arg(x):
    """
    The argument function.
    """
    from cmath import log
    return log(x).imag

def generate_values():
    """
    Create values to test the function at.
    """
    from math import sin, cos, pi
    from random import random
    # Generate 3 circles in complex plane, with diameters 0.5, 1 and 2. We
    # avoid special values like -1, +/- i, etc., because they typically send
    # the numerical values close to the branch cut, and numerical errors then
    # flip the sign, e.g.:
    #    In [1]: sqrt((-0.5j)**2)
    #    Out[1]: -0.5j
    #
    #    In [2]: (-0.5j)**2
    #    Out[2]: (-0.25-0j)
    #
    #    In [3]: sqrt(-0.25)
    #    Out[3]: 0.5j
    # Here [3] is the correct value and [1] is incorrect, but that happens due
    # to the round off errors in [2] (the small negative imaginary part makes
    # sqrt() return -0.5j instead of +0.5j).
    #
    # For this reason, we chose N=7.
    N = 7
    circle = []
    for n in range(N): circle.append(cos(2*pi*n/N)+1j*sin(2*pi*n/N))
    values = []
    for n in range(N): values.append(0.5*circle[n])
    for n in range(N): values.append(1.0*circle[n])
    for n in range(N): values.append(2.0*circle[n])
    # Add some random points:
    for n in range(30):
        values.append((random()-0.5)*20 + 1j*(random()-0.5)*20)
    return values
values = generate_values()

def feq(a, b, max_relative_error=1e-12, max_absolute_error=1e-12):
    """
    Returns True if a==b to the given relative and absolute errors, otherwise
    False.
    """
    # if the numbers are close enough (absolutely), then they are equal
    if abs(a-b) < max_absolute_error:
        return True
    # if not, they can still be equal if their relative error is small
    if abs(b) > abs(a):
        relative_error = abs(a-b)/abs(b)
    else:
        relative_error = abs(a-b)/abs(a)
    #print abs(a-b), relative_error
    return relative_error <= max_relative_error

def test_zero1(lhs, rhs):
    """
    Tests that a complex function f(x) of one complex variable is zero.
    """
    for x in values:
        r = feq(lhs(x), rhs(x))
        if not r:
            print "x lhs(x) rhs(x)"
            print x, lhs(x), rhs(x)
            assert False

def test_zero2(lhs, rhs):
    """
    Tests that a complex function f(x, y) of two complex variables is zero.
    """
    for x in values:
        for y in values:
            r = feq(lhs(x, y), rhs(x, y))
            if not r:
                print "x y lhs(x, y) rhs(x, y)"
                print x, y, lhs(x, y), rhs(x, y)
                assert False

def test_zero3(lhs, rhs):
    """
    Tests that a complex function f(x, y, z) of three complex variables is zero.
    """
    for x in values:
        for y in values:
            for z in values:
                r = feq(lhs(x, y, z), rhs(x, y, z))
                if not r:
                    print "x y z lhs(x, y, z) rhs(x, y, z)"
                    print x, y, z, lhs(x, y, z), rhs(x, y, z)
                    assert False

from math import floor, pi
from cmath import sqrt, exp, log
I = 1j

# Test the various identities
test_zero1(lambda x: sqrt(x**2), lambda x: (-1)**floor((pi-2*arg(x))/(2*pi))*x)
test_zero1(lambda x: sqrt(exp(x)), lambda x: (-1)**floor((pi-x.imag)/(2*pi))*exp(x/2))
test_zero1(lambda x: log(exp(x)), lambda x: x+2*pi*I*floor((pi-x.imag)/(2*pi)))
test_zero1(lambda x: log(abs(exp(x))), lambda x: x.real)
test_zero1(lambda z: z, lambda z: abs(z)*exp(I*arg(z)))
test_zero1(lambda z: arg(exp(z)), lambda z: z.imag + 2*pi*floor((pi-z.imag)/(2*pi)))

test_zero2(lambda a,b: exp(a)**b, lambda a,b: exp(a*b)*exp(2*pi*I*b*floor((pi-a.imag)/(2*pi))))
test_zero2(lambda x,a: log(x**a), lambda x,a: a*log(x)+2*pi*I*floor((pi-(a*log(x)).imag)/(2*pi)))
test_zero2(lambda a,b: log(a*b), lambda a,b: log(a)+log(b)+2*pi*I*floor((pi-arg(a)-arg(b))/(2*pi)))
test_zero2(lambda a,b: arg(a*b), lambda a,b: arg(a)+arg(b)+2*pi*floor((pi-arg(a)-arg(b))/(2*pi)))

test_zero3(lambda x,a,b: (x**a)**b, lambda x,a,b: x**(a*b)*exp(2*pi*I*b*floor((pi-(a*log(x)).imag)/(2*pi))))
test_zero3(lambda x,y,a: (x*y)**a, lambda x,y,a: (x**a)*(y**a)*exp(2*pi*I*a*floor((pi-arg(x)-arg(y))/(2*pi))))
