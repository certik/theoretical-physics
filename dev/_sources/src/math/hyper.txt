.. index:: Hypergeometric functions

========================
Hypergeometric Functions
========================

The series:

.. math::

    \sum_{k=0}^\infty t_k

with $t_0=1$
is geometric if the ratio of two consecutive terms $t_{k+1}/t_k$ is a constant
(with respect to $k$):

.. math::

    {t_{k+1} \over t_k} = x

then we get:

.. math::

    \sum_{k=0}^\infty t_k = 
        \sum_{k=0}^\infty x^k

It is hypergeometric if the ratio $t_{k+1}/t_k$ is a rational function (with
respect to $k$):

.. math::

    {t_{k+1} \over t_k} = {P(k)\over Q(k)}

where $P(k)$ and $Q(k)$ are polynomials in $k$, which we can completely factor
into the form

.. math::
    :label: hyper_ratio

    {t_{k+1} \over t_k} = {P(k)\over Q(k)}
        = {(k+a_1)(k+a_2)\cdots(k+a_p)\over
            (k+b_1)(k+b_2)\cdots(k+b_q)(k+1)} x

where $x$ is a constant and the $(k+1)$ factor is just a convention (if the
polynomial $Q(k)$ does not contain the factor $(k+1)$ we can just add it to
both numerator and denominator and absorb the one into $a_p$). The
hypergeometric series is then given by:

.. math::

    {}_p F_q(a_1, a_2, \dots, a_p; b_1, b_2, \dots, b_q; x)
        = \sum_{k=0}^\infty {(a_1)_k (a_2)_k \cdots (a_p)_k \over
            (b_1)_k (b_2)_k \cdots (b_q)_k} {x^k\over k!}

where

.. math::

    (a)_k = {\Gamma(a+k)\over\Gamma(a)} = \begin{cases}
        a(a+1)(a+2)\cdots(a+k-1), & \mbox{if $k\ge 1$;} \\
        1, & \mbox{if $k=0$}\\
        \end{cases}

is the rising factorial function (also called the Pochhammer symbol).

To write a function as a hypergeometric series, we simply expand it in series
and then write the ratio $t_{k+1}/t_k$ in the form :eq:`hyper_ratio` and
immediately identify the proper ${}_p F_q$ function. If the ratio cannot be
put into the form :eq:`hyper_ratio` then the function is not hypergeometric.

Convergence Conditions
======================

If any $a_i=0, -1, -2, \dots$, then the series is a polynomial of degree
$-a_i$.

If any $b_i=0, -1, -2, \dots$ then the denominators eventually become 0 (unless
the series is terminated as a polynomial before that, due to the previous
point) and the series is undefined.

Except the previous two cases, the radius of convergence $R$ of the
hypergeometric series is:

.. math::

    R = \begin{cases}
        \infty & \mbox{if $p \le q$;} \\
        1 & \mbox{if $p = q+1$;} \\
        0 & \mbox{if $p > q+1$.} \\
        \end{cases}

Elementary and Special Functions
================================

The hypergeometric functions for low $p$ and $q$ have special names:

+-----------------+----------------------------------------------------------------+
| ${}_0F_1$ | confluent hypergeometric limit function                        |
+-----------------+----------------------------------------------------------------+
| ${}_1F_1$ | Kummer's confluent hypergeometric function of the first kind   |
+-----------------+----------------------------------------------------------------+
| ${}_2F_1$ | Gauss' hypergeometric function                                 |
+-----------------+----------------------------------------------------------------+

Most common functions can be expressed using ${}_p F_q$ as follows:

The Series 0F0
--------------

Elementary functions:

.. math::

    e^{x}
        = \sum_{k=0}^\infty {x^k\over k!}
        = {}_0 F_0(x)

The Series 1F0
--------------

Elementary functions:

.. math::

    {1\over 1-x} = \sum_{k=0}^\infty x^k = {}_1 F_0(1; x)

    {1\over (1-x)^a} = \sum_{k=0}^\infty {(a+k-1)!\over (a-1)! k!} x^k
        = {}_1 F_0(a; x)

    x^a = {}_1 F_0(-a; 1-x)

    \sqrt x = {}_1 F_0(-\half; 1-x)

The Series 0F1
--------------

Elementary functions:

.. math::

    \sin z = z \ {}_0F_1({\textstyle{3\over2}}; -{z^2\over 4})

    \cos z = {}_0F_1(\half; -{z^2\over 4})

    \sinh z = z \ {}_0F_1({\textstyle{3\over2}}; {z^2\over 4})

    \cosh z = {}_0F_1(\half; {z^2\over 4})

Bessel function:

.. math::

    J_\alpha(x) = \sum_{k=0}^\infty {(-1)^k \left(x\over 2\right)^{2k+\alpha}
            \over k! (k+\alpha)!}
        = {\left(x\over2\right)^\alpha \over \Gamma(\alpha+1)}
            \ {}_0F_1\left(\alpha+1; -{x^2\over 4}\right)

Modified Bessel functions:

.. math::

    I_\nu(z) = i^{-\nu} J_\nu(iz)
        = \sum_{k=0}^\infty {\left(x\over 2\right)^{2k+\nu}
            \over k! (k+\nu)!}
        = {1\over \Gamma(\nu+1)} \left(z\over 2\right)^\nu
        {}_0F_1\left(\nu+1; {z^2\over 4}\right)

    K_\nu(z) = {\Gamma(\nu)\over 2} \left(2\over z\right)^\nu
        {}_0F_1\left(1-\nu; {z^2\over 4}\right)
            + {\Gamma(-\nu)\over 2} \left(z\over 2\right)^\nu
        {}_0F_1\left(\nu+1; {z^2\over 4}\right)

The Series 1F1
--------------

Elementary functions:


.. math::

    z^a e^z = {}_1F_1(a; a-\half; -2z)

Lower incomplete gamma function:

.. math::

    \gamma(z, x)
        = x^z \Gamma(z) e^{-x} \sum_{k=0}^\infty {x^k\over \Gamma(z+k+1)}
        = x^z z^{-1} e^{-x}\ {}_1F_1(1; z+1; x)
        = x^z z^{-1}\ {}_1F_1(z; z+1; -x)

Error function:

.. math::

    \mbox{erf}(x)
        = {1\over\sqrt\pi}\gamma(\half, x^2)
        = {2x\over\sqrt\pi}\ {}_1F_1(\half; {\textstyle{3\over2}}, -x^2)

Hermite polynomials:

.. math::

    H_{2n}(x) = (-1)^n {(2n)!\over n!}\ {}_1F_1(-n;\half; x^2)

    H_{2n+1}(x) = (-1)^n {(2n+1)!\over n!}2x
        \ {}_1F_1(-n;{\textstyle{3\over2}}; x^2)

Laguerre polynomials:

.. math::
    :label: laguerre_hyper

    L_n^\alpha(x) = \binom{n+\alpha}{n}\ {}_1F_1(-n;\alpha+1;x)

Solution $P_{nl}(r)=r R_{nl}(r)$ of the radial Schrödinger equation in the
Coulomb potential $V(r) = -{Z/r}$ (we use :eq:`laguerre_hyper` in the second
equation below):

.. math::

    P_{nl}(r) = N_{nl} \left(2Zr\over n\right)^{l+1} e^{-{Zr\over n}}
        \ {}_1F_1\left(-n+l+1; 2l+2; {2Zr\over n}\right) =

    = N_{nl} \left(2Zr\over n\right)^{l+1} e^{-{Zr\over n}}
        \ L_{n-l-1}^{2l+1}\left({2Zr\over n}\right) {(2l+1)!(n-l-1)!\over
            (n+l)!} =

    = {1\over n} \sqrt{Z (n-l-1)! \over (n+l)!}
        \left(2Zr\over n\right)^{l+1} e^{-{Zr\over n}}
            \ L_{n-l-1}^{2l+1}\left({2Zr\over n}\right)

    N_{nl} = {1\over n(2l+1)!} \sqrt{Z(n+l)!\over (n-l-1)!}


The Series 2F1
--------------

Elementary functions:

.. math::

    \log(1+z) = z\ {}_2F_1(1, 1; 2; -z)

    \log(z) = (z-1)\ {}_2F_1(1, 1; 2; 1-z)

    \arcsin z = z\ {}_2F_1(\half, \half; {\textstyle{3\over2}}; z^2)

    \arccos z = {\pi\over2}-z\ {}_2F_1(\half, \half; {\textstyle{3\over2}}; z^2)

    \arctan z = z\ {}_2F_1(1, \half; {\textstyle{3\over2}}; -z^2)

Legendre polynomials:

.. math::

    P_n(z) = {}_2F_1\left(-n, n+1; 1; {1-z\over 2}\right)

Chebyshev polynomials:

.. math::

    T_n(z) = {}_2F_1\left(-n, n;\half; {1-z\over 2}\right)

    U_n(z) = (n+1)\ {}_2F_1\left(-n, n+2;{\textstyle{3\over2}};
        {1-z\over 2}\right)

Gegenbauer polynomials:

.. math::

    C_n^\alpha(z) = {(2\alpha)_n \over n!}
        \ {}_2F_1\left(-n, 2\alpha + n;\alpha+\half; {1-z\over 2}\right)

Jacobi polynomials:

.. math::

    P_n^{(\alpha, \beta)}(z) = {(\alpha+1)_n \over n!}
        \ {}_2F_1\left(-n, 1+\alpha+\beta+n;\alpha+1; {1-z\over 2}\right)

Complete elliptic integrals:

.. math::

    K(k) = {\pi\over 2}\ {}_2F_1( \half, \half; 1; k^2)

    E(k) = {\pi\over 2}\ {}_2F_1(-\half, \half; 1; k^2)


The Series 3F2
--------------

Elementary functions:

.. math::

    \tan(z) = {8z\over \pi^2-4z^2}
    \ {}_3F_2(1, \half-{z\over\pi}, \half + {z\over\pi};
        {\textstyle{3\over2}}-{z\over\pi}, {\textstyle{3\over2}} + {z\over\pi}; 1)

Dilogarithm:

.. math::

    \mbox{Li}_2(z) = z\ {}_3F_2(1, 1, 1; 2, 2; z)

Digamma:

.. math::

    \psi(z) = (z-1)\ {}_3F_2(1, 1, 2-z; 2, 2; 1) -\gamma

The Wigner 3j symbol:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix}
    = (-1)^{-j_1 + j_2 + m_3} \delta_{-m_3, m_1+m_2}
    {1\over(-j_2+j_3+m_1)! (-j_1+j_3-m_2)!}

    {\sqrt{(j_1-j_2+j_3)! (-j_1+j_2+j_3)! (j_1+m_1)! (j_2-m_2)!
        (j_3+m_3)!(j_3-m_3)!}\over
    \sqrt{(j_1+j_2-j_3)!(j_1+j_2+j_3+1)!(j_1-m_1)!(j_2+m_2)!}}

    {}_3F_2(-j_1-j_2+j_3, m_1-j_1, -j_2-m_2;
        -j_1+j_3-m_2+1, -j_2+j_3+m_1+1; 1)

The Series pFq
--------------

Polylogarithm:

.. math::

    \mbox{Li}_s(z) = z\ {}_{s+1}F_s(1, 1, \dots, 1; 2, \dots, 2; z)


Example I
=========

By writing out the series expansion for the $t_{k+1}/t_k$ ratio we can prove
that:

.. math::

    p\ {}_1F_1(a; b; x) +
    q\ {}_1F_1(a+1; b; x) =
        (p+q)\ {}_2F_2\left(a, a\left({p\over q}+1\right)+1;
            b, a\left({p\over q}+1\right); x \right)

The left hand side is equal to:

.. math::

    p\ {}_1F_1(a; b; x) +
    q\ {}_1F_1(a+1; b; x) =
        \sum_{k=0}^\infty {p (a)_k + q(a+1)_k \over (b)_k k!} x^k

We simplify the $t_k$ term:

.. math::

    t_k = {p (a)_k + q(a+1)_k \over (b)_k k!} x^k
        = {(a)_k \left(p+q+{qk\over a}\right) \over (b)_k k!} x^k

We calculate the ratio $t_{k+1}/t_k$ as well as $t_0$ to get the normalization:

.. math::

    t_0 = p + q

    {t_{k+1}\over t_k} = {(k+a)\left(p+q+{q(k+1)\over a}\right) \over
            (k+b)(k+1) \left(p+q+{qk\over a}\right)} x
        = {(k+a)\left(k + a\left({p\over q}+1\right)+1\right) \over
        (k+b)\left(k + a\left({p\over q}+1\right)\right)(k+1)} x

From which we read the arguments of the hypergeometric function ${}_2F_2$ on
the right hand side and we need to multiply it by the normalization factor $t_0
= p+q$.

Example II
==========

By writing out the series expansion for the $t_{k+1}/t_k$ ratio we can prove
that:

.. math::

    e^{-x}\ {}_1F_1(1; 2; 2x)
        = {}_0F_1\left({\textstyle{3\over 2}}; {x^2\over 4}\right)

We can also use the substitution $z={x^2\over 4}$:

.. math::

    e^{-2\sqrt z}\ {}_1F_1(1; 2; 4\sqrt z)
        = {}_0F_1\left({\textstyle{3\over 2}}; z\right)

Which is a special case of

.. math::

    {}_0F_1\left(a; z\right)
        = e^{-2\sqrt z}\ {}_1F_1(a-\half; 2a-1; 4\sqrt z)

for $a={3\over 2}$.

Example III
===========

One way to express $\sinh(z)$ is:

.. math::

    \sinh z = z e^{-z}\ {}_1F_1(1; 2; 2z)

using the previous example, this is equal to:

.. math::

    \sinh z
        = z e^{-z}\ {}_1F_1(1; 2; 2z)
        = z\ {}_0F_1\left({\textstyle{3\over 2}}; {z^2\over 4}\right)

So the lowest hypergeometric function that can express $\sinh(z)$
is ${}_0F_1$.
