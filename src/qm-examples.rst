========
Examples
========

Two Particles in Harmonic Potential
===================================

It is a 1D, two-body problem with an interacting Hamiltonian

.. math::

    H(x_1, x_2) = -\half{\partial^2\over\partial x_1^2}
    -\half{\partial^2\over\partial x_2^2}
        +{1\over|x_1 - x_2|} + \half\omega^2 x_1^2 + \half\omega^2 x_2^2

and it can be solved analytically. The Schrödinger equation is

.. math::

    \left(-\half{\partial^2\over\partial x_1^2} -\half{\partial^2\over\partial x_2^2}
        +{1\over|x_1 - x_2|} + \half\omega^2 x_1^2 + \half\omega^2 x_2^2
    \right)\Psi(x_1, x_2) = E \Psi(x_1, x_2)

we use the substitution:

.. math::

    u = {1\over\sqrt2}(x_1 - x_2)

    v = {1\over\sqrt2}(x_1 + x_2)

then

.. math::

    {\partial^2\over\partial x_1^2} + {\partial^2\over\partial x_2^2}=
    {\partial^2\over\partial u^2} + {\partial^2\over\partial v^2}

    |x_1 - x_2| = \sqrt2|u|

    x_1 + x_2 = u^2 + v^2

and

.. math::

    \left(-\half{\partial^2\over\partial u^2} -\half{\partial^2\over\partial v^2}
        +{1\over\sqrt2 |u|} + \half\omega^2 u^2 + \half\omega^2 v^2
    \right)\Psi(u, v) = E \Psi(u, v)

so we can separate the equation:

.. math::

    \Psi(u, v) = f(u)g(v)

    \left(-\half{\d^2\over\d u^2} +{1\over\sqrt2 |u|} + \half\omega^2 u^2
    \right)f_k(u) = \epsilon_k f_k(u)

    \left(-\half{\d^2\over\d v^2} + \half\omega^2 v^2
    \right)g_l(v) = \epsilon_l g_l(v)

    E_{kl} = \epsilon_k + \epsilon_l

the solution of the second equation is:

.. math::

    g_l(v) = {1\over\sqrt{2^l l!}} \left(\omega\over\pi\right)^{1\over4}
        e^{-{\omega v^2\over2}} H_l(\sqrt\omega v)

    \epsilon_l = \omega(l+\half)\quad\mbox{for $l=0, 1, 2, \dots$}

where $H_n(x)$ are the Hermite polynomials:

.. math::

    H_n(x) = (-1)^n e^{x^2} {\d^n\over\d x^n} e^{-x^2}

The solution to the first equation can be approximated around the minimum of
the potential, which occurs at point $u=u_0$ (since the potential is symmetric
with respect to $u$, we only treat the branch $u>0$):

.. math::

    V(u) = {1\over\sqrt2 |u|} + \half\omega^2 u^2 =
        \left(2^{-{1\over 3}} + 2^{-{4\over3}}\right) \omega^{2\over3}
        +{3\over 2}\omega^2(u-u_0)^2
        +O\left((u-u_0)^3\right)

    u_0 = 2^{-{1\over6}}\omega^{-{2\over3}}

So the first few states can be approximated by the harmonic oscillator
solution with frequency $\sqrt3\omega$:

.. math::

    f_k(u) = {1\over\sqrt{2^k k!}} \left(\sqrt3\omega\over\pi\right)^{1\over4}
        e^{-{\sqrt3\omega (u-u_0)^2\over2}} H_k(3^{1\over4}\sqrt\omega (u-u_0))

    \epsilon_k =
        \left(2^{-{1\over 3}} + 2^{-{4\over3}}\right) \omega^{2\over3}
        +
        \sqrt3\omega(k+\half)\quad\mbox{for $k=0, 1, 2, \dots$}

The final solution is then:

.. math::

    \Psi_{kl}(u, v) = f_k(u) g_l(v) =

        =
        {1\over\sqrt{2^k k!}} \left(\sqrt3\omega\over\pi\right)^{1\over4}
        e^{-{\sqrt3\omega (u-u_0)^2\over2}} H_k(3^{1\over4}\sqrt\omega (u-u_0))
        {1\over\sqrt{2^l l!}} \left(\omega\over\pi\right)^{1\over4}
        e^{-{\omega v^2\over2}} H_l(\sqrt\omega v)

    E_{kl} = \epsilon_k + \epsilon_l =
        \left(2^{-{1\over 3}} + 2^{-{4\over3}}\right) \omega^{2\over3}
        +
        \sqrt3\omega(k+\half)
        +
        \omega(l+\half)
