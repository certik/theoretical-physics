Thermodynamics
==============

Fundamental Thermodynamic Relation
----------------------------------

The first law of thermodynamics is $\d U = \d Q - \d W$, where $Q$ is the heat
supplied to the system and $W$ is the work done by the system.
The second law of thermodynamics is $\d S = {\d Q \over T}$. By substituting
into the first law, and expressing the work $\d W = p \d V$ using pressure and
volume, we obtain:

.. math::

    \d U = T\d S - p \d V

This can then be generalized to:

.. math::

    \d U = T\d S - p \d V + \mu \d N

where $\mu$ is the chemical potential and $N$ the number of particles in the
system.


Thermodynamic Potentials
------------------------

We start by writing the internal energy (derived in the previous section)

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

Other first derivatives
~~~~~~~~~~~~~~~~~~~~~~~

Other commonly used first derivatives are the heat capacity at constant volume:

.. math::

    C_V = \left(\partial U \over \partial T\right)_{V, N}
        = T \left(\partial S \over \partial T\right)_{V, N}
        = -T \left(\partial^2 F \over \partial T^2\right)_{V, N}

and the heat capacity at constant pressure

.. math::

    C_p = \left(\partial H \over \partial T\right)_{p, N}
        = T \left(\partial S \over \partial T\right)_{p, N}
        = -T \left(\partial^2 G \over \partial T^2\right)_{p, N}

Note that these first derivatives are differentiating the thermodynamic
potential that is not expressed in its canonical variables (the only canonical
first derivatives are already enumerated in the previous section). In both
cases the quantity can be expressed as a second derivative of a potential in
its canonical variables.  As shown below, the canonical second derivatives can
also be enumerated.

Second derivatives
~~~~~~~~~~~~~~~~~~

Here are the most commonly used second derivatives. The particle density:

.. math::

    n = \left(\partial N \over \partial V\right)_{T, \mu}
      = -\left(\partial^2 \Omega \over \partial V\partial\mu\right)_{T}
      = \left(\partial p \over \partial \mu\right)_{T, V}

The speed of sound:

.. math::

    c = \sqrt{\left(\partial p \over \partial \rho\right)_{S,N}}
      = \sqrt{-{V^2\over m}\left(\partial p \over \partial V\right)_{S,N}}
      = \sqrt{{V^2\over m}\left(\partial^2 U \over \partial V^2\right)_{S,N}}
      = \sqrt{-v^2\left(\partial p \over \partial v\right)_{S,N}}

where $\rho={m \over V}$ is the density and $v = {V \over m}$ is the specific
volume.
The isothermal speed of sound:

.. math::

    c_T = \sqrt{\left(\partial p \over \partial \rho\right)_{T,N}}
      = \sqrt{{V^2\over m}\left(\partial^2 F \over \partial V^2\right)_{T,N}}

The adiabatic bulk modulus:

.. math::

    B_S = \rho \left(\partial p \over \partial \rho\right)_{S,N}
          = \rho c^2
          = V \left(\partial^2 U \over \partial V^2\right)_{S,N}

Adiabatic coefficient of compressibility:

.. math::

    \beta_S = {1 \over B_S}
        = -{1\over V} \left(\partial V \over \partial p\right)_{S,N}
        = -{1\over V} \left(\partial^2 H \over \partial p^2\right)_{S,N}

The isothermal bulk modulus:

.. math::

    B_T = \rho \left(\partial p \over \partial \rho\right)_{T,N}
          = \rho c_T^2
          = V \left(\partial^2 F \over \partial V^2\right)_{T,N}

Isothermal coefficient of compressibility:

.. math::

    \beta_T = {1 \over B_T}
        = -{1\over V} \left(\partial V \over \partial p\right)_{T,N}
        = -{1\over V} \left(\partial^2 G \over \partial p^2\right)_{T,N}

The Grüneisen parameter:

.. math::

    \gamma = V \left(\partial p \over \partial U\right)_{V,N}

The coefficient of thermal expansion

.. math::

    \alpha = {1\over V} \left(\partial V \over \partial T\right)_{p,N}
           = {1\over V} \left(\partial^2 G \over \partial T\partial p\right)_{N}

Note: there are three possible second derivatives of the Gibbs free energy
$G(T,p,N)$ with respect to $T$ and $p$:

.. math::

    \left(\partial^2 G \over \partial T^2\right)_{p, N}
        = - {C_p \over T}

.. math::

    \left(\partial^2 G \over \partial T\partial p\right)_{N}
        = \alpha V

.. math::

    \left(\partial^2 G \over \partial p^2\right)_{T,N}
        = -\beta_T V

Every other second derivative of other thermodynamic potentials can be
expressed using these three derivatives (i.e., using $C_p$, $\alpha$ and
$\beta_T$). For example:

.. math::

    C_V = C_p - {T V \alpha^2 \over \beta_T}

.. math::

    \beta_S = \beta_T - {T V \alpha^2 \over C_p}


Examples
--------

.. _ideal_gas:

Ideal Gas
~~~~~~~~~

The internal energy as a function of $S$, $V$ and $N$ is equal to:

.. math::
    :label: ideal-gas-U

    U(S, V, N) = c_V N k_\mathrm{B} \left({N\Phi\over V}
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}

where $c_V$ is the heat capacity at a constant volume (${3\over 2}$ for
monoatomic gases, ${5\over2}$ for diatomic gases), $k_\mathrm{B}$ is the
Boltzman constant and $\Phi$ is a constant that may vary for different gases,
but it is independent of the thermodynamic state of the gas.

At this level, the above expression is simply given. We would have to use
statistical physics in order to calculate any of the thermodynamic potentials.

Now we calculate the free energy $F(T, V, N)$. First we must calculate the
temperature $T$:

.. math::
    :label: ideal-gas-T

    T = \left(\partial U \over \partial S\right)_{V, N} =

        = {\partial \over \partial S} \left(
            c_V N k_\mathrm{B} \left({N\Phi\over V}
            e^{S\over N k_\mathrm{B}}\right)^{1\over c_V} \right) =

        = \left({N\Phi\over V}
            e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}\,.

In order to calculate the the free energy, we must use :eq:`ideal-gas-T` to
eliminate $S$:

.. math::
    :label: ideal-gas-S

    S = N k_\mathrm{B} \log \left({VT^{c_V}\over N\Phi}\right)

and then express $F$ as a function of $T$, $V$ and $N$ only:

.. math::
    :label: ideal-gas-F

    F(T, V, N) = U - TS =

        = c_V N k_\mathrm{B} \left({N\Phi\over V}
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}
        -T S =

        = c_V N k_\mathrm{B} T -T
            N k_\mathrm{B} \log \left({VT^{c_V}\over N\Phi}\right) =

        = N k_\mathrm{B} T \left(c_V
            - \log \left({VT^{c_V}\over N\Phi}\right) \right)\,.

This calculation shows that one can also express the internal energy as a
function of $T$, $V$ and $N$ as $U = U(T, V, N) = c_V N k_\mathrm{B} T$. This
is a valid expression, but unlike $U = U(S, V, N)$, this is not a thermodynamic
potential, because we lost some information. In particular, if we use $U = U(T,
V, N)$ to find $U = U(S, V, N)$:

.. math::

    U = U(T, V, N) = c_V N k_\mathrm{B} T = c_V N k_\mathrm{B}
        \left(\partial U \over \partial S\right)_{V, N}

    \d S = c_V N k_\mathrm{B} {\d U \over U}
        \quad\quad\mbox{($V$ and $N$ constant)}

    S = c_V N k_\mathrm{B} \log U + C
        \quad\quad\mbox{($V$ and $N$ constant)}

    U(S, V, N) = f(V, N) \left(e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}\,,

we can see, that we recovered the correct formula for $U(S, V, N)$ except an
arbitrary function $f(V, N)$ of $V$ and $N$. Compared to :eq:`ideal-gas-U` we
can see that it must be $f(V, N) = c_V N k_\mathrm{B} \left({N\Phi\over V}
\right)^{1\over c_V}$, but this information got lost. For this reason, only
$U=U(S, V, N)$ as well as $F=F(T, V, N)$, that we just calculated, are
thermodynamic potentials and both contain equivalent information. But $U=U(T, V,
N)$ is not and it does not contain full information.

To convert $F(T, V, N)$ back to $U(S, V, N)$, we first calculate the entropy
$S$:

.. math::

    S = -\left(\partial F \over \partial T\right)_{V, N} =

        = -{\partial\over\partial T}\left(
          N k_\mathrm{B} T \left(c_V
            - \log \left({VT^{c_V}\over N\Phi}\right) \right)
              \right) =

        = - N k_\mathrm{B} c_V
            +N k_\mathrm{B} \log \left({VT^{c_V}\over N\Phi}\right)
            +N k_\mathrm{B} T {N\Phi\over VT^{c_V}}{V c_V T^{c_V-1}\over N\Phi}
            =

        = N k_\mathrm{B} \log \left({VT^{c_V}\over N\Phi}\right)\,,

which is the same equation as :eq:`ideal-gas-S`. From this, we express $T$, we
get :eq:`ideal-gas-T`. Finally, we can calculate the internal energy and
substitute $T$ for $S$ using :eq:`ideal-gas-T`:

.. math::

    U(S, V, N) = F + TS =

        = N k_\mathrm{B} T \left(c_V
            - \log \left({VT^{c_V}\over N\Phi}\right) \right)
              + TS =

        = N k_\mathrm{B} T c_V
            - N k_\mathrm{B} T \log \left({VT^{c_V}\over N\Phi}\right)
              + TS =

        = N k_\mathrm{B} T c_V
            - TS
              + TS =

        = c_V N k_\mathrm{B} T =

        = c_V N k_\mathrm{B} \left({N\Phi\over V}
            e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}\,.

This is the same equation as :eq:`ideal-gas-U`. This shows that all
thermodynamic potentials contain the same information and can be converted to
one another using the Legendre transformation.

Note: in equations like $F(T, V, N) = U - TS$, we can use any expressions for
$U$ and $S$ (e.g. we can use $U=U(S,V,N)$ or $U=(T, V, N)$, etc.) in the
intermediate steps, but at the end, we must express the final formula using
$T$, $V$ and $N$ only.

To calculate the Gibbs energy, we need to calculate pressure first. We can use
any of the potentials $U$, $F$, $X_1$ or $\Omega$ to do so. Since the equation
of state is typicaly expressed as $p=p(T, V, N)$, then the free energy $F(T, V,
N)$ is the natural choice:

.. math::

    p = -\left(\partial F \over \partial V\right)_{T, N} =

      = -{\partial \over \partial V}\left(
        N k_\mathrm{B} T \left(c_V
            - \log \left({VT^{c_V}\over N\Phi}\right) \right)
        \right) =

      = N k_\mathrm{B} T {\partial \over \partial V}
            \log \left({VT^{c_V}\over N\Phi}\right) =

      = N k_\mathrm{B} T {1\over V}\,,

and we get the ideal gas law $p V = N k_\mathrm{B} T$. The Gibbs energy is
equal to:

.. math::
    :label: ideal-gas-G

    G(T, p, N) = U - TS + pV = F + pV =

        = N k_\mathrm{B} T \left(c_V
            - \log \left({VT^{c_V}\over N\Phi}\right) \right)
        + N k_\mathrm{B} T =

        = N k_\mathrm{B} T \left((c_V + 1)
            - \log \left({k_\mathrm{B} T^{c_V+1}\over p\Phi}\right) \right)\,.

For the enthalpy, we first need:

.. math::

    p = -\left(\partial U \over \partial V\right)_{S, N} =

    = -c_V N k_\mathrm{B} {1\over c_V} \left({N\Phi\over V}
        e^{S\over N k_\mathrm{B}}\right)^{{1\over c_V}-1}
        {N\Phi\over V} e^{S\over N k_\mathrm{B}} \left(-{1\over V}\right) =

    = {1\over V} N k_\mathrm{B} \left({N\Phi\over V}
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}\,,

we need to use this to express the volume $V$:

.. math::

    V^{c_V+1\over c_V} =
        {N k_\mathrm{B}\over p} \left(N\Phi
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}
        = \left({N^{c_V+1} k_\mathrm{B}^{c_V}\over p^{c_V}}\Phi
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}

    V = \left({N^{c_V+1} k_\mathrm{B}^{c_V}\over p^{c_V}}\Phi
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V+1}
       = {N k_\mathrm{B}\over p} \left({ p\Phi \over k_\mathrm{B} }
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V+1}

now we can calculate $H(S, p, N)$:

.. math::
    :label: ideal-gas-H

    H(S, p, N) = U + pV =

        = c_V N k_\mathrm{B} \left({N\Phi\over V}
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V}
        + pV =

      = (c_V+1) p V =

      = (c_V+1) N k_\mathrm{B} \left({ p\Phi \over k_\mathrm{B} }
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V+1} \,.

The enthalpy in terms of temperature $H = H(T, p, N)$ can be calculated as:

.. math::

    H(T, p, N) = (c_V+1) p V = (c_V+1) N k_\mathrm{B} T\,.

The specific heat capacity at a constant volume can be calculated as:

.. math::

    c_V \equiv {1\over N k_\mathrm{B}} C_V
        = {1\over N k_\mathrm{B}}
            \left(\partial U \over \partial T\right)_{V, N} =

        = {1\over N k_\mathrm{B}}
            {\partial \over \partial T}\left(c_V N k_\mathrm{B} T\right)
        = c_V

This provides proof that the $c_V$ in :eq:`ideal-gas-U` is indeed the specific
heat capacity at a constant volume.

The specific heat capacity at a constant pressure can be calculated as:

.. math::

    c_p \equiv {1\over N k_\mathrm{B}} C_p
        = {1\over N k_\mathrm{B}}
            \left(\partial H \over \partial T\right)_{p, N} =

        = {1\over N k_\mathrm{B}} {\partial H(T, p, N) \over \partial T} =

        = {1\over N k_\mathrm{B}}
            {\partial \over \partial T}\left((c_V+1) N k_\mathrm{B} T\right)
        = c_V+1\,.

Using this relation $c_p = c_V + 1$ we can then express :eq:`ideal-gas-G`:

.. math::

    G(T, p, N)
        = N k_\mathrm{B} T \left((c_V + 1)
            - \log \left({k_\mathrm{B} T^{c_V+1}\over p\Phi}\right) \right) =

        = N k_\mathrm{B} T \left(c_p
            - \log \left({k_\mathrm{B} T^{c_p}\over p\Phi}\right) \right)\,,

and :eq:`ideal-gas-H` as:

.. math::

    H(S, p, N)
      = (c_V+1) N k_\mathrm{B} \left({ p\Phi \over k_\mathrm{B} }
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_V+1} =

      = c_p N k_\mathrm{B} \left({ p\Phi \over k_\mathrm{B} }
        e^{S\over N k_\mathrm{B}}\right)^{1\over c_p} \,.

In order to calculate the grand potential, we first need to find the chemical
potential:

.. math::

    \mu = \left(\partial F \over \partial N\right)_{T, V} =

        = {\partial \over \partial N} \left(
          N k_\mathrm{B} T \left(c_V
            - \log \left({VT^{c_V}\over N\Phi}\right) \right)
              \right) =

        = k_\mathrm{B} T \left((c_V+1)
            - \log \left({VT^{c_V}\over N\Phi}\right)\right)\,,

and express $N$ using $\mu$:

.. math::

    N = {V T^{c_V} \over \Phi e^{c_V+1-{\mu\over k_\mathrm{B} T}}}

Now we can calculate $\Omega(T, V, \mu)$:

.. math::
    :label: ideal-gas-Omega

    \Omega(T, V, \mu) = U - TS - \mu N = F - \mu N =

        = N k_\mathrm{B} T \left(c_V
            - \log \left({VT^{c_V}\over N\Phi}\right) \right)
          -\mu N =

        = N k_\mathrm{B} T \left({\mu\over k_\mathrm{B} T}-1\right)
          -\mu N =

        = - N k_\mathrm{B} T =

        = - {k_\mathrm{B} V T^{c_V+1} \over
            \Phi e^{c_V+1-{\mu\over k_\mathrm{B} T}}} =

        = - {k_\mathrm{B} V T^{c_p} \over
            \Phi e^{c_p-{\mu\over k_\mathrm{B} T}}} \,.
