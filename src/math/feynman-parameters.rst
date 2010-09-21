Feynman Parameters
------------------

When integrating a denominator like ${1\over AB}$, the idea is to introduce
auxiliary parameters in order to make the denominator simpler. We start with
the identity:

.. math::
    :label: feynpar-2

    {1\over AB} = \int_0^1 \d x {1\over \left(xA + (1-x)B\right)^2}
    =
    \int_0^1 \d x \int_0^1 \d y {\delta(x+y-1)
        \over \left(xA + yB\right)^2}

which can be proven easily::

    >>> var("A B")
    (A, B)
    >>> integrate(1/(x*A + (1-x)*B)**2, (x, 0, 1))
    1/(A*B - A**2) - 1/(-A*B + B**2)
    >>> simplify(_)
    1/(A*B)

By repeatedly differentiating with respect to B:

.. math::
    :label: feynpar-abn

    {1\over AB^2} = \int_0^1 \d x \int_0^1 \d y {2 y \delta(x+y-1)
        \over \left(xA + yB\right)^3}

    {1\over AB^3} = \int_0^1 \d x \int_0^1 \d y {3 y^2 \delta(x+y-1)
        \over \left(xA + yB\right)^4}

    {1\over AB^n} = \int_0^1 \d x \int_0^1 \d y {n y^{n-1} \delta(x+y-1)
        \over \left(xA + yB\right)^{n+1}}

Then we prove:

.. math::
    :label: feynpar-n

    {1\over A_1A_2\cdots A_n} =
        \int_0^1 \d x_1\cdots\int_0^1 \d x_n {(n-1)!\,
            \delta(x_1 + \cdots + x_n-1)
            \over \left(x_1A_1 + \cdots + x_nA_n\right)^n}

For $n=2$ we get :eq:`feynpar-2` and if it holds for $n$ it also holds for
$n+1$, because we multiply :eq:`feynpar-n` by ${1\over A_{n+1}}$ and get:

.. math::

    {1\over A_1A_2\cdots A_n}{1\over A_{n+1}} =

    = \int_0^1 \d x_1\cdots\int_0^1 \d x_n (n-1)!\,\delta(x_1 + \cdots +x_n-1)
    {1 \over \left(x_1A_1 + \cdots + x_nA_n\right)^n A_{n+1}} =

    = \int_0^1 \d x_1\cdots\int_0^1 \d x_n (n-1)!\,\delta(x_1 + \cdots +x_n-1)
        \int_0^1 \d x \int_0^1 \d y {n y^{n-1} \delta(x+y-1)
                \over \left(xA_{n+1} +
                y\left(x_1A_1 + \cdots + x_nA_n\right)\right)^{n+1}}

    = \int_0^1 \d x_1\cdots\int_0^1 \d x_n
        \int_0^1 \d y {n!\,\delta(x_1 + \cdots +x_n-1) y^{n-1}
                \over \left((1-y)A_{n+1} +
                y\left(x_1A_1 + \cdots + x_nA_n\right)\right)^{n+1}}=

    = \int_0^{1\over y} \d x_1\cdots\int_0^{1\over y} \d x_n
        \int_0^1 \d y {n!\,\delta(yx_1 + \cdots +yx_n-y) y^n
                \over \left((1-y)A_{n+1} +
                y\left(x_1A_1 + \cdots + x_nA_n\right)\right)^{n+1}}=

    = \int_0^{1\over y} y\d x_1\cdots\int_0^{1\over y} y\d x_n
        \int_0^1 \d y {n!\,\delta(yx_1 + \cdots +yx_n-y)
                \over \left((1-y)A_{n+1} +
                \left(yx_1A_1 + \cdots + yx_nA_n\right)\right)^{n+1}}=

    = \int_0^1 \d z_1\cdots\int_0^1 \d z_n
        \int_0^1 \d y {n!\,\delta(z_1 + \cdots +z_n-y)
                \over \left((1-y)A_{n+1} +
                \left(z_1A_1 + \cdots + z_nA_n\right)\right)^{n+1}}=

    = -\int_0^1 \d z_1\cdots\int_0^1 \d z_n
        \int_1^0 \d y' {n!\,\delta(z_1 + \cdots +z_n+y'-1)
                \over \left(y'A_{n+1} +
                \left(z_1A_1 + \cdots + z_nA_n\right)\right)^{n+1}}=

    =
        \int_0^1 \d x_1\cdots\int_0^1 \d x_{n+1} {n!\,
            \delta(x_1 + \cdots + x_{n+1}-1)
            \over \left(x_1A_1 + \cdots + x_{n+1}A_{n+1}\right)^{n+1}}

Where we used :eq:`feynpar-abn` and the fact, that $\delta(x_1 + \cdots
+x_n-1)=y\,\delta(yx_1 + \cdots +yx_n-y)$, after the substituation we also
restricted the limits of integration from 1 to $1\over y$, since $x_1$, $x_2$,
... are all positive.

Example 1
~~~~~~~~~

.. math::

    \int {\d^4 k\over (k-p)^2 (k^2 - m^2)}
        = \int d^4 k \int_0^1\d x \d y {\delta(x+y-1)\over D^2}

where

.. math::

    D = x (k-p)^2 + y(k^2 - m^2) = (x+y)k^2 - 2xk\cdot p +xp^2-ym^2
      = k^2 - 2xk\cdot p +xp^2-ym^2

In the last part we used $x+y=1$. We now shift $k$ by introducing:

.. math::

    l = k - xp

    \d^4k = \d^4 l

and we get:

.. math::

    D = k^2 - 2xk\cdot p +xp^2-ym^2 = l^2 - x^2p^2 + xp^2 - ym^2

thus:

.. math::

    \int d^4 k \int_0^1\d x \d y {\delta(x+y-1)\over D^2} =

    = \int l^4 k \int_0^1\d x \d y {\delta(x+y-1)\over
        (l^2 - x^2p^2 + xp^2 - ym^2)^2}

Example 2
~~~~~~~~~

.. math::

    \int {\d^4 k\over (k^2-m^2+i\epsilon)((k+p)^2 - m^2 + i\epsilon)
        ((k-p)^2+i\epsilon)}
        = \int d^4 k \int_0^1\d x \d y\d z {2\delta(x+y+z-1)\over D^3}

where

.. math::

    D = x (k^2-m^2+i\epsilon) + y((k+p)^2 - m^2 + i\epsilon) +
        z((k-p)^2+i\epsilon) =

      = (x+y+z)k^2 + 2k\cdot(yq-zp) + yq^2 + zp^2 - (x+y)m^2 +
        (x+y+z)i\epsilon =

      = k^2 + 2k\cdot(yq-zp) + yq^2 + zp^2 - (x+y)m^2 + i\epsilon

In the last part we used $x+y+z=1$. We now shift $k$ by introducing:

.. math::

    l = k + yq - zp

    \d^4k = \d^4 l

and we get:

.. math::

    D = k^2 + 2k\cdot(yq-zp) + yq^2 + zp^2 - (x+y)m^2 + i\epsilon =

    = l^2 - \Delta + i\epsilon

where

.. math::

    \Delta = -xyq^2 + (1-z)^2m^2

thus:

.. math::

    \int d^4 k \int_0^1\d x \d y\d z {2\delta(x+y+z-1)\over D^3} =

    = \int \d^4 l \int_0^1\d x \d y\d z {2\delta(x+y+z-1)\over
    (l^2 - \Delta + i\epsilon)^3 } =

    = (-i)\int \d^4 l_E \int_0^1\d x \d y\d z {2\delta(x+y+z-1)\over
    (l_E^2 + \Delta)^3 } =

    = (-i)\int \d\Omega_4 \int_0^\infty \d l_E \int_0^1\d x \d y\d z
    {2\delta(x+y+z-1)l_E^3\over (l_E^2 + \Delta)^3 } =

    = (-i4\pi^2)\int_0^1\d x \d y\d z \delta(x+y+z-1) \int_0^\infty \d l_E
        {l_E^3\over (l_E^2 + \Delta)^3 } =

    = (-i4\pi^2)\int_0^1\d x \d y\d z \delta(x+y+z-1) \int_\Delta^\infty \d h
        {h-\Delta \over 2 h^3 } =

    = (-i4\pi^2)\int_0^1\d x \d y\d z \delta(x+y+z-1) {1\over 4\Delta} =

    = (-i\pi^2)\int_0^1\d x \d y\d z {\delta(x+y+z-1) \over \Delta} =

    = (-i\pi^2)\int_0^1\d x \d y\d z {\delta(x+y+z-1) \over
         (1-z)^2m^2 - xyq^2}
