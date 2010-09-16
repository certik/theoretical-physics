Polar and Spherical Coordinates
-------------------------------


Polar coordinates (radial, azimuth) $(r,\phi)$ are defined by

.. math::
    :nowrap:

    \begin{eqnarray*} x&=&r\cos\phi \\ y&=&r\sin\phi \\ \end{eqnarray*}

Spherical coordinates (radial, zenith, azimuth) $(\rho,\theta,\phi)$:

.. math::
    :nowrap:

    \begin{eqnarray*} x&=&\rho\sin\theta\cos\phi \\ y&=&\rho\sin\theta\sin\phi \\ z&=&\rho\cos\theta \\ \end{eqnarray*}

Note: this meaning of $(\theta,\phi)$ is mostly used in the USA and in many
books. In Europe people usually use different symbols, like $(\phi,\theta)$, $(\vartheta,\varphi)$ and others.

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

Systematic way to derive all multiple argument formulas is to use the following
relation:

.. math::

    \sin(a*x) = U_{a-1}(\cos x) \sin x
