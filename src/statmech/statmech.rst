Statistical Physics
===================

Microcanonical Ensemble
-----------------------

The entropy is equal to:

.. math::

    S = k_{\mathrm{B}} \log W = {1\over\beta T} \log W

where $W$ is the micronanonical partition function, the number of microstates
within the range of energy.

Canonical Ensemble
------------------

The partition function is:

.. math::

    Z_{can} = \sum_n e^{-\beta E_n}

The Helmholtz free energy is equal to:

.. math::

    F = -{1\over\beta} \log Z_{can}
      = -{1\over\beta} \log \sum_n e^{-\beta E_n}

Grand Canonical Ensemble
------------------------

The partition function for fermions is:

.. math::

    Z_{gr} = \sum_n e^{-\beta(E_n - \mu N_n)} =

      = \left(\prod_\alpha \sum_{n_\alpha=0}^1 \right) e^{-\beta(E_n - \mu N_n)}
        =

      = \left(\prod_\alpha \sum_{n_\alpha=0}^1 \right)
        e^{-\beta\left(\sum_\alpha n_\alpha \epsilon_\alpha
            - \mu \sum_\alpha n_\alpha\right)} =

      = \left(\prod_\alpha \sum_{n_\alpha=0}^1 \right) \prod_\alpha
        e^{-\beta n_\alpha\left(\epsilon_\alpha - \mu\right)} =

      = \prod_\alpha \left(\sum_{n_\alpha=0}^1
        e^{-\beta n_\alpha\left(\epsilon_\alpha - \mu\right)} \right) =

      = \prod_\alpha \left(1 + e^{-\beta (\epsilon_\alpha - \mu)} \right)

Similarly, for bosons we would get:

.. math::

    Z_{gr} = \sum_n e^{-\beta(E_n - \mu N_n)} =

      = \left(\prod_\alpha \sum_{n_\alpha=0}^\infty \right) e^{-\beta(E_n - \mu N_n)}
        =

      = \left(\prod_\alpha \sum_{n_\alpha=0}^\infty \right)
        e^{-\beta\left(\sum_\alpha n_\alpha \epsilon_\alpha
            - \mu \sum_\alpha n_\alpha\right)} =

      = \left(\prod_\alpha \sum_{n_\alpha=0}^\infty \right) \prod_\alpha
        e^{-\beta n_\alpha\left(\epsilon_\alpha - \mu\right)} =

      = \prod_\alpha \left(\sum_{n_\alpha=0}^\infty
        e^{-\beta n_\alpha\left(\epsilon_\alpha - \mu\right)} \right) =

      = \prod_\alpha \left(1 - e^{-\beta (\epsilon_\alpha - \mu)} \right)^{-1}

The grand potential for fermions is then equal to:

.. math::

    \Omega = -{1\over\beta} \log Z_{gr} =

           = -{1\over\beta} \log\left(
        \prod_\alpha \left(1 + e^{-\beta (\epsilon_\alpha - \mu)} \right)
            \right) =

           = -{1\over\beta} \sum_\alpha \log\left(
            1 + e^{-\beta (\epsilon_\alpha - \mu)} \right)

Similarly, the grand potential for bosons is equal to:

.. math::

    \Omega = -{1\over\beta} \log Z_{gr} =

           = -{1\over\beta} \log\left(
        \prod_\alpha \left(1 - e^{-\beta (\epsilon_\alpha - \mu)} \right)^{-1}
            \right) =

           = -{1\over\beta} \sum_\alpha \log\left(
            1 - e^{-\beta (\epsilon_\alpha - \mu)} \right)^{-1} =

           = {1\over\beta} \sum_\alpha \log\left(
            1 - e^{-\beta (\epsilon_\alpha - \mu)} \right)

Examples
--------

Ideal Gas
~~~~~~~~~

Ideal gas is simply a system of classical particles, where for a given
microstate specified by a set of coordinates $\mathbf{x}_i$ and momenta
$\mathbf{p}_i$ , the total energy of the microstate is given by the following
Hamiltonian:

.. math::

    H(\mathbf{x}_i, \mathbf{p}_i) = \sum_{i=1}^N {p_i^2 \over 2 m}\,,

that is, the particles are non-interacting, each has a mass $m$ and a
momentum $\mathbf{p}_i$. The canonical partition function is then equal to:

.. math::

    Z_{can}(T, V, N) = \sum_n e^{-\beta E_n} =

    = \int {\d^{3N} x\, \d^{3N} p \over N! (2\pi\hbar)^{3N}}
        e^{-\beta H(\mathbf{x}_i, \mathbf{p}_i)} =

    = \int {\d^{3N} x\, \d^{3N} p \over N! (2\pi\hbar)^{3N}}
        e^{-\beta \sum_{i=1}^N {p_i^2 \over 2 m}} =

    = {1\over N!}\left( \int {\d^3 x \d^3 p \over (2\pi\hbar)^3}
        e^{-\beta {p^2 \over 2 m}}\right)^N =

    = {1\over N!}\left(V \int_0^\infty {4\pi p^2 \d p
        \over (2\pi\hbar)^3}
        e^{-\beta {p^2 \over 2 m}}\right)^N =

    = {1\over N!}\left(V {4\pi \over (2\pi\hbar)^3}
        {\sqrt\pi (2m)^{3\over 2}\over 4 \beta^{3\over2}}
        \right)^N =

    = {1\over N!}\left(
        \left(m\over2\pi\hbar^2\beta\right)^{3\over2} V\right)^N\,,

where we used the following integral:

.. math::

    \int_0^\infty p^2 e^{-\alpha p^2} \d p =
        {\sqrt\pi\over4\alpha^{3\over2}}\,.

The Helmholtz free energy is then equal to:

.. math::

    F(T, V, N) = -{1\over\beta} \log Z_{can}(T, V, N) =

      = -{1\over\beta} \log\left( {1\over N!} \left(
        \left(m\over2\pi\hbar^2\beta\right)^{3\over2} V\right)^N\right) =

      = {N\over\beta} \left({\log N!\over N} - \log \left(
        \left(m\over2\pi\hbar^2\beta\right)^{3\over2} V\right)\right) =

      = {N\over\beta} \left(\log N - 1 + O\left(\log N\over N\right)
        - \log \left(
        \left(m\over2\pi\hbar^2\beta\right)^{3\over2} V\right)\right) =

      = {N\over\beta} \left(
        - \log \left( \left(m\over2\pi\hbar^2\beta\right)^{3\over2}
          {V e \over N}\right) + O\left(\log N\over N\right) \right) =

      = {N\over\beta} \left({3\over2}
        - \log \left( \left(m\over2\pi\hbar^2\beta\right)^{3\over2}
          {V e^{5\over2} \over N}\right) + O\left(\log N\over N\right) \right) =

      = N k_\mathrm{B} T \left({3\over2}
        - \log \left( {V T^{3\over2} \over N
          {\left(2\pi\over m k_\mathrm{B}\right)^{3\over2}
          {\hbar^3\over e^{5\over2}} }
          }\right) + O\left(\log N\over N\right) \right)\,,

where we used the Stirling's approximation for $N!$. For large $N$ this is
equal to the Helmholtz free energy of the ideal gas (see :ref:`ideal_gas`):

.. math::

    F(T, V, N)
        = N k_\mathrm{B} T \left(c_V
            - \log \left({VT^{c_V}\over N\Phi}\right) \right)\,,

with $c_V={3\over2}$ and $\Phi={\left(2\pi\over m k_\mathrm{B}\right)^{3\over2} {\hbar^3\over e^{5\over2}} }$. See that section where all other
thermodynamic properties are derived from it.

We can also start from the grand canonical partition function:

.. math::

    Z_{gr}(T, V, \mu) = \sum_{N=0}^\infty e^{\beta \mu N} Z_{can}(T, V, N) =

      = \sum_{N=0}^\infty e^{\beta \mu N}
        {1\over N!}\left(
        \left(m\over2\pi\hbar^2\beta\right)^{3\over2} V\right)^N =

      = \sum_{N=0}^\infty
        {1\over N!}\left(e^{\beta \mu}
        \left(m\over2\pi\hbar^2\beta\right)^{3\over2} V\right)^N =

      = e^{e^{\beta \mu}
        \left(m\over2\pi\hbar^2\beta\right)^{3\over2} V}

And the grand potential is:

.. math::

    \Omega(T, V, \mu) = -{1\over\beta} \log Z_{gr}(T, V, \mu) =

           = -{1\over\beta} {e^{\beta \mu}
        \left(m\over2\pi\hbar^2\beta\right)^{3\over2} V} =

           = -{k_\mathrm{B} T} {e^{\mu\over k_\mathrm{B} T}
        \left(m k_\mathrm{B} T\over2\pi\hbar^2\right)^{3\over2} V} =

        = - {k_\mathrm{B} V T^{5\over2} \over
            \left( {\left(2\pi\over m k_\mathrm{B}\right)^{3\over2}
                {\hbar^3\over e^{5\over2}} }
            \right) e^{{5\over2}-{\mu\over k_\mathrm{B} T}}} \,.

This is equal to the grand potential of an ideal gas:

.. math::

    \Omega(T, V, \mu) = - {k_\mathrm{B} V T^{c_p} \over
            \Phi e^{c_p-{\mu\over k_\mathrm{B} T}}} \,,

with
$c_p={5\over2}$ and $\Phi={\left(2\pi\over m k_\mathrm{B}\right)^{3\over2} {\hbar^3\over e^{5\over2}} }$.
The thermodynamics section then shows that the corresponding Helmholtz free
energy is the same as we obtained above from the canonical ensemble. Note that
we also obtained the same $\Phi$ as before.
