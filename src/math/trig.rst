Periodic Functions
------------------

A function $f(x)$ is periodic with period $T$:

.. math::

    f(x+T) = f(x)

Then you can shift the integration limits by the period $T$:

.. math::

    \int_a^b f(x) \d x
        = \int_a^b f(x+T) \d x
        = \int_{a+T}^{b+T} f(x) \d x

If you integrate $f(x)$ from $0$ to $T$, you can shift $x$ in $f(x)$ by any
constant $\alpha$:

.. math::

    \int_0^T f(x+\alpha) \d x =

    = \int_\alpha^{T+\alpha} f(x) \d x =

    = \int_\alpha^0 f(x) \d x
    + \int_0^T f(x) \d x
    + \int_T^{T+\alpha} f(x) \d x =

    = -\int_0^\alpha f(x) \d x
    + \int_0^T f(x) \d x
    + \int_0^\alpha f(x) \d x =

    = \int_0^T f(x) \d x

Polar Coordinates
-----------------


Polar coordinates (radial, azimuth) $(r,\phi)$ are defined by

.. math::
    :nowrap:

    \begin{eqnarray*} x&=&r\cos\phi \\ y&=&r\sin\phi \\ \end{eqnarray*}


Example
~~~~~~~

When evaluating integrals of the type:

.. math::

    l(x, y) = \int_0^{2\pi} \sqrt{(x-r\cos\phi)^2 + (y-r\sin\phi)^2} \,\d \phi

we write $x$ and $y$ using polar coordinates:

.. math::

    x = r' \cos \phi'

    y = r' \sin \phi'

and then use the $2\pi$ periodicity of $\cos x$:

.. math::

    l(x, y)
    = \int_0^{2\pi} \sqrt{(x-r\cos\phi)^2 + (y-r\sin\phi)^2} \,\d \phi =

    = \int_0^{2\pi} \sqrt{x^2 + y^2 + r^2 - 2r(x\cos\phi + y\sin\phi)} \,\d \phi =

    = \int_0^{2\pi} \sqrt{r'^2 + r^2
        - 2rr'(\cos\phi'\cos\phi + \sin\phi'\sin\phi)} \,\d \phi =

    = \int_0^{2\pi} \sqrt{r'^2 + r^2
        - 2rr'\cos(\phi-\phi')} \,\d \phi =

    = \int_0^{2\pi} \sqrt{r'^2 + r^2 - 2rr'\cos\phi} \,\d \phi =

comparing to:

.. math::

    l(0, y) = \int_0^{2\pi} \sqrt{y^2 + r^2 - 2ry\sin\phi} \,\d \phi

we can see that because the integral is symmetric, we can just set $x=0$ and
then replace $y \to r'$. The above method does everything algebraically, but
you can use this symmetry argument to remember what to do, or even skip the
calculation if you are sure that you didn't make a mistake in the "symmetry
argument".

Spherical Coordinates
---------------------

Spherical coordinates (radial, zenith, azimuth) $(\rho,\theta,\phi)$:

.. math::
    :nowrap:

    \begin{eqnarray*} x&=&\rho\sin\theta\cos\phi \\ y&=&\rho\sin\theta\sin\phi \\ z&=&\rho\cos\theta \\ \end{eqnarray*}

Note: this meaning of $(\theta,\phi)$ is mostly used in the USA and in many
books. In Europe people usually use different symbols, like $(\phi,\theta)$,
$(\vartheta,\varphi)$ and others.

The motivation is to first write $x$ and $y$ using polar coordinates:

.. math::

    x = \rho_{xy}\cos\phi

    y = \rho_{xy}\sin\phi

and then write $z$ and the projection $\rho_{xy}$ of $\rho$ onto the plane
$x-y$ using polar coordinates:

.. math::

    z = \rho\cos\theta

    \rho_{xy} = \rho\sin\theta

so by combining these two we get:

.. math::

    x = \rho_{xy}\cos\phi = \rho\sin\theta\cos\phi

    y = \rho_{xy}\sin\phi = \rho\sin\theta\sin\phi

    z = \rho\cos\theta


.. index:: delta function

Argument function, atan2
------------------------

Argument function $\arg(z)$ is any $\varphi$ such that

.. math::

    z = r e^{i\varphi}

Obviously $\arg(z)$ is unique up to any integer multiple of $2\pi$. By taking
the principal value of the $\arg(z)$ function, e.g. fixing $\arg(z)$ to the
interval $(-\pi, \pi]$ (so that the branch cut is on the negative $x$-axis, as
usual), we get the $\Arg(z)$ function:

.. math::

    -\pi < \Arg z \le \pi

then $\arg z = \Arg z + 2\pi n$, where $n=0, \pm 1, \pm 2, \dots$. We can then
use the following formula to easily calculate $\Arg z$ for any $z=x+iy$ (except
$x=y=0$, i.e. $z=0$, where it is not defined):

.. math::

    \Arg(x+iy) =\begin{cases}\pi&y=0;x<0;\cr
        2\,\atan{y\over\sqrt{x^2+y^2}+x}&\rm otherwise\cr\end{cases}

Finally we define $\atan2(y, x)$ as:

.. math::

    \atan2(y, x) = \Arg(x+iy) =
        \begin{cases}\pi&y=0;x<0;\cr
            2\,\atan{y\over\sqrt{x^2+y^2}+x}&\rm otherwise\cr\end{cases}

The angle $\phi=\atan2(y, x)$ is the angle of the point $(x, y)$ on the unit
circle (assuming the usual conventions), and it works for all quadrants
($\phi=\atan({y\over x})$ only works for the first and fourth quadrant, where
$\atan({y\over x})=\atan2(y, x)$, but in the second and third qudrant,
$\atan({y\over x})$ gives the wrong angles, while $\atan2(y, x)$ gives the
correct angles). So in particular:

.. math::

    \atan2(0, 1) = 2\,\atan{0\over\sqrt{1^2+0^2}+1} = 0

    \atan2(0, -1) = \pi

    \atan2(1, 0) = 2\,\atan{1\over\sqrt{0^2+1^2}+0} = 2\,\atan 1 =
        {\pi\over 2}

    \atan2(-1, 0) = 2\,\atan{-1\over\sqrt{0^2+1^2}+0} = -2\,\atan 1 =
        -{\pi\over 2}

This convention ($\atan2(y, x)$) is used for example in Python, C or Fortran.
Some people might interchange $x$ with $y$ in the definition (i.e. $\atan2(x,
y)= \Arg(y+ix)$), but it is not very common.

The following useful relations hold:

.. math::

    \sin\atan2(y, x) = {y\over \sqrt{x^2+y^2}}
        \quad\quad\quad\mbox{except $x=y=0$}

    \cos\atan2(y, x) = {x\over \sqrt{x^2+y^2}}
        \quad\quad\quad\mbox{except $x=y=0$}

    \tan\atan2(y, x) = {y\over x}
        \quad\quad\quad\mbox{for $x\neq 0$}

    \atan2(ky, kx) = \atan2(y, x)
        \quad\quad\quad\mbox{for $k>0$}

We now prove them. The following works for all $x, y$ except for $x=y=0$:

.. math::

    \sin\atan2(y, x)
        =\begin{cases}\sin\pi&y=0;x<0;\cr
            \sin\left(2\,\atan{y\over\sqrt{x^2+y^2}+x}\right)
                &\rm otherwise\cr\end{cases}
            =

    =\begin{cases}0&y=0;x<0;\cr
        {y\over \sqrt{x^2+y^2}}&\rm otherwise\cr\end{cases}
        =

    =\begin{cases}{y\over \sqrt{x^2+y^2}}&y=0;x<0;\cr
        {y\over \sqrt{x^2+y^2}}&\rm otherwise\cr\end{cases}
        ={y\over \sqrt{x^2+y^2}}



    \cos\atan2(y, x)
        =\begin{cases}\cos\pi&y=0;x<0;\cr
            \cos\left(2\,\atan{y\over\sqrt{x^2+y^2}+x}\right)
                &\rm otherwise\cr\end{cases}
            =

    =\begin{cases}-1&y=0;x<0;\cr
        {x\over \sqrt{x^2+y^2}}&\rm otherwise\cr\end{cases}
        =

    =\begin{cases}{x\over \sqrt{x^2+y^2}}&y=0;x<0;\cr
        {x\over \sqrt{x^2+y^2}}&\rm otherwise\cr\end{cases}
        ={x\over \sqrt{x^2+y^2}}


Tangent is infinite for $\pm{\pi\over 2}$, which corresponds to $x=0$, so the
following works for all $x\neq 0$:

.. math::

    \tan\atan2(y, x)
        =\begin{cases}\tan\pi&y=0;x<0;\cr
            \tan\left(2\,\atan{y\over\sqrt{x^2+y^2}+x}\right)
                &\rm otherwise\cr\end{cases}
            =

    =\begin{cases}0&y=0;x<0;\cr
        {y\over x}&\rm otherwise\cr\end{cases}
        =

    =\begin{cases}{y\over x}&y=0;x<0;\cr
        {y\over x}&\rm otherwise\cr\end{cases}
        ={y\over x}

In the above, we used the following double angle formulas:

.. math::

    \sin 2x = {2\tan x\over 1+\tan^2 x}

    \cos 2x = {1-\tan^2x\over 1+\tan^2 x}

    \tan 2x = {2\tan x\over 1-\tan^2 x}

to simplify the following expressions:

.. math::

    \sin\left(2\,\atan{y\over\sqrt{x^2+y^2}+x}\right) =
        {2\tan\atan{y\over\sqrt{x^2+y^2}+x}\over1+\tan^2\atan{y\over\sqrt{x^2+y^2}+x}}
        =

        =
        {2{y\over\sqrt{x^2+y^2}+x}\over1
            +\left({y\over\sqrt{x^2+y^2}+x}\right)^2}
        =
        {2y\left(\sqrt{x^2+y^2}+x\right)\over
            \left(\sqrt{x^2+y^2}+x\right)^2+y^2}
        =

        =
        {y\left(\sqrt{x^2+y^2}+x\right)\over
            x^2+y^2+x\sqrt{x^2+y^2}}
        =
        {y\left(\sqrt{x^2+y^2}+x\right)\over
            \sqrt{x^2+y^2}\left(\sqrt{x^2+y^2}+x\right)}
        =

        =
        {y\over\sqrt{x^2+y^2}}



    \cos\left(2\,\atan{y\over\sqrt{x^2+y^2}+x}\right) =
        {1-\tan^2\atan{y\over\sqrt{x^2+y^2}+x}\over1+\tan^2\atan{y\over\sqrt{x^2+y^2}+x}}
        =

        =
        {1 -\left({y\over\sqrt{x^2+y^2}+x}\right)^2\over
        1 +\left({y\over\sqrt{x^2+y^2}+x}\right)^2}
        =
        {\left(\sqrt{x^2+y^2}+x\right)^2-y^2\over
            \left(\sqrt{x^2+y^2}+x\right)^2+y^2}
        =

        =
        {x\left(\sqrt{x^2+y^2}+x\right)\over
            x^2+y^2+x\sqrt{x^2+y^2}}
        =
        {x\left(\sqrt{x^2+y^2}+x\right)\over
            \sqrt{x^2+y^2}\left(\sqrt{x^2+y^2}+x\right)}
        =

        =
        {x\over\sqrt{x^2+y^2}}



    \tan\left(2\,\atan{y\over\sqrt{x^2+y^2}+x}\right) =
        {2\tan\atan{y\over\sqrt{x^2+y^2}+x}\over1-\tan^2\atan{y\over\sqrt{x^2+y^2}+x}}
        =

        =
        {2{y\over\sqrt{x^2+y^2}+x}\over1
            -\left({y\over\sqrt{x^2+y^2}+x}\right)^2}
        =
        {2y\left(\sqrt{x^2+y^2}+x\right)\over
            \left(\sqrt{x^2+y^2}+x\right)^2-y^2}
        =

        =
        {y\left(\sqrt{x^2+y^2}+x\right)\over
            x\left(\sqrt{x^2+y^2}+x\right)}
        = {y\over x}

Finally, for all $k>0$ we get:

.. math::

    \atan2(ky, kx) = \Arg(kx + iky)
    =\begin{cases}\pi&y=0;x<0;\cr
        2\,\atan{ky\over\sqrt{(kx)^2+(ky)^2}+kx}&\rm otherwise\cr\end{cases}
    =

    =\begin{cases}\pi&y=0;x<0;\cr
        2\,\atan{y\over\sqrt{x^2+y^2}+x}&\rm otherwise\cr\end{cases}
    = \Arg(x+iy) = \atan2(y, x)


An example of an application:

.. math::

    A\sin x + B\cos x = \sqrt{A^2+B^2}\left(
        {A\over\sqrt{A^2+B^2}}\sin x + {B\over\sqrt{A^2+B^2}}\cos x\right)
    =

    = \sqrt{A^2+B^2}\left( \cos\delta\sin x + \sin\delta\cos x\right)
    = \sqrt{A^2+B^2}\sin(x+\delta)
    =

    = \sqrt{A^2+B^2}\sin(x+\atan2(B, A))

where

.. math::

    \delta = \atan2\left({B\over\sqrt{A^2+B^2}}, {A\over\sqrt{A^2+B^2}}\right)
    =\atan2(B, A)

Multiple Argument Formulas
--------------------------

sin(a x)
~~~~~~~~

Systematic way to derive all multiple argument formulas is to use the following
relation:

.. math::

    \sin(ax) = U_{a-1}(\cos x) \sin x

where $U_n(x)$ are the Chebyshev polynomials of the second kind, first few are:

.. math::

    U_{-3}(x) = -2x

    U_{-2}(x) = -1

    U_{-1}(x) = 0

    U_{- {1\over2}}(x) = {1\over \sqrt 2 \sqrt{x+1}}

    U_0(x) = 1

    U_{1\over2}(x) = {2x+1\over \sqrt 2 \sqrt{x+1}}

    U_1(x) = 2x

    U_2(x) = 4x^2 - 1

    U_3(x) = 8x^3 - 4x

    U_4(x) = 16x^4 - 12x^2 + 1

    U_5(x) = 32x^5 - 32x^3 + 6x

    U_6(x) = 64x^6 - 80x^4 + 24x^2 - 1

Code::

    >>> from sympy import chebyshevu, var
    >>> var("x")
    >>> for i in range(7): print "U_%d(x) = %s" % (i, chebyshevu(i, x))
    U_0(x) = 1
    U_1(x) = 2*x
    U_2(x) = -1 + 4*x**2
    U_3(x) = -4*x + 8*x**3
    U_4(x) = 1 - 12*x**2 + 16*x**4
    U_5(x) = 6*x - 32*x**3 + 32*x**5
    U_6(x) = -1 + 24*x**2 - 80*x**4 + 64*x**6


One can then use this to calculate:

.. math::

    \sin (-2x) = U_{-3}(\cos x) \sin x = -2\cos x\sin x

    \sin (-x) = U_{-2}(\cos x) \sin x = -\sin x

    \sin 0 = U_{-1}(\cos x) \sin x = 0

    \sin {x\over 2}  = U_{-{1\over2}}(\cos x) \sin x =
        {\sin x\over\sqrt 2\sqrt{\cos x + 1}} =
        {\sqrt{1-\cos^2x}\over\sqrt 2\sqrt{\cos x + 1}} =
        {\sqrt{1-\cos x}\over\sqrt 2}

    \sin x = U_0(\cos x) \sin x = \sin x

    \sin {3x\over 2}  = U_{1\over2}(\cos x) \sin x =
        {(2\cos x+1)\sin x\over\sqrt 2\sqrt{\cos x + 1}} =
        {(2\cos x+1)\sqrt{1-\cos^2x}\over\sqrt 2\sqrt{\cos x + 1}} =
        {(2\cos x+1)\sqrt{1-\cos x}\over\sqrt 2}

    \sin 2x = U_1(\cos x) \sin x = 2\cos x\sin x

    \sin 3x = U_2(\cos x) \sin x = (4\cos^2 x-1)\sin x

Code::

    >>> from sympy import chebyshevu, var, sin, cos
    >>> var("x")
    >>> for n in range(1, 7): print "sin(%d*x) = %s" % (n, chebyshevu(n-1, cos(x))*sin(x))
    sin(1*x) = sin(x)
    sin(2*x) = 2*cos(x)*sin(x)
    sin(3*x) = -(1 - 4*cos(x)**2)*sin(x)
    sin(4*x) = (-4*cos(x) + 8*cos(x)**3)*sin(x)
    sin(5*x) = (1 - 12*cos(x)**2 + 16*cos(x)**4)*sin(x)
    sin(6*x) = (6*cos(x) - 32*cos(x)**3 + 32*cos(x)**5)*sin(x)


cos(a x)
~~~~~~~~

Similarly as above, we use:

.. math::

    \cos(ax) = T_a(\cos x)

where $T_n(x)$ are the Chebyshev polynomials of the first kind, first few are:

.. math::

    T_0(x) = 1

    T_{1\over2}(x) = {\sqrt{x+1}\over \sqrt 2}

    T_1(x) = x

    T_{3\over2}(x) = {(2x-1)\sqrt{x+1}\over \sqrt 2}

    T_2(x) = 2x^2 - 1

    T_3(x) = 4x^3 - 3x

    T_4(x) = 8x^4 - 8x^2 + 1

    T_5(x) = 16x^5 - 20x^3 + 5x

    T_6(x) = 32x^6 - 48x^4 + 18x^2 - 1

Code::

    >>> from sympy import chebyshevt, var
    >>> var("x")
    >>> for i in range(7): print "T_%d(x) = %s" % (i, chebyshevt(i, x))
    T_0(x) = 1
    T_1(x) = x
    T_2(x) = -1 + 2*x**2
    T_3(x) = -3*x + 4*x**3
    T_4(x) = 1 - 8*x**2 + 8*x**4
    T_5(x) = 5*x - 20*x**3 + 16*x**5
    T_6(x) = -1 + 18*x**2 - 48*x**4 + 32*x**6


One can then use this to calculate:

.. math::

    \cos 0 = T_0(\cos x) = 1

    \cos {x\over 2} = T_{1\over 2}(\cos x) = {\sqrt{1+\cos x}\over\sqrt 2}

    \cos x = T_1(\cos x) = \cos x

    \cos {3x\over 2} = T_{3\over2}(\cos x) =
        {(2\cos x-1)\sqrt{1+\cos x}\over\sqrt 2}

    \cos 2x = T_2(\cos x) = 2\cos^2 x - 1

    \cos 3x = T_3(\cos x) = 4\cos^3 x - 3\cos x

Code::

    >>> from sympy import chebyshevt, var, cos
    >>> var("x")
    >>> for n in range(7): print "cos(%d*x) = %s" % (n, chebyshevt(n, cos(x)))
    cos(0*x) = 1
    cos(1*x) = cos(x)
    cos(2*x) = -1 + 2*cos(x)**2
    cos(3*x) = -3*cos(x) + 4*cos(x)**3
    cos(4*x) = 1 - 8*cos(x)**2 + 8*cos(x)**4
    cos(5*x) = 5*cos(x) - 20*cos(x)**3 + 16*cos(x)**5
    cos(6*x) = -1 + 18*cos(x)**2 - 48*cos(x)**4 + 32*cos(x)**6
