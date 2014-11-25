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

def diff(f, z0, theta, eps=1e-8):
    h = eps*exp(I*theta)
    return (f(z0+h)-f(z0)) / h

def diff2(dfdz, dfdconjz, z0, theta):
    return dfdz(z0) + dfdconjz(z0)*exp(-2*I*theta)

def test_zero(f, dfdz, dfdconjz, z0, theta, eps=1e-8):
    assert feq(diff(f, z0, theta, eps), diff2(dfdz, dfdconjz, z0, theta),
            max_relative_error=eps*1e2, max_absolute_error=eps*1e2)

from math import floor, pi
from cmath import sqrt, exp, log
I = 1j

angles = [0, pi/7, pi/4, pi/2, 3*pi/4, pi]

for x in values:
    test_zero(lambda x: abs(x), lambda x: x.conjugate()/(2*abs(x)), lambda x:
            x/(2*abs(x)), x, 0)
    test_zero(lambda x: log(x), lambda x: 1/x, lambda x: 0, x, 0)
