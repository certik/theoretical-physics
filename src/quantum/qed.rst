.. index:: QED, quantum electrodynamics

Quantum Electrodynamics (QED)
=============================

QED Lagrangian
--------------

The QED Lagrangian density is

.. math::

    \L=\bar\psi(i\hbar c\gamma^\mu D_\mu-mc^2)\psi-{1\over4}F_{\mu\nu}F^{\mu\nu}


where

.. math::

    \psi=\left( \begin{array}{c} \psi_1 \\ \psi_2 \\ \psi_3 \\ \psi_4 \\ \end{array}\right)


and

.. math::

    D_\mu=\partial_\mu+{i\over \hbar}eA_\mu


is the gauge covariant derivative and ($e$ is the elementary charge, which is $1$ in atomic units, i.e. the electron has a charge $-e$)

.. math::

    F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu


is the electromagnetic field tensor. It's astonishing, that this simple Lagrangian can account for all phenomena from macroscopic scales down to something like $10^{-13}\rm\,cm$. So it's not a surprise that Feynman, Schwinger and Tomonaga received the 1965 Nobel Prize in Physics for such a fantastic achievement.

Plugging this Lagrangian into the Euler-Lagrange equation of motion for a field, we get:

.. math::

    (i\hbar c\gamma^\mu D_\mu-mc^2)\psi=0



.. math::

    \partial_\nu F^{\nu\mu}=-ec\bar\psi\gamma^\mu\psi


The first equation is the Dirac equation in the electromagnetic field and the
second equation is a set of Maxwell equations ($\partial_\nu
F^{\nu\mu}=-ej^\mu$) with a source $j^\mu=c\bar\psi\gamma^\mu\psi$, which is a
4-current comming from the Dirac equation.

Magnetic moment of an electron
------------------------------

In this section we derive the order-$\alpha$ correction to the magnetic moment
of an electron.

We start by computing the electron vertex function for the process
$\gamma(q)\to e^+(p) + e^-(p')$:

.. math::

    i M = i e^2 \left(\bar u(p')\Gamma^\mu(p', p)u(p)\right) {1\over q^2}
        \left(\bar u(k') \gamma_\mu u(k)\right)

where $k$ corresponds to some heavy target. If $A_\mu^{\rm cl}$ is a fixed
classical potential, we get:

.. math::

    i M 2\pi \delta(p^{0'} - p^0) =
        -i e \bar u(p')\Gamma^\mu(p', p)u(p) A_\mu^{\rm cl}

Using general arguments (Lorentz invariance, parity-conservation, Ward
identity) we can always write $\Gamma^\mu$ as:

.. math::

    \Gamma^\mu(p', p) = \gamma^\mu F_1(q^2) + {i\sigma^{\mu\nu} q_\nu \over
        2m} F_2(q^2)

where $F_1$ and $F_2$ ar unknown functions of $q^2 = (p'-p)^2 = -2p'\cdot p +
2m^2$ called form factors. As we will see below, in the lowest order we get
$F_1 = 1$ and $F_2 = 0$.

We can calculate the amplitude for elastic Coulomb scattering of a
nonrelativistic electron from a region of nonzero electrostatic potential by
setting $A_\mu^{\rm cl}(x)=(\phi({\bf x}), 0)$, then:

.. math::

    A_\mu^{\rm cl}(q)=(2\pi\delta(q^0)\tilde\phi({\bf q}), 0)

    i M 2\pi \delta(p^{0'} - p^0) =
        -i e \bar u(p')\Gamma^0(p', p)u(p) 2\pi\delta(q^0)\tilde\phi({\bf q})

    i M = -i e \bar u(p')\Gamma^0(p', p)u(p) \tilde\phi({\bf q})

If the electrostatic field is very slowly varying over a large (even
macroscopic) region, $\tilde\phi({\bf q})$ will be concentrated about ${\bf q}
= 0$, then we can take the limit ${\bf q}\to 0$:

.. math::

    i M = -i e \bar u(p')\Gamma^0(p', p)u(p) \tilde\phi({\bf q})

    i M = -i e \bar u(p')
        \left(\gamma^0 F_1(q^2) + {i\sigma^{0\nu} q_\nu \over 2m} F_2(q^2)
            \right)u(p) \tilde\phi({\bf q})

    i M = -i e \bar u(p') \gamma^0 u(p) F_1(0) \tilde\phi({\bf q})

    i M = -i e 2m\xi^{'\dag}\xi F_1(0) \tilde\phi({\bf q})

    i M = -i \left( e F_1(0) \tilde\phi({\bf q})\right) 2m\xi^{'\dag}\xi

This corresponds to the Born approximation for scattering from a potential

.. math::

    V({\bf x}) = e F_1(0) \phi({\bf x})

Thus $F_1(0)$ is the electric charge of the electron, in units of $e$. Since
$F_1(0) = 1$ already in the first order of perturbation theory, radiative
corrections to $F_1(q^2)$ must vanish at $q^2=0$.

Now we calculate the scattering from a static vector potential by setting
$A_\mu^{\rm cl}(x)=(0, {\bf A}_\mu^{\rm cl}({\bf x}))$, then:

.. math::

    A^\mu_{\rm cl}(q)=(0, 2\pi\delta(q^i)\tilde A^i_{\rm cl}({\bf q}))

    i M 2\pi \delta(p^{'i} - p^i) =
        i e \bar u(p')\Gamma^i(p', p)u(p) 2\pi\delta(q^i)\tilde A^i_{\rm cl}({\bf q})

    i M = i e \bar u(p')\Gamma^i(p', p)u(p) \tilde A^i_{\rm cl}({\bf q})

    i M = i e \bar u(p')\left(\gamma^i F_1(q^2) + {i\sigma^{i\nu} q_\nu \over 2m} F_2(q^2) \right)
    u(p) \tilde A^i_{\rm cl}({\bf q})

In the limit $q\to0$ this becomes:

.. math::

    i M = i e
        2m\xi^{'\dag}\left(-i\epsilon^{ijk}{q^j\sigma^k\over 2m}(F_1(0) + F_2(0)) \right)\xi
    \tilde A^i_{\rm cl}({\bf q})

    i M = -i e
        2m\xi^{'\dag}\left(-{\sigma^k\over 2m}(F_1(0) + F_2(0)) \right)\xi
    \left(-i\epsilon^{ijk}q^j\tilde A^i_{\rm cl}({\bf q})\right)

    i M = -i e
        2m\xi^{'\dag}\left(-{\sigma^k\over 2m}(F_1(0) + F_2(0)) \right)\xi
        \tilde B^k({\bf q})

    i M = -i \left(-{e\over m} (F_1(0) + F_2(0))
        2m\xi^{'\dag}{\sigma^k\over 2}\xi
        \tilde B^k({\bf q})\right)


where

.. math::

    \tilde B^k({\bf q}) =
    \left(-i\epsilon^{ijk}q^j\tilde A^i_{\rm cl}({\bf q})\right)

is the Fourier transform of the magnetic field produced by ${\bf A}^{\rm
cl}({\bf x})$.

This corresponds to the Born approximation for scattering from a potential

.. math::

    V({\bf x}) = -{e\over m} (F_1(0) + F_2(0))
        \xi^{'\dag}{\sigma^k\over 2}\xi
        B^k({\bf x})

    V({\bf x}) = -{e\over m} (F_1(0) + F_2(0))
        \xi^{'\dag}{\bsigma\over 2}\xi\cdot {\bf B}({\bf x})

    V({\bf x}) = -<{\bmu}>\cdot {\bf B}({\bf x})

where

.. math::

    <{\bmu}> = {e\over m} (F_1(0) + F_2(0)) \xi^{'\dag}{\bsigma\over 2}\xi

    <{\bmu}> = g {e\over 2m} {\bf S}

where

.. math::

    g = 2(F_1(0) + F_2(0))

    {\bf S} = \xi^{'\dag}{\bsigma\over 2}\xi

The coefficient $g$ is called the Landé g-factor, and since the leading order
of perturbation theory gives $F_2(0)=0$ (and we know that $F_1(0)=1$ to all
orders), we get:

.. math::

    g = 2(F_1(0) + F_2(0)) = 2 + 2F_2(0) = 2 + O(\alpha)

This is the standard prediction of the Dirac equation. The anomalous magnetic
moment is then:

.. math::

    a_e = {g - 2\over 2} = F_2(0)

To calculate that, we need to evaluate the one-loop correction to the vertex
function, so we start by deriving the appropriate Green function for the
process $\gamma(q) + e^+(p) \to e^+(p')$:

.. math::

    \ket{i} = a^{r\dag}_{\bf q} b^{t\dag}_{\bf p} \ket{\Omega}

    \ket{f} = b^{s\dag}_{\bf p'} \ket{\Omega}

    \braket{f|i} =\bra{\Omega} b^s_{\bf p'} a^{r\dag}_{\bf q}
         b^{t\dag}_{\bf p} \ket{\Omega} =

        =\bra{\Omega}T b^s_{\bf p'} a^{r\dag}_{\bf q}
             b^{t\dag}_{\bf p} \ket{\Omega} =

        =\bra{\Omega}T
             \bar u^s({\bf p'}){1\over\tilde S(p')}\tilde \psi(p')
             \epsilon_\mu^{r*}({\bf q}){q^2\over i} \tilde A^\mu(-q)
             \tilde{\bar\psi}(-p){1\over\tilde S(-p)}u^t({\bf p})
             \ket{\Omega} =

        =\bar u^s({\bf p'}){1\over\tilde S(p')}
            \epsilon_\mu^{r*}({\bf q}){q^2\over i}
             \bra{\Omega}T
             \tilde \psi(p')
             \tilde A^\mu(-q)
             \tilde{\bar\psi}(-p)
             \ket{\Omega}{1\over\tilde S(-p)}u^t({\bf p}) =

        =\bar u^s({\bf p'}){1\over\tilde S(p')}
            \epsilon_\mu^{r*}({\bf q}){q^2\over i}
             \tilde G(p, p', q)
             {1\over\tilde S(-p)}u^t({\bf p}) =

where:

.. math::

    \tilde G(p, p', q) = \bra{\Omega}T \tilde \psi(p') \tilde A^\mu(-q)
             \tilde{\bar\psi}(-p)
             \ket{\Omega}

is the interacting Green function for the Lagrangian
$-\lambda \bar e \gamma^\mu e A_\mu$. In the first order:

.. math::

    \tilde G(p, p', q) = \bra{\Omega}T \tilde\psi(p') \tilde A^\mu(-q)
             \tilde{\bar\psi}(-p)
             \ket{\Omega} =

        = \int \d^4 x \bra{0}T \tilde\psi(p') \tilde A^\mu(-q)
             \tilde{\bar\psi}(-p)
             (-\lambda)\bar e(x) \gamma^\rho e(x) A_\rho(x)
             \ket{0} =

        = (-\lambda)\int \d^4 x \d\hat p'\d\hat q\d\hat p
            e^{i\hat p'p' - \hat q q
            -\hat pp}
            \bra{0}T \psi(\hat p') A^\mu(\hat q)
             {\bar\psi}(\hat p)
             \bar e(x) \gamma^\rho e(x) A_\rho(x)
             \ket{0} =

        = (-\lambda)\int \d^4 x \d\hat p'\d\hat q\d\hat p
            e^{i\hat p'p' - \hat q q
            -\hat pp}
            D^\mu_\rho(\hat q-x) S(\hat p' - x)\gamma^\rho S(\hat p-x)
            =

        = (-\lambda)(2\pi)^4\delta(p'-q-p)
            \tilde D^\mu_\rho(q) \tilde S(p')\gamma^\rho \tilde S(p)

so the amplitude is:

.. math::

        \braket{f|i}=\bar u^s({\bf p'}){1\over\tilde S(p')}
            \epsilon_\mu^{r*}({\bf q}){q^2\over i}
         (-\lambda)(2\pi)^4\delta(p'-q-p)
            \tilde D^\mu_\rho(q) \tilde S(p')\gamma^\rho \tilde S(p)
             {1\over\tilde S(-p)}u^t({\bf p}) =

        =(-\lambda)(2\pi)^4\delta(p'-q-p)\epsilon_\mu^{r*}({\bf q})
                u^s({\bf p'})\gamma^\mu u^t({\bf p})

and we got $\Gamma^\mu = \gamma^\mu$, so $F_1=1$ and $F_2=0$ in the lowest
order. In the next order we get:

.. math::

    \tilde G(p, p', q)
        = (-\lambda)(2\pi)^4\delta(p'-q-p)
            \tilde D^\mu_\rho(q) \tilde S(p')\delta\Gamma^\rho \tilde S(p)

    \delta\Gamma^\mu =
        \int {\d^4 k\over (2\pi)^4} \tilde D_{\nu\rho}(k-p)
            (-ie\gamma^\nu)
            \tilde S(k')
            \gamma^\mu
            \tilde S(k)
            (-ie\gamma^\rho)

Now we can write:

.. math::

    \bar u(p')\Gamma^\mu(p', p) u(p) =
        \bar u(p')(\gamma^\mu + \delta\Gamma^\mu) u(p)

    \bar u(p')\delta\Gamma^\mu(p', p) u(p) =
        \int {\d^4 k\over (2\pi)^4} \tilde D_{\nu\rho}(k-p)
            \bar u(p')
            (-ie\gamma^\nu)
            \tilde S(k')
            \gamma^\mu
            \tilde S(k)
            (-ie\gamma^\rho)
            u(p) =

        =
        \int {\d^4 k\over (2\pi)^4} {-ig_{\nu\rho}\over (k-p)^2 +i\epsilon}
            \bar u(p')
            (-ie\gamma^\nu)
            {i(\fslash k' + m)\over k'^2-m^2 +i\epsilon}
            \gamma^\mu
            {i(\fslash k + m)\over k^2-m^2 +i\epsilon}
            (-ie\gamma^\rho)
            u(p) =

    = 2ie^2\int {\d^4 k\over (2\pi)^4}
        {\bar u(p') \left(
            \fslash k \gamma^mu \fslash k' + m^2\gamma^\mu - 2m(k+k')^\mu
            \right) u(p) \over
        ((k-p)^2 + i\epsilon)(k'^2 - m^2 + i\epsilon)(k^2-m^2+i\epsilon)
            }=

    = \cdots =

    = 2i e^2 \int {\d^4 l\over (2\pi)^4} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
        {2\over D^3} \bar u(p') \left(
        \gamma^\mu (-\half l^2+ (1-x)(1-y)q^2 + (1-4z+z^2)m^2)
            + {i\sigma^{\mu\nu}q_\nu\over 2m} (2m^2 z(1-z))
        \right)u(p) =

    = {\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
        \bar u(p') \left(
        \gamma^\mu \left[\log {z \Lambda^2\over\Delta} + {1\over\Delta}
            \left((1-x)(1-y)q^2 + (1-4z+z^2)m^2\right)\right]
            + {i\sigma^{\mu\nu}q_\nu\over 2m}\left[{1\over\Delta}2m^2 z(1-z)
                \right] \right)u(p)

where

.. math::

    k' = k + q

    D = l^2 - \Delta + i\epsilon

    \Delta = -xyq^2 + (1-z)^2 m^2 > 0

So the expressions for the form factors are:

.. math::

    F_1(q^2) = 1 + {\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
        \left[\log {z \Lambda^2\over\Delta} + {1\over\Delta}
            \left((1-x)(1-y)q^2 + (1-4z+z^2)m^2\right)\right]
            +O(\alpha^2)

    F_2(q^2) = {\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
         \left[{1\over\Delta}2m^2 z(1-z) \right]
            +O(\alpha^2) =

    = {\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
         \left[2m^2 z(1-z)\over m^2(1-z)^2 - q^2 xy \right]
            +O(\alpha^2)

$F_1$ contains both ultraviolet and infrared divergencies. To cure the infrared
divergence, we add a term $\mu^2 z$ to $\Delta$. To cure the ultraviolet
divergence, we make the substitution:

.. math::

    F_1(q^2) \to F_1(q^2) - \delta F_1(0)

where $\delta F_1$ is the first order (in $\alpha$) correction to $F_1$ (i.e.
$F_1 = 1 + \delta F_1 + O(\alpha^2)$):

.. math::

    \delta F_1(0) = {\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
        \left[\log {z \Lambda^2\over\Delta (q^2=0)} + {1\over\Delta (q^2=0)}
            (1-4z+z^2)m^2\right]

so the corrected $F_1$ is:

.. math::

    F_1(q^2) = 1 + {\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
        \left[\log {z \Lambda^2\over\Delta} + {1\over\Delta}
            \left((1-x)(1-y)q^2 + (1-4z+z^2)m^2\right)+\right.

        \left.-\log {z \Lambda^2\over\Delta (q^2=0)} - {1\over\Delta (q^2=0)}
        (1-4z+z^2)m^2\right]
        +O(\alpha^2) =

    = 1 + {\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
        \left[\log {m^2 (1-z)^2\over m^2(1-z)^2 - q^2 x y} +
            \left((1-x)(1-y)q^2 + (1-4z+z^2)m^2\over
            m^2(1-z)^2 - q^2 x y +\mu^2z
            \right)+\right.

        \left.-{(1-4z+z^2)m^2\over m^2 (1-z)^2 + \mu^2 z}\right]
        +O(\alpha^2)

Neither the ultraviolet nor the infrared
divergence affects $F_2(q^2)$, so we just set $q=0$:

.. math::

    F_2(0) = {\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
         \left[2m^2 z(1-z)\over m^2(1-z)^2 \right] +O(\alpha^2) =

    ={\alpha\over 2\pi} \int_0^1 \d x \,\d y \,\d z\,
        \delta(x+y+z-1)
         {2 z\over 1-z} +O(\alpha^2) =

    ={\alpha\over 2\pi} \int_0^1 \d y \int_0^1 \,\d z\,
        \theta(1-(1-y-z))\theta((1-y-z)-0)
         {2 z\over 1-z} +O(\alpha^2) =

    ={\alpha\over 2\pi} \int_0^1 \d y \int_0^1 \,\d z\,
        \theta(y+z)\theta(1-y-z)
         {2 z\over 1-z} +O(\alpha^2) =

    ={\alpha\over 2\pi} \int_0^1 \d y \int_0^1 \,\d z\,
        \theta(1-y-z)
         {2 z\over 1-z} +O(\alpha^2) =

    ={\alpha\over 2\pi} \int_0^1 \d z \int_0^{1-z} \,\d y
         {2 z\over 1-z} +O(\alpha^2) =

    ={\alpha\over 2\pi} \int_0^1 \d z (1-z)
         {2 z\over 1-z} +O(\alpha^2) =

    ={\alpha\over 2\pi} \int_0^1 \d z 2z + O(\alpha^2) =

    = {\alpha\over 2\pi} + O(\alpha^2)

Thus we get the correction to the $g$-factor of the electron:

.. math::

    a_e = {g - 2\over 2} = F_2(0) = {\alpha\over 2\pi} \approx 0.0011614

Code::

    >>> from math import pi
    >>> alpha = 1/137.035999
    >>> a_e = alpha / (2*pi)
    >>> a_e
    0.0011614097335977778

Experiments give $a_e = 0.00115965218073\pm0.00000000000028$.

Higher order corrections from QED can also be calculated:

.. math::

    a_e = A_1 \left({\alpha\over \pi}\right) +
          A_2 \left({\alpha\over \pi}\right)^2 +
          A_3 \left({\alpha\over \pi}\right)^3 +
          A_4 \left({\alpha\over \pi}\right)^4 + \cdots

we already know that $A_1 = \half$. See for example `hep-ph/9410248
<http://arxiv.org/abs/hep-ph/9410248>`_ for the expression for $A_2$:

.. math::

    A_2 = \frac{197}{144} + \frac{3}{4} \zeta\left(3\right) - \frac{1}{2}
        \pi^{2} \operatorname{log}\left(2\right) + \frac{1}{12} \pi^{2} =

    = -0.328478965579\dots


Code::

    >>> from sympy import zeta, S, log
    >>> A_2 = S(197)/144 + zeta(2)/2 + 3*zeta(3)/4 - 3*zeta(2) * log(2)
    >>> A_2.n()
    -0.328478965579194




See `hep-ph/9602417 <http://arxiv.org/abs/hep-ph/9602417>`_, where the author
obtains the following expression for the coefficient $A_3$:

.. math::

    A_3 = \frac{28259}{5184} - \frac{215}{24} \zeta\left(5\right)
    + \frac{100}{3} \left(\sum_{n=1}^{\infty} \frac{1}{2^{n} n^{4}} -
      \frac{1}{24} \pi^{2} \operatorname{log}^{2}\left(2\right) + \frac{1}{24}
      \operatorname{log}^{4}\left(2\right)\right) +

    +\frac{139}{18}
    \zeta\left(3\right) - \frac{298}{9} \pi^{2}
    \operatorname{log}\left(2\right) + \frac{83}{72} \pi^{2}
    \zeta\left(3\right) + \frac{17101}{810} \pi^{2} -
    \frac{239}{2160} \pi^{4} =

    = 1.181241456\dots


Code::

    >>> from sympy import pi, zeta, S, log, sum, var, oo
    >>> var("n")
    n
    >>> a4 = sum(1/(2**n * n**4), (n, 1, oo))
    >>> A_3 = 83*pi**2*zeta(3)/72 - 215*zeta(5)/24 + 100*(a4 + log(2)**4/24 - \
    ...         pi**2*log(2)**2/24)/3 - \
    ...         239*pi**4/2160 + 139*zeta(3)/18 - 298 * pi**2 * log(2)/9 + \
    ...         17101 * pi**2 / 810 + S(28259)/5184
    >>> A_3.n()
    1.18124145658720

Numerical approximation for $A_4$ can be found in
`hep-ph/0507249 <http://arxiv.org/abs/hep-ph/0507249>`_:

.. math::

    A_4=-1.7283(35)


So the total value of $a_e$ is:

.. math::

    a_e = 0.00115965223273643 + O(\alpha^4)

    a_e = 0.00115965218242334 + O(\alpha^5)

Code::

    >>> from sympy import pi, zeta, S, log, sum, var, oo
    >>> var("n")
    n
    >>> a4 = sum(1/(2**n * n**4), (n, 1, oo))
    >>> A_1 = S(1)/2
    >>> A_2 = S(197)/144 + zeta(2)/2 + 3*zeta(3)/4 - 3*zeta(2) * log(2)
    >>> A_3 = 83*pi**2*zeta(3)/72 - 215*zeta(5)/24 + 100*(a4 + log(2)**4/24 - \
    ...         pi**2*log(2)**2/24)/3 - \
    ...         239*pi**4/2160 + 139*zeta(3)/18 - 298 * pi**2 * log(2)/9 + \
    ...         17101 * pi**2 / 810 + S(28259)/5184
    >>> alpha = 1/137.035999
    >>> a_e = A_1 * (alpha/pi) + A_2 * (alpha/pi)**2 + A_3 * (alpha/pi)**3
    >>> a_e.n()
    0.00115965223273643
    >>> A_4 = -1.7283
    >>> (a_e + A_4 * (alpha/pi)**4).n()
    0.00115965218242334
