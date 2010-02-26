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
doping concetration and $q$ is the electron charge (positive). We get:

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
generated using ${\bf E}$ and $n$ and $p$. A general model gives the
current density relations:

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

    {\partial n\over\partial t} = -R + \nabla\cdot (\mu_n n {\bf E}
        +D_n \nabla n)

    {\partial p\over\partial t} = -R - \nabla\cdot (\mu_p p {\bf E}
        -D_p \nabla p)

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n + C)


Example 1
~~~~~~~~~

We can substract the first two
equations and we get:

.. math::

    {\partial q(p-n)\over\partial t} = - \nabla\cdot (q(\mu_p p+\mu_n n) {\bf E}
        -q\nabla (D_p p-D_n n))

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n)

and using $\rho=q(p-n)$ and $\sigma=q(\mu_p p+\mu_n n)$, we get:

.. math::

    {\partial \rho\over\partial t} = - \nabla\cdot (\sigma {\bf E}
        -q\nabla (D_p p-D_n n))

    \nabla\cdot(\varepsilon {\bf E}) = \rho

Assuming $\nabla (D_p p-D_n n)=0$ and that $\rho$ doesn't depend on time, we
get:

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
