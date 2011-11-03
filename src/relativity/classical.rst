.. index:: Newtonian physics, classical mechanics

===================
Classical Mechanics
===================

Rigid Body Rotation
===================

In all the sections below, the rigid body is rotating around
the $\bomega$ axis, so:

.. math::

    {\bf v} = \bomega \times {\bf r}

Kinetic Energy
--------------

The kinetic energy is:

.. math::

    T = \int \half\rho({\bf r}) v^2 \d^3 r =

      = \int \half\rho({\bf r}) {\bf v}\cdot{\bf v} \d^3 r =

      = \int \half\rho({\bf r}) {\bf v}\cdot(\bomega \times {\bf r}) \d^3 r =

      = \int \half\rho({\bf r}) \bomega\cdot({\bf r}\times {\bf v}) \d^3 r =

      = \half \bomega \cdot \int\rho({\bf r}) ({\bf r}\times {\bf v}) \d^3 r =

      = \half \bomega \cdot {\bf L}

where ${\bf L}$ is the total angular momentum:

.. math::

      {\bf L} = \int\rho({\bf r}) ({\bf r}\times {\bf v}) \d^3 r

Angular Momentum
----------------

Total angular momentum is:

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

Moment of Inertia
-----------------

The moment of inertia tensor and its components are:

.. math::

    {\bf I} = \int \rho({\bf r}) (\one r^2 - {\bf r} {\bf r}) \d^3 r

    I^{ij} = \int \rho({\bf r}) (\delta^{ij} r_k r^k - r^i r^j) \d^3 r

Let's write $\bomega=\omega {\bf n}$ (where ${\bf n}$ is a unit vector),
then the kinetic energy is:

.. math::

    T = \half \bomega \cdot {\bf L}
      = \half \bomega \cdot {\bf I} \cdot \bomega
      = \half {\bf n} \cdot {\bf I} \cdot {\bf n}\, \omega^2
      = \half I \omega^2

where $I$ is the moment of inertia about the axis of rotation:

.. math::

    I = {\bf n} \cdot {\bf I} \cdot {\bf n} =

      = {\bf n} \cdot \int \rho({\bf r}) (\one r^2 - {\bf r} {\bf r}) \d^3 r
        \cdot {\bf n} =

      = \int \rho({\bf r}) (r^2 - ({\bf r}\cdot {\bf n})^2) \d^3 r
