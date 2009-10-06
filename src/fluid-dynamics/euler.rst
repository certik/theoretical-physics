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
$M$ is the molar mass of the gas (e.g. a mass of one mole of the gas),
$\rho={n M\over V}$ is the density of the gas,
$\bar R$ is the ideal gas constant,
$R={\bar R\over M}$ is the specific ideal gas constant,
$c_v$ is the specific heat capacity at constant volume (e.g. a heat capacity
per unit volume),
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

    {\bf f}_x =
       \left( \begin{array}{c}
           U\\
           \frac{U^2}{\varrho} + p\\
           \frac{UV}{\varrho}\\
           \frac{UW}{\varrho}\\
           \frac{U}{\varrho}(E+p)
       \end{array} \right)

    {\bf f}_y =
       \left( \begin{array}{c}
           V\\
           \frac{VU}{\varrho}\\
           \frac{V^2}{\varrho} + p\\
           \frac{VW}{\varrho}\\
           \frac{V}{\varrho}(E+p)
       \end{array} \right)

    {\bf f}_z =
       \left( \begin{array}{c}
           W\\
           \frac{WU}{\varrho}\\
           \frac{WV}{\varrho}\\
           \frac{W^2}{\varrho} + p\\
           \frac{W}{\varrho}(E+p)
       \end{array} \right)

    {\bf g} =
       \left( \begin{array}{c}
           0\\
           -f_x\\
           -f_y\\
           -f_z\\
           0\\
       \end{array} \right)

we can then write the equations as:

.. math::

    {\partial{\bf w}\over \partial t} +
    {\partial{\bf f}_x\over \partial x} +
    {\partial{\bf f}_y\over \partial y} +
    {\partial{\bf f}_z\over \partial z} +
    {\bf g}= 0

Now we write the spatial derivatives using the so called flux Jacobians
${\bf J}_x$,
${\bf J}_y$
and
${\bf J}_z$:

.. math::

    {\partial{\bf f}_x\over \partial x} =
    {\partial{\bf f}_x\over \partial {\bf w}}
    {\partial{\bf w}\over \partial x} \equiv
    {\bf J}_x
    {\partial{\bf w}\over \partial x}

    {\bf J}_x={\bf J}_x({\bf w})\equiv{\partial{\bf f}_x\over \partial {\bf w}}

Similarly for $y$ and $z$, so we get:

.. math::

    {\partial{\bf w}\over \partial t} +
    {\bf J}_x
    {\partial{\bf w}\over \partial x} +
    {\bf J}_y
    {\partial{\bf w}\over \partial y} +
    {\bf J}_z
    {\partial{\bf w}\over \partial z} +
    {\bf g}= 0

to calculate the Jacobians, we'll need:

.. math::

    {\partial p\over \partial {\bf w}}=
        {R\over c_v}
        \left( \begin{array}{ccccc}
            {U^2+V^2+W^2\over 2\rho^2} & -{U\over\rho} & -{V\over\rho}
                & -{W\over\rho} & 1\\
        \end{array} \right)

then we can calculate the Jacobians (and we substitute for $p$):

.. math::

    {\bf J}_x({\bf w}) = {\partial{\bf f}_x\over \partial {\bf w}}=
        \left( \begin{array}{ccccc}
            0 & 1 & 0 & 0 & 0\\
            -{U^2\over\rho^2} +{R\over c_v}{U^2+V^2+W^2\over 2\rho^2} &
                {2U\over\rho}-{R\over c_v}{U\over\rho} &
                -{R\over c_v}{U\over\rho} &
                -{R\over c_v}{V\over\rho} &
                {R\over c_v}\\
            -{UV\over\rho^2} & {V\over\rho} & {U\over\rho} & 0 & 0\\
            -{UW\over\rho^2} & {W\over\rho} & 0 & {U\over\rho} & 0 \\
                -{UE\over\rho^2}-{U\over\rho^2}{R\over c_v}
                    \left(E-{U^2+V^2+W^2\over 2\rho}\right)
                    +{U\over\rho}{R\over c_v}{U^2+V^2+W^2\over 2\rho} &
                {E\over\rho}+{1\over\rho}{R\over c_v}
                    \left(E-{U^2+V^2+W^2\over 2\rho}\right)
                    -{R\over c_v}{U^2\over\rho^2} &
                -{R\over c_v}{UV\over\rho^2} &
                -{R\over c_v}{UW\over\rho^2} &
                {U\over\rho}-{R\over c_v}{U\over\rho} \\
       \end{array} \right)

Sea Breeze Modeling
-------------------

In our model we make the following assumptions:

.. math::

    f_x = 0

    f_y = 0

    f_z = -\rho g

    V = 0

    {\partial U\over\partial y}
    ={\partial V\over\partial y}
    ={\partial W\over\partial y}
    ={\partial E\over\partial y}=0

so we get:

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
functions of $(t, x, z)$.

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