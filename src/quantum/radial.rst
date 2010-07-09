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
    :label: radial2

    (-\half \rho^2 R')' + (\rho^2 V + \half l(l+1)) R = \epsilon \rho^2 R

In agreement with the previous result.

Solving for u=rR
~~~~~~~~~~~~~~~~

We can also make the substitution $u = rR$ and solve for $u$:

.. math::

    R = {u\over r}

    R' = {u'\over r} - {u\over r^2}

and we substitute this to :eq:`radial2`:

.. math::

    -\half \left(r^2\left({u'\over r} - {u\over r^2}\right)\right)'+
        \left(V + {l(l+1)\over 2 r^2}\right) r u = \epsilon r u

    -\half ru''+ \left(V + {l(l+1)\over 2 r^2}\right) r u = \epsilon r u

    -\half u''+ \left(V + {l(l+1)\over 2 r^2}\right) u = \epsilon u

Weak Formulation
~~~~~~~~~~~~~~~~

The weak formulation is obtained from the action above by substituting $\delta R
\to v$ (the test function) so we get:

.. math::

    \int \half \rho^2 R'v' + (\rho^2 V + \half l(l+1)) Rv\,\d\rho =
    \epsilon \int \rho^2 Rv \,\d \rho

We can also start from the equation itself, multiply by a test function $v$:

.. math::

    (-\half \rho^2 R')'v + (\rho^2 V + \half l(l+1)) Rv = \epsilon \rho^2 Rv

We integrate it. Normally we need to be using $\rho^2\d\rho$ in order to
integrate covariantly, but the above equation was already multiplied by
$\rho^2$ (i.e. strictly speaking, it is not coordinate independent anymore), so
we only integrate by $\d\rho$:

.. math::

    \int (-\half \rho^2 R')'v + (\rho^2 V + \half l(l+1)) Rv \d\rho =
        \epsilon \int \rho^2 Rv \d\rho

After integration by parts:

.. math::

    \int \half \rho^2 R'v' + (\rho^2 V + \half l(l+1)) Rv \d\rho
        -\half[\rho^2R'v]_0^a
    =
        \epsilon \int \rho^2 Rv \d\rho

Where $a$ is the end of the domain (the origin is at $0$).
The boundary term is zero at the origin, so we get:

.. math::

    \int \half \rho^2 R'v' + (\rho^2 V + \half l(l+1)) Rv \d\rho
        +\half\rho^2R'(a)v(a)
    =
        \epsilon \int \rho^2 Rv \d\rho

We usually want to have the boundary term $\half\rho^2R'(a)v(a)$ equal to zero.
This is equivalent to either letting $R'(a) = 0$ (we prescribe the zero
derivative of the radial wave function at $a$) or we set $v(a)=0$ (which
corresponds to zero Dirichlet condition for $R$, i.e. setting $R(a)=0$).

Weak Formulation for u
^^^^^^^^^^^^^^^^^^^^^^

.. math::

    \int \half u'v' + \left(V + {l(l+1)\over 2\rho^2}\right) uv \,\d\rho
        -\half\left[u'v\right]_0^R
    =
        \epsilon \int uv \,\d\rho

We prescribe $u(0) = u(R) = 0$, so we get:

.. math::

    \int \half u'v' + \left(V + {l(l+1)\over 2\rho^2}\right) uv \,\d\rho
    =
        \epsilon \int uv \,\d\rho

Dirac Notation
^^^^^^^^^^^^^^

We can also write all the formulas using the Dirac notation:

.. math::

    \one = \int \d\rho \rho^2 \ket{\rho}\bra{\rho}

    \braket{\rho|\rho'} = {\delta(\rho-\rho')\over \rho^2}

    \braket{\rho|R} = R(\rho)

    \braket{\rho|\hat H|R} =
        {1\over\rho^2}(-\half \rho^2 R')' + (V + \half {l(l+1)\over\rho^2}) R

    \hat H \ket{R} = E\ket{R}

Then normalization is:

.. math::

    \braket{R|R} = \int \d\rho \rho^2 \braket{R|\rho}\braket{\rho|R} =
        \int \d\rho \rho^2 R^2(\rho)

The operator $\hat H$ can be written as:

.. math::

    \braket{\rho|\hat H|\rho'} = \braket{\rho|\rho'}\left(
        -\half{1\over\rho^2}{\d\over\d\rho}\left(\rho^2{\d\over\d\rho}\right)
        + (V + \half {l(l+1)\over\rho^2})
        \right)

so to recover the above formula, we do:

.. math::

    \braket{\rho|\hat H| R} = \int\d\rho'\rho'^2\braket{\rho|\hat H|\rho'}
        \braket{\rho'|R}=

    =\int\d\rho'\rho'^2
    {\delta(\rho-\rho')\over \rho^2}
    \left(
        -\half{1\over\rho^2}{\d\over\d\rho}\left(\rho^2{\d\over\d\rho}\right)
        + (V + \half {l(l+1)\over\rho^2})
        \right)
    R(\rho')
    =
        {1\over\rho^2}(-\half \rho^2 R')' + (V + \half {l(l+1)\over\rho^2}) R

Operator $\hat H$ is symmetric, because:

.. math::

    \int f{1\over\rho^2}(\rho^2 g')' \rho^2\d\rho =
    \int {1\over\rho^2}(\rho^2 f')'g \rho^2\d\rho

The weak formulation is:

.. math::

    \braket{v|H|R} = E\braket{v|R}

    \int\d\rho\rho^2 \braket{v|\rho}\braket{\rho|H|R} = E
        \int\d\rho\rho^2\braket{v|\rho}\braket{\rho|R}

    \int\d\rho\rho^2 v(\rho)\left(
        {1\over\rho^2}(-\half \rho^2 R')' + (V + \half {l(l+1)\over\rho^2}) R
    \right) = E
        \int\d\rho\rho^2v(\rho)R(\rho)

and we obtain the FE formulation by expanding $\ket{R} =\sum_j R_j \ket{j}$
(note that the basis $\ket{j}$ is not orthogonal, so in particular $\sum_j
\ket{j}\bra{j} \neq 1$):

.. math::

    \sum_j\braket{i|H|j}R_j = E\sum_j\braket{i|j}R_j

This is a generalized eigenvalue problem.
In the special case of an orthonormal basis, $\braket{i|j} = \delta_{ij}$
(which FE is not), we get:

.. math::

    \sum_j\braket{i|H|j}R_j = R_i

    R_i = \braket{i|R}

Which is an eigenvalue problem.

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

    -\hbar c Q' + \hbar c{\kappa\over\rho}Q + PV          = \epsilon P

     \hbar c P' + \hbar c{\kappa\over\rho}P + QV - 2mc^2Q = \epsilon Q

Weak Formulation
~~~~~~~~~~~~~~~~

The weak formulation can be obtained by substituting $\delta P \to v_1$ and
$\delta Q\to v_2$ into the action above (and separating the integrals) and
omitting the the boundary term:

.. math::

    \int -\hbar c Q'v_1 + \hbar c{\kappa\over\rho}Qv_1 + PVv_1\d\rho =
    \epsilon \int Pv_1 \d\rho

    \int \hbar c P'v_2 + \hbar c{\kappa\over\rho}Pv_2 + QVv_2 -2mc^2Qv_2\d\rho =
        \epsilon \int Q v_2 \d\rho

We can also start from the radial equations themselves to get the same result.
If we start from the equations themselves (which is the most elementary
approach), there are no boundary terms (because we didn't integrate by parts).
We can separate the integrals according to the matrix elements that they
contribute to:

.. math::

    \int PVv_1 \d\rho + \int -\hbar c Q'v_1 +
        \hbar c{\kappa\over\rho}Qv_1 \d\rho =
    \epsilon \int Pv_1 \d\rho

    \int \hbar c P'v_2 + \hbar c{\kappa\over\rho}Pv_2 +
        \int (V -2mc^2)Qv_2 \d\rho =
        \epsilon \int Q v_2 \d\rho

To show that this problem generates a symmetric matrix, it is helpful to write
the radial equations in the following form:

.. math::

    \hat H \ket{P, Q} = \epsilon \ket{P, Q}


where:

.. math::

    \ket{P, Q} = \left(\begin{array}{c} P(\rho) \\ Q(\rho)\end{array}\right)

    \hat H = \left(\begin{array}{cc}
        V(\rho) & \hbar c \left(-{\d\over\d\rho}+{\kappa\over\rho}\right) \\
        \hbar c \left({\d\over\d\rho}+{\kappa\over\rho}\right) & V(\rho) - 2mc^2 \\
        \end{array}\right)

the operator $\hat H$ is Hermitean ($\hat H^\dag = \hat H$), because
$\left(-{\d\over\d\rho}\right)^\dag = {\d\over\d\rho}$:

.. math::

    \int f{\d\over\d\rho}g \d\rho =
    \int \left(-{\d\over\d\rho}\right)f g \d\rho

and all the other
quantities are just scalars.

Stricly speaking, the exact Dirac notation (that is coordinate/representation
independent) would be the following (notice the missing $\rho^2$ in the
completeness relation, which is different to the radial Schrödinger equation):

.. math::

    \hat H \ket{P, Q} = \epsilon \ket{P, Q}

    \one = \int \d\rho \ket{\rho}\bra{\rho}

    \braket{\rho|\rho'} = \delta(\rho-\rho')

    \int
    \braket{\rho|\hat H|\rho'}\braket{\rho'|P, Q}\d\rho'
        = \epsilon \braket{\rho|P, Q}

    \braket{\rho|P, Q} =
        \left(\begin{array}{c} P(\rho) \\ Q(\rho)\end{array}\right)

    \braket{\rho|\hat H|\rho'} = \delta(\rho-\rho')
        \left(\begin{array}{cc}
        V(\rho) & \hbar c \left(-{\d\over\d\rho}+{\kappa\over\rho}\right) \\
        \hbar c \left({\d\over\d\rho}+{\kappa\over\rho}\right) & V(\rho) - 2mc^2 \\
        \end{array}\right)

The normalization is:

.. math::

    \braket{P, Q| P, Q} = \int \d\rho \braket{P, Q|\rho}\braket{\rho|P, Q} =
        \int \d\rho (P^2+Q^2) = 1

The weak formulation is:

.. math::

    \braket{v|\hat H|P, Q} =
        \epsilon \braket{v|P, Q}

where the test function $\ket{v}$ is one of:

.. math::

    \ket{v} = \begin{cases}
        \ket{v_1}\left(\begin{array}{c}1\\0\\\end{array}\right) \cr
        \ket{v_2}\left(\begin{array}{c}0\\1\\\end{array}\right) \cr
        \end{cases}

The FE formulation is then obtained by expanding $\ket{P, Q} = \sum_k q_k \ket{k}$:

.. math::

    \sum_l \braket{k|\hat H|l}q_l =
        \epsilon \sum_l\braket{k|l}q_l

The basis $\ket{k}$ can be for example the FE basis, some spline basis set, or
gaussians. The basis has actually $2n$ base functions and it enumerates each
equation like this:

.. math::

    \ket{k} = \begin{cases}
        \ket{i}\left(\begin{array}{c}1\\0\\\end{array}\right) &
            \mbox{for } i=k < n\cr
        \ket{i}\left(\begin{array}{c}0\\1\\\end{array}\right) &
            \mbox{for } i=k >= n\cr
        \end{cases}

So at the end of the day, the $\braket{k|\hat H|l}$ matrix looks like this:

.. math::

    \braket{k|\hat H|l} = \left(\begin{array}{cc}
        \braket{i|V(r)|j} & \hbar c \braket{i|-{\d\over\d\rho}+{\kappa\over\rho}|j} \\
        \hbar c \braket{i|{\d\over\d\rho}+{\kappa\over\rho}|j} & \braket{i|V(r) - 2mc^2|j} \\
        \end{array}\right)

The matrix is $2n \times 2n$, composed of those 4 matrices $n \times n$. The
$\braket{k|l}$ matrix looks like this:

.. math::

    \braket{k|l} = \left(\begin{array}{cc}
        \braket{i|j} & 0 \\
        0            & \braket{i|j} \\
        \end{array}\right)

We can also write the matrix elements explicitly. Let $\ket{i} = B_i(\rho)$,
then:

.. math::

    \braket{i|j} = \int B_i B_j \,\d\rho

    \braket{i|V|j} = \int B_i V B_j \,\d\rho

    \braket{i|V-2mc^2|j} = \int B_i (V-2mc^2) B_j \,\d\rho

    \hbar c \braket{i|{\d\over\d\rho}+{\kappa\over\rho}|j} =
        \hbar c\int B_i B_j' + B_i {\kappa\over\rho} B_j \,\d\rho

    \hbar c \braket{i|-{\d\over\d\rho}+{\kappa\over\rho}|j} =
        \hbar c\int -B_i B_j' + B_i {\kappa\over\rho} B_j \,\d\rho
