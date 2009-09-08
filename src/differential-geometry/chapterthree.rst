Fluid Dynamics
==============


Stress-Energy Tensor
--------------------


In general, the stress energy tensor is the flux of momentum $p^\mu$ over the
surface $x^\nu$. The Navier-Stokes equations can be derived from the
conservation law:

.. math::

    \partial_\nu T^{\mu\nu} + f^\mu = 0


Navier-Stokes Equations
-----------------------

When we write the above conservation law in a nonrelativistic limit, we get the
Cauchy momentum equation:

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

or in vector form:

.. math::

    \nabla \cdot \mathds{T} =\mu\nabla^2{\bf v}+(\mu+\lambda)\nabla \nabla\cdot{\bf v}

For incompressible fluid we have $\nabla\cdot\bf v=0$, so we get:

.. math::

    \nabla \cdot \mathds{T} =\mu\nabla^2{\bf v}

and for a perfect fluid we have no viscosity, e.g. $\mu=0$, so:

.. math::

    \nabla \cdot \mathds{T}=0

and the equations are then called Euler equations (for perfect fluid).

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
