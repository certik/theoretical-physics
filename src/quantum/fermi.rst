Quantum Ideal Gas
=================

Top Down Approach
~~~~~~~~~~~~~~~~~

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

    F_e(\beta, V, n_e) = \Omega(\beta, V, n_e) + \mu N
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
            -{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
            - E_{ee} - {1\over3}E_{xc}
        \right) =

        =\beta {\partial\over\partial \beta}\left(
            -{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
        \right) =

        =\beta \left(
            {5\over2}{2\sqrt2 \over 3 \pi^2 \beta^{7\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
            -{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            \int {3\over2} I_{1\over2}(\Phi(n_e({\bf x})))
                {\partial\Phi(n_e({\bf x}))\over\partial\beta}
            \, \d^3 x
        \right) =

        =\beta \left(
            {5\over2}{2\sqrt2 \over 3 \pi^2 \beta^{7\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
            -{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            \int {3\over2} I_{1\over2}(\Phi(n_e({\bf x})))
                (\mu-V({\bf x}))
            \, \d^3 x
        \right) =

        = {5\over2}{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
            - \int n_e({\bf x}) (\mu-V({\bf x})) \, \d^3 x =

        = {5\over3}{\sqrt2 \over \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
            -\mu N + E_{en}+2E_{ee} + {4\over 3}E_{xc}


The total energy is then equal to:

.. math::

    E = \Omega + \mu N + TS =

        = \left(-{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
            - E_{ee} - {1\over3}E_{xc}\right)
            + \mu N
            +{5\over3}{\sqrt2 \over \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
            -\mu N + E_{en}+2E_{ee} + {4\over 3}E_{xc} =

        = {\sqrt2 \over \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x
            + E_{en} + E_{ee} + E_{xc}

From which we can see that the kinetic energy $E_{kin}$ is equal to:

.. math::

    E_{kin} = E - (E_{en} + E_{ee} + E_{xc}) =

        = {\sqrt2 \over \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x

The relation between the total energy and free energy can be also written as:

.. math::

    E = F + TS = F +
        \beta \left(\partial\Omega\over\partial \beta\right)_{V,\mu} =

        = F + \beta \left(\partial F\over\partial \beta\right)_{V,\mu}
        = \left(\partial (\beta F)\over\partial \beta\right)_{V,\mu}

But it gives the same result as we obtained above.

To determine the kinetic part of the free energy, we set all potentials equal
to zero ($V({\bf x}) = V_{en}({\bf x}) = V_{ee}({\bf x}) = V_{xc}({\bf x}) =
0$) and obtain:

.. math::

    F_{kin}[\beta, n_e]
        = \int \left(-{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
              I_{3\over2}(\Phi(n_e({\bf x})))
            + {1\over \beta} n_e({\bf x}) \Phi(n_e({\bf x}))
                \right)\d^3 x\,.

If the potentials are zero, then the pressure can be calculated
from:

.. math::

    P = -{1\over V}\Omega[\beta, n_e]
        = {2\sqrt2 \over 3 \pi^2 \beta^{5\over2}V}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \,\d^3 x =

    = {2\sqrt2 \over 3 \pi^2 \beta^{5\over2}V}
            \int I_{3\over2}(\beta\mu) \,\d^3 x
    = {2\sqrt2 \over 3 \pi^2 \beta^{5\over2}} I_{3\over2}(\beta\mu) \,.

If the potentials are not zero, then one can calculate the pressure using:

.. math::

    P = - \left(\partial\Omega\over\partial V\right)_{\mu,T}
        = - \left(\partial F\over\partial V\right)_{T,N} =

        = - {\partial \over\partial V} \int f \d^3 x =

        = - \left[f+e_{ee}\right]_b
            - \int {\partial f\over\partial n_e}
              {\partial n_e\over\partial V}
              \d^3 x =

        = - \left[f+e_{ee}\right]_b
            - \mu \int {\partial n_e\over\partial V} \d^3 x =

        = - \left[f+e_{ee}\right]_b
            + \mu [n_e]_b =

        = \left[(-f)-e_{ee}+\mu n_e \right]_b =

        = \left[\left({2\over3}e_{kin} + e_{ee} + {1\over3}e_{xc}-\mu n_e\right)
            -e_{ee}+\mu n_e \right]_b =

        = \left[{2\over3}e_{kin} + {1\over3}e_{xc}\right]_b =

        = {1\over 3V} \int_b \left( {2\over3}e_{kin} + {1\over3}e_{xc}
            \right) {\bf x}\cdot{\bf n}\,\d S =

        = {1\over 3V} \int \left( {2\over3}e_{kin} + {1\over3}e_{xc}
            \right) \nabla\cdot{\bf x}\,\d^3 x
            +
        {1\over 3V} \int {\bf x}\cdot\nabla \left(
            {2\over3}e_{kin} + {1\over3}e_{xc}
            \right) \,\d^3 x =

        = {1\over 3V} (2E_{kin} + E_{xc})
            +
        {1\over 3V} \int {\bf x}\cdot \left(
            -n_e({\bf x})\nabla V({\bf x})
            + \nabla{1\over3}e_{xc}
            \right) \,\d^3 x =

        = {1\over 3V} (2E_{kin} + E_{xc})
            +
        {1\over 3V} (E_{en}+E_{ee}) =

        = {1\over 3V}(2E_{kin} + E_{en} + E_{ee} + E_{xc})

Summary:

.. math::

    \Omega = -{2\over 3} E_{kin} - E_{ee} - {1\over3}E_{xc}

    F_e = \Omega + \mu N = -{2\over 3} E_{kin} - E_{ee} - {1\over3}E_{xc}
        + \mu N

    TS = {5\over3} E_{kin} + E_{en} + 2 E_{ee} + {4\over3}E_{xc} - \mu N

    E = F + TS = \Omega + \mu N + TS = E_{kin} + E_{en} + E_{ee} + E_{xc}\,,

where:

.. math::

    E_{kin} = {\sqrt2 \over \pi^2 \beta^{5\over2}}
            \int I_{3\over2}(\Phi(n_e({\bf x}))) \, \d^3 x

    E_{en} = \int n_e({\bf x}) V_{en}({\bf x})\, \d^3 x

    E_{ee} = \half \int n_e({\bf x}) V_{ee}({\bf x})\, \d^3 x

    E_{xc} = {3\over4}\int n_e({\bf x}) V_{xc}({\bf x})\, \d^3 x

    n_e({\bf x}) = {\sqrt2 \over \pi^2 \beta^{3\over2}}
            I_{1\over2}\left( \beta\left(\mu-V({\bf x})\right) \right)

    \Phi(n_e({\bf x})) = \beta\left(\mu-V({\bf x})\right)
        = I_{1\over2}^{-1}\left(
                {\pi^2 \beta^{3\over2} \over \sqrt 2} n_e({\bf x})
            \right)

    N = \int n_e({\bf x})\, \d^3 x

    \mu = {1\over \beta} \Phi(n_e({\bf x})) + V({\bf x})

and $\mu N$ is calculated as follows:

.. math::

    \mu N = \int \mu n_e({\bf x})\, \d^3 x =

        = {1\over \beta} \int \Phi(n_e({\bf x})) n_e({\bf x})\, \d^3 x
            + \int V({\bf x}) n_e({\bf x})\, \d^3 x =

        = {1\over \beta} \int \Phi(n_e({\bf x})) n_e({\bf x})\, \d^3 x
            + E_{en} + 2 E_{ee} + {4\over3} E_{xc} \,.

So $F_e$ can also be expressed as:

.. math::

    F_e = -{2\over 3} E_{kin} - E_{ee} - {1\over3}E_{xc} + \mu N =

        = -{2\over 3} E_{kin}
           + {1\over \beta} \int \Phi(n_e({\bf x})) n_e({\bf x})\, \d^3 x
            + E_{en} + E_{ee} + E_{xc} \,.

Bottom Up Approach
~~~~~~~~~~~~~~~~~~

The other way to derive these equations is to use the following considerations.
The number of states in a box of side $L$ is given by:

.. math::

    N = \int {\d^3 p \over h^3} 2 L^3
      = \int {\d^3 p \over (2\pi\hbar)^3} 2 L^3
      = \int {\d^3 p \over (2\pi)^3} 2 L^3
      = \int_0^{p_f} {4\pi p^2 \d p\over (2\pi)^3} 2 L^3
      = {L^3\over\pi^2} \int_0^{p_f} p^2 \d p

We use atomic units, so $\hbar=1$.
The electronic particle density is:

.. math::
    :label: tf_low2

    n_e({\bf x}) = {N \over L^3}
      = {1\over\pi^2} \int_0^{p_f} p^2 \d p
      = {p_f^3 \over 3\pi^2}
      = {\left[2(E_f - V({\bf x}))\right]^{3\over2} \over 3\pi^2}

where we used the relation for Fermi energy $E_f = {p_f^2\over 2} + V({\bf
x})$. The potential $V({\bf x})$ is the total potential that the electrons
experience (it contains Hartree, nuclear and XC terms).
At finite temperature $T$ we need to use the Fermi distribution and this
generalizes to:

.. math::

    n_e({\bf x})
      = {1\over\pi^2} \int_0^{\infty} {p^2 \d p \over
            e^{\beta(E-\mu)} + 1}

Now we use the relation $E = {p^2\over 2} + V({\bf x})$ and substitutions
$\epsilon={p^2\over 2}$, $y = \beta \epsilon$ to rewrite this using the
:ref:`fermi_integral`:

.. math::

    n_e({\bf x})
      = {1\over\pi^2} \int_0^{\infty} {p^2 \d p \over
            e^{\beta(E-\mu)} + 1}
      = {1\over\pi^2} \int_0^{\infty} {p^2 \d p \over
            e^{\beta({p^2\over 2} + V({\bf x})-\mu)} + 1}
      = {\sqrt 2\over\pi^2} \int_0^{\infty} {\sqrt\epsilon \d \epsilon \over
            e^{\beta(\epsilon + V({\bf x})-\mu)} + 1}
      =

      = {\sqrt 2\over\pi^2 \beta^{3\over2}} \int_0^{\infty} {\sqrt y \d y \over
            e^{y - \beta(\mu - V({\bf x}))} + 1}
      = {\sqrt 2\over\pi^2 \beta^{3\over2}}
            I_{1\over2}\left(\beta(\mu - V({\bf x}))\right)

At low temperature ($T\to0$) we have
$\beta \to \infty$, $I_{1\over2}(x) \to {2\over3} x^{3\over 2}$ and we obtain:

.. math::

    n_e({\bf x}) \to
      {2\sqrt 2\over 3\pi^2 \beta^{3\over2}}
            \left(\beta(\mu - V({\bf x}))\right)^{3\over2}
      ={\left[2(\mu - V({\bf x}))\right]^{3\over2} \over 3\pi^2}

Identical with :eq:`tf_low2`. We can see that the chemical potential $\mu$
becomes the Fermi energy $E_f$ in the limit $T\to0$. In the finite-temperature
case, $\mu$ is determined from the normalization condition for the number of
electrons $N$:

.. math::

    N = \int n_e({\bf x})\, d^3 x

The kinetic energy is

.. math::

    E_{kin} = \int \d^3 x \int 2 {\d^3p\over (2\pi)^3} {p^2\over 2}
        {1\over e^{\beta(E-\mu)}+1}
    =

    = \int \d^3 x \int_0^\infty 2 {4\pi p^2 \d p\over (2\pi)^3} {p^2\over 2}
        {1\over e^{\beta(E-\mu)}+1} =

    = \int \d^3 x \int_0^\infty 2 {4\pi \sqrt 2\sqrt \epsilon \d \epsilon \over
        (2\pi)^3} \epsilon {1\over e^{\beta(\epsilon + V({\bf x})-\mu)}+1} =

    = {\sqrt 2 \over \pi^2} \int \d^3 x \int_0^\infty
        {\epsilon^{3\over2} \d \epsilon \over
        e^{\beta(\epsilon + V({\bf x})-\mu)}+1} =

    = {\sqrt 2 \over \pi^2 \beta^{5\over2}} \int \d^3 x \int_0^\infty
        {y^{3\over2} \d y \over e^{y - \beta(\mu -V({\bf x}))}+1} =

    = {\sqrt 2 \over \pi^2 \beta^{5\over2}}
        \int I_{3\over2}\left(\beta(\mu - V({\bf x}))\right) \d^3 x

From the last formula it can be shown that the kinetic energy is equal to

.. math::

    E_{kin} = {3\over 2} P V - {1\over 2} E_{en} - {1\over 2} E_{ee}

The potential energy is equal to:

.. math::

    E_{pot} = E_{en} + E_{ee}


The internal energy $E$ is equal to:

.. math::

    E = E_{kin} + E_{pot}
        = E_{kin} + E_{en} + E_{ee} =

        = {3\over 2} P V + {1\over 2} E_{en} + {1\over 2} E_{ee}

The entropy $S$ is equal to:

.. math::

    TS
       = -{1\over\beta}
         \sum_i [n_i\log n_i + (1-n_i)\log(1-n_i)] =

       = -{1\over\beta}
         \sum_i \left[n_i\log\left(n_i\over 1-n_i\right)
            + \log(1-n_i)\right] =

       =  \left[\sum_i n_i\epsilon_i\right]
       +
        \left[-\sum_i n_i \mu\right]
       +
            \left[-{1\over\beta} \sum_i\log(1-n_i)\right] =

       = \left[E_{kin} + E_{en} + 2 E_{ee}\right]
        +
        \left[-\mu N\right]
        +
        \left[{2\over3}E_{kin}\right]
        =

       = {5\over3}E_{kin} + E_{en} + 2 E_{ee} -\mu N =

       = {5\over2}P V + {1\over6}E_{en} + {7\over6}E_{ee} -\mu N

where $n_i={1\over1+e^{\beta(\epsilon_i-\mu)}}$ is the number of states at
energy $\epsilon_i$. We used the following calculation expressing one of the
sums in terms of the kinetic energy:

.. math::

    -{1\over\beta} \sum_i\log(1-n_i) =

        = -{1\over\beta}\int {2\d^3 x \d^3 p\over (2\pi)^3}
            \log {e^{\beta(E-\mu)}\over 1+e^{\beta(E-\mu)}} =

        = -{\sqrt 2\over \pi^2 \beta^{5\over2}}\int \d^3 x \int_0^\infty
            \sqrt{y}\, \d y
            \log {e^{y-\beta(\mu-V({\bf x}))}\over
                1+e^{y-\beta(\mu-V({\bf x}))}} =

        = -{\sqrt 2\over \pi^2 \beta^{5\over2}}\int \d^3 x \left[
            -{2\over3}\int_0^\infty {y^{3\over2} \d y \over
                1+e^{y-\beta(\mu-V({\bf x}))}} \right] =

        = {2\over 3}{\sqrt 2\over \pi^2 \beta^{5\over2}}\int
            I_{3\over2}\left(\beta(\mu-V({\bf x}))\right) \d^3 x =

        = {2\over 3} E_{kin} \,,

where we used $E={p^2\over2}+V({\bf x})$.

The free energy is equal to:

.. math::

    F = E - TS = -{2\over3}E_{kin} - E_{ee} + \mu N =

        = -PV + {1\over3}E_{en} - {2\over3}E_{ee} +\mu N

The grand potential is equal to:

.. math::

    \Omega = F - \mu N = -{2\over3}E_{kin} - E_{ee} =

        = -PV + {1\over3}E_{en} - {2\over3}E_{ee}

We can now express the free energy functional $F_e[\beta, n_e]$ as a function
of the density:

.. math::

    F_e[\beta, n_e] = -{2\over3}E_{kin} - E_{ee} + \mu N =

        = \int \left(-{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
              I_{3\over2}(\Phi(n_e({\bf x})))
              -\half n_e({\bf x}) V_{ee}({\bf x})
            + \mu n_e({\bf x}) \right)\d^3 x =

        = \int \left(-{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
              I_{3\over2}(\Phi(n_e({\bf x})))
              -\half n_e({\bf x}) V_{ee}({\bf x})
            + {1\over \beta} n_e({\bf x}) \Phi(n_e({\bf x}))
                + n_e({\bf x}) V({\bf x}) \right)\d^3 x =

        = \int \left(-{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
              I_{3\over2}(\Phi(n_e({\bf x})))
              -\half n_e({\bf x}) V_{ee}({\bf x})
            + {1\over \beta} n_e({\bf x}) \Phi(n_e({\bf x}))
                + n_e({\bf x}) (V_{en}({\bf x}) + V_{ee}({\bf x})
                    + V_{xc}({\bf x}))
                  \right)\d^3 x =

        = \int \left(-{2\sqrt2 \over 3 \pi^2 \beta^{5\over2}}
              I_{3\over2}(\Phi(n_e({\bf x})))
            + {1\over \beta} n_e({\bf x}) \Phi(n_e({\bf x}))
                + n_e({\bf x}) (V_{en}({\bf x}) +\half V_{ee}({\bf x})
                    + V_{xc}({\bf x}))
                  \right)\d^3 x =

        = \left( -{2\over3}E_{kin}
            + \int {1\over \beta} n_e({\bf x}) \Phi(n_e({\bf x}))\, \d^3 x
              \right)
            + E_{en} + E_{ee} + E_{xc}
