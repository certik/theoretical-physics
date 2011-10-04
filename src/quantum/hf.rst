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

where:

.. math::

    n({\bf x}) = \sum_{i=1}^Z |\psi_i({\bf x})|^2

The application of the exchange potential $\hat V_x$ on any function
$f({\bf x})$ can be calculated by:

.. math::

    \hat V_x f({\bf x}) = - \sum_{j=1}^Z W_{fj}({\bf x})\psi_j({\bf x})

    W_{fj}({\bf x}) = \int {f({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y

    \nabla^2 W_{fj}({\bf x}) = -4\pi f({\bf x})\psi_j^*({\bf x})

Exchange Integral in Spherical Symmetry
---------------------------------------

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


Occupation Numbers
------------------

We have a sum over $N$ electron states like this:

.. math::

    \sum_{i=1}^N A_i({\bf x}) = \sum_{nlms} A_{nlms}({\bf x})

where $A_{nlms}({\bf x})$ are some functions that depend on the state numbers
(for example squares of the wavefunctions). Then there are two options ---
either there is a way to sum over the $m$ and $s$ degrees of freedom, so that
the sum can be written exactly as:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) = \sum_{nlms} B_{nl}({\bf x})

where $B_{nl}$ (that don't depend on $m$ and $s$) will in general be different
to $A_{nlms}$, but the sum will be the same. Or we have to approximate the sum
(for example by averaging over the angles, or in some other way) as:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) \to \sum_{nlms} B_{nl}({\bf x})

In either case, the occupation numbers $f_{nl}$ are simply the number of times
the functions $B_{nl}({\bf x})$ appear in the sum for the given $n$ and $l$:

.. math::

    \sum_{nlms} B_{nl}({\bf x}) = \sum_{nl} f_{nl} B_{nl}({\bf x})

So for closed shells atoms, it is always:

.. math::

    f_{nl} = 2(2l+1)

because there are two spins, and $2l+1$ possibilities for $m$, for open shell
atoms, $f_{nl}$ is anything between $0$ and $2l+1$.

Example I
~~~~~~~~~

As an example, let's say that after some calculation for closed shell systems
we get exactly:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) = \sum_{nl} 2(2l+1) B_{nl}({\bf x})

Then because there are exactly $2(2l+1)$ states in the $nl$ shell, we write the
above as:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) = \sum_{nl} 2(2l+1) B_{nl}({\bf x})
        = \sum_{nl} f_{nl} B_{nl}({\bf x})

Then we do similar calculation for the open shell system, and we have to use
some approximations to get the following formula, where the $B_{nl}({\bf x})$
happen to be exactly the same as for the closed shell system:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) \to \sum_{nlm} 2 B_{nl}({\bf x})

Then we denote by $f_{nl}$ the number of electrons in the shell $nl$ (at least
one of them will be open, for which $nl$ we have $f_{nl} < 2(2l+1)$), and we
can write the above as:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) \to \sum_{nlm} 2 B_{nl}({\bf x})
        = \sum_{nl} f_{nl} B_{nl}({\bf x})

Example II
~~~~~~~~~~

The usual chemical occupation numbers for the Uranium atom are:

.. math::

    f_{1l} & = 2 (2l+1)    \\
    f_{2l} & = 2 (2l+1)    \\
    f_{3l} & = 2 (2l+1)    \\
    f_{4l} & = 2 (2l+1)    \\
    f_{5l} & = 2 (2l+1)\quad\quad\mbox{for $l\le2$}    \\
    f_{53} & = 3    \\
    f_{60} & = 2    \\
    f_{61} & = 6    \\
    f_{62} & = 1    \\
    f_{70} & = 2    \\

So the $n=5$, $l=3$ and $n=6$, $l=2$ shells are open, all others are closed.
By summing all these $f_{nl}$, we get 92 states as expected:

.. math::

    \sum_{nl} f_{nl} = 2 + (2+6) + (2+6+10) + (2+6+10+14) + (2+6+10) +

        + 3 + 2 + 6 + 1 + 2 = 92

Code::

    def f_nl(n, l):
        if n < 5 or (n == 5 and l <= 2):
            return 2*(2*l+1)
        else:
            d = {
                (5, 3): 3,
                (6, 0): 2,
                (6, 1): 6,
                (6, 2): 1,
                (7, 0): 2,
                }
            if (n, l) in d:
                return d[n, l]
            else:
                return 0

    print "Sum f_nl =", sum([f_nl(n, l) for n in range(8) for l in range(n)])

prints::

    Sum f_nl = 92

Hartree Screening Functions
---------------------------

Hartree screening function $Y^k(f, r)$ is defined as:

.. math::

    Y^k(f, r) = r
    \int_0^\infty
    {r_{<}^k\over r_{>}^{k+1}}
    f(r')
    \d r'

and it occurs in many formulas in the Hartree Fock theory, so this section shows
how to calculate it. It depends on $k$ and a function $f(r)$.

We first do the integral:

.. math::

    Y^k(f, r) = r
    \int_0^\infty
    {r_{<}^k\over r_{>}^{k+1}}
    f(r')
    \d r'
    = r
    \int_0^r
    {r'^k\over r^{k+1}}
    f(r')
    \d r'
    +
    r \int_r^\infty
    {r^k\over r'^{k+1}}
    f(r')
    \d r'
    =

    =
    {1\over r^k}
    \int_0^r
    {x^k}
    f(x)
    \d x
    +
    r^{k+1}
    \int_r^\infty
    {1\over x^{k+1}}
    f(x)
    \d x
    =Z^k(r)
    +
    r^{k+1}
    \int_r^\infty {1\over x^{k+1}} f(x) \d x

where:

.. math::

    Z^k(r) =
    {1\over r^k}
    \int_0^r
    {x^k}
    f(x)
    \d x

    {\d Z^k(r) \over \d r}= -{k\over r} Z^k(r) + f(r)

    Z^k(0) = 0

Now we differentiate $Y^k(r)$:

.. math::

    {\d Y^k(r) \over \d r} = {\d Z^k(r) \over \d r}
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} f(x) \d x
        -f(r)
    =

    =
    -{k\over r} Z^k(r) + f(r)
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} f(x) \d x
        -f(r) =

    =
    -{k\over r} Z^k(r)
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} f(x) \d x =

    =
    -{k\over r} Z^k(r)
        + {k+1\over r} (Y^k(r) - Z^k(r)) =

    =
    -{2k+1\over r} Z^k(r) + {k+1\over r} Y^k(r)

Also $Y^k(\infty) = Z^k(\infty)$, so we get the following set of first order
differential equations with boundary conditions:

.. math::

    \left({\d\over\d r} - {k+1\over r}\right) Y^k(r) = -{2k+1\over r} Z^k(r)

    \left({\d\over\d r} + {k\over r}\right) Z^k(r) = f(r)

    Y^k(\infty) = Z^k(\infty)

    Z^k(0) = 0

One way to calculate the Hartree screening function is to integrate the second
equation from the left using the boundary condition $Z^k(0) = 0$ and then
integrate the first equation from the right, using the boundary condition
$Y^k(\infty) = Z^k(\infty)$.

Another way is to obtain one second order equation. Expressing $Z^k$ from the
first equation:

.. math::

    Z^k(r) = -{r\over 2k+1}\left({\d\over\d r} - {k+1\over r}\right) Y^k(r) =

    =-{r\over 2k+1}{\d Y^k(r)\over \d r} + {k+1\over 2k+1} Y^k(r)

and substituting into the second equation we get:

.. math::

    -\left({\d\over\d r} + {k\over r}\right)
        \left({r\over 2k+1}{\d Y^k(r)\over \d r} + {k+1\over 2k+1} Y^k\right)
        = f(r)

    -{r\over 2k+1}\left({\d^2\over\d r^2} - {k(k+1)\over r^2}\right)
        Y^k(r)
        = f(r)

    \left(-{\d^2\over\d r^2} + {k(k+1)\over r^2}\right) Y^k(r)
        = {2k+1\over r} f(r)

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

which for $r\to\infty$ becomes:

.. math::

    \left.{\d Y^k(r)\over \d r}\right|_{r=\infty} = 0

but in practise, it's better to use the former Newton (Robin) boundary
condition. We have obtain one second order equation for $Y^k(r)$

.. math::

    \left(-{\d^2\over\d r^2} + {k(k+1)\over r^2}\right) Y^k(r)
        = {2k+1\over r} f(r)

with boundary conditions:

.. math::

    Y^k(0) = 0

    {\d Y^k(r)\over \d r} + {k\over r} Y^k(r) = 0

The
weak formulation is:

.. math::

    \int_0^{r_{max}} Y^k{}'(r) v'(r) + {k(k+1)\over r^2} Y^k(r) v(r) \d r
        -[Y^k{}'(r)v(r)]_0^{r_{max}}
        = \int_0^{r_{max}} {2k+1\over r}f(r)v(r) \d r

The boundary term can be simplified using the boundary conditions as:

.. math::

        -[Y^k{}'(r)v(r)]_0^{r_{max}}
        = -Y^k{}'(r_{max})v(r_{max}) + Y^k{}'(0) v(0)
        = -Y^k{}'(r_{max})v(r_{max})
        = {k\over r_{max}} Y^k(r_{max})v(r_{max})

so we get

.. math::

    \int_0^{r_{max}} Y^k{}'(r) v'(r) + {k(k+1)\over r^2} Y^k(r) v(r) \d r
        + {k\over r_{max}} Y^k(r_{max})v(r_{max})
        = \int_0^{r_{max}} {2k+1\over r}f(r)v(r) \d r

where the test functions $v(r)$ have the constrain $v(0)=0$ on the left
boundary and no constrain on the right.

Hartree Potential in Spherical Symmetry
---------------------------------------

For both open and closed shell atoms we get exactly:

.. math::

    V_H({\bf x})
        = \int {n({\bf y})\over|{\bf x}-{\bf y}|} \d^3 y
        = \int {\sum_{j=1}^Z|\psi_j({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y =

        = 2\sum_{nlm}\int {|Y_{lm}(\Omega')|^2 P_{nl}^2(r')\over
            |{\bf x}-{\bf y}|} \d\Omega' \d r' =

        = 2\sum_{nlm}\sum_{l'm'}\int {r_<^{l'}\over r_>^{l'+1}}
            {4\pi\over 2l'+1}
            Y_{lm}^*(\Omega')Y_{lm}(\Omega')
            Y_{l'm'}^*(\Omega)Y_{l'm'}(\Omega') P_{nl}^2(r') \d\Omega' \d r' =

        = 2\sum_{nlm}\sum_{l'}\int {r_<^{l'}\over r_>^{l'+1}}
            {4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega) \sqrt{2l'+1\over 4\pi}
                c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = 2\sum_{nl}\sum_{l'=0}^{2l}\int {r_<^{l'}\over r_>^{l'+1}}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)
                \sum_m c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = 2\sum_{nl}\int {1\over r_>}
            \sqrt{4\pi}
            Y_{00}^*(\Omega)
                \sum_m c^0(l, m, l, m) P_{nl}^2(r') \d r' +

        + 2\sum_{nl}\sum_{l'=1}^{2l}\int {r_<^{l'}\over r_>^{l'+1}}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)
                \sum_m c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = \sum_{nl}2\sum_m c^0(l, m, l, m) \int {1\over r_>}
                 P_{nl}^2(r') \d r' +

        + 2\sum_{nl}\sum_{l'=1}^{2l}\int {r_<^{l'}\over r_>^{l'+1}}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)
                \sum_m c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = \sum_{nl}2\sum_m \int {1\over r_>}
                 P_{nl}^2(r') \d r' +

        + 2\sum_{nl}\sum_{l'=1}^{2l}\int {r_<^{l'}\over r_>^{l'+1}}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)
                \sum_m c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = \sum_{nl} f_{nl} \int {1\over r_>} P_{nl}^2(r') \d r' +

        + 2\sum_{nl}\sum_{l'=1}^{2l}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)\sum_m c^{l'}(l, m, l, m)
          \int {r_<^{l'}\over r_>^{l'+1}} P_{nl}^2(r') \d r'

For closed shell atoms we use the fact, that

.. math::

        \sum_{m=-l}^l c^{l'}(l, m, l, m) = (2l+1) \delta_{l' 0}

and the second term disappears, and for open shell atoms
we have to use the central field approximation: we average
the integral for $V_H$ over the angles:

.. math::

    V_H({\bf x}) \to V_H(r) = {1\over 4\pi} \int V_H({\bf x})\, \d \Omega

and using the fact, that

.. math::

    \int Y_{l'0}^*(\Omega)\, \d \Omega = \sqrt{4\pi} \delta_{l' 0}

the second term disappears as well. We got the same expression for both open
shell (with central field approximation) and closed shell (no approximation)
atoms.  The radial charge density is:

.. math::

    n(r) = {1\over 4\pi} \sum_{nl} f_{nl} \left(P_{nl}(r)\over r\right)^2

So we got:

.. math::

    V_H(r) =
       \sum_{nl} f_{nl} \int {1\over r_>} P_{nl}^2(r') \d r'
       =\int {4\pi n(r') r'^2 \over r_>} \d r'
       = {Y^0(4\pi n(r) r^2, r) \over r}

The Hartree screening function $Y^0(4\pi n(r) r^2, r)$ is given by the equation:

.. math::

    -{\d^2\over\d r^2} Y^0(r) = {1\over r} 4\pi n(r) r^2

So $V_H(r)$ satisfies the radial Poisson equation:

.. math::

    (V_H(r) r)'' = -{1\over r} 4\pi n(r) r^2

    V_H''(r) r + 2V_H'(r) = - 4\pi n(r) r

    V_H''(r) + {2\over r}V_H'(r) = -4\pi n(r)

Nonlocal Exchange Potential in Spherical Symmetry
-------------------------------------------------

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
            P_{n'l'}(r) =

    =
    {Y_{lm}(\Omega)\over r}
    \sum_{n'l'}\sum_{k=|l-l'|}^{k=l+l'}
        (2l'+1)
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'\,
            P_{n'l'}(r) =

    =
    {Y_{lm}(\Omega)\over r}
    \sum_{n'l'} f_{n'l'} \sum_{k=|l-l'|}^{k=l+l'}
        \half
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'\,
            P_{n'l'}(r)

Functions with different spins don't contribute to the sum, so there is no
multiplication by 2. We assumed closed shells atoms (we summed over all $m'$ in
the above). We used the result of the integral in
:ref:`five_spherical_harmonics` and also:

.. math::
    :label: using3j

    \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
        = \sqrt{2l'+1\over 2l+1}
            \sqrt{(2l'+1)(2l+1)}
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        = (2l'+1)
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2


Radial Hartre-Fock Equations
----------------------------

Using the above integrals, the HF equations become:

.. math::

    -\half P_{nl}''(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)P_{nl}(r) +

            -\sum_{n'l'}
                f_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int
                {r_{<}^k\over r_{>}^{k+1}}
                P_{nl}(r')
                P_{n'l'}(r')
                \d r'\,
                    P_{n'l'}(r)
        = \epsilon_{nl} P_{nl}(r)

with:

.. math::

    V_H(r) =
       \sum_{nl} f_{nl} \int {1\over r_>} P_{nl}^2(r') \d r'

Using the Hartree screening functions, the HF equations are:

.. math::

    -\half P_{nl}''(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)P_{nl}(r) +

            -\sum_{n'l'}
                f_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                {Y^k(P_{nl}(r) P_{n'l'}(r), r) \over r}
                P_{n'l'}(r)
        = \epsilon_{nl} P_{nl}(r)

with:

.. math::

    V_H(r) = \sum_{nl} f_{nl} {Y^0(P_{nl}^2(r), r) \over r}
        = {Y^0(4\pi n(r) r^2, r) \over r}

Example: Helium
~~~~~~~~~~~~~~~

For Helium atom, the only nonzero occupation numbers are:

.. math::

    f_{10} = 2

and the sum over $n'l'$ simplifies to:

.. math::

    \sum_{n'l'}
        f_{n'l'}
        \sum_{k=|l-l'|}^{k=l+l'}
        \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
    = f_{10} \half \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}^2
    = f_{10} \half = 1

so we only need to solve for the $1s$ state and we get:

.. math::

    -\half P_{10}''(r) +
        \left(-{Z\over r} + V_H(r)\right)P_{10}(r)
            -{Y^0(P_{10}(r) P_{10}(r), r) \over r}
                P_{10}(r)
        = \epsilon_{10} P_{10}(r)

with:

.. math::

    V_H(r) = 2 {Y^0(P_{10}^2(r), r) \over r}
        = {Y^0(4\pi n(r) r^2, r) \over r}

We can combine the equations:

.. math::

    -\half P_{10}''(r) +
        \left(-{Z\over r} + 2 {Y^0(P_{10}^2(r), r) \over r}\right)P_{10}(r)
            -{Y^0(P_{10}^2(r), r) \over r}
                P_{10}(r)
        = \epsilon_{10} P_{10}(r)

and we obtain:

.. math::

    -\half P_{10}''(r) +
        \left(-{Z\over r} + {Y^0(P_{10}^2(r), r) \over r}\right)P_{10}(r)
        = \epsilon_{10} P_{10}(r)

FEM
---

The weak formulation is ($u(r) = P_{nl}(r)$):

.. math::

    \int_0^\infty \left( \half u'(r) v'(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)u(r)v(r)
            \right) \d r+

            -\sum_{n'l'}
                f_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int_0^\infty
                v(r)
                P_{n'l'}(r)
                {Y^k(u(r) P_{n'l'}(r), r)\over r}
                \d r
        = \epsilon \int_0^\infty u(r)v(r)\d r
