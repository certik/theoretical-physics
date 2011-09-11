.. index:: spherical harmonics

Spherical Harmonics
===================


Are defined by

.. math::

       Y_{lm}(\theta,\phi)=\sqrt{{2l+1\over4\pi}{(l-m)!\over(l+m)!}}\,P_l^m(\cos\theta)\,e^{im\phi}

where $P_l^m$ are associated Legendre polynomials defined by

.. math::

       P_l^m(x)=(-1)^m (1-x^2)^{m/2}{\d^m\over\d x^m} P_l(x)

and $P_l$ are Legendre polynomials defined by the formula

.. math::

       P_l(x)={1\over2^l l!}{\d^l\over\d x^l}[(x^2-1)^l]

they also obey the completeness relation

.. math::
    :label: Lorto

       \sum_{l=0}^\infty {2l+1\over2}P_l(x')P_l(x)=\delta(x-x')

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

    Y_{l m}^*(\Omega) = (-1)^m Y_{l; -m}(\Omega)

    (-1)^m Y_{l; -m}^*(\Omega) = Y_{lm}(\Omega)


Gaunt Coefficients
------------------

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

where we used:

.. math::

        \int_{-1}^1 P_k(x) P_l(x) P_m(x) \d x =
        2\begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2

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

This is the most symmetric relation.
