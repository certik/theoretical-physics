Hartree-Fock (HF) Method
========================

Derivation
----------

The interacting Hamiltonian is (see the general QFT notes for derivation):

.. math::

    i\hbar\partial_t\ket{\Psi(t)} = \hat H\ket{\Psi(t)}

    \hat H = \hat T + \hat V = \sum_{ij} c_i^\dag\braket{i|T|j}c_j +
        \half \sum_{ijkl} c_i^\dag c_j^\dag\braket{ij|V|kl}c_l c_k

We would like to minimize the energy $E = \braket{\Psi | \hat H | \Psi }$ using
the following basis for $Z$ electrons:

.. math::

    \ket{\Psi} = c_1^\dag c_2^\dag \cdots c_Z^\dag\ket{0}

We express the energy $E$ in this basis:

.. math::

    E = \braket{\Psi | \hat H | \Psi } =

    = \bra{0}c_Z\cdots c_2 c_1 \hat H
        c_1^\dag c_2^\dag \cdots c_Z^\dag\ket{0} =

    = \bra{0}c_Z\cdots c_2 c_1
    \left(\sum_{i,j=1}^Z c_i^\dag\braket{i|T|j}c_j +
        \half \sum_{i,j,k,l=1}^Z c_i^\dag c_j^\dag\braket{ij|V|kl}c_l c_k\right)
        c_1^\dag c_2^\dag \cdots c_Z^\dag\ket{0} =

    = \sum_{i=1}^Z \braket{i|T|i} +
        \half \sum_{i,j=1}^Z \left(\braket{ij|V|ij}-\braket{ij|V|ji}\right)

We minimize it with the constrain $\braket{i|j} = \delta_{ij}$:

.. math::

    \delta \left(E - \sum_{i,j=1}^Z \epsilon_{ij} \braket{i|j}\right) = 0

We obtain:

.. math::

    T \ket{i} + \sum_{j=1}^Z \left(\braket{j|V|ij}-\braket{j|V|ji}\right)
        = \epsilon_i \ket{i}

in the $x$-representation:

.. math::

    \braket{{\bf x} | T | i}
        + \sum_{j=1}^Z \left(\bra{{\bf x}}\braket{j|V|ij}-
            \bra{{\bf x}}\braket{j|V|ji}\right)
        = \epsilon_i \braket{{\bf x} | i}

    \braket{{\bf x} | T | i}
        + \sum_{j=1}^Z \left(\braket{j{\bf x}|V|ij}-
            \braket{j{\bf x}|V|ji}\right)
        = \epsilon_i \braket{{\bf x} | i}

And writing the individual terms explicitly:

.. math::

    \braket{{\bf x} | i} = \psi_i({\bf x})

    \braket{{\bf x} | T | i}
        = \left(-\half \nabla^2 -{Z\over |{\bf x}|}\right)\psi_i({\bf x})

    \braket{j{\bf x}|V|ij}
        = \int \psi_j^*({\bf y}){1\over|{\bf x}-{\bf y}|}
            \psi_i({\bf x})\psi_j({\bf y}) \d^3 y
        = \int {|\psi_j({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_i({\bf x})

    \braket{j{\bf x}|V|ji}
        = \int \psi_j^*({\bf y}){1\over|{\bf x}-{\bf y}|}
            \psi_j({\bf x})\psi_i({\bf y}) \d^3 y
        = \int {\psi_i({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_j({\bf x})

we get the Hartree-Fock equations:

.. math::

    \left(-\half \nabla^2 -{Z\over |{\bf x}|}
    +
    \int {\sum_{j=1}^Z|\psi_j({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y\right)\psi_i({\bf x})
    - \sum_{j=1}^Z\int {\psi_i({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_j({\bf x})
    =
    \epsilon_i \psi_i({\bf x})

Let's introduce the number density $n({\bf x})$, Hartree potential $V_H({\bf
x})$ and nonlocal exchange potential $V_x$ with its kernel $U({\bf x}, {\bf
y})$:

.. math::

    n({\bf x}) = \sum_{j=1}^Z|\psi_j({\bf y})|^2

    V_H({\bf x}) = \int {\sum_{j=1}^Z|\psi_j({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y
        = \int {n({\bf y})\over|{\bf x}-{\bf y}|} \d^3 y

    \hat V_x f({\bf x}) =
    - \sum_{j=1}^Z\int {f({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_j({\bf x})
    = \int U({\bf x}, {\bf y}) f({\bf y}) \d^3 y

    U({\bf x}, {\bf y}) =
    - \sum_{j=1}^Z {\psi_j({\bf x})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}

then we can write the HF equations as:

.. math::

    \left(-\half \nabla^2 -{Z\over |{\bf x}|} + V_H({\bf x})
        + \hat V_x
        \right)\psi_i({\bf x})
    =
    \epsilon_i \psi_i({\bf x})

    \left(-\half \nabla^2 -{Z\over |{\bf x}|} + V_H({\bf x})
        \right)\psi_i({\bf x})
    + \int U({\bf x}, {\bf y}) \psi_i({\bf y}) \d^3 y
    =
    \epsilon_i \psi_i({\bf x})

The Hartree potential can be calculated by solving the Poisson equation:

.. math::

    \nabla^2V_H({\bf x}) = -4\pi n({\bf x})

The application of the exchange potential $\hat V_x$ on any function
$f({\bf x})$ can be calculated by:

.. math::

    \hat V_x f({\bf x}) = - \sum_{j=1}^Z W_{fj}({\bf x})\psi_j({\bf x})

    W_{fj}({\bf x}) = \int {f({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y

    \nabla^2 W_{fj}({\bf x}) = -4\pi f({\bf x})\psi_j^*({\bf x})

Exchange Integral
-----------------

Let's calculate the exchange integral

.. math::

    \int {\psi_i^*({\bf x})\psi_j({\bf x})\psi_j^*({\bf x}')\psi_i({\bf x}')
        \over |{\bf x} - {\bf x}'|} \d^3 x \d^3 x'

for the particular choice of the functions $\psi$:

.. math::

    \psi_i({\bf x}) = {P_{nl}(r)\over r} Y_{lm}(\Omega)

    \psi_j({\bf x}) = {P_{n'l'}(r)\over r} Y_{l'm'}(\Omega)

We use multipole expansion:

.. math::

    {1\over |{\bf x}-{\bf x}'|}
        = \sum_{k,q}{r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}Y_{kq}(\Omega)Y_{kq}^*(\Omega')

And we get:

.. math::

    \int {\psi_i^*({\bf x})\psi_j({\bf x})\psi_j^*({\bf x}')\psi_i({\bf x}')
        \over |{\bf x} - {\bf x}'|} \d^3 x \d^3 x' =

    = \int
        {P_{nl}(r)\over r} Y_{lm}^*(\Omega)
        {P_{n'l'}(r)\over r} Y_{l'm'}(\Omega)
        {P_{n'l'}(r')\over r'} Y_{l'm'}^*(\Omega')
        {P_{nl}(r')\over r'} Y_{lm}(\Omega')

        \sum_{k,q}{r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}Y_{kq}(\Omega)Y_{kq}^*(\Omega')
        r^2 r'^2 \d r \d r' \d \Omega \d \Omega' =

    =
    \sum_{k,q}
    \int
        Y_{lm}^*(\Omega)
        Y_{l'm'}(\Omega)
        Y_{kq}(\Omega)
        \d \Omega
      \int
        Y_{l'm'}^*(\Omega')
        Y_{lm}(\Omega')
        Y_{kq}^*(\Omega')
        \d \Omega'

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k,q}
    \int
        Y_{lm}^*(\Omega)
        Y_{l'm'}(\Omega)
        Y_{kq}(\Omega)
        \d \Omega
        (-1)^{m+m'+q}
      \int
        Y_{l',-m'}(\Omega')
        Y_{l,-m}^*(\Omega')
        Y_{k,-q}(\Omega')
        \d \Omega'

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k}
        c^k(l, m, l', m') \sqrt{2k+1\over 4\pi}
        (-1)^{m+m'+m-m'}
        c^k(l, -m, l', -m') \sqrt{2k+1\over 4\pi}

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k}
        c^k(l, m, l', m')
        c^k(l, -m, l', -m')
      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k}
        c^k(l, m, l', m')
        c^k(l, m, l', m')
      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k=|l-l'|}^{l+l'}
        \left(
        c^k(l, m, l', m')
        \right)^2
      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r'

Nonlocal Exchange Potential
---------------------------

Similarly, we calculate:

.. math::

    \sum_{j=1}^Z\int {\psi_i({\bf x'})\psi_j^*({\bf x'})\over|{\bf x}-{\bf x'}|}
            \d^3 x'\,\,\psi_j({\bf x}) =

    = \sum_{n'l'm'}\sum_{k,q}\int
        {P_{nl}(r')\over r'} Y_{lm}(\Omega')
        {P_{n'l'}(r')\over r'} Y_{l'm'}^*(\Omega')
        {P_{n'l'}(r)\over r} Y_{l'm'}(\Omega)

        {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}Y_{kq}(\Omega)Y_{kq}^*(\Omega')
        r'^2 \d r' \d \Omega' =

    = \sum_{n'l'm'}\sum_{k,q}
            {P_{n'l'}(r)\over r}
            {4\pi\over 2k+1}
        \int Y_{lm}(\Omega') Y_{l'm'}^*(\Omega') Y_{kq}^*(\Omega')
            Y_{l'm'}(\Omega)
            Y_{kq}(\Omega)
            \d \Omega'
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'  =

    = \sum_{n'l'}\sum_{k}
            {P_{n'l'}(r)\over r}
            {4\pi\over 2k+1}
            {2k+1\over 4\pi}
                \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
                Y_{lm}(\Omega)
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'  =

    =
    {Y_{lm}(\Omega)\over r}
    \sum_{n'l'}\sum_{k=|l-l'|}^{k=l+l'}
            \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'\,
            P_{n'l'}(r)

Where we used the result of the integral in
:ref:`five_spherical_harmonics`. Note that:

.. math::
    :label: using3j

    \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
        = \sqrt{2l'+1\over 2l+1}
            \sqrt{(2l'+1)(2l+1)}
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        = (2l'+1)
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2

Spherical Symmetry
------------------

In the central field approximation, we average the integral for $V_H$ over the
angles:

.. math::

    V_H({\bf x}) \to V_H(r) = {1\over 4\pi} \int V_H({\bf x})\, \d \Omega

Using the above integrals, the HF equations become:

.. math::

    -\half P_{nl}''(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)P_{nl}(r) +

            -\sum_{n'l'}\sum_{k=|l-l'|}^{k=l+l'}
                    \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
                \int
                {r_{<}^k\over r_{>}^{k+1}}
                P_{nl}(r')
                P_{n'l'}(r')
                \d r'\,
                    P_{n'l'}(r)
        = \epsilon_{nl} P_{nl}(r)

or using :eq:`using3j`:

.. math::

    -\half P_{nl}''(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)P_{nl}(r) +

            -\sum_{n'l'}
                (2l'+1)
                \sum_{k=|l-l'|}^{k=l+l'}
                    \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int
                {r_{<}^k\over r_{>}^{k+1}}
                P_{nl}(r')
                P_{n'l'}(r')
                \d r'\,
                    P_{n'l'}(r)
        = \epsilon_{nl} P_{nl}(r)


FEM
---

The weak formulation is ($u(r) = P_{nl}(r)$):

.. math::

    \int_0^\infty \half u'(r) v'(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)u(r)v(r) \d r+

            -\sum_{n'l'}
                (2l'+1)
                \sum_{k=|l-l'|}^{k=l+l'}
                    \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int_0^\infty
                \int_0^\infty
                {r_{<}^k\over r_{>}^{k+1}}
                u(r')v(r)
                P_{n'l'}(r')
                P_{n'l'}(r)
                \d r'\,
                \d r
        = \epsilon \int_0^\infty u(r)v(r)\d r

The radial double integral can be done in the following way:

.. math::

    \int_0^\infty
    \int_0^\infty
    {r_{<}^k\over r_{>}^{k+1}}
    u(r')v(r)
    f(r')
    g(r)
    \d r'\,
    \d r
    = \int_0^\infty g(r) v(r) {Y^k(r)\over r}

where:

.. math::

    Y^k(r) = r
    \int_0^\infty
    {r_{<}^k\over r_{>}^{k+1}}
    u(r')
    f(r')
    \d r'
    = r
    \int_0^r
    {r'^k\over r^{k+1}}
    u(r')
    f(r')
    \d r'
    +
    r \int_r^\infty
    {r^k\over r'^{k+1}}
    u(r')
    f(r')
    \d r'
    =

    =
    {1\over r^k}
    \int_0^r
    {x^k}
    u(x)
    f(x)
    \d x
    +
    r^{k+1}
    \int_r^\infty
    {1\over x^{k+1}}
    u(x)
    f(x)
    \d x
    =Z^k(r)
    +
    r^{k+1}
    \int_r^\infty {1\over x^{k+1}} u(x) f(x) \d x

where:

.. math::

    Z^k(r) =
    {1\over r^k}
    \int_0^r
    {x^k}
    u(x)
    f(x)
    \d x

    {\d Z^k(r) \over \d r}= -{k\over r} Z^k(r) + u(r) f(r)

    Z^k(0) = 0

Now we differentiate $Y^k(r)$:

.. math::

    {\d Y^k(r) \over \d r} = {\d Z^k(r) \over \d r}
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} u(x) f(x) \d x
        -u(r) f(r)
    =

    =
    -{k\over r} Z^k(r) + u(r) f(r)
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} u(x) f(x) \d x
        -u(r) f(r) =

    =
    -{k\over r} Z^k(r)
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} u(x) f(x) \d x =

    =
    -{k\over r} Z^k(r)
        + {k+1\over r} (Y^k(r) - Z^k(r)) =

    =
    -{2k+1\over r} Z^k(r) + {k+1\over r} Y^k(r)

Also $Y^k(\infty) = Z^k(\infty)$, so we get the following set of differential
equations with boundary conditions:

.. math::

    \left({\d\over\d r} - {k+1\over r}\right) Y^k(r) = -{2k+1\over r} Z^k(r)

    \left({\d\over\d r} + {k\over r}\right) Z^k(r) = u(r) f(r)

    Y^k(\infty) = Z^k(\infty)

    Z^k(0) = 0

Expressing $Z^k$ from the first equation:

.. math::

    Z^k(r) = -{r\over 2k+1}\left({\d\over\d r} - {k+1\over r}\right) Y^k(r) =

    =-{r\over 2k+1}{\d Y^k(r)\over \d r} + {k+1\over 2k+1} Y^k(r)

and substituting into the second equation we get:

.. math::

    -\left({\d\over\d r} + {k\over r}\right)
        \left({r\over 2k+1}{\d Y^k(r)\over \d r} + {k+1\over 2k+1} Y^k\right)
        = u(r) f(r)

    -{r\over 2k+1}\left({\d^2\over\d r^2} - {k(k+1)\over r^2}\right)
        Y^k(r)
        = u(r) f(r)

    \left({\d^2\over\d r^2} - {k(k+1)\over r^2}\right) Y^k(r)
        = -{2k+1\over r}u(r) f(r)

With boundary condition on the left:

.. math::

    Z^k(0) = {k+1\over 2k+1} Y^k(0) = 0

    Y^k(0) = 0

and on the right:

.. math::

    Z^k(r)
        =-{r\over 2k+1}{\d Y^k(r)\over \d r} + {k+1\over 2k+1} Y^k(r)
        = Y^k(r)

    -{r\over 2k+1}{\d Y^k(r)\over \d r} - {k\over 2k+1} Y^k(r) = 0

    {\d Y^k(r)\over \d r} + {k\over r} Y^k(r) = 0

so for $r\to\infty$:

.. math::

    \left.{\d Y^k(r)\over \d r}\right|_{r=\infty} = 0
