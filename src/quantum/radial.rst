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

Note: to apply the variation $\delta$ correctly, one uses the definition:

.. math::

    \delta F[\psi] \equiv \left.{\d\over\d\epsilon}F[\psi + \epsilon \delta\psi]
        \right|_{\epsilon=0}

Weak Formulation
~~~~~~~~~~~~~~~~

The weak formulation is obtained from the above by substituting $\delta\psi
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

     \nabla^2f =  {\partial^2 f\over\partial\rho^2} +{2\over \rho}{\partial^2 f\over\partial\rho^2} -{L^2 f\over \rho^2}


.. math::

     L^2= -{\partial^2\over\partial\theta^2} -{1\over\sin^2\theta}{\partial^2\over\partial\phi^2} -{1\over\tan\theta}{\partial\over\partial\theta}

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

    = \int (\half (R'^2Y^2 + R^2(\nabla Y)^2 + 2RR'({\bf\hat\rho}Y)\cdot\nabla Y) + V (RY)^2  )\rho^2\d \rho \d\Omega =

    = \int \left(\half \left(R'^2 + R^2{l(l+1)\over\rho^2}\right) + V R^2\right)\rho^2\d \rho =

    = \int \half \rho^2 R'^2 + (\rho^2 V + \half l(l+1)) R^2\,\d \rho =

where we used the following properties of spherical harmonics:

.. math::

    \int Y^2\d\Omega = 1

    \int \rho^2 (\nabla Y)^2\d\Omega = l(l+1)

    (Y{\bf \hat \rho})\cdot(\rho \nabla Y) = 0

We now minimize the action (subject to the normalization $\int \rho^2 R^2\d\rho
= 1$) to obtain the radial equation:

.. math::

    0 = \delta (S - \epsilon N) = \delta
    \int \half \rho^2 R'^2 + (\rho^2 V + \half l(l+1)) R^2 - \epsilon \rho^2R^2
        \,\d \rho =

    = 2\int \half \rho^2 R'(\delta R)' + (\rho^2 V + \half l(l+1)) R\delta R -
    \epsilon \rho^2 R\delta R \,\d \rho =

    = 2\int \left( (-\half \rho^2 R')' + (\rho^2 V + \half l(l+1)) R - \epsilon \rho^2
    R\right)\delta R \,\d \rho + [\rho^2 R' \delta R]^a_b

So the radial equation is:

.. math::

    (-\half \rho^2 R')' + (\rho^2 V + \half l(l+1)) R = \epsilon \rho^2 R

In agreement with the previous result.

Weak Formulation
~~~~~~~~~~~~~~~~

The weak formulation is obtained from the above by substituting $\delta R
\to v$ (the test function) so we get:

.. math::

    \int \half \rho^2 R'v' + (\rho^2 V + \half l(l+1)) Rv\,\d\rho =
    \epsilon \int \rho^2 Rv \,\d \rho

Variational Formulation of the Dirac equation
---------------------------------------------

The QED Lagrangian density is

.. math::

    \L=\bar\psi(i\hbar c\gamma^\mu D_\mu-mc^2)\psi-{1\over4}F_{\mu\nu}F^{\mu\nu}

where:

.. math::

    D_\mu=\partial_\mu+{i\over \hbar}eA_\mu

    F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu

We will treat the fields as classical fields, so we get the classical wave
Dirac equation, after plugging this Lagrangian into the Euler-Lagrange equation
of motion:

.. math::

    (i\hbar c\gamma^\mu D_\mu-mc^2)\psi=0

    \partial_\nu F^{\nu\mu}=-ec\bar\psi\gamma^\mu\psi

Notice that the Lagrangian happens to be zero for the solution of Dirac
equation (e.g. the extremum of the action). This has nothing to do with the
variational principle itself, it's just a coincindence.

In this section we are only interested in the Dirac equation, so we write the
Lagrangian as:

.. math::

    \L=\bar\psi(i\hbar c\gamma^\mu D_\mu-mc^2)\psi =

    =\psi^\dag\gamma^0(i\hbar c\gamma^\mu D_\mu-mc^2)\psi=

    =\psi^\dag\gamma^0(i\hbar c\gamma^0(\partial_0+{i\over\hbar}eA_0)+ic\gamma^i (\partial_i+{i\over\hbar}eA_i)-mc^2)\psi=

    =\psi^\dag(i\hbar c\partial_0+i\hbar c\gamma^0\gamma^i\partial_i-\gamma^0mc^2-ceA_0 -ce\gamma^0\gamma^iA_i)\psi=

    =\psi^\dag(i\hbar{\partial\over\partial t}+c\alpha^i p_i-\beta mc^2-ceA_0-ce\alpha^iA_i)\psi=

    =-\psi^\dag(-i\hbar{\partial\over\partial t}+c\alpha^i (-p_i+eA_i)+\beta mc^2+ceA_0)\psi=

    =-\psi^\dag(-i\hbar{\partial\over\partial t}+c{\boldsymbol\alpha}\cdot({\bf p}-e{\bf A})+\beta mc^2+V)\psi

where we introduced the potential by $V = c e A_0$. We also could have done the
same manipulation to the dirac equation itself and we would get the same
expression:

.. math::

    (-i\hbar{\partial\over\partial t}+c{\boldsymbol\alpha}\cdot({\bf p}-e{\bf A})+\beta mc^2+V)\psi = 0

The corresponding eigenvalue problem is:

.. math::

    (c{\boldsymbol\alpha}\cdot({\bf p}-e{\bf A})+\beta mc^2+V)\psi = W\psi

Radial Dirac equation
---------------------

As for the Schrödinger equation, there are two ways to obtain the radial Dirac
equation. Either from the Lagrangian, or from the equation itself.

From the Equation
~~~~~~~~~~~~~~~~~

The manipulations are well known, one starts by writing the Dirac spinors using
the spin angular functions and radial components $P$ and $Q$:

.. math::

    \psi = \left(\begin{array}{c}{P\over\rho}\chi^{j_3}_\kappa\\
        i{Q\over\rho}\chi^{j_3}_{-\kappa}\end{array}\right)

    \psi^\dag = \left(\begin{array}{cc}{P\over\rho}\chi^{j_3}_\kappa &
        -i{Q\over\rho}\chi^{j_3}_{-\kappa}\end{array}\right)

and putting this into the Dirac equation one obtains:

.. math::

    \left(\begin{array}{cc}
        \left(-\hbar c \left({\d\over\d\rho} - {\kappa\over\rho}\right)Q + (V+mc^2-W)P\right)  & 0\\
        0 & \left(\hbar c \left({\d\over\d\rho} + {\kappa\over\rho}\right)P + (V-mc^2-W)Q\right) 
        \end{array}\right)
        \left(
        \begin{array}{c}
        {1\over \rho}\chi^{j_3}_\kappa \\
        i{1\over\rho}\chi^{j_3}_{-\kappa}
        \end{array}
        \right)
        =0

So one obtains the following radial equations:

.. math::

    -\hbar c \left({\d\over\d\rho} - {\kappa\over\rho}\right)Q + (V+mc^2-W)P=0

    \hbar c \left({\d\over\d\rho} + {\kappa\over\rho}\right)P + (V-mc^2-W)Q=0

From the Lagrangian
~~~~~~~~~~~~~~~~~~~

We can reuse the calculations from the previous sections, because the Lagrangian
happens to be zero for the solution of the Dirac equation:

.. math::

    \L=\bar\psi(i\hbar c\gamma^\mu D_\mu-mc^2)\psi =

    =-\psi^\dag(-i\hbar{\partial\over\partial t}+c{\boldsymbol\alpha}\cdot({\bf
        p}-e{\bf A})+\beta mc^2+V)\psi=

    =
    \left(\begin{array}{cc}{P\over\rho}\chi^{j_3}_\kappa &
        -i{Q\over\rho}\chi^{j_3}_{-\kappa}\end{array}\right)
    \left(\begin{array}{cc}
        \left(-\hbar c \left({\d\over\d\rho} - {\kappa\over\rho}\right)Q + (V+mc^2)P\right)  & 0\\
        0 & \left(\hbar c \left({\d\over\d\rho} + {\kappa\over\rho}\right)P + (V-mc^2)Q\right)
        \end{array}\right)
        \left(
        \begin{array}{c}
        {1\over \rho}\chi^{j_3}_\kappa \\
        i{1\over\rho}\chi^{j_3}_{-\kappa}
        \end{array}
        \right)
    =

    =
    {1\over\rho^2}
    P
    \left(-\hbar c \left({\d\over\d\rho} - {\kappa\over\rho}\right)Q + (V+mc^2)P\right)
    \chi^{j_3}_\kappa\chi^{j_3}_\kappa
    +
    {1\over\rho^2}
    Q
    \left(\hbar c \left({\d\over\d\rho} + {\kappa\over\rho}\right)P + (V-mc^2)Q\right)
    \chi^{j_3}_{-\kappa}\chi^{j_3}_{-\kappa}

We can now write the action:

.. math::

    S = \int \L \,\rho^2 \,\d\rho\d\Omega

the spin angular functions integrate to $1$:

.. math::

    \int \chi^{j_3}_\kappa\chi^{j_3}_\kappa \d\Omega = 1

    \int \chi^{j_3}_{-\kappa}\chi^{j_3}_{-\kappa} \d\Omega = 1

the $\rho^2$ cancels out and we
get:

.. math::

    S[P, Q] = \int
    P
    \left(-\hbar c \left({\d\over\d\rho} - {\kappa\over\rho}\right)Q + (V+mc^2)P\right)
    +
    Q
    \left(\hbar c \left({\d\over\d\rho} + {\kappa\over\rho}\right)P + (V-mc^2)Q\right)
    \,\d\rho=

    =\int -\hbar c(PQ' - QP') + \hbar c {2\kappa\over\rho} PQ +
        V(P^2+Q^2) + m c^2 (P^2 - Q^2) \d\rho

the normalization condition is:

.. math::

    N = \int P^2 + Q^2 \d\rho - 1 = 0

and we can variate the action, we also shift the energy $W=\epsilon + mc^2$:

.. math::

    0 = \delta (S - W N) = \delta (S - \epsilon N - mc^2N)

which effectively adds $-mc^2(P^2+Q^2)$ into the Lagrangian, which changes the
term $mc^2(P^2 - Q^2)$ into $-2mc^2 Q^2$.
We can now variate the (constrained) action:

.. math::

    0=\delta\int -\hbar c(PQ' - QP') + \hbar c {2\kappa\over\rho} PQ +
        V(P^2+Q^2) - 2m c^2 Q^2 \d\rho=

    = 2\int \left(-\hbar c((\delta P)Q' - P'\delta Q) + \hbar c{\kappa\over\rho}
        ((\delta P)Q + P\delta Q)) + (P\delta P + Q\delta Q)V
        -2mc^2Q\delta Q - \epsilon(P\delta P + Q\delta Q)\right)\d\rho

        +[P\delta Q - Q\delta P]^R_0 =

    = 2\int
    \delta P \left(-\hbar c Q' + \hbar c{\kappa\over\rho}Q + PV -          \epsilon P
    \right)+
    \delta Q \left(\hbar c P' + \hbar c{\kappa\over\rho}P + QV - 2mc^2Q - \epsilon Q
    \right)\d\rho
        +[P\delta Q - Q\delta P]^R_0 =

which gives the two radial equations:

.. math::

    -\hbar c Q' + c{\kappa\over\rho}Q + PV          = \epsilon P

     \hbar c P' + c{\kappa\over\rho}P + QV - 2mc^2Q = \epsilon Q
