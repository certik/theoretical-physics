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

    P_k(x) P_l(x)
        = \sum_{m=|k-l|}^{k+l}
        \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2
        (2m+1) P_m(x)

This was first proven by [Adams]_, where he shows:

.. math::

    P_k(x) P_l(x) = \sum_{m=|k-l|}^{k+l} {A(s-k) A(s-l) A(s-m)\over A(s)}
        {2m+1\over 2s+1} P_m(x)

where $s={k+l+m\over 2}$ and

.. math::

    A(n) = {1\cdot3\cdot5 \cdot \dots \cdot (2n-1) \over
        1\cdot 2\cdot 3\cdot \dots \cdot n} =
            {(2n)!\over 2^n (n!)^2} = {1\over 2^n}\binom{2n}{n}

The coefficient in the expansion can then be written using a $3j$ symbol as:

.. math::

    {A(s-k) A(s-l) A(s-m)\over A(s)} {1\over 2s+1} =

    = {
            {1\over2^{s-k}}\binom{2s-2k}{s-k}
            {1\over2^{s-l}}\binom{2s-2l}{s-l}
            {1\over2^{s-m}}\binom{2s-2m}{s-m}
            \over
            {1\over2^{s}}\binom{2s}{s}
        } {1\over 2s+1} =

    = {2^s\over2^{s-k+s-l+s-m}} {
            \binom{2s-2k}{s-k}
            \binom{2s-2l}{s-l}
            \binom{2s-2m}{s-m}
            \over
            \binom{2s}{s}
        } {1\over 2s+1} =

    = {
            \binom{2s-2k}{s-k}
            \binom{2s-2l}{s-l}
            \binom{2s-2m}{s-m}
            \over
            \binom{2s}{s}
        } {1\over 2s+1} =

    = {
            {(2s-2k)! \over ((s-k)!)^2}
            {(2s-2l)! \over ((s-l)!)^2}
            {(2s-2m)! \over ((s-m)!)^2}
            {(s!)^2 \over (2s)!}
        } {1\over 2s+1} =

    = {(2s-2k)! (2s-2l)! (2s-2m)! \over (2s+1)!}
        \left[{s! \over (s-k)! (s-l)! (s-m)!}\right]^2
       =

    = \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2

So we will be just using the $3j$ symbol form from now on.
We can now calculate the integral of three Legendre polynomials:

.. math::
    :label: int_three_legendre_polys

    \int_{-1}^1 P_k(x) P_l(x) P_m(x) \d x =

    = \int_{-1}^1
        \sum_{n=|k-l|}^{k+l}
        \begin{pmatrix} k & l & n \\ 0 & 0 & 0 \end{pmatrix}^2
        (2n+1) P_n(x)
    P_m(x) \d x =

    =
        \sum_{n=|k-l|}^{k+l}
        \begin{pmatrix} k & l & n \\ 0 & 0 & 0 \end{pmatrix}^2
        (2n+1) {2\delta_{nm}\over 2n+1}
    =

    = 2 \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2

This is consistent with the series expansion:

.. math::

    P_k(x) P_l(x) = \sum_{m=|k-l|}^{k+l}
        {2m+1\over 2}\int_{-1}^1 P_k(x) P_l(x) P_m(x) \d x\,\,
        P_m(x) =

    = \sum_{m=|k-l|}^{k+l}
        \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2
        (2m+1) P_m(x)

Any function $f(x)$ (where $-1\le x \le 1$) can be expanded as:

.. math::

    f(x) = \sum_{l=0}^\infty f_l P_l(x)

    f_l = {(2l+1)\over 2} \int_{-1}^1 f(x) P_l(x) \d x

For the following choice of $f(x)$ we get (for $|t| \le 1$):

.. math::

    f(x) = {1\over\sqrt{1-2xt+t^2}}

    f_l = {(2l+1)\over 2} \int_{-1}^1 {P_l(x)\over\sqrt{1-2xt+t^2}} \d x
        = {(2l+1)\over 2} \int_{|1+t|}^{|1-t|}
                 {P_l\left(1-R^2-t^2\over 2 t\right)\over R}
                 \left(-{R\over t}\right) \d R
        =

        = {(2l+1)\over 2 t} \int_{|1-t|}^{|1+t|}
                 P_l\left(1-R^2-t^2\over 2 t\right) \d R
        = {(2l+1)\over 2 t} \int_{1-t}^{1+t}
                 P_l\left(1-R^2-t^2\over 2 t\right) \d R
        =

        = t^l

Code::

    >>> from sympy import var, legendre, integrate
    >>> var("l R t")
    (l, R, t)
    >>> f = (2*l+1) / (2*t) * integrate(legendre(l, (1-R**2+t**2) / (2*t)),
    ...         (R, 1-t, 1+t))
    >>> for _l in range(20): print _l, f.subs(l, _l).doit().simplify()
    ...
    0 1
    1 t
    2 t**2
    3 t**3
    4 t**4
    5 t**5
    6 t**6
    7 t**7
    8 t**8
    9 t**9
    10 t**10
    11 t**11
    12 t**12
    13 t**13
    14 t**14
    15 t**15
    16 t**16
    17 t**17
    18 t**18
    19 t**19


So the Legendre polynomials are the coefficients of the following expansion
for $|t| \le 1$:

.. math::

    {1\over\sqrt{1-2xt+t^2}} = \sum_{l=0}^\infty P_l(x) t^l

Note that for $|t| > 1$ we get:

.. math::

    {1\over\sqrt{1-2xt+t^2}}
    = {1\over |t|}{1\over\sqrt{1-2x{1\over t}+\left({1\over t}\right)^2}}
    = {1\over |t|}\sum_{l=0}^\infty P_l(x) \left({1\over t}\right)^l
    = \sign t \sum_{l=0}^\infty P_l(x) t^{-l-1}


.. [Adams] Adams, J. C. (1878). On the Expression of the Product of Any Two Legendre’s Coefficients by Means of a Series of Legendre's Coefficients.  Proceedings of the Royal Society of London, 27, 63-71.

Example I
~~~~~~~~~

Very important is the following multipole expansion:

.. math::
    :label: legendre_expansion

    {1\over |{\bf r}-{\bf r'}|}
        ={1\over \sqrt{({\bf r}-{\bf r'})^2}}
        ={1\over \sqrt{r^2-2{\bf r}\cdot {\bf r'} + r'^2}}
        ={1\over r_>\sqrt{1-2\left(r_<\over r_>\right){\bf\hat r}\cdot {\bf\hat
            r'} + \left(r<\over r_>\right)^2}} =

    ={1\over r_>}\sum_{l=0}^\infty\left(r_<\over r_>\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'})
    =\sum_{l=0}^\infty {r_<^l\over r_>^{l+1}} P_l({\bf\hat r}\cdot {\bf\hat r'})

Where $r_{>} = \max(r, r')$ and
$r_{<} = \min(r, r')$.
Assuming $r > r'$, we get for the first few terms:

.. math::

    {1\over |{\bf r}-{\bf r'}|}
    ={1\over r}\left( P_0({\bf\hat r}\cdot {\bf\hat r'}) + P_1({\bf\hat r}\cdot {\bf\hat r'}){r'\over r} + P_2({\bf\hat r}\cdot {\bf\hat r'})\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =

    ={1\over r}\left( 1 + {\bf\hat r}\cdot {\bf\hat r'} {r'\over r} + \half\left(3({\bf\hat r}\cdot {\bf\hat r'})^2-1\right)\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =

    ={1\over r} +{{\bf r}\cdot {\bf r'}\over r^3} +{3({\bf r}\cdot {\bf r'})^2-r^2r'^2\over 2r^5} + O\left(r'^3\over r^4\right)

Example II
~~~~~~~~~~

Let's find the expansion of

.. math::

    f(x) = {e^{-\alpha \sqrt{1-2xt+t^2}}\over\sqrt{1-2xt+t^2}}

for $|t| \le 1$. We get:

.. math::

    f_l = {(2l+1)\over 2} \int_{-1}^1
        {P_l(x)e^{-\alpha \sqrt{1-2xt+t^2}}\over\sqrt{1-2xt+t^2}} \d x
        = {(2l+1)\over 2} \int_{|1+t|}^{|1-t|}
                 {P_l\left(1-R^2-t^2\over 2 t\right)e^{-\alpha R}\over R}
                 \left(-{R\over t}\right) \d R
        =

        = {(2l+1)\over 2 t} \int_{|1-t|}^{|1+t|}
                 P_l\left(1-R^2-t^2\over 2 t\right) e^{-\alpha R} \d R
        = {(2l+1)\over 2 t} \int_{1-t}^{1+t}
                 P_l\left(1-R^2-t^2\over 2 t\right) e^{-\alpha R} \d R

Here is the result for the first few $l$:

.. math::

    f_0 & = \frac{\left(e^{2 \alpha t} -1\right) e^{- \alpha t - \alpha}}{2 \alpha t} \\
    f_1 & = \frac{3}{2} \frac{\left(\alpha^{2} t e^{2 \alpha t} + \alpha^{2} t + \alpha t e^{2 \alpha t} + \alpha t - \alpha e^{2 \alpha t} + \alpha - e^{2 \alpha t} + 1\right) e^{- \alpha t - \alpha}}{\alpha^{3} t^{2}} \\
    f_2 & = \frac{5}{2} \frac{\left(\alpha^{4} t^{2} e^{2 \alpha t} - \alpha^{4} t^{2} + 3 \alpha^{3} t^{2} e^{2 \alpha t} - 3 \alpha^{3} t^{2} - 3 \alpha^{3} t e^{2 \alpha t} - 3 \alpha^{3} t + 3 \alpha^{2} t^{2} e^{2 \alpha t} - 3 \alpha^{2} t^{2} - 9 \alpha^{2} t e^{2 \alpha t} - 9 \alpha^{2} t + X\right) e^{- \alpha t - \alpha}}{\alpha^{5} t^{3}}

    X = 3 \alpha^{2} e^{2 \alpha t} - 3 \alpha^{2} - 9 \alpha t e^{2 \alpha t} - 9 \alpha t + 9 \alpha e^{2 \alpha t} - 9 \alpha + 9 e^{2 \alpha t} -9


Expanding in $t$ up to
$\operatorname{\mathcal{O}}\left(t^{7}\right)$ we get:

.. math::

    f_l & = e^\alpha g_l \\
    g_0 & = 1 + \frac{1}{6} \alpha^{2} t^{2} + \frac{1}{120} \alpha^{4} t^{4} + \frac{1}{5040} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_1 & = t + \alpha t + \frac{1}{10} \alpha^{2} t^{3} + \frac{1}{10} \alpha^{3} t^{3} + \frac{1}{280} \alpha^{4} t^{5} + \frac{1}{280} \alpha^{5} t^{5} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_2 & = t^{2} + \alpha t^{2} + \frac{1}{3} \alpha^{2} t^{2} + \frac{1}{14} \alpha^{2} t^{4} + \frac{1}{14} \alpha^{3} t^{4} + \frac{1}{42} \alpha^{4} t^{4} + \frac{1}{504} \alpha^{4} t^{6} + \frac{1}{504} \alpha^{5} t^{6} + \frac{1}{1512} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_3 & = t^{3} + \alpha t^{3} + \frac{2}{5} \alpha^{2} t^{3} + \frac{1}{18} \alpha^{2} t^{5} + \frac{1}{15} \alpha^{3} t^{3} + \frac{1}{18} \alpha^{3} t^{5} + \frac{1}{45} \alpha^{4} t^{5} + \frac{1}{270} \alpha^{5} t^{5} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_4 & = t^{4} + \alpha t^{4} + \frac{3}{7} \alpha^{2} t^{4} + \frac{1}{22} \alpha^{2} t^{6} + \frac{2}{21} \alpha^{3} t^{4} + \frac{1}{22} \alpha^{3} t^{6} + \frac{1}{105} \alpha^{4} t^{4} + \frac{3}{154} \alpha^{4} t^{6} + \frac{1}{231} \alpha^{5} t^{6} + \frac{1}{2310} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\



Code::

    >>> from sympy import var, legendre, integrate, exp, latex, cse
    >>> var("l R t alpha")
    (l, R, t, alpha)
    >>> 
    >>> f = (2*l+1) / (2*t) * integrate(legendre(l, (1-R**2+t**2) / (2*t)) \
    ...         * exp(-alpha*R),
    ...         (R, 1-t, 1+t))
    >>> 
    >>> for _l in range(3):
    ...     print "f_%d & =" %_l, latex(f.subs(l, _l).doit().simplify()), "\\\\"
    ... 
    f_0 & = \frac{\left(e^{2 \alpha t} -1\right) e^{- \alpha t - \alpha}}{2 \alpha t} \\
    f_1 & = \frac{3}{2} \frac{\left(\alpha^{2} t e^{2 \alpha t} + \alpha^{2} t + \alpha t e^{2 \alpha t} + \alpha t - \alpha e^{2 \alpha t} + \alpha - e^{2 \alpha t} + 1\right) e^{- \alpha t - \alpha}}{\alpha^{3} t^{2}} \\
    f_2 & = \frac{5}{2} \frac{\left(\alpha^{4} t^{2} e^{2 \alpha t} - \alpha^{4} t^{2} + 3 \alpha^{3} t^{2} e^{2 \alpha t} - 3 \alpha^{3} t^{2} - 3 \alpha^{3} t e^{2 \alpha t} - 3 \alpha^{3} t + 3 \alpha^{2} t^{2} e^{2 \alpha t} - 3 \alpha^{2} t^{2} - 9 \alpha^{2} t e^{2 \alpha t} - 9 \alpha^{2} t + 3 \alpha^{2} e^{2 \alpha t} - 3 \alpha^{2} - 9 \alpha t e^{2 \alpha t} - 9 \alpha t + 9 \alpha e^{2 \alpha t} - 9 \alpha + 9 e^{2 \alpha t} -9\right) e^{- \alpha t - \alpha}}{\alpha^{5} t^{3}} \\
    >>> for _l in range(5):
    ...     result = f.subs(l, _l).doit().simplify() / exp(-alpha)
    ...     print "g_%d & =" %_l, latex(result.series(t, 0, 7)), "\\\\"
    ... 
    g_0 & = 1 + \frac{1}{6} \alpha^{2} t^{2} + \frac{1}{120} \alpha^{4} t^{4} + \frac{1}{5040} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_1 & = t + \alpha t + \frac{1}{10} \alpha^{2} t^{3} + \frac{1}{10} \alpha^{3} t^{3} + \frac{1}{280} \alpha^{4} t^{5} + \frac{1}{280} \alpha^{5} t^{5} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_2 & = t^{2} + \alpha t^{2} + \frac{1}{3} \alpha^{2} t^{2} + \frac{1}{14} \alpha^{2} t^{4} + \frac{1}{14} \alpha^{3} t^{4} + \frac{1}{42} \alpha^{4} t^{4} + \frac{1}{504} \alpha^{4} t^{6} + \frac{1}{504} \alpha^{5} t^{6} + \frac{1}{1512} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_3 & = t^{3} + \alpha t^{3} + \frac{2}{5} \alpha^{2} t^{3} + \frac{1}{18} \alpha^{2} t^{5} + \frac{1}{15} \alpha^{3} t^{3} + \frac{1}{18} \alpha^{3} t^{5} + \frac{1}{45} \alpha^{4} t^{5} + \frac{1}{270} \alpha^{5} t^{5} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_4 & = t^{4} + \alpha t^{4} + \frac{3}{7} \alpha^{2} t^{4} + \frac{1}{22} \alpha^{2} t^{6} + \frac{2}{21} \alpha^{3} t^{4} + \frac{1}{22} \alpha^{3} t^{6} + \frac{1}{105} \alpha^{4} t^{4} + \frac{3}{154} \alpha^{4} t^{6} + \frac{1}{231} \alpha^{5} t^{6} + \frac{1}{2310} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\


Example III
~~~~~~~~~~~

.. math::

    {e^{-{|{\bf r}-{\bf r'}|\over D}}\over |{\bf r}-{\bf r'}|}
        = {e^{-r_>\sqrt{1-2\left(r_<\over r_>\right)
                {\bf\hat r}\cdot {\bf\hat r'}
            +\left(r_<\over r_>\right)^2}\over D}\over
                r_>\sqrt{1-2\left(r_<\over r_>\right)
                        {\bf\hat r}\cdot {\bf\hat r'}
                +\left(r_<\over r_>\right)^2}}
        = {1\over r_>}
            {e^{-\alpha \sqrt{1-2xt+t^2}}\over\sqrt{1-2xt+t^2}}

where:

.. math::

    \alpha & = {r_>\over D} \\
    x & = {\bf\hat r}\cdot {\bf\hat r'} \\
    t & = {r_<\over r_>}


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

Example V
~~~~~~~~~

.. math::

    \sum_{m'} \left(c^k(l, m, l', m')\right)^2 =

        = \sum_{m'}
        (2l+1)(2l'+1)
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix}^2 =

        =
        (2l+1)(2l'+1)
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        \sum_{m'}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix}^2 =

        =
        (2l+1)(2l'+1)
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        {1\over 2l+1} =

        =
        (2l'+1)
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        =

        =\sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)


.. _five_spherical_harmonics:

Example VI
~~~~~~~~~~

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
            {2l'+1\over 4\pi} P_{l'}({\bf \hat x}\cdot{\bf \hat x}')
            {2k+1\over 4\pi} P_k({\bf \hat x}\cdot{\bf \hat x}')
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
    = {2l'+1\over 4\pi} P_{l'}({\bf \hat x}\cdot{\bf \hat x}')

    \sum_{q}
        Y_{kq}(\Omega)
        Y_{kq}^*(\Omega')
    = {2k+1\over 4\pi} P_k({\bf \hat x}\cdot{\bf \hat x}')

    P_k({\bf \hat x}\cdot{\bf \hat x}')P_{l'}({\bf \hat x}\cdot{\bf \hat x}')
    = \sum_{\lambda=|l'-k|}^{l'+k}
        \begin{pmatrix} k & l' & \lambda \\ 0 & 0 & 0 \end{pmatrix}^2
        (2\lambda+1) P_\lambda({\bf \hat x}\cdot{\bf \hat x}') =

        = \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
            \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
            P_\lambda({\bf \hat x}\cdot{\bf \hat x}') =

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

Orthogonality relations:

.. math::

    \sum_{m_1 m_2}
    \begin{pmatrix} j_1 & j_2 & j \\ m_1 & m_2 & m \end{pmatrix}
    \begin{pmatrix} j_1 & j_2 & j' \\ m_1 & m_2 & m' \end{pmatrix} =
        {\delta_{jj'}\delta_{mm'}
            \over
        2j+1}

As a special case, we get:

.. math::
    :label: 3j-square-sum

    \sum_{m'}
    \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix}^2
    =
        {1 \over 2l+1}

Here is a script to check that the equation :eq:`3j-square-sum` works::

    from sympy import S
    from sympy.physics.wigner import wigner_3j

    def doit(l, k, lp, m):
        s = 0
        for mp in range(-lp, lp+1):
            s += wigner_3j(l, k, lp, -m, m-mp, mp)**2
        print "%2d %2d %2d %2d  " % (l, k, lp, m), s, " ", S(1)/(2*l+1)

    k = 4
    lp = 3
    print " l  k  lp m:  lhs   rhs"
    for l in range(1, 6):
        for m in range(-l, l+1):
            doit(l, k, lp, m)

it prints::

     l  k  lp m:  lhs   rhs
     1  4  3 -1   1/3   1/3
     1  4  3  0   1/3   1/3
     1  4  3  1   1/3   1/3
     2  4  3 -2   1/5   1/5
     2  4  3 -1   1/5   1/5
     2  4  3  0   1/5   1/5
     2  4  3  1   1/5   1/5
     2  4  3  2   1/5   1/5
     3  4  3 -3   1/7   1/7
     3  4  3 -2   1/7   1/7
     3  4  3 -1   1/7   1/7
     3  4  3  0   1/7   1/7
     3  4  3  1   1/7   1/7
     3  4  3  2   1/7   1/7
     3  4  3  3   1/7   1/7
     4  4  3 -4   1/9   1/9
     4  4  3 -3   1/9   1/9
     4  4  3 -2   1/9   1/9
     4  4  3 -1   1/9   1/9
     4  4  3  0   1/9   1/9
     4  4  3  1   1/9   1/9
     4  4  3  2   1/9   1/9
     4  4  3  3   1/9   1/9
     4  4  3  4   1/9   1/9
     5  4  3 -5   1/11   1/11
     5  4  3 -4   1/11   1/11
     5  4  3 -3   1/11   1/11
     5  4  3 -2   1/11   1/11
     5  4  3 -1   1/11   1/11
     5  4  3  0   1/11   1/11
     5  4  3  1   1/11   1/11
     5  4  3  2   1/11   1/11
     5  4  3  3   1/11   1/11
     5  4  3  4   1/11   1/11
     5  4  3  5   1/11   1/11


Values of the $3j$ coefficients for a few special cases (use the symmetries
above to obtain values for permuted symbols):

.. math::

    \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}
        &= (-1)^s \sqrt{(2s-2k)! (2s-2l)! (2s-2m)! \over (2s+1)!}
            {s! \over (s-k)! (s-l)! (s-m)!}
            \quad\quad\mbox{for $2s=k+l+m$ even} \\
    \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}
        &= 0
            \quad\quad\mbox{for $2s=k+l+m$ odd} \\
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
        &= (-1)^{j-m-\half} \sqrt{j-m+\half
            \over (2j+1)(2j+2)} \\
    \begin{pmatrix} j+1 & j & 1 \\ m & -m-1 & 1 \end{pmatrix}
        &= (-1)^{j-m-1} \sqrt{(j-m)(j-m+1)
            \over (2j+1)(2j+2)(2j+3)} \\
    \begin{pmatrix} j+1 & j & 1 \\ m & -m & 0 \end{pmatrix}
        &= (-1)^{j-m-1} \sqrt{2(j+m+1)(j-m+1)
            \over (2j+1)(2j+2)(2j+3)}

Examples
~~~~~~~~

.. math::

    \begin{pmatrix} j_3-\half & \half & j_3 \\
        m_3-\half & \half & -m_3 \end{pmatrix} =
    \begin{pmatrix} j_3 & j_3-\half & \half \\
        -m_3 & m_3-\half & \half \end{pmatrix} =
        \left.
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
    \right|_{j=j_3-\half;m=-m_3}
    =

    = (-1)^{j_3-\half+m_3-\half}\sqrt{j_3-\half+m_3+\half\over
        (2 j_3-1+1) (2j_3-1+2)}
    = (-1)^{j_3+m_3-1}\sqrt{j_3+m_3\over 2 j_3 (2j_3+1)}



    \begin{pmatrix} j_3-\half & \half & j_3 \\
        m_3+\half & -\half & -m_3 \end{pmatrix} =
        (-1)^{j_3-\half + \half + j_3}
    \begin{pmatrix} j_3 & j_3-\half & \half \\
        m_3 & -m_3-\half & \half \end{pmatrix} =
        (-1)^{2j_3}
        \left.
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
    \right|_{j=j_3-\half;m=m_3}
    =

    = (-1)^{2j_3}
    (-1)^{j_3-\half-m_3-\half}\sqrt{j_3-\half-m_3+\half\over
        (2 j_3-1+1) (2j_3-1+2)}
    = (-1)^{2j_3} (-1)^{j_3-m_3-1}\sqrt{j_3-m_3\over 2 j_3 (2j_3+1)}



    \begin{pmatrix} j_3+\half & \half & j_3 \\
        m_3-\half & \half & -m_3 \end{pmatrix} =
        (-1)^{j_3+\half+\half+j_3}
    \begin{pmatrix} j_3+\half & j_3 & \half \\
        m_3-\half & -m_3 & \half \end{pmatrix} =
        (-1)^{2j_3+1}
        \left.
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
    \right|_{j=j_3;m=m_3-\half}
    =

    =(-1)^{2j_3+1}(-1)^{j_3-m_3+\half-\half}\sqrt{j_3-m_3+\half+\half \over
        (2j_3+1)(2j_3+2)}
    =(-1)^{2j_3+1}(-1)^{j_3-m_3}\sqrt{j_3-m_3+1 \over (2j_3+1)(2j_3+2)}




    \begin{pmatrix} j_3+\half & \half & j_3 \\
        m_3+\half & -\half & -m_3 \end{pmatrix} =
    \begin{pmatrix} j_3+\half & j_3 & \half \\
        -m_3-\half & m_3 & \half \end{pmatrix} =
        \left.
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
    \right|_{j=j_3;m=-m_3-\half}
    =

    =(-1)^{j_3+m_3+\half-\half}\sqrt{j_3+m_3+\half+\half \over
        (2j_3+1)(2j_3+2)}
    =(-1)^{j_3+m_3}\sqrt{j_3+m_3+1 \over (2j_3+1)(2j_3+2)}


.. index:: multipole expansion

Multipole Expansion
===================

Using :eq:`legendre_expansion` we get:

.. math::

    {1\over |{\bf r}-{\bf r'}|}
        =\sum_{l=0}^\infty{r_{<}^l\over r_{>}^{l+1}} P_l({\bf\hat r}\cdot {\bf\hat r'})
        = \sum_{l,m}{r_{<}^l\over r_{>}^{l+1}}
            {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')

where we used the formula:

.. math::

    \sum_m \braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r}'}
        ={2l+1 \over 4\pi} \braket{{\bf\hat r}\cdot{\bf\hat r'}|P_l}
