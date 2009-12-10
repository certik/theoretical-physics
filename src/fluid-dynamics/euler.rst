.. index::
    triple: compressible; Euler; equations
    single: fluid dynamics

Compressible Euler Equations
============================

The compressible Euler equations are:

.. math::

    {\partial\rho\over\partial t} + \nabla\cdot(\rho{\bf u}) = 0

    {\partial(\rho{\bf u})\over\partial t} + \nabla\cdot(\rho{\bf u}{\bf u}^T)
        + \nabla p - {\bf f} = 0

    {\partial E\over\partial t} + \nabla\cdot({\bf u}(E+p)) = 0

where

.. math::

    E = \rho e + \half \rho u^2

is the total energy per unit volume ($\half \rho u^2$ is the kinetic energy per
unit volume), $e$ is the internal energy per unit mass ($e={U\over nM}$)
and we use the ideal gas equations, so:

.. math::

    e = T c_v

    p = {n\over V} \bar RT =
    {n M\over V} {\bar R\over M}T =
    \rho RT = \rho R {e\over c_v} =
        {R\over c_v} (E-\half \rho u^2)

where
$n$ is the number of moles of gas,
$M$ is the molar mass of the gas (i.e. a mass of one mole of the gas, e.g. for
dry air we get $M=28.956\rm\,g/mol$, as it is mainly composed of 20% of oxygen
with atomic mass 16 and 78% of nitrogen with atomic mass $14$, both form
diatomic molecules, so the molecular mass is twice the atomic mass
giving the total of $0.2\cdot2\cdot16+0.78\cdot2\cdot14 = 28.24$, the rest is
given by the other components and one also has to average over all isotopes),
$\bar R=N_A k_B\doteq8.3145\rm\,{J\over K\, mol}$ is the ideal gas constant
($N_A$ is the Avogadro constant and $k_B$ is the Boltzmann constant),
$R={\bar R\over M}$ is the specific ideal gas constant (e.g. for dry air we get
$R = {8.3145\over 28.956}\rm\,{J\over g\,K}\doteq 287.14\rm\,{J\over kg\,K}$),
$\rho={n M\over V}={p\over RT}$ is the density of the gas (e.g. for dry air at
the pressure $10^5\rm\,Pa$ and temperature $22\rm\,^\circ C$ we get
$\rho = {10^5\over 287.14 \cdot (22+273.15)}\rm\,{kg\over m^3}
=1.18\,{kg\over m^3}$),
$c_v$ is the specific heat capacity at constant volume (i.e. the amount of
energy needed to heat one kg by one Kelvin at constant volume, e.g. for dry air
the experimental value is about $c_v = 717.5\rm\,{J\over kg\,K}$),
$V$ is the volume
and $T$ is the temperature of the gas.
Of those, $V$, $n$, $M$, $R$, $\bar R$ are constants, $\rho$, $e$, $E$ and $T$ are
functions of $(t, x, y, z)$.

We use the substitution:

.. math::

    {\bf U} = \rho {\bf u}

    p = {R\over c_v} (E-\half \rho u^2) =
        {R\over c_v} \left(E-{{\bf U}^2\over2\rho}\right)

and we get:

.. math::

    {\partial\rho\over\partial t} + \nabla\cdot{\bf U} = 0

    {\partial{\bf U}\over\partial t}
        + \nabla\cdot\left({{\bf U}{\bf U}^T\over\rho}+p\one\right)
        - {\bf f} = 0

    {\partial E\over\partial t}
        + \nabla\cdot\left({{\bf U}\over\rho}(E+p)\right) = 0

Now we write ${\bf U} = (U, V, W)$ and we get:

.. math::

       \frac{\partial}{\partial t} \left( \begin{array}{c}
           \varrho\\ U\\ V\\ W\\ E
       \end{array} \right)
       + \frac{\partial}{\partial x} \left( \begin{array}{c}
           U\\
           \frac{U^2}{\varrho} + p\\
           \frac{UV}{\varrho}\\
           \frac{UW}{\varrho}\\
           \frac{U}{\varrho}(E+p)
       \end{array} \right)
       + \frac{\partial}{\partial y} \left( \begin{array}{c}
           V\\
           \frac{VU}{\varrho}\\
           \frac{V^2}{\varrho} + p\\
           \frac{VW}{\varrho}\\
           \frac{V}{\varrho}(E+p)
       \end{array} \right)
       + \frac{\partial}{\partial z} \left( \begin{array}{c}
           W\\
           \frac{WU}{\varrho}\\
           \frac{WV}{\varrho}\\
           \frac{W^2}{\varrho} + p\\
           \frac{W}{\varrho}(E+p)
       \end{array} \right) + \left( \begin{array}{c}
           0\\
           -f_x\\
           -f_y\\
           -f_z\\
           0\\
       \end{array} \right) =
       \left( \begin{array}{c} 0\\ 0\\ 0\\ 0\\ 0 \end{array} \right)

    p = {R\over c_v} \left(E-{U^2+V^2+W^2\over2\rho}\right)

We solve for the unknowns $\rho$, $U$, $V$, $W$ and $E$ as functions of $(t,
x, y, z)$, the rest ($R$, $c_v$, $f_x$, $f_y$, $f_z$) are either constants or
depend on the unknowns.

After introducing:

.. math::

    {\bf w} =
       \left( \begin{array}{c}
           \varrho\\ U\\ V\\ W\\ E
       \end{array} \right)
       =
       \left( \begin{array}{c}
           \varrho\\ \rho u_1\\ \rho u_2\\ \rho u_3\\ E
       \end{array} \right)
       =
       \left( \begin{array}{c}
           w_0 \\
           w_1 \\
           w_2 \\
           w_3 \\
           w_4 \\
       \end{array} \right)

    {\bf f}_x =
       \left( \begin{array}{c}
           U\\
           \frac{U^2}{\varrho} + p\\
           \frac{UV}{\varrho}\\
           \frac{UW}{\varrho}\\
           \frac{U}{\varrho}(E+p)
       \end{array} \right)
       =
       \left( \begin{array}{c}
           w_1\\
           \frac{w_1^2}{w_0} + p\\
           \frac{w_1w_2}{w_0}\\
           \frac{w_1w_3}{w_0}\\
           \frac{w_1}{w_0}(w_4+p)
       \end{array} \right)

    {\bf f}_y =
       \left( \begin{array}{c}
           V\\
           \frac{VU}{\varrho}\\
           \frac{V^2}{\varrho} + p\\
           \frac{VW}{\varrho}\\
           \frac{V}{\varrho}(E+p)
       \end{array} \right)
       =
       \left( \begin{array}{c}
           w_2\\
           \frac{w_2w_1}{w_0}\\
           \frac{w_2^2}{w_0} + p\\
           \frac{w_2w_3}{w_0}\\
           \frac{w_2}{w_0}(w_4+p)
       \end{array} \right)

    {\bf f}_z =
       \left( \begin{array}{c}
           W\\
           \frac{WU}{\varrho}\\
           \frac{WV}{\varrho}\\
           \frac{W^2}{\varrho} + p\\
           \frac{W}{\varrho}(E+p)
       \end{array} \right)
       =
       \left( \begin{array}{c}
           w_3\\
           \frac{w_3w_1}{w_0}\\
           \frac{w_3w_2}{w_0}\\
           \frac{w_3^2}{w_0} + p\\
           \frac{w_3}{w_0}(w_4+p)
       \end{array} \right)

    {\bf g} =
       \left( \begin{array}{c}
           0\\
           -f_x\\
           -f_y\\
           -f_z\\
           0\\
       \end{array} \right)

    p = {R\over c_v} \left(E-{U^2+V^2+W^2\over2\rho}\right)
    = {R\over c_v} \left(w_4-{w_1^2+w_2^2+w_3^2\over2w_0}\right)

we can then write the equations as:

.. math::

    {\partial{\bf w}\over \partial t} +
    {\partial{\bf f}_x\over \partial x} +
    {\partial{\bf f}_y\over \partial y} +
    {\partial{\bf f}_z\over \partial z} +
    {\bf g}= 0

Note: ${\bf U}\equiv{\bf j}$, where ${\bf j}$ is the fluid density current
(it's a 3-vector) and also $w^\mu \equiv j^\mu$ (here $w^\mu$ is the same as
$w_\mu$, e.g. we are a bit sloppy about the notation), where $j^\mu$ is the
density 4-current (e.g. the first 4 components of ${\bf w}$ are exactly the
components of the 4-current $j^\mu$):

.. math::

    j^\mu =\rho v^\mu = \rho\gamma (c, {\bf u}) =
        \gamma
        \left( \begin{array}{c}
            c\rho\\
            \rho u_1\\
            \rho u_2\\
            \rho u_3\\
        \end{array} \right)

where as usual $\mu = 0, 1, 2, 3$ is the relativistic index, $c$ is the speed
of light, and in the nonrelativistic limit ($c\to\infty$) we get $\gamma\to1$
and the remaining $c$ in $j^0$ will cancel with $c$ in
$\partial_0 = {1\over c}{\partial\over\partial t}$,
so it will not be present in the final equations (that involve terms like
$\partial_\mu j^\mu$). We can also just set $c=1$ as usual in relativistic
physics.

Now we write the spatial derivatives using so called flux Jacobians
${\bf A}_x$,
${\bf A}_y$
and
${\bf A}_z$:

.. math::

    {\partial{\bf f}_x\over \partial x} =
    {\partial{\bf f}_x\over \partial {\bf w}}
    {\partial{\bf w}\over \partial x} \equiv
    {\bf A}_x
    {\partial{\bf w}\over \partial x}

    {\bf A}_x={\bf A}_x({\bf w})\equiv{\partial{\bf f}_x\over \partial {\bf w}}

Similarly for $y$ and $z$, so we get:

.. math::

    {\partial{\bf w}\over \partial t} +
    {\bf A}_x
    {\partial{\bf w}\over \partial x} +
    {\bf A}_y
    {\partial{\bf w}\over \partial y} +
    {\bf A}_z
    {\partial{\bf w}\over \partial z} +
    {\bf g}= 0

One nice thing about these particular
${\bf f}_x$,
${\bf f}_y$ and
${\bf f}_z$ functions is that they are homogeneous of degree 1:

.. math::

    {\bf f}_x(\lambda{\bf w})
    =\lambda\,{\bf f}_x({\bf w})

so the Euler equation/formula for the homogeneous function is:

.. math::

    {\bf w}\cdot {\partial {\bf f}_x({\bf w})\over\partial {\bf w}}
    ={\bf f}_x({\bf w})

    {\bf w}\cdot {\bf A}_x ={\bf f}_x({\bf w})

So both the ${\bf f}_x$ and it's derivative can be nicely factored out using
the flux Jacobian:

.. math::

    {\bf f}_x = {\bf A}_x\, {\bf w}

    {\partial{\bf f}_x\over \partial x} =
        {\bf A}_x {\partial{\bf w}\over \partial x}

by differentiating the first equation and substracting the second, we get:

.. math::

    {\partial {\bf A}_x\over\partial x}\, {\bf w} = 0

similarly for $y$ and $z$.
To calculate the Jacobians, we'll need:

.. math::

    {\partial p\over \partial {\bf w}}=
        {R\over c_v}
        \left( \begin{array}{ccccc}
            {w_1^2+w_2^2+w_3^2\over 2w_0^2} & -{w_1\over w_0} & -{w_2\over w_0}
                & -{w_3\over w_0} & 1\\
        \end{array} \right)

then we can calculate the Jacobians (and we substitute for $p$):

.. math::

    {\bf A}_x({\bf w}) = {\partial{\bf f}_x\over \partial {\bf w}}=
        \left( \begin{array}{ccccc}
            0 & 1 & 0 & 0 & 0\\
            -{w_1^2\over w_0^2} +{R\over c_v}{w_1^2+w_2^2+w_3^2\over 2 w_0^2} &
                {2w_1\over w_0}-{R\over c_v}{w_1\over w_0} &
                -{R\over c_v}{w_2\over w_0} &
                -{R\over c_v}{w_3\over w_0} &
                {R\over c_v}\\
            -{w_1w_2\over w_0^2} & {w_2\over w_0} & {w_1\over w_0} & 0 & 0\\
            -{w_1w_3\over w_0^2} & {w_3\over w_0} & 0 & {w_1\over w_0} & 0 \\
                -{w_1w_4\over w_0^2}-{w_1\over w_0^2}{R\over c_v}
                    \left(w_4-{w_1^2+w_2^2+w_3^2\over 2 w_0}\right)
                    +{w_1\over w_0}{R\over c_v}{w_1^2+w_2^2+w_3^2\over 2 w_0^2}&
                {w_4\over w_0}+{1\over w_0}{R\over c_v}
                    \left(w_4-{w_1^2+w_2^2+w_3^2\over 2 w_0}\right)
                    -{R\over c_v}{w_1^2\over w_0^2} &
                -{R\over c_v}{w_1w_2\over w_0^2} &
                -{R\over c_v}{w_1w_3\over w_0^2} &
                {w_1\over w_0}+{R\over c_v}{w_1\over w_0} \\
       \end{array} \right)

    {\bf A}_y({\bf w}) = {\partial{\bf f}_y\over \partial {\bf w}}=
        \left( \begin{array}{ccccc}
            0 & 0 & 1 & 0 & 0\\
            -{w_2w_1\over w_0^2} & {w_2\over w_0} & {w_1\over w_0} & 0 & 0\\
            -{w_2^2\over w_0^2} +{R\over c_v}{w_1^2+w_2^2+w_3^2\over 2 w_0^2} &
                -{R\over c_v}{w_1\over w_0} &
                {2w_2\over w_0}-{R\over c_v}{w_2\over w_0} &
                -{R\over c_v}{w_3\over w_0} &
                {R\over c_v}\\
            -{w_2w_3\over w_0^2} & 0 & {w_3\over w_0} & {w_2\over w_0} & 0 \\
            \cdot & \cdot & \cdot & \cdot & \cdot \\
       \end{array} \right)

    {\bf A}_z({\bf w}) = {\partial{\bf f}_z\over \partial {\bf w}}=
        \left( \begin{array}{ccccc}
            0 & 0 & 0 & 1 & 0\\
            -{w_3w_1\over w_0^2} & {w_3\over w_0} & 0 & {w_1\over w_0} & 0 \\
            -{w_3w_2\over w_0^2} & 0 & {w_3\over w_0} & {w_2\over w_0} & 0 \\
            -{w_3^2\over w_0^2} +{R\over c_v}{w_1^2+w_2^2+w_3^2\over 2 w_0^2} &
                -{R\over c_v}{w_1\over w_0} &
                -{R\over c_v}{w_2\over w_0} &
                {2w_3\over w_0} -{R\over c_v}{w_3\over w_0} &
                {R\over c_v}\\
                -{w_3w_4\over w_0^2}-{w_3\over w_0^2}{R\over c_v}
                    \left(w_4-{w_1^2+w_2^2+w_3^2\over 2 w_0}\right)
                    +{w_3\over w_0}{R\over c_v}{w_1^2+w_2^2+w_3^2\over 2 w_0^2}&
                -{R\over c_v}{w_3w_1\over w_0^2} &
                -{R\over c_v}{w_3w_2\over w_0^2} &
                {w_4\over w_0}+{1\over w_0}{R\over c_v}
                    \left(w_4-{w_1^2+w_2^2+w_3^2\over 2 w_0}\right)
                    -{R\over c_v}{w_3^2\over w_0^2} &
                {w_3\over w_0}+{R\over c_v}{w_3\over w_0} \\
       \end{array} \right)

Dimensionless Euler Equations
-----------------------------

We choose 3 constants $l_r$, $u_r$ and $\rho_r$ - characteristic length of the
domain, velocity and density. Now we multiply the Euler equations with proper
combinations of these constants as follows:

.. math::

    \left[{\partial\rho\over\partial t} + \nabla\cdot(\rho{\bf u})\right]
    {l_r\over\rho_r u_r}
    = 0

    \left[{\partial(\rho{\bf u})\over\partial t} + \nabla\cdot(\rho{\bf u}{\bf u}^T)
        + \nabla p - {\bf f}\right]
    {l_r\over\rho_r u_r^2}
    = 0

    \left[{\partial E\over\partial t} + \nabla\cdot({\bf u}(E+p))\right]
    {l_r\over\rho_r u_r^3}
    = 0

This is equal to:

.. math::

    {\partial\tilde\rho\over\partial \tilde t} + \tilde\nabla\cdot(\tilde\rho
    \tilde{\bf u}) = 0

    {\partial(\tilde \rho\tilde{\bf u})\over\partial \tilde t} +
        \tilde\nabla\cdot(\tilde\rho\tilde{\bf u}\tilde{\bf u}^T)
        + \tilde\nabla\tilde p - \tilde{\bf f} = 0

    {\partial\tilde E\over\partial\tilde t} + \tilde\nabla\cdot(
    \tilde{\bf u}(\tilde E+\tilde p)) = 0

where:

.. math::

    t_r = {l_r\over u_r}

    \tilde t = {t\over t_r}

    \tilde \rho = {\rho\over\rho_r}

    \tilde{\bf u} = {{\bf u}\over u_r}

    \tilde\nabla = l_r\nabla

    \tilde E = {E\over \rho_r u^2_r}

    \tilde p = {p\over \rho_r u^2_r}

    \tilde {\bf f} = {\bf f}{l_r\over\rho_r u^2_r}

In particular, if ${\bf f}=(0, 0, -\rho g)$, then

.. math::

    \tilde{\bf f}=(0, 0, -\tilde\rho \tilde g)

    \tilde g = g{l_r\over u^2_r} = g{t_r^2\over l_r}

So the dimensionless Euler equations look exactly the same as the original
ones, we just need to rescale all the quantities using the relations above.

FEM Formulation
---------------

The Euler equations:

.. math::

    {\partial{\bf w}\over \partial t} +
    {\bf A}_x({\bf w})
    {\partial{\bf w}\over \partial x} +
    {\bf A}_y({\bf w})
    {\partial{\bf w}\over \partial y} +
    {\bf A}_z({\bf w})
    {\partial{\bf w}\over \partial z} +
    {\bf g}= 0

are nonlinear. The simplest approximation is to linearize them by:

.. math::

    {{\bf w}^{n+1}-{\bf w}^n\over \tau} +
    {\bf A}_x({\bf w}^n)
    {\partial{\bf w}^{n+1}\over \partial x} +
    {\bf A}_y({\bf w}^n)
    {\partial{\bf w}^{n+1}\over \partial y} +
    {\bf A}_z({\bf w}^n)
    {\partial{\bf w}^{n+1}\over \partial z} +
    {\bf g}= 0

Then we multiply by the test functions (one by one):

.. math::

    \left( \begin{array}{c}
        \varphi^0 \\
        0 \\
        0 \\
        0 \\
        0 \\
    \end{array} \right),\ 
    \left( \begin{array}{c}
        0 \\
        \varphi^1 \\
        0 \\
        0 \\
        0 \\
    \end{array} \right),\ 
    \left( \begin{array}{c}
        0 \\
        0 \\
        \varphi^2 \\
        0 \\
        0 \\
    \end{array} \right),\ 
    \left( \begin{array}{c}
        0 \\
        0 \\
        0 \\
        \varphi^3 \\
        0 \\
    \end{array} \right),\ 
    \left( \begin{array}{c}
        0 \\
        0 \\
        0 \\
        0 \\
        \varphi^4 \\
    \end{array} \right)

and integrate over the 3D domain $\Omega$, so we get (here the index
$i=0, 1, 2, 3, 4$ is numbering the 5 equations, so we are *not* summing over
it):

.. math::

    \int_{\Omega} {w_i^{n+1}-w_i^n\over\tau}\varphi^i
        + \left({\bf A}_x({\bf w}^n)\right)_{ij}
          {\partial w_j^{n+1}\over\partial x} \varphi^i
        + \left({\bf A}_y({\bf w}^n)\right)_{ij}
          {\partial w_j^{n+1}\over\partial y} \varphi^i
        + \left({\bf A}_z({\bf w}^n)\right)_{ij}
          {\partial w_j^{n+1}\over\partial z} \varphi^i
        + g_i \varphi^i
        \ \d^3 x
        =0

Now we integrate by parts and use the homogeneity property (
$w_j {\partial\left({\bf A}_z({\bf w}^n)\right)_{ij}\over\partial x}
\varphi^i = 0$):

.. math::

    \int_{\Omega} {w_i^{n+1}-w_i^n\over\tau}\varphi^i
        - \left({\bf A}_x({\bf w}^n)\right)_{ij}
          w_j^{n+1} {\partial \varphi^i\over\partial x}
        - \left({\bf A}_y({\bf w}^n)\right)_{ij}
          w_j^{n+1} {\partial \varphi^i\over\partial y}
        - \left({\bf A}_z({\bf w}^n)\right)_{ij}
          w_j^{n+1} {\partial \varphi^i\over\partial z}
        + g_i \varphi^i
        \ \d^3 x
        +

    +\int_{\partial\Omega}
    \left({\bf A}_x({\bf w}^n)\right)_{ij}w_j^{n+1}
        \varphi^i\, n_x
    + \left({\bf A}_y({\bf w}^n)\right)_{ij}w_j^{n+1}
        \varphi^i\, n_y
    + \left({\bf A}_z({\bf w}^n)\right)_{ij}w_j^{n+1}
        \varphi^i\, n_z
    \ \d^2 x
    =0

where ${\bf n} = (n_x, n_y, n_z)$ is the outward surface normal to
$\partial\Omega$. Rearranging:

.. math::

    \int_{\Omega} {w_i^{n+1}\over\tau}\varphi^i
        - \left({\bf A}_x({\bf w}^n)\right)_{ij}
          w_j^{n+1} {\partial \varphi^i\over\partial x}
        - \left({\bf A}_y({\bf w}^n)\right)_{ij}
          w_j^{n+1} {\partial \varphi^i\over\partial y}
        - \left({\bf A}_z({\bf w}^n)\right)_{ij}
          w_j^{n+1} {\partial \varphi^i\over\partial z}
        \ \d^3 x
        +

    +\int_{\partial\Omega}
    \left({\bf A}_x({\bf w}^n)\right)_{ij}w_j^{n+1}
        \varphi^i\, n_x
    + \left({\bf A}_y({\bf w}^n)\right)_{ij}w_j^{n+1}
        \varphi^i\, n_y
    + \left({\bf A}_z({\bf w}^n)\right)_{ij}w_j^{n+1}
        \varphi^i\, n_z
    \ \d^2 x
    =
    \int_{\Omega} {w_i^n\over\tau}\varphi^i
        - g_i \varphi^i
        \ \d^3 x


Sea Breeze Modeling
-------------------

In our model we make the following assumptions:

.. math::

    f_x = 0

    f_y = 0

    f_z = -\rho g = -w_0 g

    V = 0

    {\partial U\over\partial y}
    ={\partial V\over\partial y}
    ={\partial W\over\partial y}
    ={\partial E\over\partial y}=0

so we get a 2D model:

.. math::

       \frac{\partial}{\partial t} \left( \begin{array}{c}
           \varrho\\ U\\ 0\\ W\\ E
       \end{array} \right)
       + \frac{\partial}{\partial x} \left( \begin{array}{c}
           U\\
           \frac{U^2}{\varrho} + p\\
           0\\
           \frac{UW}{\varrho}\\
           \frac{U}{\varrho}(E+p)
       \end{array} \right)
       + \frac{\partial}{\partial z} \left( \begin{array}{c}
           W\\
           \frac{WU}{\varrho}\\
           0\\
           \frac{W^2}{\varrho} + p\\
           \frac{W}{\varrho}(E+p)
       \end{array} \right) + \left( \begin{array}{c}
           0\\
           0\\
           0\\
           \rho g\\
           0\\
       \end{array} \right) =
       \left( \begin{array}{c} 0\\ 0\\ 0\\ 0\\ 0 \end{array} \right)

    p = {R\over c_v} \left(E-{U^2+W^2\over2\rho}\right)

where we prescribe $R$, $c_v$, $g$ and solve for $\rho$, $U$, $W$ and $E$ as
functions of $(t, x, z)$. We delete the row for $y$, which only contains zeros
anyway and introduce:

.. math::

    {\bf w} =
       \left( \begin{array}{c}
           \varrho\\ \rho u_1\\ \rho u_3\\ E
       \end{array} \right)
       =
       \left( \begin{array}{c}
           w_0 \\
           w_1 \\
           w_3 \\
           w_4 \\
       \end{array} \right)

.. math::

    {\bf A}_x({\bf w}) = {\partial{\bf f}_x\over \partial {\bf w}}=
        \left( \begin{array}{cccc}
            0 & 1 & 0 & 0\\
            -{w_1^2\over w_0^2} +{R\over c_v}{w_1^2+w_3^2\over 2 w_0^2} &
                {2w_1\over w_0}-{R\over c_v}{w_1\over w_0} &
                -{R\over c_v}{w_3\over w_0} &
                {R\over c_v}\\
            -{w_1w_3\over w_0^2} & {w_3\over w_0} & {w_1\over w_0} & 0 \\
                -{w_1w_4\over w_0^2}-{w_1\over w_0^2}{R\over c_v}
                    \left(w_4-{w_1^2+w_3^2\over 2 w_0}\right)
                    +{w_1\over w_0}{R\over c_v}{w_1^2+w_3^2\over 2 w_0^2} &
                {w_4\over w_0}+{1\over w_0}{R\over c_v}
                    \left(w_4-{w_1^2+w_3^2\over 2 w_0}\right)
                    -{R\over c_v}{w_1^2\over w_0^2} &
                -{R\over c_v}{w_1w_3\over w_0^2} &
                {w_1\over w_0}+{R\over c_v}{w_1\over w_0} \\
       \end{array} \right)

    {\bf A}_z({\bf w}) = {\partial{\bf f}_z\over \partial {\bf w}}=
        \left( \begin{array}{cccc}
            0 & 0 & 1 & 0\\
            -{w_3w_1\over w_0^2} & {w_3\over w_0} & {w_1\over w_0} & 0 \\
            -{w_3^2\over w_0^2} +{R\over c_v}{w_1^2+w_3^2\over 2 w_0^2} &
                -{R\over c_v}{w_1\over w_0} &
                {2w_3\over w_0} -{R\over c_v}{w_3\over w_0} &
                {R\over c_v}\\
            -{w_3w_4\over w_0^2}-{w_3\over w_0^2}{R\over c_v}
                    \left(w_4-{w_1^2+w_3^2\over 2 w_0}\right)
                    +{w_3\over w_0}{R\over c_v}{w_1^2+w_3^2\over 2 w_0^2}&
                -{R\over c_v}{w_3w_1\over w_0^2} &
                {w_4\over w_0}+{1\over w_0}{R\over c_v}
                    \left(w_4-{w_1^2+w_3^2\over 2 w_0}\right)
                    -{R\over c_v}{w_3^2\over w_0^2} &
                {w_3\over w_0}+{R\over c_v}{w_3\over w_0} \\
       \end{array} \right)

The weak formulation in 2D is (here $i = 0, 1, 3, 4$):

.. math::

    \int_{\Omega} {w_i^{n+1}\over\tau}\varphi^i
        - \left({\bf A}_x({\bf w}^n)\right)_{ij}
          w_j^{n+1} {\partial \varphi^i\over\partial x}
        - \left({\bf A}_z({\bf w}^n)\right)_{ij}
          w_j^{n+1} {\partial \varphi^i\over\partial z}
        \ \d^2 x
        +

    +\int_{\partial\Omega}
    \left({\bf A}_x({\bf w}^n)\right)_{ij}w_j^{n+1}
        \varphi^i\, n_x
    + \left({\bf A}_z({\bf w}^n)\right)_{ij}w_j^{n+1}
        \varphi^i\, n_z
    \ \d x
    =
    \int_{\Omega} {w_i^n\over\tau}\varphi^i
        - g_i \varphi^i
        \ \d^2 x

In order to specify the input forms for Hermes, we'll write the weak
formulation as:

.. math::

    B_{00}(w_0, \varphi^0) + B_{01}(w_1, \varphi^0) +
        B_{03}(w_3, \varphi^0)+ B_{04}(w_4, \varphi^0) = l_0(\varphi^0)

    B_{10}(w_0, \varphi^1) + B_{11}(w_1, \varphi^1) +
        B_{13}(w_3, \varphi^1)+ B_{14}(w_4, \varphi^1) = l_1(\varphi^1)

    B_{30}(w_0, \varphi^3) + B_{31}(w_1, \varphi^3) +
        B_{33}(w_3, \varphi^3)+ B_{34}(w_4, \varphi^3) = l_3(\varphi^3)

    B_{40}(w_0, \varphi^4) + B_{41}(w_1, \varphi^4) +
        B_{43}(w_3, \varphi^4)+ B_{44}(w_4, \varphi^4) = l_4(\varphi^4)

where the forms are (we write $w_i$ instead of $w_i^{n+1}$):

.. math::

    l_0(\varphi^0) = \int_\Omega {w_0^n\varphi^0\over\tau} \,\d^2 x

    l_1(\varphi^1) = \int_\Omega {w_1^n\varphi^1\over\tau} \,\d^2 x

    l_3(\varphi^3) = \int_\Omega {w_3^n\varphi^3\over\tau} + \rho g \varphi^3
        \,\d^2 x

    l_4(\varphi^4) = \int_\Omega {w_4^n\varphi^4\over\tau} \,\d^2 x

    B_{ij}(w_j, \varphi^i) = \int_{\Omega} {w_i\over\tau}\varphi^i
        \delta_{ij}
        - \left({\bf A}_x({\bf w}^n)\right)_{ij}
          w_j {\partial \varphi^i\over\partial x}
        - \left({\bf A}_z({\bf w}^n)\right)_{ij}
          w_j {\partial \varphi^i\over\partial z}
        \ \d^2 x

In the last expression we do *not* sum over $i$ nor $j$.
In particular:

.. math::

    B_{00}(w_0, \varphi^0) = \int_{\Omega} {w_0\over\tau}\varphi^0
        - \left({\bf A}_x({\bf w}^n)\right)_{00}
          w_0 {\partial \varphi^0\over\partial x}
        - \left({\bf A}_z({\bf w}^n)\right)_{00}
          w_0 {\partial \varphi^0\over\partial z}
        \ \d^2 x
        =
        \int_{\Omega} {w_0\over\tau}\varphi^0
        \ \d^2 x

    B_{01}(w_1, \varphi^0) = \int_{\Omega}
        - \left({\bf A}_x({\bf w}^n)\right)_{01}
          w_1 {\partial \varphi^0\over\partial x}
        - \left({\bf A}_z({\bf w}^n)\right)_{01}
          w_1 {\partial \varphi^0\over\partial z}
        \ \d^2 x
        =
        \int_{\Omega}
        - \left({\bf A}_x({\bf w}^n)\right)_{01}
          w_1 {\partial \varphi^0\over\partial x}
        \ \d^2 x

    B_{03}(w_3, \varphi^0) = \int_{\Omega}
        - \left({\bf A}_x({\bf w}^n)\right)_{03}
          w_3 {\partial \varphi^0\over\partial x}
        - \left({\bf A}_z({\bf w}^n)\right)_{03}
          w_3 {\partial \varphi^0\over\partial z}
        \ \d^2 x
        =
        \int_{\Omega}
        - \left({\bf A}_z({\bf w}^n)\right)_{03}
          w_3 {\partial \varphi^0\over\partial z}
        \ \d^2 x

    B_{04}(w_4, \varphi^0) = \int_{\Omega}
        - \left({\bf A}_x({\bf w}^n)\right)_{04}
          w_4 {\partial \varphi^0\over\partial x}
        - \left({\bf A}_z({\bf w}^n)\right)_{04}
          w_4 {\partial \varphi^0\over\partial z}
        \ \d^2 x
        =0

    B_{10}(w_0, \varphi^1) = \int_{\Omega}
        - \left({\bf A}_x({\bf w}^n)\right)_{10}
          w_0 {\partial \varphi^1\over\partial x}
        - \left({\bf A}_z({\bf w}^n)\right)_{10}
          w_0 {\partial \varphi^1\over\partial z}
        \ \d^2 x

    B_{11}(w_1, \varphi^1) = \int_{\Omega} {w_1\over\tau}\varphi^1
        - \left({\bf A}_x({\bf w}^n)\right)_{11}
          w_1 {\partial \varphi^1\over\partial x}
        - \left({\bf A}_z({\bf w}^n)\right)_{11}
          w_1 {\partial \varphi^1\over\partial z}
        \ \d^2 x

    \cdots

Boundary Conditions
~~~~~~~~~~~~~~~~~~~

In the boundary (line) integral we prescribe $w_4^{n+1}$ using a Dirichlet
condition and calculate it at each iteration using:

.. math::

    w_4^{n+1} = E = \rho T c_v + \half \rho u^2 = w_0 T c_v +
        {w_1^2+w_3^2\over 2w_0}

where $T(t)$ is a known function of time (it changes with the day and night)
and also prescribe $w_1^{n+1}=0$ on the left and right end of the domain and
$w_3^{n+1}=0$ at the top and bottom.

All the surface integrals turn out to be zero. On the top and bottom edges we
have ${\bf n} = (n_x, n_z) = (0, \pm 1)$ respectively and we prescribe $w_3=0$,
so we get (remember we do not sum over $i$):

.. math::

    \int_{\partial\Omega}
    \left({\bf A}_x({\bf w}^n)\right)_{ij}w_j
        \varphi^i\, n_x
    + \left({\bf A}_z({\bf w}^n)\right)_{ij}w_j
        \varphi^i\, n_z
    \ \d x
    =

    =
    \int_{\partial\Omega}
    \left({\bf f}_x({\bf w}^n)\right)_i
        \varphi^i\, n_x
    + \left({\bf f}_z({\bf w}^n)\right)_i
        \varphi^i\, n_z
    \ \d x
    =

    =
    \pm\int_{\partial\Omega}
    \left({\bf f}_z({\bf w}^n)\right)_i
        \varphi^i
    \ \d x

where:

.. math::

    {\bf f}_z =
       \left( \begin{array}{c}
           w_3\\
           \frac{w_3w_1}{w_0}\\
           \frac{w_3^2}{w_0} + p\\
           \frac{w_3}{w_0}(w_4+p)
       \end{array} \right)
       =
       \left( \begin{array}{c}
           0\\
           0\\
           p\\
           0
       \end{array} \right)

So all the components $i\neq 3$ of the surface integral are zero, and for $i=3$
the test function $\varphi^3$ is not there, because we prescribe the Dirichlet
BC $w^3=0$, so the surface integral vanishes for all $i$.

Similarly on the left and right edges we
have ${\bf n} = (n_x, n_z) = (\pm1, 0)$ respectively and we prescribe $w_1=0$,
so we get (remember we do not sum over $i$):

.. math::

    \int_{\partial\Omega}
    \left({\bf A}_x({\bf w}^n)\right)_{ij}w_j
        \varphi^i\, n_x
    + \left({\bf A}_z({\bf w}^n)\right)_{ij}w_j
        \varphi^i\, n_z
    \ \d x
    =

    =
    \int_{\partial\Omega}
    \left({\bf f}_x({\bf w}^n)\right)_i
        \varphi^i\, n_x
    + \left({\bf f}_z({\bf w}^n)\right)_i
        \varphi^i\, n_z
    \ \d x
    =

    =
    \pm\int_{\partial\Omega}
    \left({\bf f}_x({\bf w}^n)\right)_i
        \varphi^i
    \ \d x

where:

.. math::

    {\bf f}_x =
       \left( \begin{array}{c}
           w_1\\
           \frac{w_1^2}{w_0} + p\\
           \frac{w_1w_3}{w_0}\\
           \frac{w_1}{w_0}(w_4+p)
       \end{array} \right)
       =
       \left( \begin{array}{c}
           0\\
           p\\
           0\\
           0
       \end{array} \right)

So all the components $i\neq 1$ of the surface integral are zero, and for $i=1$
the test function $\varphi^1$ is not there, because we prescribe the Dirichlet
BC $w^1=0$, so the surface integral vanishes for all $i$.


Older notes
-----------

Author: Pavel Solin

Governing Equations and Boundary Conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::
    :label: one

       \frac{\partial}{\partial t} \left( \begin{array}{c} \varrho\\ U\\ W\\
       \theta \end{array} \right) + \frac{\partial}{\partial x} \left(
       \begin{array}{c} U\\ \frac{U^2}{\varrho} + R\theta\\
       \frac{UW}{\varrho}\\ \frac{\theta U}{\varrho} \end{array} \right) +
       \frac{\partial}{\partial z} \left( \begin{array}{c} W\\
       \frac{UW}{\varrho}\\ \frac{W^2}{\varrho} + R\theta\\ \frac{\theta
       W}{\varrho} \end{array} \right) + \left( \begin{array}{c} 0\\ 0\\
       \varrho g\\ \frac{R\theta}{c_v}\mbox{div}{\bf v} \end{array} \right) =
       \left( \begin{array}{c} 0\\ 0\\ 0\\ 0 \end{array} \right),


where $\varrho$ is the air density, ${\bf v} = (u,w)$ is the velocity, $U =
\varrho u$, $W = \varrho w$, $T$ is the temperature, $\theta = \varrho T$, and
$g$ is the gravitational acceleration constant.  We use the perfect gas state
equation $p = \varrho R T = R \theta$ for the pressure.

Boundary conditions are prescribed as follows: 

* edge $a$: $\partial \varrho / \partial \nu = 0$, $\partial U / \partial \nu = 0$, $W = 0$, $\theta = \mbox{tanh}(x)*\mbox{sin}(\pi t /86400)$
* edges $b, c$: $\partial \varrho / \partial \nu = 0$, $U = 0$, $\partial W / \partial \nu = 0$, $\partial \theta/ \partial \nu = 0$
* edge $d$: $\partial \varrho / \partial \nu = 0$, $\partial U / \partial \nu = 0$, $W = 0$, $\partial \theta/ \partial \nu = 0$

Initial conditions have the form 

.. math::
    :nowrap:

    \begin{eqnarray*} p(z) &=& p_0 - 11476\frac{z}{1000}  + 529.54 \left(\frac{z}{1000} \right)^2 - 9.38 \left(\frac{z}{1000} \right)^3,\\ T(z) &=& T_0 - 8.3194 \frac{z}{1000} + 0.2932 \left(\frac{z}{1000} \right)^2 - 0.0109 \left(\frac{z}{1000} \right)^3,\\ \varrho(z) &=& \frac{p(z)}{R T(z)},\\ \theta(z) &=& \varrho(z)T(z),\\ U(z) &=& 0, \\  W(z) &=& 0. \end{eqnarray*}


Discretization and the Newton's Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


We will use the implicit Euler method in time, i.e., 


.. math::

     \frac{\partial \varrho}{\partial t} \approx \frac{\varrho^{n+1} - \varrho^n}{\tau}

etc. Let's discuss one equation of :eq:`one` at a time:

`Continuity equation`:
The weak formulation of 

.. math::

     \frac{\varrho^{n+1} - \varrho^n}{\tau} + \frac{\partial U^{n+1}}{\partial x} + \frac{\partial W^{n+1}}{\partial z} = 0

reads


.. math::
    :label: cont

    F_i^{\varrho}(Y^{n+1}) = \int_{\Omega} \frac{\varrho^{n+1}}{\tau}
    \varphi^{\varrho}_i
    - \int_{\Omega} \frac{\varrho^{n}}{\tau} \varphi^{\varrho}_i 
      + \int_{\Omega} \frac{\partial U^{n+1}}{\partial x} \varphi^{\varrho}_i
        + \int_{\Omega} \frac{\partial W^{n+1}}{\partial z} \varphi^{\varrho}_i = 0


The global coefficient vector $Y^{n+1}$ consists of four parts $Y^{\varrho}$, $Y^{U}$, $Y^{W}$
and $Y^{\theta}$ corresponding to the fields $\varrho$, $U$, $W$ and $\theta$, respectively.
The same holds for the vector function $F$ which consists of four parts $F^{\varrho}$, $F^{U}$, $F^{W}$
and $F^{\theta}$. Thus the global Jacobi matrix will have a four-by-four block structure. We
denote 


.. math::
    :label: two

    \varrho^{n+1} = \sum_{k=1}^{N^{\varrho}} y^{\varrho}_k \varphi^{\varrho}_k, \ \
    \
    U^{n+1} = \sum_{k=1}^{N^{U}} y^{U}_k \varphi^{U}_k, \ \ \
    W^{n+1} = \sum_{k=1}^{N^{W}} y^{W}_k \varphi^{W}_k, \ \ \
    \theta^{n+1} = \sum_{k=1}^{N^{\theta}} y^{\theta}_k \varphi^{\theta}_k.


It follows from :eq:`cont` and :eq:`two` that


.. math::

     \frac{\partial F^{\varrho}_i}{\partial y^{\varrho}_j} = \int_{\Omega} \frac{\varphi^{\varrho}_j}{\tau} \varphi^{\varrho}_i, \ \ \ \frac{\partial F^{\varrho}_i}{\partial y^{U}_j} = \int_{\Omega} \frac{\partial \varphi^{U}_j}{\partial x} \varphi^{\varrho}_i, \ \ \ \frac{\partial F^{\varrho}_i}{\partial y^{W}_j} = \int_{\Omega} \frac{\partial \varphi^{W}_j}{\partial z} \varphi^{\varrho}_i, \ \ \ \frac{\partial F^{\varrho}_i}{\partial y^{W}_j} = 0.

`First momentum equation`: The second equation of :eq:`one` has the form 


.. math::

     \frac{\partial U}{\partial t} + \frac{2U}{\varrho}\frac{\partial U}{\partial x}  - \frac{U^2}{\varrho^2} \frac{\partial \varrho}{\partial x} + R\frac{\partial \theta}{\partial x} + \frac{W}{\varrho}\frac{\partial U}{\partial z} + \frac{U}{\varrho}\frac{\partial W}{\partial z} - \frac{UW}{\varrho^2}\frac{\partial \varrho}{\partial z} = 0.

After applying the implicit Euler method, we obtain 


.. math::

     \frac{\partial U^{n+1}}{\tau} - \frac{\partial U^{n}}{\tau} + \frac{2U^{n+1}}{\varrho^{n+1}}\frac{\partial U^{n+1}}{\partial x}  - \frac{(U^{n+1})^2}{(\varrho^{n+1})^2} \frac{\partial \varrho^{n+1}}{\partial x} + R\frac{\partial \theta^{n+1}}{\partial x}


.. math::

     + \frac{W^{n+1}}{\varrho^{n+1}}\frac{\partial U^{n+1}}{\partial z} + \frac{U^{n+1}}{\varrho^{n+1}}\frac{\partial W^{n+1}}{\partial z} - \frac{U^{n+1}W^{n+1}}{(\varrho^{n+1})^2}\frac{\partial \varrho^{n+1}}{\partial z} = 0.

Thus we obtain 

.. math::

     \frac{\partial F^{U}_i}{\partial y^{\varrho}_j} =  - \int_{\Omega}\frac{2U}{\varrho^2}\frac{\partial U}{\partial x} \varphi^{\varrho}_j \varphi^{U}_i  -  \int_{\Omega} U^2 \left[(-2)\frac{1}{\varrho^3}\frac{\partial \varrho}{\partial x} \varphi^{\varrho}_j  + \frac{1}{\varrho^2}\frac{\partial \varphi^{\varrho}_j}{\partial x}\right] \varphi^U_i


.. math::

     + \int_{\Omega} \frac{W}{\varrho^2}\frac{\partial U}{\partial z}(-1)\varphi^{\varrho}_j \varphi^U_i + \int_{\Omega} \frac{U}{\varrho^2}\frac{\partial W}{\partial z}(-1)\varphi^{\varrho}_j \varphi^U_i - \int_{\Omega} UW \left[(-2)\frac{1}{\varrho^3}\frac{\partial \varrho}{\partial z} \varphi^{\varrho}_j + \frac{1}{\varrho^2}\frac{\partial \varphi^{\varrho}_j}{\partial z} \right] \varphi^{U}_i.

Analogously,

.. math::

     \frac{\partial F^{U}_i}{\partial y^{U}_j} =  \int_{\Omega}\frac{\varphi^U_j}{\tau}\varphi^U_i + \int_{\Omega}\frac{2}{\varrho} \left[ \frac{\partial U}{\partial x}\varphi^U_j + U \frac{\partial \varphi^U_j}{\partial x} \right] \varphi^U_i - \int_{\Omega} \frac{2U}{\varrho^2}\frac{\partial \varrho}{\partial x} \varphi^U_j \varphi^U_i


.. math::

     + \int_{\Omega} \frac{W}{\varrho}\frac{\partial \varphi^U_j}{\partial z} \varphi^U_i  + \int_{\Omega} \frac{1}{\varrho}\frac{\partial W}{\partial z} \varphi^U_j \varphi^U_i  - \int_{\Omega} \frac{W}{\varrho^2}\frac{\partial \varrho}{\partial z} \varphi^U_j \varphi^U_i,


.. math::

     \frac{\partial F^{U}_i}{\partial y^{W}_j} =  \int_{\Omega} \frac{1}{\varrho}\frac{\partial U}{\partial z} \varphi^W_j \varphi^U_i + \int_{\Omega} \frac{U}{\varrho}\frac{\partial \varphi^W_j}{\partial z} \varphi^U_i - \int_{\Omega} \frac{U}{\varrho^2}\frac{\partial \varrho}{\partial z} \varphi^W_j \varphi^U_i,


.. math::

     \frac{\partial F^{U}_i}{\partial y^{\theta}_j} =  \int_{\Omega} R \frac{\partial \varphi^{\theta}_j}{\partial x} \varphi^U_i.


`Second momentum equation`: The third equation of :eq:`one` reads 


.. math::

     \frac{\partial W}{\partial t}  + \frac{W}{\varrho}\frac{\partial U}{\partial x} + \frac{U}{\varrho}\frac{\partial W}{\partial x} - \frac{UW}{\varrho^2}\frac{\partial \varrho}{\partial x}  + \frac{2W}{\varrho}\frac{\partial W}{\partial z}  - \frac{W^2}{\varrho^2} \frac{\partial \varrho}{\partial x} + R\frac{\partial \theta}{\partial z} + \varrho g= 0.

After applying the implicit Euler method, we obtain 


.. math::

     \frac{\partial W^{n+1}}{\tau} - \frac{\partial W^{n}}{\tau}  + \frac{W^{n+1}}{\varrho^{n+1}}\frac{\partial U^{n+1}}{\partial x} + \frac{U^{n+1}}{\varrho^{n+1}}\frac{\partial W^{n+1}}{\partial x} - \frac{U^{n+1}W^{n+1}}{(\varrho^{n+1})^2}\frac{\partial \varrho^{n+1}}{\partial x}


.. math::

     + \frac{2W^{n+1}}{\varrho^{n+1}}\frac{\partial W^{n+1}}{\partial z}  - \frac{(W^{n+1})^2}{(\varrho^{n+1})^2} \frac{\partial \varrho^{n+1}}{\partial x} + R\frac{\partial \theta^{n+1}}{\partial z} + \varrho^{n+1} g= 0.

Thus we obtain 

.. math::

     \frac{\partial F^{W}_i}{\partial y^{\varrho}_j} =  + \int_{\Omega} \frac{W}{\varrho^2}\frac{\partial U}{\partial x}(-1)\varphi^{\varrho}_j \varphi^W_i + \int_{\Omega} \frac{U}{\varrho^2}\frac{\partial W}{\partial x}(-1)\varphi^{\varrho}_j \varphi^W_i - \int_{\Omega}\frac{2W}{\varrho^2}\frac{\partial W}{\partial x} \varphi^{\varrho}_j \varphi^{W}_i


.. math::

     - \int_{\Omega} UW \left[(-2)\frac{1}{\varrho^3}\frac{\partial \varrho}{\partial x} \varphi^{\varrho}_j  + \frac{1}{\varrho^2}\frac{\partial \varphi^{\varrho}_j}{\partial x} \right] \varphi^{W}_i -  \int_{\Omega} W^2 \left[(-2)\frac{1}{\varrho^3}\frac{\partial \varrho}{\partial z} \varphi^{\varrho}_j  + \frac{1}{\varrho^2}\frac{\partial \varphi^{\varrho}_j}{\partial z}\right] \varphi^W_i  + \int_{\Omega}g \varphi^{\varrho}_j \varphi^{W}_i.

Analogously,

.. math::

     \frac{\partial F^{W}_i}{\partial y^{U}_j} =  \int_{\Omega} \frac{W}{\varrho}\frac{\partial \varphi^U_j}{\partial x} \varphi^W_i + \int_{\Omega} \frac{1}{\varrho}\frac{\partial W}{\partial x} \varphi^U_j \varphi^W_i - \int_{\Omega} \frac{W}{\varrho^2}\frac{\partial \varrho}{\partial x} \varphi^U_j \varphi^W_i,


.. math::

     \frac{\partial F^{W}_i}{\partial y^{W}_j} =  \int_{\Omega}\frac{\varphi^W_j}{\tau}\varphi^W_i + \int_{\Omega} \frac{1}{\varrho}\frac{\partial U}{\partial x} \varphi^W_j \varphi^W_i  + \int_{\Omega} \frac{U}{\varrho}\frac{\partial \varphi^W_j}{\partial x} \varphi^W_i  - \int_{\Omega} \frac{U}{\varrho^2}\frac{\partial \varrho}{\partial x} \varphi^W_j \varphi^W_i


.. math::

     + \int_{\Omega}\frac{2}{\varrho} \left[ \frac{\partial W}{\partial z}\varphi^W_j + W \frac{\partial \varphi^W_j}{\partial z} \right] \varphi^W_i  - \int_{\Omega} \frac{2W}{\varrho^2}\frac{\partial \varrho}{\partial z} \varphi^W_j \varphi^W_i,


.. math::

     \frac{\partial F^{W}_i}{\partial y^{\theta}_j} =  \int_{\Omega} R \frac{\partial \varphi^{\theta}_j}{\partial z} \varphi^W_i.


`Internal energy equation`: The last equation of :eq:`one` has the form


.. math::

     \frac{\partial \theta}{\partial t} + \mbox{div}(\theta {\bf v}) + \frac{R
     \theta}{c_v} \mbox{div}{\bf v} = 0
 
where $\theta = \varrho T$. This can be written equivalently as


.. math::

     \frac{\partial \theta}{\partial t} + \nabla \theta \cdot {\bf v} + \gamma
     \theta \mbox{div} {\bf v} = 0.

Written in terms of single derivatives, this is 

.. math::

     \frac{\partial \theta}{\partial t} + \frac{\partial \theta}{\partial x} \frac{U}{\varrho} + \frac{\partial \theta}{\partial z} \frac{W}{\varrho}  + \gamma \theta \frac{\partial}{\partial x}\left(\frac{U}{\varrho}  \right) + \gamma \theta \frac{\partial}{\partial z}\left(\frac{W}{\varrho}  \right) = 0,

i.e.,

.. math::

     \frac{\partial \theta}{\partial t}  + \frac{\partial \theta}{\partial x} \frac{U}{\varrho} + \frac{\partial \theta}{\partial z} \frac{W}{\varrho}  + \gamma \frac{\theta}{\varrho} \frac{\partial U}{\partial x} - \gamma \frac{\theta U}{\varrho^2}\frac{\partial \varrho}{\partial x} + \gamma \frac{\theta}{\varrho} \frac{\partial W}{\partial z} - \gamma \frac{\theta W}{\varrho^2}\frac{\partial \varrho}{\partial z} = 0.






`Weak formulation`:


.. math::

     F^{\theta}_i(Y) =  \int_{\Omega} \frac{\theta^{n+1}}{\tau} \varphi^{\theta}_i - \int_{\Omega} \frac{\theta^{n}}{\tau} \varphi^{\theta}_i + \int_{\Omega} \frac{\partial \theta^{n+1}}{\partial x} \frac{U^{n+1}}{\varrho^{n+1}}\varphi^{\theta}_i + \int_{\Omega} \frac{\partial \theta^{n+1}}{\partial z} \frac{W^{n+1}}{\varrho^{n+1}} \varphi^{\theta}_i


.. math::

     + \int_{\Omega} \gamma \frac{\theta^{n+1}}{\varrho^{n+1}} \frac{\partial U^{n+1}}{\partial x}\varphi^{\theta}_i - \int_{\Omega} \gamma \frac{\theta^{n+1} U^{n+1}}{(\varrho^{n+1})^2}\frac{\partial \varrho^{n+1}}{\partial x}\varphi^{\theta}_i + \int_{\Omega} \gamma \frac{\theta^{n+1}}{\varrho^{n+1}} \frac{\partial W^{n+1}}{\partial z}\varphi^{\theta}_i -\int_{\Omega}  \gamma \frac{\theta^{n+1} W^{n+1}}{(\varrho^{n+1})^2}\frac{\partial \varrho^{n+1}}{\partial z} \varphi^{\theta}_i= 0.

For the derivatives of the weak form we obtain:

.. math::

     \frac{\partial F^{\theta}_i}{\partial y^{\varrho}_j} =  - \int_{\Omega} \frac{\partial \theta}{\partial x} \frac{U}{\varrho^2}\varphi^{\varrho}_j\varphi^{\theta}_i - \int_{\Omega} \frac{\partial \theta}{\partial z} \frac{W}{\varrho^2}\varphi^{\varrho}_j\varphi^{\theta}_i - \int_{\Omega} \gamma \frac{\theta}{\varrho^2} \frac{\partial U}{\partial x}\varphi^{\varrho}_j\varphi^{\theta}_i - \int_{\Omega} \gamma \frac{\theta}{\varrho^2} \frac{\partial W}{\partial z}\varphi^{\varrho}_j\varphi^{\theta}_i


.. math::

     + \int_{\Omega} 2\gamma \frac{\theta U}{\varrho^3}\frac{\partial \varrho}{\partial x}\varphi^{\varrho}_j\varphi^{\theta}_i - \int_{\Omega} \gamma \frac{\theta U}{\varrho^2}\frac{\varphi^{\varrho}_j}{\partial x}\varphi^{\theta}_i + \int_{\Omega} 2\gamma \frac{\theta W}{\varrho^3}\frac{\partial \varrho}{\partial z}\varphi^{\varrho}_j\varphi^{\theta}_i - \int_{\Omega} \gamma \frac{\theta W}{\varrho^2}\frac{\varphi^{\varrho}_j}{\partial z}\varphi^{\theta}_i.


.. math::

     \frac{\partial F^{\theta}_i}{\partial y^{U}_j} =  \int_{\Omega} \frac{\partial \theta}{\partial x} \frac{1}{\varrho} \varphi^{U}_j\varphi^{\theta}_i + \int_{\Omega} \gamma \frac{\theta}{\varrho}\frac{\varphi^{U}_j}{\partial x}\varphi^{\theta}_i - \int_{\Omega} \gamma \frac{\theta}{\varrho^2}\frac{\partial \varrho}{\partial x}\varphi^{U}_j\varphi^{\theta}_i.


.. math::

     \frac{\partial F^{\theta}_i}{\partial y^{W}_j} =  \int_{\Omega} \frac{\partial \theta}{\partial z} \frac{1}{\varrho} \varphi^{W}_j\varphi^{\theta}_i + \int_{\Omega} \gamma \frac{\theta}{\varrho}\frac{\varphi^{W}_j}{\partial z}\varphi^{\theta}_i - \int_{\Omega} \gamma \frac{\theta}{\varrho^2}\frac{\partial \varrho}{\partial z}\varphi^{W}_j\varphi^{\theta}_i.


.. math::

     \frac{\partial F^{\theta}_i}{\partial y^{\theta}_j} =  \int_{\Omega} \frac{1}{\tau} \varphi^{\theta}_j\varphi^{\theta}_i + \int_{\Omega} \frac{U}{\varrho}\frac{\varphi^{\theta}_j}{\partial x}\varphi^{\theta}_i + \int_{\Omega} \frac{W}{\varrho}\frac{\varphi^{\theta}_j}{\partial z}\varphi^{\theta}_i


.. math::

     + \int_{\Omega} \frac{\gamma}{\varrho} \frac{\partial U}{\partial x} \varphi^{\theta}_j\varphi^{\theta}_i + \int_{\Omega} \frac{\gamma}{\varrho} \frac{\partial W}{\partial z} \varphi^{\theta}_j\varphi^{\theta}_i - \int_{\Omega} \frac{\gamma U}{\varrho^2} \frac{\partial \varrho}{\partial x} \varphi^{\theta}_j\varphi^{\theta}_i - \int_{\Omega} \frac{\gamma W}{\varrho^2} \frac{\partial \varrho}{\partial z} \varphi^{\theta}_j\varphi^{\theta}_i.
