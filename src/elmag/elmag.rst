Maxwell's Equations
===================

The Maxwell's equations are:

.. math::

    \partial_\alpha F^{\beta\alpha} = \mu_0 j^\beta

    \epsilon^{\alpha\beta\gamma\delta}\partial_\gamma F_{\alpha\beta} = 0

and the Lorentz force is:

.. math::

    {\d p_\alpha\over\d \tau} = q F_{\alpha\beta} u^\beta

where:

.. math::

    j^\alpha = (c\rho, {\bf j})

    F_{\alpha\beta} = \left(\begin{array}{cccc}
    0 & {E_1\over c} & {E_2\over c} & {E_3\over c} \\
    -{E_1\over c} & 0 & -B_3 & B_2 \\
    -{E_2\over c} & B_3 & 0 & -B_1 \\
    -{E_3\over c} & -B_2 & B_1 & 0 \\
    \end{array}\right)

This corresponds to:

.. math::

    \nabla\cdot{\bf E} = c^2\mu_0 \rho

    \nabla\times{\bf B} = \mu_0 {\bf j} + {1\over c^2}{\partial{\bf E}
        \over \partial t}

    \nabla\cdot{\bf B} = 0

    \nabla\times{\bf E} = -{\partial{\bf B}\over\partial t}

Four Potential
--------------

The four potential is defined by:

.. math::

    A^\alpha = \left({\phi\over c}, {\bf A}\right)

    F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha

this corresponds to:

.. math::

    {\bf E} = -\nabla\phi - {\partial {\bf A}\over\partial t}

    {\bf B} = \nabla\times{\bf A}

The Maxwell's equations can then be written as (note that the two eq. without
sources are automatically satisfied by the four potential):

.. math::

    \partial_\alpha F^{\beta\alpha} =
        \partial_\alpha (\partial^\beta A^\alpha - \partial^\alpha A^\beta) =
        -\partial_\alpha \partial^\alpha A^\beta =
        \mu_0 j^\beta

where we have employed the Lorentz gauge $\partial_\alpha A^\alpha=0$.

Examples
--------

Magnetic Dipole
~~~~~~~~~~~~~~~

.. math::

    {\bf A}({\bf r}) = {\mu_0\over 4\pi} {{\bf m}\times{\bf r}\over r^3}

    {\bf B}({\bf r}) = \nabla\times {\bf A}
    = {\mu_0\over 4\pi} \nabla\times
        \left({{\bf m}\times{\bf r}\over r^3}\right) =

    = {\mu_0\over 4\pi} \left({\bf m}\nabla\cdot\left({\bf r}\over r^3\right)
        -{\bf m}\cdot\nabla\left({\bf r}\over r^3\right)
        \right) =

    = {\mu_0\over 4\pi} \left({\bf m}\left(\left(\nabla{1\over r^3}\right)
            \cdot{\bf r}+{1\over r^3}\nabla\cdot{\bf r}\right)
        -{\bf m}\cdot\left(\left(\nabla{1\over r^3}\right)
            {\bf r}+{1\over r^3}\nabla{\bf r}\right)\right)
        =

    = {\mu_0\over 4\pi} \left({\bf m}\left(\left(-{3{\bf r}\over r^5}\right)
            \cdot{\bf r}+{1\over r^3}3\right)
        -{\bf m}\cdot\left(\left(-{3{\bf r}\over r^5}\right)
            {\bf r}+{1\over r^3}\one\right)\right)
        =

    = {\mu_0\over 4\pi} \left({\bf m}\left(-{3\over r^3}+{3\over r^3}\right)
        +{\bf m}\cdot\left({3{\bf r}{\bf r}\over r^5}-{\one\over r^3}\right)
        \right)
        =

    = {\mu_0\over 4\pi} \left({3{\bf r}({\bf m}\cdot{\bf r})\over r^5}
        -{{\bf m}\over r^3}\right)

Bar Magnet
~~~~~~~~~~

A good model of a bar magnet of the length $L$ and width $W$ is a combination
of two magnetic monopoles (that sit inside the magnet, so one cannot actually
see them, just their behavior outside the magnet):

.. math::

    {\bf B}({\bf x}) = {\mu_0 Q_m\over 4\pi} \left(
        {{\bf x}-{\bf p}_1 \over |{\bf x}-{\bf p}_1|^3}
        -
        {{\bf x}-{\bf p}_2 \over |{\bf x}-{\bf p}_2|^3}
        \right)

where:

.. math::

    {\bf p}_1 = (0, 0, d)

    {\bf p}_2 = (0, 0, -d)

    d = {L-W\over 2}

The magnetic moment vector is:

.. math::

    {\bf m} = Q_m ({\bf p}_1 - {\bf p}_2)

and its magnitude then is:

.. math::

    m = 2 Q_m d

Bar Magnet in a Coil
~~~~~~~~~~~~~~~~~~~~

We throw a magnet through a coil and calculate the voltage on the coil.
We use two model of the bar magnet: a magnetic dipole and two monopoles $2d$
apart.

Geometry:

.. math::

    {\bf v} = (0, 0, v)

    {\bf l} = (a\cos\phi, a\sin\phi, z)

    {\d{\bf l}\over \d\phi} = (-a\sin\phi, a\cos\phi, 0)

Field of the dipole:

.. math::

    {\bf E} = 0

    {\bf B}({\bf r}) = {\mu_0\over 4\pi} \left({3{\bf r}({\bf m}\cdot{\bf r})\over r^5}
        -{{\bf m}\over r^3}\right)

    {\bf m} = (0, 0, m)

we will need:

.. math::

    {\bf v}\times{\bf B}({\bf l})
    = {\mu_0\over 4\pi}{\bf v}\times
        \left({3{\bf l}({\bf m}\cdot{\bf l})\over l^5}
    -{{\bf m}\over l^3}\right) =

    = {\mu_0\over 4\pi}
        \left({3({\bf v}\times{\bf l})({\bf m}\cdot{\bf l})\over l^5}
    -{{\bf v}\times{\bf m}\over l^3}\right) =

    = {\mu_0\over 4\pi}
        {3({\bf v}\times{\bf l})({\bf m}\cdot{\bf l})\over l^5}
        =

    = {\mu_0\over 4\pi}
        {3(va\sin\theta, -va\cos\theta, 0)mz\over (a^2 + z^2)^{5\over2}} =

    = {3\mu_0 m\over 4\pi}
        {a v z\over (a^2 + z^2)^{5\over2}} (\sin\theta, -\cos\theta, 0)

and

.. math::

    {\bf v}\times{\bf B}\cdot{\d{\bf l}\over \d\phi} =

    = {3\mu_0 m\over 4\pi}
        {a v z\over (a^2 + z^2)^{5\over2}} (\sin\theta, -\cos\theta, 0)
        \cdot
    (-a\sin\phi, a\cos\phi, 0) =

    = -{3\mu_0 m\over 4\pi}
        {a^2 v z\over (a^2 + z^2)^{5\over2}}

Field of two monopoles:

.. math::

    {\bf E} = 0

    {\bf B}({\bf x}) = {\mu_0 Q_m\over 4\pi} \left(
        {{\bf x}-{\bf p}_1 \over |{\bf x}-{\bf p}_1|^3}
        -
        {{\bf x}-{\bf p}_2 \over |{\bf x}-{\bf p}_2|^3}
        \right)

    {\bf p}_1 = (0, 0, d)

    {\bf p}_2 = (0, 0, -d)

    d = {L-W\over 2}

we will need:

.. math::

    {\bf v}\times{\bf B}({\bf l})
        = {\mu_0 Q_m\over 4\pi} \left(
        {{\bf v}\times({\bf l}-{\bf p}_1) \over |{\bf l}-{\bf p}_1|^3}
        -
        {{\bf v}\times({\bf l}-{\bf p}_2) \over |{\bf l}-{\bf p}_2|^3}
        \right) =

        = {\mu_0 Q_m\over 4\pi} \left(
        {(0, 0, v)\times(a\cos\phi, a\sin\phi, z-d) \over
            (a^2+(z-d)^2)^{3\over2}}
        -
        {(0, 0, v)\times(a\cos\phi, a\sin\phi, z+d) \over
            (a^2+(z+d)^2)^{3\over2}}
        \right) =

        = {\mu_0 Q_m a v \over 4\pi} \left(
        {1 \over (a^2+(z-d)^2)^{3\over2}}
        -
        {1 \over (a^2+(z+d)^2)^{3\over2}}
        \right) (\sin\phi, -\cos\phi, 0)

and

.. math::

    {\bf v}\times{\bf B}\cdot{\d{\bf l}\over \d\phi} =

    = {\mu_0 Q_m a v \over 4\pi} \left(
    {1 \over (a^2+(z-d)^2)^{3\over2}}
    -
    {1 \over (a^2+(z+d)^2)^{3\over2}}
    \right) (\sin\phi, -\cos\phi, 0)
        \cdot
    (-a\sin\phi, a\cos\phi, 0) =

    = -{\mu_0 Q_m a^2 v \over 4\pi} \left(
    {1 \over (a^2+(z-d)^2)^{3\over2}}
    -
    {1 \over (a^2+(z+d)^2)^{3\over2}}
    \right)

Now we can calculate the voltage:

.. math::

    V = \oint \left({\bf E} + {\bf v}\times{\bf B}\right) \cdot {\d{\bf l}} =

        = \oint {\bf v}\times{\bf B} \cdot {\d{\bf l}} =

        = \int_0^{2\pi} {\bf v}\times{\bf B} \cdot {\d{\bf l}\over \d\phi}
            \d\phi

for the dipole we get

.. math::

        V = \cdots
        = -\int_0^{2\pi} {3\mu_0 m\over 4\pi}
        {a^2 v z\over (a^2 + z^2)^{5\over2}}
            \d\phi =

        = -{3\mu_0 m\over 2}
        {a^2 v z\over (a^2 + z^2)^{5\over2}}

For two monopoles we get

.. math::

        V = \cdots
        = -\int_0^{2\pi} {\mu_0 Q_m a^2 v \over 4\pi} \left(
            {1 \over (a^2+(z-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z+d)^2)^{3\over2}}
            \right)
            \d\phi =

        = -{\mu_0 Q_m a^2 v \over 2} \left(
            {1 \over (a^2+(z-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z+d)^2)^{3\over2}}
            \right)


For the dipole, the function

.. math::

    {z\over(a^2+z^2)^{5\over 2}}

has a maximum and minimum for:

.. math::

    z = \pm{a\over 2}

with the max value:

.. math::

    {z\over(a^2+z^2)^{5\over 2}} =
    {{a\over 2}\over(a^2+\left({a\over 2}\right)^2)^{5\over 2}} =
    {16\sqrt 5 \over 125 a^4}

Code::

    >>> from sympy import var, solve, S, refine, Q
    >>> var("a z")
    (a, z)
    >>> f = z / (a**2+z**2)**(S(5)/2)
    >>> solve(f.diff(z), z)
    [-a/2, a/2]
    >>> f.subs(z, a/2)
    16*sqrt(5)*a/(125*(a**2)**(5/2))
    >>> refine(f.subs(z, a/2), Q.positive(a))
    16*sqrt(5)/(125*a**4)


So the maximum voltage is:

.. math::

    V = {\mu_0\over 2} {3va^2mz\over (a^2 + z^2)^{5\over2}}
        = {\mu_0\over 2} {3mva^2 {16\sqrt 5 \over 125 a^4}} =

        = {24\sqrt 5\over125} {\mu_0 m v\over a^2}

If we drop the magnet from height $h$ above the coil into it, then its speed
will be $v_0 = \sqrt{2hg}$ in the middle of the coil, when $t=0$. Then:

.. math::

    z = v_0 t + \half g t^2

    v = v_0 + g t

And we get for the voltage dependence for dipole:

.. math::

    V = - {\mu_0\over 2} {3va^2mz\over (a^2 + z^2)^{5\over2}}
        =- {\mu_0\over 2} {3(v_0+gt)a^2m(v_0 t + \half g t^2)\over
             (a^2 + (v_0 t + \half g t^2)^2)^{5\over2}}

The time difference between the maximum and minimum is the time difference
between $z=-{a\over2}$ and $z=+{a\over2}$, so:

.. math::

    \Delta t = \sqrt{2h+a\over g} - \sqrt{2h-a\over g}

The total flux doesn't depend on the particular dependence of $z(t)$ and
$v(t)$:

.. math::

    \Phi = \int_0^\infty V(t) \d t =

        = - {3\mu_0 m\over 2} \int_0^\infty{v(t)a^2z(t)
                \over (a^2 + z(t)^2)^{5\over2}} \d t =

        = - {3\mu_0 m\over 2} \int_0^\infty{{\d z\over\d t}a^2z(t)
                \over (a^2 + z(t)^2)^{5\over2}} \d t =

        = - {3\mu_0 m\over 2} \int_0^\infty{a^2z
                \over (a^2 + z^2)^{5\over2}} \d z =

        = - {3\mu_0 m\over 4} \int_{a^2}^\infty{a^2
                \over u^{5\over2}} \d u =

        = - {3\mu_0 m a^2\over 4} \left(-{2\over 3}\right)
            \left[1\over u^{3\over2}\right]_{a^2}^\infty =

        = - {3\mu_0 m a^2\over 4} \left(-{2\over 3}\right)
            \left[-1\over a^3\right] =

        = - {\mu_0 m \over 2a}

For the voltage dependence of two monopoles, we get:

.. math::

    V = -{\mu_0 Q_m a^2 v \over 2} \left(
            {1 \over (a^2+(z-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z+d)^2)^{3\over2}}
            \right) =

    = -{\mu_0 Q_m a^2 (v_0+gt) \over 2} \left(
            {1 \over (a^2+(v_0 t + \half g t^2-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(v_0 t + \half g t^2+d)^2)^{3\over2}}
            \right)

The total flux doesn't depend on the particular dependence of $z(t)$ and
$v(t)$:

.. math::

    \Phi = \int_0^\infty V(t) \d t =

        =-\int_0^\infty {\mu_0 Q_m a^2 v(t) \over 2} \left(
            {1 \over (a^2+(z(t)-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z(t)+d)^2)^{3\over2}}
            \right)
            \d t =

        =-\int_0^\infty {\mu_0 Q_m a^2 {\d z\over \d t} \over 2} \left(
            {1 \over (a^2+(z(t)-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z(t)+d)^2)^{3\over2}}
            \right)
            \d t =

        =-\int_0^\infty {\mu_0 Q_m a^2 \over 2} \left(
            {1 \over (a^2+(z-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z+d)^2)^{3\over2}}
            \right)
            \d z =

        =- {\mu_0 Q_m a^2 \over 2} \left(
            \int_0^\infty{1 \over (a^2+(z-d)^2)^{3\over2}} \d z
            -
            \int_0^\infty{1 \over (a^2+(z+d)^2)^{3\over2}} \d z
            \right) =

        =- {\mu_0 Q_m a^2 \over 2} \left(
            {1\over a^2}\left(1 + {d\over\sqrt{a^2 + d^2}}\right)
            -
            {1\over a^2}\left(1 - {d\over\sqrt{a^2 + d^2}}\right)
            \right) =

        =- {\mu_0 Q_m d\over\sqrt{a^2 + d^2}}

Note that in the limit $d\to 0$, we get the magnetic moment $m = 2 d Q_m$ and
the last formula for two monopoles flux becomes the dipole flux.

As a particular example, consider a coil with $N=500$ loops, $a=1.4\rm\,cm$,
$d=1.8\rm\,cm$, $Q_m=43\rm\,A\cdot m$. Then the total flux from the second peak
is:

.. math::

    \Phi =- {N\mu_0 Q_m d\over\sqrt{a^2 + d^2}} = -0.021 \rm\, V\cdot s

Code::

    >>> from math import pi, sqrt
    >>> mu0 = 4*pi*1e-7
    >>> cm = 0.01
    >>> Q_m = 43.
    >>> d = 1.8*cm
    >>> a = 1.4*cm
    >>> N = 500
    >>> -N*mu0*Q_m*d/sqrt(a**2+d**2)
    -0.02132647889395681

For a single loop with $a=1.25\rm\,cm$ we get:

.. math::

    \Phi =- {\mu_0 Q_m d\over\sqrt{a^2 + d^2}} = -4.44\times 10^{-5}
        \rm\, V\cdot s

and for a single loop with $a=1.8\rm\,cm$ we get:

.. math::

    \Phi =- {\mu_0 Q_m d\over\sqrt{a^2 + d^2}} = -3.82\times 10^{-5}
        \rm\, V\cdot s

Code::

    >>> a = 1.25*cm
    >>> -mu0*Q_m*d/sqrt(a**2+d**2)
    -4.438304942066266e-05
    >>> a = 1.8*cm
    >>> -mu0*Q_m*d/sqrt(a**2+d**2)
    -3.820879326816195e-05



RC Circuit
~~~~~~~~~~

Let's consider resistor (with voltage $V=RI$) and capacitor (with voltage
$V={Q\over C}$ and current $I(t) = Q'(t)$) in a series. Voltage on the battery
is $V$, then the equation for the circuit is:

.. math::

    RI(t) + {Q(t)\over C} = V

with initial condition $Q(0) = 0$. We differentiate it:

.. math::

    RI'(t) + {I(t)\over C} = 0

and the initial condition follows from the first equation $I(0) = {V\over R}$.
The solution is:

.. math::

    I(t) = {V\over R} e^{-{t\over RC}}

Now we calculate the charge (using the initial condition for the charge above
for the lower bound of the integral):

.. math::

    Q(t) = \int_0^t I(t') \d t'
         = {V\over R} \int_0^t e^{-{t'\over RC}} \d t'
         = {V\over R} \left[-RC e^{-{t'\over RC}}\right]_0^t =

         = {V\over R} \left[-RC e^{-{t\over RC}}+RC\right]
         = VC \left(1-e^{-{t\over RC}}\right)

The voltage on the resistor is:

.. math::

    R I(t) = R {V\over R} e^{-{t\over RC}} = V e^{-{t\over RC}}

The voltage on the capacitor is:

.. math::

    {Q(t)\over C} = {VC \left(1-e^{-{t\over RC}}\right) \over C}
        = V \left(1-e^{-{t\over RC}}\right)

Half life of the capacitor is defined as the time $\tau$ so that the charge is
half of the total charge, and we get:

.. math::

    Q(\tau) = \half Q(\infty)

    VC \left(1-e^{-{\tau\over RC}}\right) = \half VC

    1-e^{-{\tau\over RC}} = \half

    \half = e^{-{\tau\over RC}}

    \log \half = -{\tau\over RC}

    \tau = -RC \log \half = RC\log 2


Semiconductor Device Physics
============================

In general, the task is to find the five quantities:

.. math::

    n({\bf x}, t),
    p({\bf x}, t),
    {\bf J}_n({\bf x}, t),
    {\bf J}_h({\bf x}, t),
    {\bf E}({\bf x}, t)

where $n$ ($p$) is the electron (hole) concentration, ${\bf J}_n$
(${\bf J}_p$) is the electron (hole) current density, ${\bf E}$ is the
electric field.

And we have five equations that relate them. We start with the continuity
equation:

.. math::

    \nabla\cdot{\bf J} +{\partial\rho\over\partial t} = 0

where the current density ${\bf J}$ is composed of electron and hole current
densities:

.. math::

    {\bf J} = {\bf J}_n + {\bf J}_p

and the charge density $\rho$ is composed of mobile (electrons and holes) and
fixed charges (ionized donors and acceptors):

.. math::

    \rho = q(p-n+C)

where $n$ and $p$ is the electron and hole concetration, $C$ is the net
doping concetration ($C=p_D-n_A$ where $p_D$ is the concentration of ionized
donors, charged positive, and $n_A$ is the concentration of ionized acceptors,
charged negative) and $q$ is the electron charge (positive). We get:

.. math::

    \nabla\cdot{\bf J}_n + \nabla\cdot{\bf J}_p + q\left(
        {\partial p\over\partial t}
        -{\partial n\over\partial t}
        +{\partial C\over\partial t}
        \right) = 0

Assuming the fixed charges $C$ are time invariant, we get:

.. math::

    \nabla\cdot{\bf J}_n - q {\partial n\over\partial t} =
        -\left( \nabla\cdot{\bf J}_p + q{\partial p\over\partial t}
        \right) \equiv qR

where $R$ is the net recombination rate for electrons and holes (a positive
value means recombination, a negative value generation of carriers). We get the
carrier continuity equations:

.. math::
    :label: continuity

    {\partial n\over\partial t} = -R + {1\over q} \nabla\cdot {\bf J}_n

    {\partial p\over\partial t} = -R - {1\over q} \nabla\cdot {\bf J}_p

Then we need material relations that express how the current ${\bf J}$ is
generated using ${\bf E}$ and $n$ and $p$. A drift-diffusion model is to assume
a drift current ($q\mu_n n {\bf E}$) and a diffusion ($q D_n \nabla n$),
which gives:

.. math::
    :label: drift

    {\bf J}_n = q\mu_n n {\bf E} + q D_n \nabla n

    {\bf J}_p = q\mu_p p {\bf E} - q D_p \nabla p

where $\mu_n$, $\mu_p$, $D_n$, $D_p$ are the carrier mobilities and
diffusivities.

Final equation is the Gauss's law:

.. math::

    \nabla\cdot (\varepsilon{\bf E}) = \rho

.. math::
    :label: gauss

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n + C)


Equations
---------

Combining :eq:`drift` and :eq:`continuity` we get the following three
equations for three unknowns $n$, $p$ and ${\bf E}$:

.. math::

    {\partial n\over\partial t} = -R + \nabla\cdot (\mu_n n {\bf E})
        +\nabla\cdot (D_n \nabla n)

    {\partial p\over\partial t} = -R - \nabla\cdot (\mu_p p {\bf E})
        +\nabla\cdot (D_p \nabla p)

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n + C)

And it is usually assumed that the magnetic field is time independent, so
${\bf E}=-\nabla\phi$ and we get:

.. math::
    :label: semicond-eq

    {\partial n\over\partial t} = -R - \nabla\cdot (\mu_n n \nabla\phi)
        +\nabla\cdot (D_n \nabla n)

    {\partial p\over\partial t} = -R + \nabla\cdot (\mu_p p \nabla\phi)
        +\nabla\cdot (D_p \nabla p)

    \nabla\cdot(\varepsilon \nabla\phi) = -q(p-n + C)

These are three nonlinear (due to the terms $\mu_n n \nabla\phi$ and
$\mu_p p \nabla\phi$) equations for three unknown functions $n$, $p$ and $\phi$.

Example 1
~~~~~~~~~

We can substract the first two
equations and we get:

.. math::

    {\partial q(p-n)\over\partial t} = - q\nabla\cdot ((\mu_p p+\mu_n n){\bf E})
        +q\nabla\cdot(D_p \nabla p-D_n\nabla n)

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n+C)

and using $\rho=q(p-n+C)$ and $\sigma=q(\mu_p p+\mu_n n)$, we get:

.. math::

    {\partial \rho\over\partial t} -q{\partial C\over\partial t} =
        - \nabla\cdot (\sigma {\bf E})
        +q\nabla\cdot(D_p \nabla p-D_n\nabla n)

    \nabla\cdot(\varepsilon {\bf E}) = \rho

So far we didn't make any assumptions. Most of the times the net doping
concetration $C$ is time independent, which gives:

.. math::

    {\partial \rho\over\partial t} =
        - \nabla\cdot (\sigma {\bf E})
        +q\nabla\cdot(D_p \nabla p-D_n\nabla n)

    \nabla\cdot(\varepsilon {\bf E}) = \rho

Assuming further $D_p \nabla p-D_n\nabla n=0$, we just get the equation of
continuity and the Gauss law:

.. math::

    {\partial \rho\over\partial t} + \nabla\cdot (\sigma {\bf E}) = 0

    \nabla\cdot(\varepsilon {\bf E}) = \rho

Finally, assuming also that that $\rho$ doesn't depend on
time, we get:

.. math::

    \nabla\cdot (\sigma {\bf E}) = 0

    \nabla\cdot(\varepsilon {\bf E}) = \rho


Example 2
~~~~~~~~~

As a simple model, assume $D_n$, $D_p$, $\mu_n$, $\mu_p$ and $\varepsilon$
are position independent and $C=0$, $R=0$:

.. math::

    {\partial n\over\partial t} =
        +\mu_n n \nabla\cdot {\bf E}
        +\mu_n {\bf E}\cdot\nabla n
        +D_n \nabla^2 n

    {\partial p\over\partial t} =
        -\mu_p p \nabla\cdot {\bf E}
        -\mu_p {\bf E}\cdot\nabla p
        +D_p \nabla^2 p

    \varepsilon\nabla\cdot {\bf E} = q(p-n)


Using ${\bf E} = -\nabla \phi$ we get:

.. math::

    {\partial n\over\partial t} =
        -\mu_n n \nabla^2\phi
        -\mu_n \nabla\phi\cdot\nabla n
        +D_n \nabla^2 n

    {\partial p\over\partial t} =
        +\mu_p p \nabla^2\phi
        +\mu_p \nabla\phi\cdot\nabla p
        +D_p \nabla^2 p

    \varepsilon\nabla^2\phi = -q(p-n)

Example 3
---------

Let's calculate the 1D pn-junction. We take the equations :eq:`semicond-eq` and
write them in 1D for the stationary state
(${\partial n\over\partial t}={\partial p\over\partial t}=0$):

.. math::

    0 = -R - (\mu_n n \phi')' + (D_n n')'

    0 = -R + (\mu_p p \phi')' + (D_p p')'

    (\varepsilon \phi')' = -q(p-n + C)

We expand the derivatives and assume that $\mu$ and $D$ is constant:

.. math::

    0 = -R - \mu_n n' \phi' - \mu_n n \phi'' + D_n n''

    0 = -R + \mu_p p' \phi' + \mu_p p \phi'' + D_p p''

    \varepsilon \phi'' = -q(p-n + C)

and we put the second derivatives on the left hand side:

.. math::
    :label: 1d-pn-junction1

    n'' = {1\over D_n}(R + \mu_n n' \phi' + \mu_n n \phi'')

    p'' = {1\over D_p}(R - \mu_p p' \phi' - \mu_p p \phi'')

    \phi'' = -{q\over\varepsilon} (p-n + C)

now we introduce the variables $y_i$:

.. math::

    y_0 = n

    y_1 = y_0' = n'

    y_2 = p

    y_3 = y_2' = p'

    y_4 = \phi

    y_5 = y_4' = \phi'

and rewrite :eq:`1d-pn-junction1`:

.. math::

    y_1' = {1\over D_n}(R + \mu_n y_1 y_5 + \mu_n y_0 y_5')

    y_3' = {1\over D_p}(R - \mu_p y_3 y_5 - \mu_p y_2 y_5')

    y_5' = -{q\over\varepsilon} (y_2-y_0 + C)

So we are solving the following six nonlinear first order ODE:

.. math::
    :label: 1d-pn-junction2

    y_5' = -{q\over\varepsilon} (y_2-y_0 + C)

    y_0' = y_1

    y_1' = {1\over D_n}(R + \mu_n y_1 y_5 + \mu_n y_0 y_5')

    y_2' = y_3

    y_3' = {1\over D_p}(R - \mu_p y_3 y_5 - \mu_p y_2 y_5')

    y_4' = y_5
