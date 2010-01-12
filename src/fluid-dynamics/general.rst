.. index:: fluid dynamics

Fluid Dynamics
==============

.. index::
    pair: stress-energy; tensor

Stress-Energy Tensor
--------------------


In general, the stress energy tensor is the flux of momentum $p^\mu$ over the
surface $x^\nu$. It is a machine that contains a knowledge of the energy
density, momentum density and stress as measured by any observer of the event.

Imagine a (small) box in the spacetime. Then the observer with a 4-velocity
$u^\mu$ measures the density of 4-momentum $\d p^\alpha\over\d V$
in his frame as:

.. math::

    {\d p^\alpha\over\d V} = -T^\alpha{}_\beta u^\beta

and the energy density that he measures is:

.. math::

    \rho = {E\over V} = -{u^\alpha p_\alpha \over V}
    = - u^\alpha {\d p_\alpha\over\d V}
    = u^\alpha T_{\alpha\beta} u^\beta

One can also obtain the stress energy tensor from the Lagrangian
$\L=\L(\eta_\rho, \partial_\nu \eta_\rho, x^\nu)$ by combining the
Euler-Lagrange equations

.. math::

    { \partial \L\over\partial \eta_\rho}
        -
        \partial_\nu\left(
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \right)
    =0

with the total derivative ${\d \L\over \d x^\mu}$:

.. math::

    {\d \L\over \d x^\mu} = {\partial\L\over\partial\eta_\rho}
        \partial_\mu \eta_\rho
        +
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \partial_\mu\partial_\nu\eta_\rho + \partial_\mu\L
    =

    =
        \partial_\nu\left(
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \right)
        \partial_\mu \eta_\rho
        +
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \partial_\nu\partial_\mu\eta_\rho + \partial_\mu\L
    =

    =
        \partial_\nu\left(
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \partial_\mu \eta_\rho
        \right)
        + \partial_\mu\L

or

.. math::

        \partial_\nu\left(
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \partial_\mu \eta_\rho
        -\L \delta_\mu{}^\nu
        \right)
        + \partial_\mu\L
          =0

This can be written as:

.. math::

    \partial_\nu T_\mu{}^\nu + f_\mu = 0

where

.. math::

    T_\mu{}^\nu =
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \partial_\mu \eta_\rho
        -\L \delta_\mu{}^\nu

    f_\mu = \partial_\mu\L

The Navier-Stokes equations can be derived from the
conservation law:

.. math::

    \partial_\nu T^{\mu\nu} + f^\mu = 0

To obtain some Lagrangian (and action) for the perfect fluid, so that we can
derive the stress energy tensor $T^{\mu\nu}$ from that, is not trivial, see for
example `arXiv:gr-qc/9304026 <http://arxiv.org/abs/gr-qc/9304026>`_. One has to
take into account the equation of state and incorporate the particle number
conservation $\nabla_\mu(nu^\mu)=0$ and no entropy exchange
$\nabla_\mu(nsu^\mu)=0$ constraints.

Perfect Fluids
~~~~~~~~~~~~~~

Perfect fluids have no heat conduction ($T^{i0} = T^{0i} = 0$) and no
viscosity ($T^{ij} = p\one$), so in the MCRF:

.. math::

    T^{\alpha\beta} = \diag(\rho c^2, p, p, p) =
    \left(\rho+{p\over c^2}\right)u^\alpha u^\beta + p g^{\alpha\beta}

where in MCRF we have $g^{\mu\nu} = \diag(-1, 1, 1, 1)$, $u^0=c$ and $u^i=0$,
but $\partial_\alpha U^i\neq0$. $p$ is the pressure with units
$[p] =\rm N\,m^{-2}=kg\,m^{-1}\,s^{-2}$ (then
$[{p\over c^2}] =\rm kg\,m^{-3}$), $\rho$ is the rest mass density with units
$[\rho] =\rm kg\,m^{-3}$, and $\rho c^2$ is the energy density with units
$[\rho c^2] =\rm kg\,m^{-1}\,s^{-2}$.

The last equation is a tensor equation so it
holds in any frame. The nonrelativistic limit of this stress energy tensor is
obtained by approximating $u^0\approx c$ and $u^j$ by the nonrelativistic
velocity (and we can also neglect ${p\over c^2}$ compared to $\rho$):

.. math::

    T^{00} = \left(\rho+{p\over c^2}\right)u^0u^0 - p \approx \rho c^2+p-p
        \approx \rho c^2

    T^{0j} = T^{j0} = \left(\rho+{p\over c^2}\right)u^0u^j \approx
        \left(\rho + {p\over c^2}\right) c u^j
        \approx
        \rho c u^j

    T^{jk} = \left(\rho+{p\over c^2}\right) u^ju^k + p \delta^{jk}
        \approx \rho u^j u^k + p \delta^{jk}

Substituting this into the conversation law $\partial_\beta
T^{\alpha\beta}=0$ we get for $\alpha=0$:

.. math::

    \partial_\beta T^{0\beta} = 0

    \partial_0 T^{00} + \partial_i T^{0i} = 0

    \partial_0 (\rho c^2) + \partial_i (\rho c u^i) = 0

    \partial_t\rho + \partial_i(\rho u^i) = 0

    {\partial \rho\over\partial t} + \nabla \cdot (\rho {\bf u}) = 0

This is the continuity equation for the energy ($\rho$ here is the energy
density). For $\alpha=i$ we get:

.. math::

    \partial_\beta T^{i\beta} = 0

    \partial_0 T^{i0} + \partial_j T^{ij} = 0

    \partial_0 (\rho c u^i) + \partial_j (\rho u^i u^j + p\delta^{ij}) = 0

    \partial_t (\rho u^i) + \partial_j (\rho u^i u^j + p\delta^{ij}) = 0

    {\partial (\rho{\bf u})\over\partial t} + \nabla \cdot
        (\rho {\bf u}{\bf u}^T) + \nabla p = 0

Which are the Euler equations, sometimes also written as (using the continuity
equation):

.. math::

    \rho\partial_t u^i + \rho u^j\partial_j u^i + \delta^{ij}\partial_j p = 0

The equation of continuity follows from the
conservation of the baryon number --- the volume $V$ that contains certain
number of baryons can change, but the total number of baryons $nV$ must remain
constant:

.. math::

    {\d (nV)\over\d\tau} = 0

    {\d n\over\d\tau}V + n{\d V\over\d\tau} = 0

    u^\alpha (\partial_\alpha n)V + n(\partial_\alpha u^\alpha) V = 0

    \partial_\alpha (n u^\alpha) = 0

and in the limit $c\to\infty$:

.. math::

    {\partial n\over \partial t} + \nabla\cdot(n{\bf v}) = 0


Navier-Stokes Equations
-----------------------

When we write the relativistic conservation law in a nonrelativistic limit (for
a general fluid), we get the Cauchy momentum equation:

.. math::

    \rho\left({\partial {\bf v}\over\partial t} +{\bf v}\cdot\nabla{\bf v} \right) = \nabla \cdot \mathds{\sigma} + {\bf f}

where the stress tensor $\sigma$ can be written as:

.. math::

    \sigma=-p\mathds{1} + \mathds{T}

and we get the Navier-Stokes equations:

.. math::

    \rho\left({\partial {\bf v}\over\partial t} +{\bf v}\cdot\nabla{\bf v} \right) = -\nabla p + \nabla \cdot \mathds{T} + {\bf f}

Those are the most general equations. If we assume some more things about the
fluid, they can be further simplified.

For Newtonean fluids, we want $\mathds{T}$ to be isotropic, linear in strain
rates and it's divergence zero for fluid at rest. It follows that the only way
to write the tensor under these conditions is:

.. math::

    T_{ij} = 2\mu\epsilon_{ij} + \delta_{ij} \lambda \nabla\cdot{\bf v}

where the strain rate is:

.. math::

    \epsilon_{ij}={1\over 2}\left(\partial_j v_i+\partial_i v_j\right)

The divergence of the tensor is:

.. math::

    \partial_j T_{ij} =2\mu\partial_j\epsilon_{ij} + \partial_j\delta_{ij} \lambda \nabla\cdot{\bf v} =\mu\partial_j\partial_j v_i+\mu\partial_i \nabla\cdot{\bf v} + \lambda \partial_i  \nabla\cdot{\bf v} =\mu\partial_j\partial_j v_i+(\mu+\lambda)\partial_i \nabla\cdot{\bf v}

or in vector form (these are usually called the compressible Navier-Stokes
equations):

.. math::

    \nabla \cdot \mathds{T} =\mu\nabla^2{\bf v}+(\mu+\lambda)\nabla \nabla\cdot{\bf v}

For incompressible fluid we have $\nabla\cdot\bf v=0$, so we get the
incompressible Navier-Stokes equations:

.. math::

    \nabla \cdot \mathds{T} =\mu\nabla^2{\bf v}

and for a perfect fluid we have no viscosity, e.g. $\mu=0$, then we get the
Euler equations (for perfect fluid):

.. math::

    \nabla \cdot \mathds{T}=0

Energy Equation
~~~~~~~~~~~~~~~

We have the following two Euler equations:

.. math::

    \partial_t\rho + \partial_i(\rho u^i) = 0

    \rho\partial_t u^i + \rho u^j\partial_j u^i + \delta^{ij}\partial_j p = 0

We'll need the following formulas:

.. math::

    \partial_t (u_i u^i) = (\partial_t u_i) u^i + u_i \partial_t u^i =
    (\partial_t u_i)\delta^{ij} u_j + u_i \partial_t u^i =

    = (\partial_t u_i\delta^{ij}) u_j + u_i \partial_t u^i =
    (\partial_t u^j) u_j + u_i \partial_t u^i =
    2 u_i \partial_t u^i

    \partial_j (u_i u^i) = 2 u_i \partial_j u^i

    \partial_t\rho =- \partial_i(\rho u^i)

    \partial_t u^i =- u^j\partial_j u^i - {\delta^{ij}\over\rho}\partial_j p

    - u^j\partial_j p + \partial_t(\rho U) =

      = - {\d p \over\d t} +\partial_t p + \partial_t(\rho U) =

      = - {\d p \over\d t} +\partial_t (\rho U + p) =

      = - {\d p \over\d t} +{\d\over\d t} (\rho U + p)
        -u^j\partial_j (\rho U + p)=

      = - {\d p \over\d t} +{\d\rho\over\d t} \left(U + {p\over\rho}\right)
        +\rho{\d\over\d t} \left(U + {p\over\rho}\right)
        -u^j\partial_j (\rho U + p)=

      = - {\d p \over\d t} +{\d\rho\over\d t} \left(U + {p\over\rho}\right)
        +\rho{\d\over\d t} \left(U + {p\over\rho}\right)
        + (\rho U + p)\partial_j u^j
        -\partial_j (\rho U u^j + p u^j) =

      = \left[\rho {\d\over\d t}\left(U + {p\over\rho}\right) - {\d p\over\d t}
        \right]
        +
        \left(U + {p\over\rho}\right)\left[ {\d\rho\over\d t} + \rho
            \partial_j u^j \right]
        -\partial_j (\rho U u^j + p u^j) =

      = - \partial_j(\rho U u^j + p u^j)

      0 = \d Q = T\d S = \d U + p\d V = \d (U + pV) - V\d p
        = \d\left(U+{p\over\rho}\right) - {1\over \rho}\d p
        = \d H - {1\over \rho}\d p

where $V = {1\over\rho}$ is the specific volume and
$H = U+{p\over\rho}$ is entalphy (heat content).

Then:

.. math::

    \partial_t E =

    = \partial_t (\half \rho u_i u^i + \rho U) =

    = \half u_i u^i \partial_t \rho
        +\half\rho\partial_t(u_i u^i) + \partial_t(\rho U) =

    = -\half u_i u^i \partial_j(\rho u^j)
        +\rho u_i\partial_t u^i + \partial_t(\rho U) =

    = -\half u_i u^i \partial_j(\rho u^j)
        - \rho u_i u^j\partial_j u^i - u_i\delta^{ij}\partial_j p
        + \partial_t(\rho U) =

    = -\half u_i u^i \partial_j(\rho u^j)
        - \half\rho u^j\partial_j (u_i u^i) - u_i\delta^{ij}\partial_j p
        + \partial_t(\rho U) =

    = -\half\partial_j(\rho u_i u^i u^j)
        - u^j\partial_j p + \partial_t(\rho U) =

    = -\half\partial_j(\rho u_i u^i u^j)
        - \partial_j(\rho U u^j + p u^j) =

    = -\partial_j\left(u^j\left(\half\rho u_i u^i+\rho U + p \right)\right) =

    = -\partial_j\left(u^j\left(E + p \right)\right)

so:

.. math::

    \partial_t E + \partial_j\left(u^j\left(E + p \right)\right) = 0

    {\partial E\over\partial t}
        + \nabla\cdot\left({\bf u}\left(E + p \right)\right) = 0


Relativistic Derivation of the Energy Equation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section is only approximate, it roughly gets the right equations, but some
small things still have to be improved.

We have to write $T = \diag(\rho c^2 + \rho U, p, p, p)$, where $U$ is the
classical internal energy per unit mass and $\rho$ is the rest
mass density (so $\rho c^2$ is the energy density, excluding the internal
energy, that is taken care of by the $\rho U$ term):

.. math::

    T^{\alpha\beta} = \diag(\rho c^2 +\rho U, p, p, p) =
    \left(\rho+{\rho U + p\over c^2}\right)u^\alpha u^\beta + p g^{\alpha\beta}

Then we write things explicitly using $u^0=\gamma c$ and $u^i = \gamma v^i$:

.. math::

    T^{00} =
    \left(\rho+{\rho U +p\over c^2}\right)u^0u^0 - p
    =
    \left(\rho+{\rho U +p\over c^2}\right)\gamma^2 c^2 - p
    =
    \rho c^2 \gamma^2 +(\rho U +p)\gamma^2 - p

    T^{0j} = T^{j0} =
        \left(\rho+{\rho U +p\over c^2}\right)u^0u^j =
        \left(\rho+{\rho U +p\over c^2}\right)\gamma^2 c v^j =
        \rho c v^j \gamma^2 + {1\over c} (\rho U + p) v^j \gamma^2

    T^{jk} =
        \left(\rho+{\rho U +p\over c^2}\right) u^ju^k + p \delta^{jk} =
        \left(\rho+{\rho U +p\over c^2}\right) \gamma^2 v^jv^k
            + p \delta^{jk} =
        \rho v^j v^k \gamma^2 + {1\over c^2}(\rho U +p) \gamma^2 v^jv^k
            + p \delta^{jk}

And we write for $\alpha=0$:

.. math::

    \partial_\beta T^{0\beta} = 0

    \partial_0 T^{00} + \partial_i T^{0i} = 0

    \partial_0 \left(\rho c^2 \gamma^2 +(\rho U +p)\gamma^2 - p\right)
        + \partial_i \left( \rho c v^i \gamma^2 + {1\over c} (\rho U + p) v^i
          \gamma^2 \right) = 0

    \partial_t \left(\rho c \gamma^2 +{1\over c}(\rho U +p)\gamma^2 -
        {1\over c}p\right)
        + \partial_i \left( \rho c v^i \gamma^2 + {1\over c} (\rho U + p) v^i
          \gamma^2 \right) = 0

.. math::
    :label: euler5

    \partial_t (\rho c^2 \gamma^2) + \partial_i ( \rho c^2 v^i \gamma^2) +
    \partial_t (\rho U \gamma^2 + p\gamma^2 - p) +
    \partial_i \left((\rho U + p) v^i\gamma^2\right)
    = 0

Now we use the approximation $c^2\gamma^2\approx c^2 + v^2$ and
$\gamma\approx1$:

.. math::

    \partial_t \left(\rho c^2 +\rho v^2 \right) + \partial_i \left(
        (\rho c^2 +\rho v^2) v^i\right) +
    \partial_t (\rho U) +
    \partial_i \left((\rho U + p) v^i\right)
    = 0

    c^2 \left[\partial_t \rho + \partial_i \left( \rho v^i\right) \right]
    +
    \partial_t (\rho v^2+\rho U) +
    \partial_i \left((\rho v^2+\rho U + p) v^i\right)
    = 0

The first term vanishes (it is the continuity equation) and thus we get the
equation for the energy $E =\half\rho v^2+\rho U$, except that we don't have
the $\half$ in there.

.. math::

    \partial_t (\half\rho v^2+\rho U) +
    \partial_i \left((\half\rho v^2+\rho U + p) v^i\right)
    = 0

    \partial_t E + \partial_i \left((E + p) v^i\right) = 0

We can also write the equation :eq:`euler5` as (here we use $T=
\diag(\rho c^2, p, p, p)$:

.. math::

    \partial_t \left(\left(\rho c^2 + p\left(1-{1\over\gamma^2}
        \right)\right)\gamma^2\right)
    +
    \partial_i\left(\left(\rho c^2 + p\right)v^i \gamma^2\right)
    =0

    \partial_t \left(\left(\rho c^2 + p{v^2\over c^2}\right)\gamma^2\right)
    +
    \partial_i\left(\left(\rho c^2 + p\right)v^i \gamma^2\right)
    =0

which becomes for large $c$:

.. math::

    \partial_t \left(\rho c^2\right)
    +
    \partial_i\left(\left(\rho c^2 + p\right)v^i\right)
    =0

and that can be interpreted either as $E=\rho c^2$:

.. math::
    :label: euler8

    \partial_t E
    +
    \partial_i\left(\left(E + p\right)v^i\right)
    =0

or as:

.. math::

    \partial_t \rho
    +
    \partial_i\left(\left(\rho + {p\over c^2}\right)v^i\right)
    =0

which reduces to:

.. math::
    :label: euler9

    \partial_t \rho
    +
    \partial_i\left(\rho v^i\right)
    =0

But both equations :eq:`euler8` and :eq:`euler9` are equivalent, because $E$ is
much larger than $p$ in :eq:`euler8`, so $p$ can be negleted. In order to get
the equation we want, we need to get rid of the rest mass $mc^2$ energy first
(as we roughly did in the treatment in :eq:`euler5`),
and only the rest is comparable with $p$.

For $\alpha=i$ we get:

.. math::

    \partial_\beta T^{i\beta} = 0

    \partial_0 T^{i0} + \partial_j T^{ij} = 0

    \cdots

and those are the Euler equations in the limit.


Bernoulli's Principle
---------------------


Bernoulli's principle works for a perfect fluid, so we take the Euler equations:

.. math::

    \rho\left({\partial {\bf v}\over\partial t} +{\bf v}\cdot\nabla{\bf v} \right) = -\nabla p + {\bf f}

and put it into a vertical gravitational field ${\bf f} = (0, 0, -\rho g)=-\rho
g\nabla z$, so:

.. math::

    \rho\left({\partial {\bf v}\over\partial t} +{\bf v}\cdot\nabla{\bf v} \right) = -\nabla p - \rho g\nabla z

we divide by $\rho$:

.. math::

    {\partial {\bf v}\over\partial t} +{\bf v}\cdot\nabla{\bf v} = -\nabla \left({p\over\rho} + g z\right)

and use the identity ${\bf v}\cdot\nabla{\bf v}={1\over 2}\nabla v^2
+ (\nabla \times {\bf v})\times{\bf v}$:

.. math::

    {\partial {\bf v}\over\partial t} +{1\over 2}\nabla v^2+(\nabla \times {\bf v})\times{\bf v} +\nabla \left({p\over\rho} + g z\right)=0

so:

.. math::

    {\partial {\bf v}\over\partial t} +(\nabla \times {\bf v})\times{\bf v} +\nabla \left({v^2\over 2} + gz + {p\over\rho} \right)=0

If the fluid is moving, we integrate this along a streamline from the point $A$
to $B$:

.. math::

    \int {\partial {\bf v}\over\partial t} \cdot \d {\bf l} +\left[{v^2\over 2} + gz + {p\over\rho} \right]_A^B=0

So far we didn't do any approximation (besides having a perfect fluid in a
vertical gravitation field).
Now we assume a steady flow, so ${\partial {\bf
v}\over\partial t}=0$ and since points $A$ and $B$ are arbitrary, we get:

.. math::

    {v^2\over 2} + gz + {p\over\rho}={\rm const.}

along the streamline. This is called the Bernoulli's principle.
If the fluid is not moving, we set ${\bf v}=0$ in the equations above and
immediately get:

.. math::

    {v^2\over 2} + gz + {p\over\rho}={\rm const.}

The last equation then holds everywhere in the (nonmoving) fluid (as opposed to
the previous equation that only holds along the streamline).


Hydrostatic Pressure
~~~~~~~~~~~~~~~~~~~~

Let $p_1$ be the pressure on the water surface and $p_2$ the pressure $h$
meters below the surface. From the Bernoulli's principle:

.. math::

    {p_1\over\rho} = g\cdot (-h) + {p_2\over \rho}

so

.. math::

    p_1 + h\rho g = p_2

and we can see, that the pressure $h$ meters below the surface is $h\rho g$
plus the (atmospheric) pressure $p_1$ on the surface.

Torricelli's Law
~~~~~~~~~~~~~~~~

We want to find the speed $v$ of the water flowing out of the tank (of the
height $h$) through a small hole at the bottom. The (atmospheric) pressure at
the water surface and also near the small hole is $p_1$. From the Bernoulli's
principle:

.. math::

    {p_1\over\rho} = {v^2\over 2} + g\cdot (-h) + {p_1\over \rho}

so:

.. math::

    v=\sqrt{2g h}

This is called the Torricelli's law.

Venturi Effect
~~~~~~~~~~~~~~

A pipe with a cross section $A_1$, pressure $p_1$ and the speed of a
perfect liquid $v_1$ changes it's cross section to $A_2$, so the pressure
changes to $p_2$ and the speed to $v_2$. Given $\Delta p = p_1-p_2$, $A_1$ and
$A_2$, calculate $v_1$ and $v_2$.

We use the continuity equation:

.. math::

    A_1 v_1 = A_2 v_2

and the Bernoulli's principle:

.. math::

    {v_1^2\over 2} + {p_1\over\rho} = {v_2^2\over 2} + {p_2\over\rho}

so we have two equations for two unknowns $v_1$ and $v_2$, after solving it we
get:

.. math::

    v_1 = A_2\sqrt{2\Delta p\over \rho(A_1^2-A_2^2)}


.. math::

    v_2 = A_1\sqrt{2\Delta p\over \rho(A_1^2-A_2^2)}

.. index::
    pair: Hagen-Poiseuille; Law

Hagen-Poiseuille Law
~~~~~~~~~~~~~~~~~~~~

We assume incompressible (but viscuous) Newtonean fluid (in no external force
field):

.. math::

    \rho\left({\partial {\bf v}\over\partial t} +{\bf v}\cdot\nabla{\bf v} \right) = -\nabla p + \mu\nabla^2{\bf v}

flowing in the vertical pipe of radius $R$ and we further assume steady flow
${\partial {\bf v}\over\partial t}=0$, axis symmetry
$v_r=v_\theta=\partial_\theta(\cdots)=0$ and a fully developed flow $\partial_z
v_z=0$. We write the Navier-Stokes equations above in the cylindrical
coordinates and using the stated assumptions, the only nonzero equations are:

.. math::

    0=-\partial_r p


.. math::

    0=-\partial_z p+\mu{1\over r}\partial_r(r\partial_r v_z)

from the first one we can see the $p=p(z)$ is a function of $z$ only and we can
solve the second one for $v_z=v_z(r)$:

.. math::

    v_z(r) = {1\over 4\mu}(\partial_z p) r^2 + C_1\log r + C_2

We want $v_z(r=0)$ to be finite, so $C_1=0$, next we assume the no slip
boundary conditions $v_z(r=R)=0$, so $C_2 = -{1\over 4\mu}(\partial_z p) R^2$
and we get the parabolic velocity profile:

.. math::

    v_z(r) = {1\over 4\mu}(-\partial_z p) (R^2-r^2)

Assuming that the pressure decreases linearly across the length of the pipe, we
have $-\partial_z p = {\Delta P\over L}$ and we get:

.. math::

    v_z(r) = {\Delta P\over 4\mu L}(R^2-r^2)

We can now calculate the volumetric flow rate:

.. math::

    Q = {\d V\over\d t} ={\d\over \d t}\int z\, \d S =\int {\d z\over \d t} \d S =\int v_z \,\d S =\int_0^{2\pi}\int_0^R v_z\, r\, \d r\,\d\phi =


.. math::

     ={\Delta P\pi\over 2\mu L}\int_0^R (R^2-r^2) r\, \d r ={\Delta P \pi R^4\over 8 \mu L}

so we can see that it depends on the 4th power of $R$. This is called the
Hagen-Poiseuille law.
