.. index:: MHD, magnetohydrodynamics

MHD Equations
=============

Introduction
------------

The magnetohydrodynamics (MHD) equations are:

.. math::
    :label: MHD1

    \frac{\partial \rho}{\partial t} + \nabla\cdot(\rho {\bf v}) = 0

.. math::
    :label: MHD2

    \rho\left(\frac{\partial {\bf v}}{\partial t} + ({\bf v} \cdot \nabla)
     {\bf v} \right) = -\nabla p +
     {1\over\mu}(\nabla\times{\bf B}) \times {\bf B} + \rho {\bf g}

.. math::
    :label: MHD3

    {\partial {\bf B}\over\partial t}
            = \nabla\times({\bf v}\times{\bf B}) + \eta\nabla^2{\bf B}

.. math::
    :label: MHD4

    \nabla\cdot{\bf B} = 0

assuming $\eta$ is constant. See the next section for a derivation. We can now
apply the following identities (we use the fact that $\nabla\cdot{\bf
B}=0$):

.. math::

    \left[(\nabla\times{\bf B}) \times {\bf B}\right]_i =
        \varepsilon_{ijk}(\nabla\times{\bf B})_j B_k =
        \varepsilon_{ijk}\varepsilon_{jlm}(\partial_l B_m)B_k =
        (\delta_{kl}\delta_{im}-\delta_{km}\delta_{il})(\partial_l B_m)B_k =

    =(\partial_k B_i)B_k - (\partial_i B_k)B_k
        =\left[({\bf B}\cdot\nabla){\bf B} -
        {1\over2}\nabla|{\bf B}|^2\right]_i

    (\nabla\times{\bf B}) \times {\bf B} &=
        ({\bf B}\cdot\nabla){\bf B} - {1\over2}\nabla|{\bf B}|^2=
        ({\bf B}\cdot\nabla){\bf B} + {\bf B}(\nabla\cdot{\bf B})
            - {1\over2}\nabla|{\bf B}|^2
        =\nabla\cdot({\bf B}{\bf B}^T) - {1\over2}\nabla|{\bf B}|^2\\
    \nabla\times({\bf v} \times {\bf B}) &=
        ({\bf B}\cdot\nabla){\bf v} - {\bf B}(\nabla\cdot{\bf v})
        +{\bf v}(\nabla\cdot {\bf B}) - ({\bf v}\cdot\nabla) {\bf B}
        =
        \nabla\cdot({\bf B}{\bf v}^T - {\bf v}{\bf B}^T)\\
    \nabla\cdot(\rho{\bf v}{\bf v}^T) &=
        \left(\nabla\cdot(\rho{\bf v})\right){\bf v}
        + \rho({\bf v}\cdot\nabla){\bf v}=
        -{\bf v}\frac{\partial \rho}{\partial t}
        + \rho({\bf v}\cdot\nabla){\bf v}

So the MHD equations can alternatively be written as:

.. math::
    :label: MHD1b

    \frac{\partial \rho}{\partial t} + \nabla\cdot(\rho {\bf v}) = 0

.. math::
    :label: MHD2b

    \frac{\partial \rho{\bf v}}{\partial t} + \nabla\cdot(\rho{\bf v}{\bf v}^T)
        = -\nabla p +
        {1\over\mu}\left(\nabla\cdot({\bf B}{\bf B}^T)
            - {1\over2}\nabla|{\bf B}|^2\right) + \rho {\bf g}

.. math::
    :label: MHD3b

    {\partial {\bf B}\over\partial t}
            = \nabla\cdot({\bf B}{\bf v}^T - {\bf v}{\bf B}^T) + \eta\nabla^2{\bf B}

.. math::
    :label: MHD4b

    \nabla\cdot{\bf B} = 0

One can also introduce a new variable $p^* = p + {1\over2}\nabla|{\bf B}|^2$, that simplifies :eq:`MHD2b` a bit.

.. index::
    pair: magnetohydrodynamics; derivation

Derivation
----------

The above equations can easily be derived. We have the continuity equation:

.. math::

    \frac{\partial \rho}{\partial t} + \nabla\cdot(\rho {\bf v}) = 0

Navier-Stokes equations (momentum equation) with the Lorentz force on the
right-hand side:

.. math::

    \rho\left(\frac{\partial {\bf v}}{\partial t} + ({\bf v} \cdot \nabla)
     {\bf v} \right) = -\nabla p + {\bf j} \times {\bf B} + \rho {\bf g}

where the current density ${\bf j}$ is given by the Maxwell equation (we
neglect the displacement current ${\partial{\bf E}\over\partial t}$):

.. math::

    {\bf j} = {1\over\mu}\nabla\times{\bf B}

and the Lorentz force:

.. math::

    {1\over\sigma}{\bf j} = {\bf E} + {\bf v}\times{\bf B}

from which we eliminate ${\bf E}$:

.. math::

    {\bf E} = - {\bf v}\times{\bf B} + {1\over\sigma}{\bf j} =
              - {\bf v}\times{\bf B} + {1\over\sigma\mu}\nabla\times{\bf B}

and put it into the Maxwell equation:

.. math::

    {\partial {\bf B}\over\partial t} = -\nabla\times{\bf E}

so we get:

.. math::

    {\partial {\bf B}\over\partial t} = \nabla\times({\bf v}\times{\bf B})
                - \nabla\times\left({1\over\sigma\mu}\nabla\times{\bf B}\right)

assuming the magnetic diffusivity $\eta={1\over\sigma\mu}$ is constant, we
get:

.. math::

    {\partial {\bf B}\over\partial t} = \nabla\times({\bf v}\times{\bf B})
                - \eta\nabla\times\left(\nabla\times{\bf B}\right)
            = \nabla\times({\bf v}\times{\bf B})
                + \eta\left(\nabla^2{\bf B}-\nabla(\nabla\cdot{\bf B})\right)
            = \nabla\times({\bf v}\times{\bf B}) + \eta\nabla^2{\bf B}

where we used the Maxwell equation:

.. math::

    \nabla\cdot{\bf B} = 0

.. index::
    pair: magnetohydrodynamics; FEM

Finite Element Formulation
--------------------------

We solve the following ideal MHD equations (we use
$p^* = p + {1\over2}\nabla|{\bf B}|^2$, but we drop the star):

.. math::
    :label: FEM1a

    \frac{\partial {\bf u}}{\partial t} + ({\bf u} \cdot \nabla)
     {\bf u} - ({\bf B}\cdot\nabla){\bf B} + \nabla p = 0

.. math::
    :label: FEM2a

    {\partial {\bf B}\over\partial t} + ({\bf u}\cdot\nabla){\bf B}
        - ({\bf B}\cdot\nabla){\bf u} = 0

.. math::
    :label: FEM3a

    \nabla\cdot{\bf u} = 0

.. math::
    :label: FEM4a

    \nabla\cdot{\bf B} = 0

If the equation :eq:`FEM4a` is satisfied initially, then it is
satisfied all the time, as can be easily proved by applying a divergence to
the Maxwell equation
${\partial {\bf B}\over\partial t} = -\nabla\times{\bf E}$ (or the
equation :eq:`FEM2a`, resp. :eq:`MHD3`) and we get
${\partial \over\partial t}(\nabla\cdot{\bf B}) = 0$, so
$\nabla\cdot{\bf B}$ is constant, independent of time. As a consequence,
we are essentially only solving equations :eq:`FEM1a`, :eq:`FEM2a` and
:eq:`FEM3a`, which consist of 5 equations for 5 unknowns
(components of ${\bf u}$, $p$ and ${\bf B}$).

We discretize in time by introducing a small time step $\tau$ and we also
linearize the convective terms:

.. math::
    :label: FEM1b

    \frac{{\bf u}^n-{\bf u}^{n-1}}{\tau} + ({\bf u}^{n-1} \cdot \nabla)
     {\bf u}^n - ({\bf B}^{n-1}\cdot\nabla){\bf B}^n + \nabla p = 0

.. math::
    :label: FEM2b

    {{\bf B}^n-{\bf B}^{n-1}\over\tau} + ({\bf u}^{n-1}\cdot\nabla){\bf B}^n
        - ({\bf B}^{n-1}\cdot\nabla){\bf u}^n = 0

.. math::
    :label: FEM3b

    \nabla\cdot{\bf u}^n = 0

Testing :eq:`FEM1b` by the test functions $(v_1, v_2)$, :eq:`FEM2b` by
the functions $(C_1, C_2)$ and :eq:`FEM3b` by the test function
$q$, we obtain the following weak formulation:

.. math::
    :label: FEM1c

    \int_\Omega {u_1 v_1\over\tau} + ({\bf u}^{n-1}\cdot\nabla)u_1 v_1
        - ({\bf B}^{n-1}\cdot\nabla)B_1 v_1
        -p {\partial v_1\over\partial x} \,{\rm d}{\bf x} =
        \int_\Omega {u_1^{n-1} v_1\over\tau}\,{\rm d}{\bf x}

    \int_\Omega {u_2 v_2\over\tau} + ({\bf u}^{n-1}\cdot\nabla)u_2 v_2
        - ({\bf B}^{n-1}\cdot\nabla)B_2 v_2
        -p {\partial v_2\over\partial y} \,{\rm d}{\bf x} =
        \int_\Omega {u_2^{n-1} v_2\over\tau}\,{\rm d}{\bf x}

.. math::
    :label: FEM2c

    \int_\Omega {B_1 C_1\over\tau} + ({\bf u}^{n-1}\cdot\nabla)B_1 C_1
        - ({\bf B}^{n-1}\cdot\nabla)u_1 C_1 \,{\rm d}{\bf x} =
        \int_\Omega {B_1^{n-1} C_1\over\tau}\,{\rm d}{\bf x}

    \int_\Omega {B_2 C_2\over\tau} + ({\bf u}^{n-1}\cdot\nabla)B_2 C_2
        - ({\bf B}^{n-1}\cdot\nabla)u_2 C_2 \,{\rm d}{\bf x} =
        \int_\Omega {B_2^{n-1} C_2\over\tau}\,{\rm d}{\bf x}

.. math::
    :label: FEM3c

    \int_\Omega {\partial u_1\over\partial x}q + {\partial u_2\over\partial y}q
        \,{\rm d}{\bf x} = 0

To better understand the structure of these equations, we write it using
bilinear and linear forms, as well as take into account the symmetries of
the forms. Then we get a particularly simple structure:

.. math::
    :nowrap:

    $$\begin{array}{lclclclclcl}
    +A(u_1, v_1) &&  && -X(p, v_1) && -B(B_1, v_1) &&  &=& l_1(v_1)\\
      && +A(u_2, v_2) && -Y(p, v_2) &&  && -B(B_2, v_2) &=& l_2(v_2)\\
    +X(q, u_1) && +Y(q, u_2) &&  &&  &&  &=& 0\\
    -B(u_1, C_1) &&  &&  && +A(B_1, C_1) &&  &=& l_4(C_1)\\
     && -B(u_2, C_2) &&  &&  && +A(B_2, C_2) &=& l_5(C_2)
    \end{array}$$

where:

.. math::

    A(u, v) &= \int_\Omega {u v\over\tau} +
        ({\bf u}^{n-1}\cdot\nabla)u v\,{\rm d}{\bf x}\\
    B(u, v) &= \int_\Omega ({\bf B}^{n-1}\cdot\nabla)uv\,{\rm d}{\bf x}\\
    X(u, v) &= \int_\Omega u {\partial v\over\partial x} \,{\rm d}{\bf x}\\
    Y(u, v) &= \int_\Omega u {\partial v\over\partial y} \,{\rm d}{\bf x}\\
    l_1(v) &= \int_\Omega {u_1^{n-1} v\over\tau} \,{\rm d}{\bf x}\\
    l_2(v) &= \int_\Omega {u_2^{n-1} v\over\tau} \,{\rm d}{\bf x}\\
    l_4(v) &= \int_\Omega {B_1^{n-1} v\over\tau} \,{\rm d}{\bf x}\\
    l_5(v) &= \int_\Omega {B_2^{n-1} v\over\tau} \,{\rm d}{\bf x}

E.g. there are only 4 distinct bilinear forms. Schematically we can visualize
the structure by:

+----+----+----+----+----+
| A  |    | -X | -B |    |
+----+----+----+----+----+
|    | A  | -Y |    | -B |
+----+----+----+----+----+
| X  | Y  |    |    |    |
+----+----+----+----+----+
| -B |    |    | A  |    |
+----+----+----+----+----+
|    | -B |    |    | A  |
+----+----+----+----+----+

In order to solve it with Hermes, we first need to write it in the block form:

.. math::
    :nowrap:

    $$\begin{array}{lclclclclcl}
    a_{11}(u_1, v_1) &+& a_{12}(u_2, v_1) &+& a_{13}(p, v_1) &+&
        a_{14}(B_1, v_1) &+& a_{15}(B_2, v_1) &=& l_1(v_1)\\
    a_{21}(u_1, v_2) &+& a_{22}(u_2, v_2) &+& a_{23}(p, v_2) &+&
        a_{24}(B_1, v_2) &+& a_{25}(B_2, v_2) &=& l_2(v_2)\\
    a_{31}(u_1, q) &+& a_{32}(u_2, q) &+& a_{33}(p, q) &+&
        a_{34}(B_1, q) &+& a_{35}(B_2, q) &=& l_3(q)\\
    a_{41}(u_1, C_1) &+& a_{42}(u_2, C_1) &+& a_{43}(p, C_1) &+&
        a_{44}(B_1, C_1) &+& a_{45}(B_2, C_1) &=& l_4(C_1)\\
    a_{51}(u_1, C_2) &+& a_{52}(u_2, C_2) &+& a_{53}(p, C_2) &+&
        a_{54}(B_1, C_2) &+& a_{55}(B_2, C_2) &=& l_5(C_2)
    \end{array}$$

comparing to the above, we get the following nonzero forms:

.. math::
    :nowrap:

    $$\begin{array}{lclclclclcl}
    a_{11}(u_1, v_1) &+& 0 &+& a_{13}(p, v_1) &+&
        a_{14}(B_1, v_1) &+& 0 &=& l_1(v_1)\\
    0 &+& a_{22}(u_2, v_2) &+& a_{23}(p, v_2) &+&
        0 &+& a_{25}(B_2, v_2) &=& l_2(v_2)\\
    a_{31}(u_1, q) &+& a_{32}(u_2, q) &+& 0 &+&
        0 &+& 0 &=& 0\\
    a_{41}(u_1, C_1) &+& 0 &+& 0 &+&
        a_{44}(B_1, C_1) &+& 0 &=& l_4(C_1)\\
    0 &+& a_{52}(u_2, C_2) &+& 0 &+&
        0 &+& a_{55}(B_2, C_2) &=& l_5(C_2)
    \end{array}$$

where:

.. math::

    a_{11}(u_1, v_1) &= A(u_1, v_1)\\
    a_{22}(u_2, v_2) &= A(u_2, v_2)\\
    a_{44}(B_1, C_1) &= A(B_1, C_1)\\
    a_{55}(B_2, C_1) &= A(B_2, C_2)\\
    a_{13}(p, v_1) &= -X(p, v_1)\\
    a_{31}(u_1, q) &= X(q, u_1)\\
    a_{23}(p, v_2) &= -Y(p, v_2)\\
    a_{32}(u_2, q) &= Y(q, u_2)\\
    a_{14}(B_1, v_1) &= -B(B_1, v_1)\\
    a_{41}(u_1, C_1) &= -B(u_1, C_1)\\
    a_{25}(B_2, v_2) &= -B(B_2, v_2)\\
    a_{52}(u_2, C_2) &= -B(u_2, C_2)

and $l1$, ..., $l5$ are the same as above.
