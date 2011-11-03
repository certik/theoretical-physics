.. index:: Newtonian physics, classical mechanics

Classical Mechanics
===================

Moment of Inertia
-----------------

Total angular momentum for a rigid body rotating around
the $\bomega$ axis is:

.. math::

    {\bf L}
        = \int \rho({\bf r}) ({\bf r} \times {\bf v}) \d^3 r =

        = \int \rho({\bf r}) ({\bf r} \times (\bomega \times {\bf r}))
                \d^3 r=

        = \int \rho({\bf r}) (\bomega r^2 - {\bf r} ({\bf r}
                \cdot \bomega)) \d^3 r =

        = \int \rho({\bf r}) (\one r^2 - {\bf r} {\bf r})
                \d^3 r \cdot \bomega =

        = {\bf I} \cdot \bomega

Where ${\bf I}$ is the moment of inertia tensor:

.. math::

    {\bf I} = \int \rho({\bf r}) (\one r^2 - {\bf r} {\bf r}) \d^3 r

in components:

.. math::

    I^{ij} = \int \rho({\bf r}) (\delta^{ij} r_k r^k - r^i r^j) \d^3 r
