Thermodynamics
==============

Thermodynamics Potentials
-------------------------

We start by writing the internal energy

.. math::

    U=U(S, V, N)=\int(T\d S - p \d V + \mu \d N)

as a function of entropy $S$, volume $V$ and a number of particles $N$. Now we
want to express it as a function of temperature $T$, pressure $p$ or a chemical
potential $\mu$, without losing any information, i.e. we still want to just
differentiate to obtain other quantities. In order to do that, we have to use
the Legendre transform. Including $U$, there are 8 possible combinations of
Legendre transforms that one can do (three of them are applying it to just one
variable, three of them to two variables, one to all three variables):


.. math::

    U = U(S, V, N) = \int (T\d S - p \d V + \mu \d N)

    F = F(T, V, N) = U - TS = \int (-S\d T - p \d V + \mu \d N)

    H = H(S, p, N) = U + pV = \int (T\d S + V \d p + \mu \d N)

    X_1 = X_1(S, V, \mu) = U - \mu N = \int (T\d S - p \d V - N \d \mu)

    G = G(T, p, N) = U - TS + pV = \int (-S\d T + V \d p + \mu \d N)

    \Omega = \Omega(T, V, \mu) = U-TS-\mu N = \int (-S\d T - p \d V - N \d \mu)

    X_2 = X_2(S, p, \mu) = U + pV-\mu N = \int (T\d S + V \d p - N \d \mu)

    X_3 = X_3(T, p, \mu) = U-TS+pV-\mu N = \int (-S\d T + V \d p - N \d \mu)

Of these, $U$ is the internal energy, $F$ is the Helmholtz free energy, $H$ is
the enthalpy, $G$ is the Gibbs free energy, $\Omega$ is the grand potential
(sometimes also called a Landau potential). The unnamed potentials are simply
labeled $X_1$, $X_2$ and $X_3$. The $X_3$ is sometimes called a null function.

From the differentials, we can then read off the derivatives (and what other
variables are constant), here are all the combinations:

.. math::

    T = \left(\partial U \over \partial S\right)_{V, N}
      = \left(\partial H \over \partial S\right)_{p, N}
      = \left(\partial X_1 \over \partial S\right)_{V, \mu}
      = \left(\partial X_2 \over \partial S\right)_{p, \mu}

    S = -\left(\partial F \over \partial T\right)_{V, N}
      = -\left(\partial G \over \partial T\right)_{p, N}
      = -\left(\partial \Omega \over \partial T\right)_{V, \mu}
      = -\left(\partial X_3 \over \partial T\right)_{p, \mu}

    p = -\left(\partial U \over \partial V\right)_{S, N}
      = -\left(\partial F \over \partial V\right)_{T, N}
      = -\left(\partial X_1 \over \partial V\right)_{S, \mu}
      = -\left(\partial \Omega \over \partial V\right)_{T, \mu}

    V = \left(\partial H \over \partial p\right)_{S, N}
      = \left(\partial G \over \partial p\right)_{T, N}
      = \left(\partial X_2 \over \partial p\right)_{S, \mu}
      = \left(\partial X_3 \over \partial p\right)_{T, \mu}

    \mu = \left(\partial U \over \partial N\right)_{S, V}
        = \left(\partial F \over \partial N\right)_{T, V}
        = \left(\partial H \over \partial N\right)_{S, p}
        = \left(\partial G \over \partial N\right)_{T, p}

    N = -\left(\partial X_1 \over \partial \mu\right)_{S, V}
      = -\left(\partial \Omega \over \partial \mu\right)_{T, V}
      = -\left(\partial X_2 \over \partial \mu\right)_{S, p}
      = -\left(\partial X_3 \over \partial \mu\right)_{T, p}

A large system is defined as: if the number of particles $N$ is made $\lambda$
times as large, $U$, $V$, and $S$ all become $\lambda$ times larger. In other
words, the internal energy of a large system is a homogeneous function of $S$,
$V$, and $N$ of order one:

.. math::

    U(\lambda S, \lambda V, \lambda N) = \lambda U(S, V, N)

Now we can apply the Euler's theorem (see :ref:`homogeneous-functions`):

.. math::

    U(S, V, N) = S\left(\partial U\over\partial S\right)_{V, N}
            + V \left(\partial U\over\partial V\right)_{S, N}
            + N \left(\partial U\over\partial N\right)_{S, V}
        = TS - pV + \mu N

And from the definitions of all the potentials we can calculate their
forms for large systems:

.. math::

    U(S, V, N) = TS - pV + \mu N

    F(T, V, N) = U - TS = -pV + \mu N

    H(S, p, N) = U + pV = TS + \mu N

    X_1(S, V, \mu) = U - \mu N = TS - pV

    G(T, p, N) = U - TS + pV = \mu N

    \Omega(T, V, \mu) = U-TS-\mu N = -pV

    X_2(S, p, \mu) = U + pV-\mu N = TS

    X_3(T, p, \mu) = U-TS+pV-\mu N = 0
