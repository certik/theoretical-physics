Ordinary Differential Equations
===============================

Finite Difference Formulas
--------------------------

We define the backward difference operator $\nabla_h$ by:

.. math::

    \nabla_h f(a) = f(a) - f(a-h)

Repeated application gives:

.. math::

    \nabla_h^2 f(a) = \nabla_h (f(a) - f(a-h))
        = f(a) - f(a-h) -f(a-h) + f(a-2h)
        = f(a) - 2f(a-h) + f(a-2h)

    \nabla_h^3 f(a) = f(a) - 3f(a-h) + 3f(a-2h)-f(a-3h)

    \nabla_h^n f(a) = \sum_{k=0}^n \binom{n}{k}(-1)^k f(a-kh)

We can also derive a formula for $f(a+t)$ where $t$ is any real number,
independent of $h$:

.. math::

    f(a-h) = (1-\nabla_h) f(a)

    (1-\nabla_h)^{-1} f(a-h) = f(a)

    (1-\nabla_h)^{-1} f(a) = f(a+h)

    (1-\nabla_h)^{-n} f(a) = f(a+nh)

    (1-\nabla_h)^{-{t\over h}} f(a) = f(a+t)

Now we can express the following general integral using the function value from
either left ($f(a)$) or right ($f(a+h)$) hand side of the interval $h$:

.. math::

    \int_a^{a+h} f(t) \,\d t
        = \int_0^h f(a+t) \,\d t
        = \int_0^h (1-\nabla_h)^{-{t\over h}} f(a) \,\d t
        =

        = - {h\nabla_h\over (1-\nabla_h) \log(1-\nabla_h)}f(a) =

        = h \left(1+\half\nabla_h + {5\over 12}\nabla_h^2+{3\over8}
            \nabla_h^3+\cdots\right) f(a) =

        = - {h\nabla_h\over \log(1-\nabla_h)} (1-\nabla_h)^{-1}f(a)
        = - {h\nabla_h\over \log(1-\nabla_h)} f(a+h) =

        = h \left(1-\half\nabla_h - {1\over 12}\nabla_h^2-{1\over24}
            \nabla_h^3+\cdots\right) f(a+h)

Code::

    >>> from sympy import var, simplify, integrate
    >>> var("nabla t h")
    (nabla, t, h)
    >>> s = integrate((1-nabla)**(-t/h), (t, 0, h))
    >>> simplify(s)
    h*nabla/(-log(1 - nabla) + nabla*log(1 - nabla))
    >>> s.series(nabla, 0, 5)
    h + h*nabla/2 + 5*h*nabla**2/12 + 3*h*nabla**3/8 + 251*h*nabla**4/720 + O(nabla**5)
    >>> s2 = s*(1-nabla)
    >>> simplify(s2)
    -h*nabla/log(1 - nabla)
    >>> s2.series(nabla, 0, 5)
    h - h*nabla/2 - h*nabla**2/12 - h*nabla**3/24 - 19*h*nabla**4/720 + O(nabla**5)


Keeping terms only to third-order, we obtain:

.. math::

    \int_a^{a+h} f(t) \,\d t
        = - {h\nabla_h\over (1-\nabla_h) \log(1-\nabla_h)}f(a)
        \approx h \left(1+\half\nabla_h + {5\over 12}\nabla_h^2+{3\over8}
            \nabla_h^3\right) f(a)
        =

        = h f(a) + h\half\left(f(a)-f(a-h)\right)
            +h{5\over 12}\left(f(a)-2f(a-h)+f(a-2h)\right)+

            +h{3\over8}\left(f(a)-3f(a-h)+3f(a-2h)-f(a-3h)\right)
        =

        = h\left(1+\half+{5\over12}+{3\over8}\right)f(a)
          -h\left(\half+{2\cdot5\over12}+{3\cdot3\over8}\right)f(a-h) +

          +h\left({5\over12}+{3\cdot3\over8}\right)f(a-2h)
          -h\left({3\over8}\right)f(a-3h)
        =

        = h{55\over24}f(a) -h{59\over24}f(a-h) +
          h{37\over24}f(a-2h) -h{3\over8}f(a-3h)
        =

        = {h\over24}\left(55f(a) -59f(a-h) + 37f(a-2h) -9f(a-3h)\right)

Similarly:

.. math::

    \int_a^{a+h} f(t) \,\d t
        = - {h\nabla_h\over\log(1-\nabla_h)}f(a+h)
        \approx h \left(1-\half\nabla_h - {1\over 12}\nabla_h^2-{1\over24}
            \nabla_h^3\right) f(a+h)
        =

        = {h\over24}\left(9f(a+h) +19f(a) -5f(a-h) +f(a-2h)\right)

Code::

    >>> from sympy import var
    >>> var("f0 f1 f2 f3")
    (f0, f1, f2, f3)
    >>> nabla1 = f0 - f1
    >>> nabla2 = f0 - 2*f1 + f2
    >>> nabla3 = f0 - 3*f1 + 3*f2 - f3
    >>> 24*(f0 + nabla1/2 + 5*nabla2/12 + 3*nabla3/8)
    -59*f1 - 9*f3 + 37*f2 + 55*f0
    >>> 24*(f0 - nabla1/2 - nabla2/12 - nabla3/24)
    f3 - 5*f2 + 9*f0 + 19*f1

Integrating ODE
---------------

Set of linear ODEs can be written in the form:

.. math::
    :label: ode_eq

    {\d y\over\d r} = G y

For example for the Schrödinger we have

.. math::

    y = \begin{pmatrix}
        P \\
        Q
        \end{pmatrix}

    G = \begin{pmatrix}
        0 & 1 \\
        -2(E-V) - {l(l+1)\over r^2} & 0 \\
        \end{pmatrix}

Now we need to choose a grid $r = r(t)$, where $t$ is some uniform grid. For
example $r = r_0 (e^t-1)$:

.. math::

    r_i = r_0 (e^{t_i} - 1)

    t_i = (i-1)h

where $i = 1, 2, 3, \dots, N$. We also need the derivative, for the exampe
above we get:

.. math::

    {\d r\over\d t} = r_0 e^t

Now we substitute this into :eq:`ode_eq`:

.. math::

    {\d y\over\d t} = {\d r\over\d t} G y

We can integrate this system from $a$ to $a+h$ on a uniform grid $t_i$:

.. math::

    y(a+h) = y(a) + \int_a^{a+h} {\d r\over\d t} G y\,\d t
        = y(a) + \int_a^{a+h} f(t)\,\d t

where $f(t) = {\d r\over\d t} G y$ and we use some method to approximate the
integral, see the previous section.

Radial Poisson Equation
~~~~~~~~~~~~~~~~~~~~~~~

Radial Poisson equation is:

.. math::
    :label: poisson-V

    V''(r) + {2\over r} V'(r) = -4\pi n(r)

The left hand side can be written as:

.. math::

    V'' + {2\over r} V'
        = {1\over r} \left(r V'' + 2V'\right)
        = {1\over r} \left(r V\right)''

So the Poisson equation can also be written as:

.. math::
    :label: poisson-rV

    (rV)'' = -4\pi r\, n

Now we determine the values of $V(0)$, $V'(0)$ and the behavior of
$V(\infty)$ and $V'(\infty)$. The equation determines $V$ up to an
arbitrary constant, so we set $V(\infty) = 0$ and now the potential $V$ is
determined uniquely.

The 3D integral of the (number) density is equal to the total (numeric) charge, which is equal to $Z$ (number of electrons). We can then use the Poisson equation to rewrite the integral in terms of $V$:

.. math::

    Z = \int n({\bf x}) \d^3 x
        = \int n(r) r^2\d\Omega\d r
        = \int_0^\infty 4\pi n(r) r^2\d r =

        = -\int_0^\infty (rV)'' r\d r =

        = \int_0^\infty (rV)'\d r - [(rV)'r]_0^\infty =

        = [rV]_0^\infty - [(rV)'r]_0^\infty =

        = [rV - (rV)'r]_0^\infty =

        = -[V'r^2]_0^\infty =

        = -\lim_{r\to\infty} V'(r)r^2

So in the limit $r\to\infty$, we get the equation:

.. math::

    V'(r) = -{Z\over r^2}

by integrating (and requiring that $V$ vanished in infinity to get rid of the
integration constant), we get for $r\to\infty$:

.. math::

    V(r) = {Z\over r}

Integrating :eq:`poisson-rV` directly, we get:

.. math::

    [(rV)']_0^\infty = -4\pi\int_0^\infty r n(r) \d r

    [V + rV']_0^\infty = -4\pi\int_0^\infty r n(r) \d r

We already know that $V'$ behaves like $-{Z\over r^2}$ in infinity,
so $rV'$ vanishes. Requiring $V$ itself to
vanish in infinity, the left hand side simplifies to $-V(0)$ and we get:

.. math::

    V(0) = 4\pi\int_0^\infty r n(r) \d r

Last thing to determine is $V'(0)$. To do that, we expand the charge density
and potential (and it's derivatives) into a series around the origin:

.. math::

    n(r) = n_0 + n_1 r + n_2 r^2 + \cdots = \sum_{k=0}^\infty n_k r^k

    V(r) = V_0 + V_1 r + V_2 r^2 + \cdots = \sum_{k=0}^\infty V_k r^k

    V'(r) = \sum_{k=1}^\infty V_k k r^{k-1}

    V''(r) = \sum_{k=2}^\infty V_k k(k-1) r^{k-2}

And substitute into the equation :eq:`poisson-V`:

.. math::

    \sum_{k=2}^\infty V_k k(k-1) r^{k-2} +
        {2\over r}\sum_{k=1}^\infty V_k k r^{k-1} =
        -4\pi \sum_{k=0}^\infty n_k r^k

    \sum_{k=2}^\infty V_k k(k-1) r^{k-2} + {2\over r} V_1 +
        {2\over r}\sum_{k=2}^\infty V_k k r^{k-1} =
        -4\pi \sum_{k=0}^\infty n_k r^k

    \sum_{k=2}^\infty V_k k(k-1) r^{k-2} + {2\over r} V_1 +
        \sum_{k=2}^\infty 2V_k k r^{k-2} =
        -4\pi \sum_{k=0}^\infty n_k r^k

    {2\over r} V_1 +
        \sum_{k=2}^\infty V_k k\left((k-1) +2\right)r^{k-2}
        =
        -4\pi \sum_{k=0}^\infty n_k r^k

    {2\over r} V_1 +
        \sum_{k=2}^\infty V_k k(k+1)r^{k-2}
        =
        -4\pi \sum_{k=0}^\infty n_k r^k

    {2\over r} V_1 +
        \sum_{l=0}^\infty V_{l+2} (l+2)(l+3)r^l
        =
        -4\pi \sum_{k=0}^\infty n_k r^k

    {2\over r} V_1
        =
        -\sum_{k=0}^\infty \left(4\pi n_k+V_{k+2} (k+2)(k+3)\right) r^k

We now multiply the whole equation by $r$ and then set $r=0$. We get
$V_1 = 0$, so $V'(0) = V_1 = 0$. We put it back into the equation to get:

.. math::

    \sum_{k=0}^\infty \left(4\pi n_k+V_{k+2} (k+2)(k+3)\right) r^k = 0

This must hold for all $r$, so we get the following set of equations for $k=0,
1, \cdots$:

.. math::

    4\pi n_k+V_{k+2} (k+2)(k+3) = 0

from which we express $V_k$ for all $k \ge 2$.
We already know the values for $k=1$ and
$k=0$ from earlier, so overall we get:

.. math::

    V_0 = 4\pi\int_0^\infty r n(r) \d r

    V_1 = 0

    V_{k+2} = -{4\pi n_k\over (k+2)(k+3)}

in particular:

.. math::

    V_2 = - {4\pi n_0\over 6} = -{2\pi\over 3} n_0

    V_3 = - {4\pi n_1\over 12} = -{\pi\over 3} n_1

    V_4 = - {4\pi n_2\over 20} = -{\pi\over 5} n_2

    V_5 = - {4\pi n_3\over 30} = -{2\pi\over 15} n_3

    \cdots

So we get the following series expansion for $V$ and $V'$:

.. math::

    V = V_0 -{2\pi\over 3} n_0 r^2 -{\pi\over 3} n_1 r^3-{\pi\over 5} n_2 r^4
        -{2\pi\over 15} n_3 r^5 - \cdots

    V' = -{4\pi\over 3} n_0 r -\pi n_1 r^2-{4\pi\over 5} n_2 r^3
        -{2\pi\over 3} n_3 r^4 - \cdots

Analytic Testing Example
^^^^^^^^^^^^^^^^^^^^^^^^

Good analytic testing solution, that satisfies the asymptotic relations is:

.. math::

    V(r) = Z \,{\mbox{erf}(\alpha r) \over r}

    V'(r) = -Z\, {\mbox{erf}(\alpha r) \over r^2} +
                {2 Z \alpha\over r\sqrt\pi } e^{-\alpha^2 r^2}

    r V = Z \,\mbox{erf}(\alpha r)

    (rV)' = {2 Z\alpha\over \sqrt\pi } e^{-\alpha^2 r^2}

    (rV)'' = -{4\alpha^3 r Z\over \sqrt\pi } e^{-\alpha^2 r^2}

    n = {Z\alpha^3 \over \pi^{3\over2} } e^{-\alpha^2 r^2}
