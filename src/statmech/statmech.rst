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
