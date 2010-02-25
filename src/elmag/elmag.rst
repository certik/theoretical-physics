Maxwell's equations
===================

xxx

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

And we have five equations that relate them. Drift-diffusion equations:

.. math::
    :label: drift

    {\bf J}_n = q\mu_n n {\bf E} + q D_n \nabla n

    {\bf J}_p = q\mu_p p {\bf E} - q D_p \nabla p

where $\mu_n$, $\mu_p$, $D_n$, $D_p$ are the carrier mobilities and
diffusivities, $q$ is the electron charge (positive).
Continuity equations:

.. math::
    :label: continuity

    {\partial n\over\partial t} = -q R + {1\over q} \nabla\cdot {\bf J}_n

    {\partial p\over\partial t} = -q R - {1\over q} \nabla\cdot {\bf J}_p

where $R$ is the recombination rate.
And the Gauss's law:

.. math::
    :label: gauss

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n + N_c)

Equations
---------

Combining :eq:`drift` and :eq:`continuity` we get the following three
equations for three unknowns $n$, $p$ and ${\bf E}$:

.. math::

    {\partial n\over\partial t} = -q R + \nabla\cdot (\mu_n n {\bf E}
        +D_n \nabla n)

    {\partial p\over\partial t} = -q R - \nabla\cdot (\mu_p p {\bf E}
        -D_p \nabla p)

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n + N_c)

Example
~~~~~~~

As a simple model, assume $D_n$, $D_p$, $\mu_n$, $\mu_p$ and $\varepsilon$
are position independent and $N_c=0$, $R=0$:

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
