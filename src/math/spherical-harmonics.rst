.. index:: Legendre polynomials

Legendre Polynomials
====================

Legendre polynomials $P_l(x)$ defined by the Rodrigues's formula

.. math::

       P_l(x)={1\over2^l l!}{\d^l\over\d x^l}[(x^2-1)^l]

they also obey the completeness relation

.. math::
    :label: Lorto

       \sum_{l=0}^\infty {2l+1\over2}P_l(x')P_l(x)=\delta(x-x')

and orthogonality relation:

.. math::

    \int_{-1}^1 P_k(x) P_l(x) \d x = {2\delta_{kl} \over 2k+1}

Two Legendre polynomials can be expanded in a series:

.. math::

    P_k(x) P_l(x) = \sum_{n=0}^{k+l} {A(s-k) A(s-n) A(s-l)\over A(s)}
        {2n+1\over 2s+1} P_n(x)

where $s={k+l+n\over 2}$ and

.. math::

    A(m) = {1\cdot3\cdot5 \cdot \dots \cdot (2m-1) \over
        1\cdot 2\cdot 3\cdot \dots \cdot m} =
            {(2m)!\over 2^m (m!)^2} = {1\over 2^m}\binom{2m}{m}

This can be proven by induction, see [Adams]_.
We can now calculate the integral of three Legendre polynomials:

.. math::
    :label: int_three_legendre_polys

    \int_{-1}^1 P_k(x) P_l(x) P_m(x) \d x =

    = \int_{-1}^1
        \sum_{n=0}^{k+l} {A(s-k) A(s-n) A(s-l)\over A(s)}
        {2n+1\over 2s+1} P_n(x)
        P_m(x) \d x =

    = \sum_{n=0}^{k+l} {A(s-k) A(s-n) A(s-l)\over A(s)}
        {2n+1\over 2s+1}
        \int_{-1}^1 P_n(x) P_m(x) \d x =

    = \sum_{n=0}^{k+l} {A(s-k) A(s-n) A(s-l)\over A(s)}
        {2n+1\over 2s+1}
        {2\over 2n+1} \delta_{nm} =

    = 2 {A(s-k) A(s-l) A(s-m)\over A(s)} {1\over 2s+1} =

    = 2 {
            {1\over2^{s-k}}\binom{2s-2k}{s-k}
            {1\over2^{s-l}}\binom{2s-2l}{s-l}
            {1\over2^{s-m}}\binom{2s-2m}{s-m}
            \over
            {1\over2^{s}}\binom{2s}{s}
        } {1\over 2s+1} =

    = 2 {2^s\over2^{s-k+s-l+s-m}} {
            \binom{2s-2k}{s-k}
            \binom{2s-2l}{s-l}
            \binom{2s-2m}{s-m}
            \over
            \binom{2s}{s}
        } {1\over 2s+1} =

    = 2 {
            \binom{2s-2k}{s-k}
            \binom{2s-2l}{s-l}
            \binom{2s-2m}{s-m}
            \over
            \binom{2s}{s}
        } {1\over 2s+1} =

    = 2 {
            {(2s-2k)! \over ((s-k)!)^2}
            {(2s-2l)! \over ((s-l)!)^2}
            {(2s-2m)! \over ((s-m)!)^2}
            {(s!)^2 \over (2s)!}
        } {1\over 2s+1} =

    = 2 {(2s-2k)! (2s-2l)! (2s-2m)! \over (2s+1)!}
        \left[{s! \over (s-k)! (s-l)! (s-m)!}\right]^2
       =

    = 2 \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2

As such, we can write the series expansion as:

.. math::

    P_k(x) P_l(x) = \sum_{m=|k-l|}^{k+l}
        {2m+1\over 2}\int_{-1}^1 P_k(x) P_l(x) P_m(x) \d x\,\,
        P_m(x) =

    = \sum_{m=|k-l|}^{k+l}
        \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2
        (2m+1) P_m(x)


.. [Adams] Adams, J. C. (1878). On the Expression of the Product of Any Two Legendre’s Coefficients by Means of a Series of Legendre's Coefficients.  Proceedings of the Royal Society of London, 27, 63-71.


.. index:: spherical harmonics

Spherical Harmonics
===================


Are defined by

.. math::

       Y_{lm}(\theta,\phi)=\sqrt{{2l+1\over4\pi}{(l-m)!\over(l+m)!}}\,P_l^m(\cos\theta)\,e^{im\phi}

where $P_l^m$ are associated Legendre polynomials defined by

.. math::

       P_l^m(x)=(-1)^m (1-x^2)^{m/2}{\d^m\over\d x^m} P_l(x)

and $P_l$ are Legendre polynomials. Sometimes the spherical harmonics are
written as:

.. math::

    Y_{lm}(\theta,\phi) = \Theta_{lm}(\theta) \Phi_m(\phi)

where:

.. math::

    \Phi_m(\phi) &= {1\over\sqrt{2\pi}} e^{im\phi} \\
    \Theta_{lm}(\theta) &= \sqrt{{2l+1\over2}{(l-m)!\over(l+m)!}}\,P_l^m(\cos\theta)

The spherical harmonics are ortonormal:

.. math::
    :label: Yorto

       \int Y_{lm}\,Y^*_{l'm'}\,\d\Omega = \int_0^{2\pi}\int_0^{\pi} Y_{lm}(\theta,\phi)\,Y^*_{l'm'}(\theta,\phi)\sin\theta\,\d\theta\,\d\phi = \delta_{mm'}\delta_{ll'}

and complete (both in the $l$-subspace and the whole space):

.. math::
    :label: lcomplete

       \sum_{m=-l}^l|Y_{lm}(\theta,\phi)|^2={2l+1\over4\pi}


.. math::
    :label: Ycomplete

       \sum_{l=0}^\infty\sum_{m=-l}^lY_{lm}(\theta,\phi)Y_{lm}^*(\theta',\phi') ={1\over\sin\theta}\delta(\theta-\theta')\delta(\phi-\phi')= \delta({\bf\hat r}-{\bf\hat r'})

The relation :eq:`lcomplete` is a special case of an addition theorem for spherical harmonics

.. math::
    :label: lsum

       \sum_{m=-l}^lY_{lm}(\theta,\phi)Y_{lm}^*(\theta',\phi')= {2l+1\over 4\pi}P_l(\cos\gamma)

where $\gamma$ is the angle between the unit vectors given by ${\bf\hat r}=(\theta,\phi)$ and ${\bf\hat r'}=(\theta',\phi')$:

.. math::

       \cos\gamma=\cos\theta\cos\theta'+\sin\theta\sin\theta'\cos(\phi-\phi') ={\bf\hat r}\cdot{\bf\hat r'}

Relations between complex conjugates is:

.. math::

    Y_{l m}^*(\Omega) = (-1)^m Y_{l,-m}(\Omega)

    (-1)^m Y_{l,-m}^*(\Omega) = Y_{lm}(\Omega)

Examples
~~~~~~~~

.. math::

    \int_{-1}^1 P_k(x) \d x
        = \int_{-1}^1 P_k(x) P_0(x) \d x
        = 2\delta_{k0}

    \int Y_{k0}(\Omega) \d \Omega
        = \int Y_{k0}(\Omega) \sqrt{4\pi} Y_{00}(\Omega) \d \Omega
        = \sqrt{4\pi} \delta_{k0}


Gaunt Coefficients
==================

We use the Wigner-Eckart theorem:

.. math::

    \braket{j m | T^k_q | j' m'} = (-1)^{j-m}
        \begin{pmatrix} j & k & j' \\ -m & q & m' \end{pmatrix}
        (j || T^k || j')

Where:

.. math::

    T^k_q = Y_{k q}

In order to calculate the reduced matrix element $(j || T^k || j')$, we
evaluate the W-E theorem for $m=q=m'=0$:

.. math::

    \braket{j 0 | T^k_0 | j' 0} = (-1)^{j}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix}
        (j || T^k || j')

and also evaluate the left hand side explicitly:

.. math::

    \braket{j 0 | T^k_0 | j' 0}
        = \braket{j 0 | Y_{k 0} | j' 0}
        = \int Y_{j0}^*(\Omega) Y_{k0}(\Omega) Y_{j'0}(\Omega) \d \Omega =

    = \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi} {1\over 4\pi}
        \int P_j(\cos\theta) P_k(\cos\theta) P_{j'}(\cos\theta) \sin\theta
            \d \theta \d \phi =

    = \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi} {1\over 2}
        \int_{-1}^1 P_j(x) P_k(x) P_{j'}(x) \d x =

    = \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix}^2

where we used :eq:`int_three_legendre_polys`.
Comparing these two results, we get:

.. math::

    (j || T^k || j') = (-1)^{-j}
        \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix}

and finally:

.. math::

    \int Y_{jm}^*(\Omega) Y_{kq}(\Omega) Y_{j'm'}(\Omega) \d \Omega =

    =\braket{j m | T^k_q | j' m'} = (-1)^{j-m}
        \begin{pmatrix} j & k & j' \\ -m & q & m' \end{pmatrix}
        (j || T^k || j') =

    = (-1)^{j-m}
        \begin{pmatrix} j & k & j' \\ -m & q & m' \end{pmatrix}
        (-1)^{-j}
        \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix} =

    = (-1)^{-m}
        \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} j & k & j' \\ -m & q & m' \end{pmatrix}

In order to evaluate other integrals of spherical harmonics, we just use the
above result, for example:

.. math::

    \int Y_{l_1 m_1}(\Omega) Y_{l_2 m_2}(\Omega) Y_{l_3 m_3}(\Omega) \d\Omega =

    =(-1)^{m_1}\int Y_{l_1 -m_1}^*(\Omega) Y_{l_2 m_2}(\Omega)
        Y_{l_3 m_3}(\Omega) \d\Omega=

    =(-1)^{m_1}
    (-1)^{-(-m_1)}
        \sqrt{(2l_1+1)(2l_2+1)(2l_3+1)\over 4\pi}
        \begin{pmatrix} l_1 & l_2 & l_3 \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l_1 & l_2 & l_3 \\ -(-m_1) & m_2 & m_3 \end{pmatrix}=

    = \sqrt{(2l_1+1)(2l_2+1)(2l_3+1)\over 4\pi}
        \begin{pmatrix} l_1 & l_2 & l_3 \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l_1 & l_2 & l_3 \\ m_1 & m_2 & m_3 \end{pmatrix}

This is the most symmetric relation. It was first obtained by [Gaunt]_
(equation (9), p. 194, where he expanded the $3j$ symbols, so his formula is
more complex but equivalent to the above).

It is useful to incorporate
the selection rule $m_1 + m_2 + m_3 = 0$ of the $3j$ symbols into the formula
and we get:

.. math::

    c^k(l, m, l', m') =
        \sqrt{4\pi \over 4k+1}
    \int Y_{lm}^*(\Omega) Y_{k, m-m'}(\Omega) Y_{l'm'}(\Omega) \d\Omega =

    = (-1)^{-m}
        \sqrt{4\pi \over 4k+1}
        \sqrt{(2l+1)(2k+1)(2l'+1)\over 4\pi}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    = (-1)^{-m}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix}

From the other selection rules of the $3j$ symbols it follows, that
the $c^k(l, m, l', m')$ coefficients are nonzero only when:

.. math::

    |l-l'| \le k \le l + l'

    l+l'+k = \mbox{even integer}

.. [Gaunt] Gaunt, J. A. (1929). The Triplets of Helium. Philosophical Transactions of the Royal Society of London, 228, 151-196.


Example I
~~~~~~~~~

.. math::

    c^0(l, m, l', m')
        =\sqrt{4\pi}
    \int Y_{lm}^*(\Omega) Y_{00}(\Omega) Y_{l'm'}(\Omega) \d\Omega
        =\delta_{l l'}\delta_{m m'}

Example II
~~~~~~~~~~

.. math::

    \sum_{m=-l}^l c^k(l, m, l, m)
        = \sum_m
        \sqrt{4\pi \over 4k+1}
        \int Y_{lm}^*(\Omega) Y_{k0}(\Omega) Y_{lm}(\Omega) \d\Omega =

        =
        \sqrt{4\pi \over 4k+1}
        \int \sum_m |Y_{lm}(\Omega)|^2 Y_{k0}(\Omega) \d\Omega =

        =
        \sqrt{4\pi \over 4k+1}
        {2l+1\over 4\pi} \int Y_{k0}(\Omega) \d\Omega =

        =
        \sqrt{4\pi \over 4k+1}
        {2l+1\over 4\pi}
        \sqrt{4\pi} \delta_{k0} =

        =
        (2l+1) \delta_{k0}

Example III
~~~~~~~~~~~

.. math::

    c^k(l, m, l', m') =
        \sqrt{4\pi \over 4k+1}
    \int Y_{lm}^*(\Omega) Y_{k, m-m'}(\Omega) Y_{l'm'}(\Omega) \d\Omega =

    = \sqrt{4\pi \over 4k+1}
    \int \Theta_{lm}\Phi_m^* \Theta_{k, m-m'}\Phi_{m-m'} \Theta_{l'm'}\Phi_{m'}
        \sin\theta \d\theta \d\phi =

    = \sqrt{4\pi \over 4k+1}
    \int_0^\pi \Theta_{lm} \Theta_{k, m-m'} \Theta_{l'm'} \sin\theta \d\theta
    \int_0^{2\pi} \Phi_m^* \Phi_{m-m'} \Phi_{m'} \d\phi =

    = \sqrt{4\pi \over 4k+1}
    \int_0^\pi \Theta_{lm} \Theta_{k, m-m'} \Theta_{l'm'} \sin\theta \d\theta
    \left(1\over\sqrt{2\pi}\right)^3
    \int_0^{2\pi} e^{-im\phi} e^{i(m-m')\phi} e^{im'\phi} \d\phi =

    = \sqrt{4\pi \over 4k+1}
    \int_0^\pi \Theta_{lm} \Theta_{k, m-m'} \Theta_{l'm'} \sin\theta \d\theta
    \left(1\over\sqrt{2\pi}\right)^3
    \int_0^{2\pi} \!\!\!\d\phi =

    = \sqrt{2\over 4k+1}
    \int_0^\pi \Theta_{lm} \Theta_{k, m-m'} \Theta_{l'm'} \sin\theta \d\theta

Example IV
~~~~~~~~~~

.. math::

    c^k(l, -m, l', -m') =

    = (-1)^{m}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ m & -m+m' & -m' \end{pmatrix} =

    = (-1)^{m}(-1)^{l+k+l'}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    = (-1)^{-m}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    c^k(l, m, l', m')

Where we used the fact, that $l+k+l'$ is an even integer and
$(-1)^m=(-1)^{-m}$. $c^k$ is not symmetric in $l m$ and $l' m'$:

.. math::

    c^k(l', m', l, m)

    = (-1)^{-m'}
        \sqrt{(2l'+1)(2l+1)}
        \begin{pmatrix} l' & k & l \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l' & k & l \\ -m' & m'-m & m \end{pmatrix} =

    = (-1)^{-m'}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ m & m'-m & -m' \end{pmatrix} =

    = (-1)^{-m'}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    = (-1)^{m-m'} (-1)^{-m}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    = (-1)^{m-m'} c^k(l, m, l', m')

Few other identities:

.. math::

    c^k(l, 0, l', 0)
        = \sqrt{(2l+1)(2l'+1)}
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2

    \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        = {c^k(l, 0, l', 0) \over \sqrt{(2l+1)(2l'+1)}}
        = {c^{l'}(l, 0, k, 0) \over \sqrt{(2l+1)(2k+1)}}
        = {c^{l}(l', 0, k, 0) \over \sqrt{(2l'+1)(2k+1)}}

    c^k(l, 0, l', 0) = c^k(l', 0, l, 0)

.. _five_spherical_harmonics:

Example V
~~~~~~~~~

.. math::
    :label: five_spherical_harmonics

    \sum_{m'}\sum_{q}\int
            Y_{l'm'}(\Omega)
            Y_{l'm'}^*(\Omega')
            Y_{kq}(\Omega)
            Y_{kq}^*(\Omega')
            Y_{lm}(\Omega')
            \d \Omega' =

    =\int
            {2l'+1\over 4\pi} P_{l'}({\bf x}\cdot{\bf x}')
            {2k+1\over 4\pi} P_k({\bf x}\cdot{\bf x}')
            Y_{lm}(\Omega')
            \d \Omega' =

    =\int
            {2l'+1\over 4\pi}
            {2k+1\over 4\pi}
            \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
                \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
                {4\pi \over 2\lambda+1}
                \sum_{\mu=-\lambda}^\lambda
                Y_{\lambda\mu}^*(\Omega')
                Y_{\lambda\mu}(\Omega)
            Y_{lm}(\Omega')
            \d \Omega' =

    =
            {2l'+1\over 4\pi}
            {2k+1\over 4\pi}
            \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
                \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
                {4\pi \over 2\lambda+1}
                \sum_{\mu=-\lambda}^\lambda
                Y_{\lambda\mu}(\Omega)
            \delta_{\lambda l}
            \delta_{\mu m}
            =

    =
            {2k+1\over 4\pi}
                \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
                Y_{lm}(\Omega)


Where we used the following identities:

.. math::

    \sum_{m'}
        Y_{l'm'}(\Omega)
        Y_{l'm'}^*(\Omega')
    = {2l'+1\over 4\pi} P_{l'}({\bf x}\cdot{\bf x}')

    \sum_{q}
        Y_{kq}(\Omega)
        Y_{kq}^*(\Omega')
    = {2k+1\over 4\pi} P_k({\bf x}\cdot{\bf x}')

    P_k({\bf x}\cdot{\bf x}')P_{l'}({\bf x}\cdot{\bf x}')
    = \sum_{\lambda=|l'-k|}^{l'+k}
        \begin{pmatrix} k & l' & \lambda \\ 0 & 0 & 0 \end{pmatrix}^2
        (2\lambda+1) P_\lambda({\bf x}\cdot{\bf x}') =

        = \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
            \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
            P_\lambda({\bf x}\cdot{\bf x}') =

    = \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
        \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
        {4\pi \over 2\lambda+1}
        \sum_{\mu=-\lambda}^\lambda
        Y_{\lambda\mu}^*(\Omega')
        Y_{\lambda\mu}(\Omega)

Note: using the integral of 3 spherical harmonics directly in
:eq:`five_spherical_harmonics`:

.. math::

    \sum_{m'}\sum_{q}\int
            Y_{l'm'}(\Omega)
            Y_{l'm'}^*(\Omega')
            Y_{kq}(\Omega)
            Y_{kq}^*(\Omega')
            Y_{lm}(\Omega')
            \d \Omega' =

    =\sum_{m'}
            Y_{l'm'}(\Omega)
            Y_{k, m-m'}(\Omega)
            \sqrt{4\pi\over 2k+1}
            c^k(l, m, l', m')

doesn't straightforwardly lead to the final result, as it is not obvious how to
simplify things further.


Wigner 3j Symbols
=================

Relation between the Wigner $3j$ symbols and Clebsch-Gordan coefficients:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix}
        = {(-1)^{j_1-j_2-m_3}\over \sqrt{2j_3+1}}
            (j_1 m_1 j_2 m_2 | j_3 -m_3)

    (j_1 m_1 j_2 m_2 | j_3 m_3)
        = (-1)^{j_1-j_2+m_3}\sqrt{2j_3+1}
        \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & -m_3 \end{pmatrix}

They are nonzero only when:

.. math::

    m_1 + m_2 + m_3 = 0

    j_1+j_2+j_3 = \mbox{integer (or even integer if $m_1=m_2=m_3=0$)}

    |m_i| \le j_i

    |j_1-j_2| \le j_3 \le j_1+j_2

They have lots of symmetries. The $3j$ symbol is invariant for an even
permutation of columns:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} =

        = \begin{pmatrix} j_2 & j_3 & j_1 \\ m_2 & m_3 & m_1 \end{pmatrix} =

        = \begin{pmatrix} j_3 & j_1 & j_2 \\ m_3 & m_1 & m_2 \end{pmatrix}

For an odd permutation of columns it changes sign if $j_1+j_2+j+3$ is an odd
integer:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} =

        = (-1)^{j_1+j_2+j_3}
        \begin{pmatrix} j_2 & j_1 & j_3 \\ m_2 & m_1 & m_3 \end{pmatrix} =

        = (-1)^{j_1+j_2+j_3}
        \begin{pmatrix} j_1 & j_3 & j_2 \\ m_1 & m_3 & m_2 \end{pmatrix} =

        = (-1)^{j_1+j_2+j_3}
        \begin{pmatrix} j_3 & j_2 & j_1 \\ m_3 & m_2 & m_1 \end{pmatrix}

and the same if you change the sign of the second row:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} =

        = (-1)^{j_1+j_2+j_3}
        \begin{pmatrix} j_1 & j_2 & j_3 \\ -m_1 & -m_2 & -m_3 \end{pmatrix}


.. index:: multipole expansion

Multipole expansion
===================

Assuming $r' \ll r$:


.. math::

    {1\over |{\bf r}-{\bf r'}|} ={1\over \sqrt{({\bf r}-{\bf r'})^2}} ={1\over \sqrt{r^2-2{\bf r}\cdot {\bf r'} + r'^2}} ={1\over r\sqrt{1-2\left(r'\over r\right){\bf\hat r}\cdot {\bf\hat r'} + \left(r'\over r\right)^2}} =

    ={1\over r}\sum_{l=0}^\infty\left(r'\over r\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =

    ={1\over r}\left( P_0({\bf\hat r}\cdot {\bf\hat r'}) + P_1({\bf\hat r}\cdot {\bf\hat r'}){r'\over r} + P_2({\bf\hat r}\cdot {\bf\hat r'})\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =

    ={1\over r}\left( 1 + {\bf\hat r}\cdot {\bf\hat r'} {r'\over r} + \half\left(3({\bf\hat r}\cdot {\bf\hat r'})^2-1\right)\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =

    ={1\over r} +{{\bf r}\cdot {\bf r'}\over r^3} +{3({\bf r}\cdot {\bf r'})^2-r^2r'^2\over 2r^5} + O\left(r'^3\over r^4\right)

We can also use the formula:

.. math::

    \sum_m \braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r}'}
        ={2l+1 \over 4\pi} \braket{{\bf\hat r}\cdot{\bf\hat r'}|P_l}

and rewrite the expansion using spherical harmonics:

.. math::

    {1\over |{\bf r}-{\bf r'}|} ={1\over r}\sum_{l=0}^\infty\left(r'\over r\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =

    ={1\over r}\sum_{l,m}\left(r'\over r\right)^l {4\pi\over 2l+1}\braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r}'}
    ={1\over r}\sum_{l,m}\left(r'\over r\right)^l {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')

Assuming $r' \gg r$ we get:

.. math::

    {1\over |{\bf r}-{\bf r'}|} ={1\over r'}\sum_{l=0}^\infty\left(r\over r'\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =

    = {1\over r'}\sum_{l,m}\left(r\over r'\right)^l
    {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')

We can combine the two formulas by introducing $r_{>} = \max(r, r')$ and
$r_{<} = \min(r, r')$ and then for any $r$ and $r'$ we get:

.. math::

    {1\over |{\bf r}-{\bf r'}|}
        ={1\over r_{>}}\sum_{l=0}^\infty\left(r_{<}\over r_{>}\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =

        = {1\over r_{>}}\sum_{l,m}\left(r_{<}\over r_{>}\right)^l
            {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}') =

        = \sum_{l,m}{r_{<}^l\over r_{>}^{l+1}}
            {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')
