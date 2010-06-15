Radial Schrödinger and Dirac Equations
======================================

Variational Formulation of the Schrödinger equation
---------------------------------------------------

Lagrangian is:

.. math::

    \L(\psi) = \half (\nabla \psi)^2 + V(x) \psi^2(x)

Subject to the normalization constrain:

.. math::

    N[\psi] = \int|\psi(x)|^2 \d^3 x - 1 = 0

The action is:

.. math::

    S[\psi] = \int \L \d^3 x

Variating it (subject to the normalization condition) we get:

.. math::

    0 = \delta (S - \epsilon N) =
    \delta\int\half (\nabla \psi)^2 + V(x) \psi^2(x) \d^3x
     - \epsilon \left(\int|\psi(x)|^2 \d^3 x - 1\right)
    =

    = \int (\nabla \psi)\cdot(\nabla\delta\psi) + 2 V \psi \delta \psi
            -2\epsilon\psi\delta\psi\d^3 x

    = 2\int \left(-\half\nabla^2 \psi + V \psi - \epsilon\psi\right) \delta \psi
            \d^3 x + \int ({\bf n}\cdot\nabla\psi) \delta \psi\, \d^2 x

Which gives the Schrödinger equation assuming the surface integral vanishes.

Finite Element Formulation
~~~~~~~~~~~~~~~~~~~~~~~~~~

The FE weak formulation is obtained from the above by substituting $\delta\psi
\to v$ (the test function) so we get:

.. math::

    \int \half(\nabla \psi)\cdot(\nabla v) + V \psi v - \epsilon\psi v\,\d^3 x

Radial Schrödinger equation
---------------------------

There are two ways to obtain the radial Schrödinger equation. Either from the
Lagrangian, or from the equation itself.

From the Equation
~~~~~~~~~~~~~~~~~

.. math::

     -{1\over2}\nabla^2\psi({\bf x})+V(r)\psi({\bf x})=E\psi({\bf x})

The way to solve it is to separate the equation into radial and angular parts
by writing the Laplace operator in spherical coordinates as:

.. math::

     \nabla^2f =  {\partial^2 f\over\partial\rho^2} +{2\over \rho}{\partial^2 f\over\partial\rho^2} -{L^2\over \rho^2}


.. math::

     L^2= -{\partial^2 f\over\partial\theta^2} -{1\over\sin^2\theta}{\partial^2 f\over\partial\phi^2} -{1\over\tan\theta}{\partial f\over\partial\theta}

Substituting $\psi({\bf x})=R(\rho)Y(\theta,\phi)$ into the Schrödinger equation
yields:

.. math::

    -{1\over2}\nabla^2(RY)+VRY=ERY


.. math::

    -{1\over2}R''Y-{1\over\rho}R'Y+{L^2RY\over2\rho^2}+VRY=ERY

Using the fact that $L^2Y=l(l+1)Y$ we can cancel $Y$ and we get the radial
Schrödinger equation:

.. math::

    -{1\over2}R''-{1\over\rho}R'+{l(l+1)R\over2\rho^2}+VR=ER

From the Lagrangian
~~~~~~~~~~~~~~~~~~~

We need to convert the Lagrangian to spherical coordinates. In order to easily
make sure we do things covariantly, we start from the action (which is a
scalar):

.. math::

    S[\psi] = \int \half (\nabla \psi)^2 + V(x) \psi^2(x) \, \d^3 x =

    = \int (\half (\nabla (RY))^2 + V (RY)^2  )\rho^2\d \rho \d\Omega =

    = \int (\half (R'^2Y^2 + R^2(\nabla Y)^2 + 2RR'({\bf\hat r}Y)\cdot\nabla Y) + V (RY)^2  )\rho^2\d \rho \d\Omega =

    = \int \left(\half \left(R'^2 + R^2{l(l+1)\over\rho^2}\right) + V R^2\right)\rho^2\d \rho =

    = \int \half \rho^2 R'^2 + (\rho^2 V + \half l(l+1)) R^2\,\d \rho =
