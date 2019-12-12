Quantum Ideal Gas
=================

We start with a grand potential for fermions:

.. math::

    \Omega(\beta, V, \mu)
    = -\sum_i {1\over\beta}
        \log\left(\sum_{N=0}^1 e^{-\beta\left(N\epsilon_i - N\mu\right)}\right)
            =

    = -\sum_i {1\over\beta}
        \log\left(1 + e^{-\beta\left(\epsilon_i - \mu\right)}\right)
            =

    = -{1\over\beta}
        \int \int {2\d^3 x \d^3 p \over (2\pi)^3} \log\left(1 +
            e^{-\beta\left({p^2\over 2} - \mu\right)}\right)
            =

    = -{2\over\beta}
        \int \d^3 x \int_0^\infty{ 4\pi p^2 \d p \over (2\pi)^3} \log\left(1 +
            e^{-\beta\left({p^2\over 2} - \mu\right)}\right)
            =

    = -{1\over \pi^2 \beta}
        \int \d^3 x \int_0^\infty p^2 \log\left(1 +
            e^{-\beta\left({p^2\over 2} - \mu\right)}\right) \d p
            =

    = -{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
        \int \d^3 x \int_0^\infty {u^{3\over2} \over
            1 + e^{u-\beta\mu}} \d u
                =

    = -{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
        \int I_{3\over2}\left(\beta\mu\right) \,\d^3 x
        =

    = -{2\sqrt2 V \over 3 \pi^2 \beta^{5\over2}}
        I_{3\over2}\left(\beta\mu\right) \,.

Note: to write this thermodynamic potential in the canonical form
$\Omega=\Omega(T, V, \mu)$, we simply
use the relation $\beta = {1 \over k_B T}$ and get:

.. math::

    \Omega(T, V, \mu)
        = -{2\sqrt2 V (k_B T)^{5\over2} \over 3 \pi^2}
            I_{3\over2}\left(\mu\over k_B T\right) \,.

Let us compute the particle density:

.. math::

    n_e = - \left({\partial^2 \Omega(\beta, V, \mu) \over
            \partial V \partial \mu}\right)_\beta
        = {2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            {\partial \over \partial \mu}
                I_{3\over2}\left(\beta\mu\right)
        = {2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            \beta {3\over 2} I_{1\over2}
                \left(\beta\mu\right)
        = {\sqrt2 \over \pi^2 \beta^{3\over2}} I_{1\over2}
                \left(\beta\mu\right)

and express the chemical potential $\mu=\mu(n_e)$ as a function of the particle
density $n_e$:

.. math::
    :label: mu_ne

    \mu = {1\over\beta} I_{1\over2}^{-1}\left(
                {\pi^2 \beta^{3\over2} \over \sqrt 2} n_e
            \right)

We write the grand potential using $n_e$ as follows:

.. math::
    :label: Omega_ne

    \Omega(\beta, V, n_e)
        = -{2\sqrt2 V \over 3 \pi^2 \beta^{5\over2}}
            I_{3\over2}\left(
            I_{1\over2}^{-1}\left(
                            {\pi^2 \beta^{3\over2} \over \sqrt 2} n_e
                        \right)
            \right)\,.

Now we can calculate the free energy:

.. math::

    F_e(\beta, V, n_e) = \Omega(\beta, V, n_e) + \mu N =

        = -{2\sqrt2 V \over 3 \pi^2 \beta^{5\over2}}
            I_{3\over2}\left(\beta\mu \right)
            + \mu n_e V =

        = -{2\sqrt2 V \over 3 \pi^2 \beta^{5\over2}}
            I_{3\over2}\left(
            I_{1\over2}^{-1}\left(
                            {\pi^2 \beta^{3\over2} \over \sqrt 2} n_e
                        \right)
            \right)
            +
            {1\over\beta} I_{1\over2}^{-1}\left(
                            {\pi^2 \beta^{3\over2} \over \sqrt 2} n_e
                        \right) n_e V

where we used :eq:`Omega_ne`, :eq:`mu_ne` and the fact that $n_e = N / V$.
Note: we can express the free energy in canonical form $F = F(T, V, N)$ using
$\beta = {1 \over k_B T}$ and $n_e = N / V$:

.. math::

    F_e(T, V, N)
        = -{2\sqrt2 V (k_B T)^{5\over2} \over 3 \pi^2 }
            I_{3\over2}\left(
            I_{1\over2}^{-1}\left(
                            {\pi^2 N \over \sqrt 2 (k_B T)^{3\over2} V}
                        \right)
            \right)
            +
            k_B T I_{1\over2}^{-1}\left(
                            {\pi^2 N \over \sqrt 2 (k_B T)^{3\over2} V}
                        \right) N \,.

We can calculate the entropy
$S=-\left(\partial\Omega\over\partial T\right)_{V,\mu}$ as follows:

.. math::

    TS
        =-T \left(\partial\Omega\over\partial T\right)_{V,\mu} =

        =\beta \left(\partial\Omega\over\partial \beta\right)_{V,\mu} =

        =\beta {\partial\over\partial \beta}\left(
            -{2\sqrt2 V \over 3 \pi^2 \beta^{5\over2}}
                I_{3\over2}\left(\beta\mu\right)
        \right) =

        =\beta \left(
            {5\over2}{2\sqrt2 V \over 3 \pi^2 \beta^{7\over2}}
            I_{3\over2}(\beta\mu)
            -{2\sqrt2 V \over 3 \pi^2 \beta^{5\over2}}
            {3\over2} I_{1\over2}(\beta\mu) \mu
        \right) =

        = {5\over3}{\sqrt2 V \over \pi^2 \beta^{5\over2}} I_{3\over2}(\beta\mu)
            -{\sqrt2\over \pi^2 \beta^{3\over2}} I_{1\over2}(\beta\mu) \mu V =

        = {5\over3}{\sqrt2 V \over \pi^2 \beta^{5\over2}} I_{3\over2}(\beta\mu)
            -n_e \mu V =

        = {5\over3}{\sqrt2 V \over \pi^2 \beta^{5\over2}} I_{3\over2}(\beta\mu)
            -\mu N \,.


The total energy $U$ is then equal to:

.. math::

    U = \Omega + \mu N + TS =

        = -{2\sqrt2 V \over 3 \pi^2 \beta^{5\over2}}
        I_{3\over2}\left(\beta\mu\right)
        + \mu N
        + {5\over3}{\sqrt2 V \over \pi^2 \beta^{5\over2}} I_{3\over2}(\beta\mu)
            -\mu N =

        = {\sqrt2 V \over \pi^2 \beta^{5\over2}}
        I_{3\over2}\left(\beta\mu\right) \,.

Note: the kinetic energy $E_{kin} = U$ is equal to the total energy, as the gas
is non-interacting.

The pressure $p$ can be calculated from:

.. math::

    p = - \left(\partial\Omega\over\partial V\right)_{\mu,\beta}
    = {2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
        I_{3\over2}\left(\beta\mu\right) =

        = {2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            I_{3\over2}\left(
            I_{1\over2}^{-1}\left(
                            {\pi^2 \beta^{3\over2} \over \sqrt 2} n_e
                        \right)
            \right) \,.

Note that we got $p = {2 U \over 3 V}$, $\Omega=-{2\over3} U$,
$F=-{2\over3} U + \mu N$ and $TS = {5\over 3} U -\mu N$.
