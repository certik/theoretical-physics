from sympy import (sympify, factorial, var, cos, S, sin, Dummy, sqrt, pi, exp,
        I, latex, symbols)

def Plm(l, m, z):
    """
    Returns the associated Legendre polynomial P_{lm}(z).

    The Condon & Shortley (-1)^m factor is included.
    """
    l = sympify(l)
    m = sympify(m)
    z = sympify(z)
    if m >= 0:
        r = ((z**2-1)**l).diff(z, l+m)
        return (-1)**m * (1-z**2)**(m/2) * r / (2**l * factorial(l))
    else:
        m = -m
        r = ((z**2-1)**l).diff(z, l+m)
        return factorial(l-m)/factorial(l+m) * (1-z**2)**(m/2) * r / (2**l * factorial(l))


def Plm_cos(l, m, theta):
    """
    Returns the associated Legendre polynomial P_{lm}(cos(theta)).

    The Condon & Shortley (-1)^m factor is included.
    """
    l = sympify(l)
    m = sympify(m)
    theta = sympify(theta)
    z = Dummy("z")
    r = ((z**2-1)**l).diff(z, l+m).subs(z**2-1, -sin(theta)**2).subs(z, cos(theta))
    return (-1)**m * sin(theta)**m * r / (2**l * factorial(l))

def Ylm(l, m, theta, phi):
    """
    Returns the spherical harmonics Y_{lm}(theta, phi) using the Condon & Shortley convention.
    """
    l, m, theta, phi = sympify(l), sympify(m), sympify(theta), sympify(phi)
    return sqrt((2*l+1)/(4*pi) * factorial(l-m)/factorial(l+m)) * Plm_cos(l, m, theta) * exp(I*m*phi)

def Zlm(l, m, theta, phi):
    """
    Returns the real spherical harmonics Z_{lm}(theta, phi).
    """
    l, m, theta, phi = sympify(l), sympify(m), sympify(theta), sympify(phi)
    if m > 0:
        return sqrt((2*l+1)/(2*pi) * factorial(l-m)/factorial(l+m)) * Plm_cos(l, m, theta) * cos(m*phi)
    elif m < 0:
        m = -m
        return sqrt((2*l+1)/(2*pi) * factorial(l-m)/factorial(l+m)) * Plm_cos(l, m, theta) * sin(m*phi)
    elif m == 0:
        return sqrt((2*l+1)/(4*pi)) * Plm_cos(l, 0, theta)
    else:
        raise ValueError("Invalid m.")

def Zlm_xyz(l, m, x, y, z):
    """
    Returns the real spherical harmonics Z_{lm}(x, y, z).

    It is assumed x**2 + y**2 + z**2 == 1.
    """
    l, m, x, y, z = sympify(l), sympify(m), sympify(x), sympify(y), sympify(z)
    if m > 0:
        r = (x+I*y)**m
        r = r.as_real_imag()[0]
        return sqrt((2*l+1)/(2*pi) * factorial(l-m)/factorial(l+m)) * Plm(l, m, z) * r / sqrt(1-z**2)**m
    elif m < 0:
        m = -m
        r = (x+I*y)**m
        r = r.as_real_imag()[1]
        return sqrt((2*l+1)/(2*pi) * factorial(l-m)/factorial(l+m)) * Plm(l, m, z) * r / sqrt(1-z**2)**m
    elif m == 0:
        return sqrt((2*l+1)/(4*pi)) * Plm(l, 0, z)
    else:
        raise ValueError("Invalid m.")


var("theta phi")
x, y, z = symbols("x y z", real=True)
print "Spherical harmonics:"
print
print ".. math::"
print
for l in range(4):
    for m in range(-l, l+1):
        print r"    Y_{%d,%d}(\theta, \phi) =" % (l, m), \
            latex(Ylm(l, m, theta, phi))
        print

print
print "Real spherical harmonics:"
print
print ".. math::"
print
for l in range(4):
    for m in range(-l, l+1):
        print r"    Z_{%d,%d}(\theta, \phi) =" % (l, m), \
            latex(Zlm(l, m, theta, phi))
        print

print
print "Real spherical harmonics (using $x$, $y$ and $z$, assuming $x^2 + y^2 + z^2 = 1$):"
print
print ".. math::"
print
for l in range(4):
    for m in range(-l, l+1):
        print r"    Z_{%d,%d}(x, y, z) =" % (l, m), \
            latex(Zlm_xyz(l, m, x, y, z).simplify())
        print
