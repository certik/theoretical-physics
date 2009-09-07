Maxwell's Equations
===================

Electromagnetic Field
---------------------

The electromagnetic field is fully described by a vector field called the
4-potential $A^\alpha$. It has four components that we can label any way we
want, the traditional way is to use:

.. math::

    A^\alpha = \left({\phi\over c}, {\bf A}\right)

where $\phi$ is called the electrostatic scalar potential, ${\bf A}$ is called
the vector potential and $c$ is the speed of light.
The Lagrangian density for the free (noninteracting) field is:

.. math::

    \L = -{1\over 2\mu_0} \partial_\alpha A_\beta \partial^\alpha A^\beta

The Lagrangian for a (charged) particle is:

.. math::

    L(x^\mu, v^\mu) = -\half m v_\alpha v^\alpha

it produces the following charge density:

.. math::

    \rho = q \delta({\bf r} - {\bf s})

The interaction between the charged particle (or in general any charged body)
with some charge density and the electromagnetic field is given by the
Lagrangian density:

.. math::

    \L = -j_\alpha A^\alpha

where:

.. math::

    j^\mu = \rho v^\mu = \gamma \rho (c, {\bf v})

There are several approaches how to obtain the above Lagrangians from some
other assumptions, but ultimately the exact form of the Lagrangians has to be
given by experiment. It is our only assumption and we derive everything else
from it.
All together, the Lagrangian of a charged particle and an electromagnetic field
is:

.. math::
    :label: lagem

    L(x^\mu, v^\mu, A^\mu, \partial_\nu A^\mu)
      =-\half m v_\alpha v^\alpha
        -\int {1\over 2\mu_0} \partial_\alpha A_\beta \partial^\alpha A^\beta
            \d^3 x
            - \int j_\alpha A^\alpha \d^3 x =

      =-\half m v_\alpha v^\alpha
        -\int {1\over 2\mu_0} \partial_\alpha A_\beta \partial^\alpha A^\beta
            \d^3 x
            - \int \rho v_\alpha A^\alpha \d^3 x =

      =-\half m v_\alpha v^\alpha
        -\int {1\over 2\mu_0} \partial_\alpha A_\beta \partial^\alpha A^\beta
            \d^3 x
            - q v_\alpha A^\alpha

Note that:

.. math::

    v_\alpha A^\alpha = - \gamma \phi + \gamma {\bf v} \cdot {\bf A}

The Euler-Lagrange equations for the electromagnetic field (in terms of $A^\mu$
and $\partial_\nu A^\mu$) are:

.. math::

    \partial^\mu {\partial\over\partial (\partial^\mu A^\nu)}
    \left(
        -{1\over 2\mu_0} \partial_\alpha A_\beta \partial^\alpha A^\beta
               - j_\alpha A^\alpha
        \right)
    ={\partial\over\partial A^\nu}
        \left(
        -{1\over 2\mu_0} \partial_\alpha A_\beta \partial^\alpha A^\beta
               - j_\alpha A^\alpha\right)

    \partial^\mu {\partial\over\partial (\partial^\mu A^\nu)}
    \left(
        {1\over 2\mu_0} g_{\delta\alpha} g_{\epsilon\beta}
        \partial^\delta A^\epsilon \partial^\alpha A^\beta
        \right)
    ={\partial\over\partial A^\nu} j_\alpha A^\alpha

    {1\over 2\mu_0} \partial^\mu g_{\delta\alpha} g_{\epsilon\beta}
    \left(
        \delta^\delta_\mu \delta^\epsilon_\nu \partial^\alpha A^\beta
        +
        \partial^\delta A^\epsilon \delta^\alpha_\mu \delta^\beta_\nu
        \right)
    = j_\alpha \delta^\alpha_\nu

    {1\over 2\mu_0} \partial^\mu
    \left(  g_{\mu\alpha} g_{\nu\beta}
        \partial^\alpha A^\beta
        +g_{\delta\mu} g_{\epsilon\nu}
        \partial^\delta A^\epsilon
        \right)
    = j_\nu

    {1\over 2\mu_0} \partial^\mu
    \left(\partial_\mu A_\nu + \partial_\mu A_\nu \right)
    = j_\nu

    {1\over \mu_0} \partial^\mu \partial_\mu A_\nu = j_\nu

.. math::
    :label: Aeq1

    \partial^\mu \partial_\mu A_\nu = \mu_0 j_\nu

Equations for the particle (in terms of $x^\mu$ and $v^\mu$) are:

.. math::

    {\d \over \d \tau} {\partial L\over \partial v_\mu}
         = {\partial L \over \partial x_\mu}

    {\d \over \d \tau} {\partial \over \partial v_\mu}
        \left(\half m g^{\alpha\beta} v_\alpha v_\beta
            + q v_\alpha A^\alpha\right)
         = q v_\alpha {\partial A^\alpha \over \partial x_\mu}

    {\d \over \d \tau}
        \left(
            \half m g^{\alpha\beta} (\delta_{\alpha\mu} v_\beta
            + v_\alpha \delta_{\beta\mu})
            + q \delta_{\alpha\mu} A^\alpha\right)
         = q v_\alpha {\partial A^\alpha \over \partial x_\mu}

    {\d \over \d \tau}
        \left(
            \half m (g^{\mu\beta} v_\beta + g^{\alpha\mu} v_\alpha)
            + q A^\mu\right)
         = q v_\alpha {\partial A^\alpha \over \partial x_\mu}

    {\d \over \d \tau}
        \left(
            \half m (v^\mu + v^\mu)
            + q A^\mu\right)
         = q v_\alpha {\partial A^\alpha \over \partial x_\mu}

    {\d \over \d \tau}
        \left(m v^\mu + q A^\mu\right)
         = q v_\alpha {\partial A^\alpha \over \partial x_\mu}

    m {\d v^\mu \over \d \tau}
         = q \left(-{\d A^\mu\over\d\tau}
            + v_\alpha \partial^\mu A^\alpha\right)

    m {\d v^\mu \over \d \tau}
         = q \left(-v_\alpha \partial^\alpha A^\mu
            + v_\alpha \partial^\mu A^\alpha\right)

    m {\d v^\mu \over \d \tau}
         = q (\partial^\mu A^\alpha - \partial^\alpha A^\mu) v_\alpha

.. math::
    :label: lorentz_rel

    m {\d v^\mu \over \d \tau}
         = q F^{\mu\alpha} v_\alpha

Where $F^{\mu\nu}$ is called the electromagnetic field strength tensor:

.. math::

    F^{\mu\nu} =  \partial^\mu A^\nu - \partial^\nu A^\mu

The only way to measure the electric field is through its interaction with the
charge particle. As such, the actual physical field (that can be measured) is
$F^{\mu\nu}$, which is invariant under any gauge transformation:

.. math::

    A^\alpha \to A^\alpha + \partial^\alpha \psi

where $\psi$ is a gauge function:

.. math::

    F^{\mu\nu} \to  \partial^\mu (A^\nu+\partial^\nu\psi)
         - \partial^\nu (A^\mu+\partial^\mu\psi)
        = \partial^\mu A^\nu - \partial^\nu A^\mu
            +\partial^\mu \partial^\nu\psi - \partial^\nu \partial^\mu\psi
        = \partial^\mu A^\nu - \partial^\nu A^\mu
        = F^{\mu\nu}

In other words, two different $A^\mu$ related by the gauge transformation
represent the exact same physical electromagnetic field (as given by the field
tensor). As such, we can modify the Lagrangian by applying the gauge
transformation to the field $A^\mu$: this changes the equations of motion for
the field (thus the numerical values for $A^\mu$ will be different), but
doesn't change the equation of motion for the particle, so the change will not
have any physical effect (cannot be measured).

By choosing $\psi$ as a solution to the equation
$\partial_\mu\partial^\mu\psi=-\partial_\mu A^\mu$, we get:

.. math::

    \partial_\mu (A^\mu + \partial^\mu \psi)
        = \partial_\mu A^\mu + \partial_\mu\partial^\mu \psi
        = \partial_\mu A^\mu - \partial_\mu A^\mu
        = 0

So for any 4-potential we can find $\psi$ such that the transformed 4-potential
$A^\mu$ obeys the Lorenz gauge condition $\partial_\mu A^\mu=0$.

In order to obtain a gauge
invariant Lagrangian, we need to express it using $F^{\mu\nu}$ using the
following identity:

.. math::

    {1\over 4} F_{\alpha\beta} F^{\alpha\beta}
        ={1\over 4}(\partial_\alpha A_\beta - \partial_\beta A_\alpha)
            (\partial^\alpha A^\beta - \partial^\beta A^\alpha) =

        ={1\over 4}(
            \partial_\alpha A_\beta
            \partial^\alpha A^\beta
             - \partial_\beta A_\alpha
            \partial^\alpha A^\beta
            -\partial_\alpha A_\beta
             \partial^\beta A^\alpha
             + \partial_\beta A_\alpha
              \partial^\beta A^\alpha
            ) =

        ={1\over 2}(
            \partial_\alpha A_\beta
            \partial^\alpha A^\beta
             - \partial_\beta A_\alpha
            \partial^\alpha A^\beta
            ) =

        =\half \partial_\alpha A_\beta \partial^\alpha A^\beta
             - \half\partial_\beta A_\alpha \partial^\alpha A^\beta =

        =\half \partial_\alpha A_\beta \partial^\alpha A^\beta
               -\half (\partial^\alpha A_\alpha)^2
             - \half\partial_\beta (A_\alpha \partial^\alpha A^\beta
               -A^\beta\partial^\alpha A_\alpha)

The 4-divergence
$\partial_\beta (A_\alpha \partial^\alpha A^\beta -A^\beta\partial^\alpha A_\alpha)$
doesn't change Euler-Lagrange equations, so we can ignore it.
We can see, that in the Lorenz gauge $\partial^\alpha A_\alpha=0$ the term
${1\over 4} F_{\alpha\beta} F^{\alpha\beta}$ (which is gauge invariant)
simplifies to the term $\partial_\alpha A_\beta \partial^\alpha A^\beta$ in the
Lagrangian :eq:`lagem`. The gauge invariant Lagrangian is:

.. math::
    :label: lagem2

    L(x^\mu, v^\mu, A^\mu, \partial_\nu A^\mu)
      =-\half m v_\alpha v^\alpha
        -\int {1\over 4\mu_0} F_{\alpha\beta} F^{\alpha\beta} \d^3 x
            - \int j_\alpha A^\alpha \d^3 x

The E.-L. equation for the particle doesn't change, the equation for the field
becomes:

.. math::

    \partial^\mu (\partial_\mu A_\nu-\partial_\nu A_\mu) = \mu_0 j_\nu

.. math::
    :label: Feq1

    \partial^\mu F_{\mu\nu} = \mu_0 j_\nu

Which in Lorenz gauge simplifies to equation :eq:`Aeq1`.
In order to write equations of motion in terms of $F^{\mu\nu}$ only, we
need another equation for it:

.. math::
    :label: Feq2

    \epsilon^{\alpha\beta\gamma\delta}\partial_\gamma F_{\alpha\beta}
        = \epsilon^{\alpha\beta\gamma\delta}\partial_\gamma
            (\partial_\alpha A_\beta - \partial_\beta A_\alpha) =

        = \epsilon^{\alpha\beta\gamma\delta}\partial_\gamma
            \partial_\alpha A_\beta
            -\epsilon^{\alpha\beta\gamma\delta}\partial_\gamma
            \partial_\beta A_\alpha = 0

We used the fact, that the partial derivatives are symmetric in the indices
$\gamma\alpha$ and $\gamma\beta$ while
$\epsilon^{\alpha\beta\gamma\delta}$ is antisymmetric.

Maxwell's Equations
-------------------

Maxwell's equations are the equations for the electromagnetic field in terms of
the physical field strengh tensor, equations :eq:`Feq1` and :eq:`Feq2`:

.. math::

    \partial^\mu F_{\mu\nu} = \mu_0 j_\nu

    \epsilon^{\alpha\beta\gamma\delta}\partial_\gamma F_{\alpha\beta} = 0

The field strength tensor is antisymmetric, so it has 6 independent components
(we use metric tensor with signature -2):

.. math::

    F^{0i} = \partial^0 A^i - \partial^i A^0
        = {1\over c}{\partial A^i\over \partial t} +
            {\partial\over\partial x_i} {\phi\over c}
        = -{1\over c}\left(-{\partial\phi\over\partial x_i}
                -{\partial A^i\over \partial t} \right)


    F^{ij} = \partial^i A^j - \partial^j A^i
        = -{\partial A^j\over\partial x_i} +{\partial A^i\over\partial x_j}
        = -(\delta^i{}_l\delta^j{}_m - \delta^i{}_m\delta^j{}_l)
            {\partial A^m\over\partial x_l}
        = -\epsilon^{ij}{}_k\epsilon^k{}_{lm} {\partial A^m\over\partial x_l}

There is freedom in how we label the components. The standard way is to express
them using physical fields ${\bf E}$ and ${\bf B}$ that are introduced by:

.. math::

    {\bf E} = -\nabla\phi - {\partial {\bf A}\over\partial t}

    {\bf B} = \nabla\times{\bf A}

or in components:

.. math::

    E^i = -{\partial\phi\over\partial x_i}
                -{\partial A^i\over \partial t}

    B^k = \epsilon^k{}_{lm} \nabla^l A^m

Comparing to the above, we get:

.. math::

    F^{0i} = -{E^i\over c}

    F^{ij} = -\epsilon^{ij}{}_k B^k

In particular:

.. math::

    F^{12} = -\epsilon^{12}{}_k B^k = -\epsilon^{12}{}_3 B^3 = - B^3

    F^{13} = -\epsilon^{13}{}_k B^k = -\epsilon^{13}{}_2 B^2 = + B^2

    F^{23} = -\epsilon^{23}{}_k B^k = -\epsilon^{23}{}_1 B^1 = - B^1

so we get:

.. math::

    F^{\mu\nu} = \left(\begin{array}{cccc}
    0 & -{E^1\over c} & -{E^2\over c} & -{E^3\over c} \\
    {E^1\over c} & 0 & -B^3 & B^2 \\
    {E^2\over c} & B^3 & 0 & -B^1 \\
    {E^3\over c} & -B^2 & B^1 & 0 \\
    \end{array}\right)

    F_{\mu\nu} = g_{\mu\alpha}g_{\nu\beta}F^{\alpha\beta}
        = \left(\begin{array}{cccc}
    0 & {E^1\over c} & {E^2\over c} & {E^3\over c} \\
    -{E^1\over c} & 0 & -B^3 & B^2 \\
    -{E^2\over c} & B^3 & 0 & -B^1 \\
    -{E^3\over c} & -B^2 & B^1 & 0 \\
    \end{array}\right)

In terms of $\bf E$ and $\bf B$ fields, the Maxwell's equations become:

.. math::

    \nabla\cdot{\bf E} = c^2\mu_0 \rho

    \nabla\times{\bf B} = \mu_0 {\bf j} + {1\over c^2}{\partial{\bf E}
        \over \partial t}

    \nabla\cdot{\bf B} = 0

    \nabla\times{\bf E} = -{\partial{\bf B}\over\partial t}

In Lorenz gauge, the equation for the 4-potential is :eq:`Aeq1`:

.. math::

    \partial^\mu \partial_\mu A_\nu = \mu_0 j_\nu

The solution to this equation is:

.. math::

    A^\beta({\bf x}, t) = {\mu_0\over 4\pi}\int
         {j^\beta({\bf y},t-{ |{\bf x} - {\bf y}| \over c})
            \over |{\bf x} - {\bf y}| }\d^3 y

For scalar potential ($\beta=0$) we get:

.. math::

    {\phi({\bf x}, t)\over c} = {\mu_0\over 4\pi}\int
         {c \rho({\bf y},t-{ |{\bf x} - {\bf y}| \over c})
            \over |{\bf x} - {\bf y}| }\d^3 y

    \phi({\bf x}, t) = {\mu_0 c^2\over 4\pi}\int
         {\rho({\bf y},t-{ |{\bf x} - {\bf y}| \over c})
            \over |{\bf x} - {\bf y}| }\d^3 y
        = {1\over 4\pi\epsilon_0}\int
         {\rho({\bf y},t-{ |{\bf x} - {\bf y}| \over c})
            \over |{\bf x} - {\bf y}| }\d^3 y

And for vector potential ($\beta=i$) we get:

.. math::
    :label: Avec_sol

    {\bf A}({\bf x}, t) = {\mu_0\over 4\pi}\int
         {{\bf j}({\bf y},t-{ |{\bf x} - {\bf y}| \over c})
            \over |{\bf x} - {\bf y}| }\d^3 y

Lorentz Force
-------------

The equation for the charge particle :eq:`lorentz_rel` is:

.. math::

    m {\d v^\mu \over \d \tau}
         = q F^{\mu\alpha} v_\alpha

In components:

.. math::

    m {\d v^0 \over \d \tau}
         = q F^{0\alpha} v_\alpha
         = -q {E^i\over c} \gamma v_i

    m {\d v^i \over \d \tau}
         = q F^{i\alpha} v_\alpha
         = q \left(-{E^i\over c} v_0 - \epsilon^{ij}{}_k B^k v_j\right)
         = q \left({E^i\over c} v^0 + \epsilon^i{}_{jk} B^k v^j\right)
         = q\gamma \left(E^i + ({\bf v}\times{\bf B})^i\right)

Using coordinate time $t$ and coordinates ${\bf x}$ instead of the proper time
$\tau$ and 4-vector $x^\mu$, we need to rewrite the action:

.. math::

    S = \int L(x^\mu, v^\mu) \d \tau
      = \int {1\over\gamma}L(x^\mu, v^\mu) \d t
      = \int L_{coord}({\bf x}, {\bf v}) \d t

where $L_{coord}({\bf x}, {\bf v})$ is the Lagrangian expressed in coordinates
${\bf x}$ and ${\bf v}$ (and thus is not Lorentz invariant):

.. math::

    L_{coord}({\bf x}, {\bf v}) = {1\over\gamma}L(x^\mu, v^\mu) =

         = -{m c^2\over\gamma} + {e\over\gamma}v_\alpha A^\alpha =

         = -{m c^2\over\gamma} + {e\over\gamma}(-c\gamma A^0 +\gamma v_i A^i) =

         = -m c^2\sqrt{1-{v^2\over c^2}} - e\phi + e{\bf v}\cdot {\bf A}

the particle's canonical momentum ${\bf P}$ is:

.. math::

    P_i = {\partial L(t)\over\partial v_i}
        =-mc^2 {1\over 2\sqrt{1-{v^2\over c^2}}}\left(-2v_i\over c^2\right)
             + e A_i
        ={m v_i\over\sqrt{1-{v^2\over c^2}}} + e A_i

    {\bf P} = {m{\bf v}\over\sqrt{1-{v^2\over c^2}}} + e{\bf A}
        = \gamma m{\bf v} + e{\bf A}
        = {\bf p} + e{\bf A}

where ${\bf p} = {\bf P}-e{\bf A} = \gamma m{\bf v}$ is the kinetic momentum.
Euler-Lagrange equations are:

.. math::

    {\d \over \d t} {\partial L_{coord}\over \partial v_i}
         = {\partial L_{coord} \over \partial x_i}

    {\d \over \d t} P_i = {\partial L_{coord} \over \partial x_i}

    {\d \over \d t} \left({m v_i\over\sqrt{1-{v^2\over c^2}}} + e A_i\right)
         = {\partial \over \partial x_i}\left(-m c^2\sqrt{1-{v^2\over c^2}}
             - e\phi + e{\bf v}\cdot {\bf A}\right)

    {\d \over \d t} \left({m v_i\over\sqrt{1-{v^2\over c^2}}}\right)
         + e {\d A_i\over \d t}
         = -e{\partial \phi\over \partial x_i}
           +e{\bf v}\cdot{\partial {\bf A}\over \partial x_i}

    {\d \over \d t} \left({m v_i\over\sqrt{1-{v^2\over c^2}}}\right)
         = e\left(-{\partial \phi\over \partial x_i}
           -{\d A_i\over \d t}
           +v_j{\partial A_j\over \partial x_i}\right)

    {\d \over \d t} \left({m v_i\over\sqrt{1-{v^2\over c^2}}}\right)
         = e\left(-{\partial \phi\over \partial x_i}
           -{\partial A_i\over \partial t}-v_j{\partial A_i\over\partial x_j}
           +v_j{\partial A_j\over \partial x_i}\right)

    {\d \over \d t} \left({m {\bf v}\over\sqrt{1-{v^2\over c^2}}}\right)
         = e\left({\bf E} + {\bf v}\times {\bf B}\right)

For continuous case (current), the force due to the magnetic field is:

.. math::

    {\bf F} = \int {\bf j}\times {\bf B} \d^3 x
        = I \int \d {\bf l}\times {\bf B}

Hamiltonian
-----------

Expressing ${\bf v}$ in terms of ${\bf P}$ we get:

.. math::

    {\bf P} = {m{\bf v}\over\sqrt{1-{v^2\over c^2}}} + e{\bf A}

    {\bf P} - e{\bf A} = {m{\bf v}\over\sqrt{1-{v^2\over c^2}}}

    P_i - e A_i = {m v_i\over\sqrt{1-{v^2\over c^2}}}

    (P_i - e A_i)^2\left(1-{v^2\over c^2}\right) = m^2 v_i^2

    (P_i - e A_i)^2\left(1-{(v_1^2 + v_2^2 + v_3^3)^2\over c^2}\right)
        = m^2 v_i^2

    v_i^2 = {(P_i - e A_i)^2 c^2 \over m c^2 + ({\bf P} - e{\bf A})^2}

    |v_i| = {|P_i - e A_i| \over \sqrt {m + {1\over c^2 } ({\bf P} - e{\bf A})^2}}

    v_i = {P_i - e A_i \over \sqrt {m + {1\over c^2 } ({\bf P} - e{\bf A})^2}}

    {\bf v} = {{\bf P} - e{\bf A}\over\sqrt{m^2 +
        {1\over c^2}({\bf P} - e{\bf A})^2}}

    {\bf v} = {c({\bf P} - e{\bf A})\over\sqrt{m^2c^2 + ({\bf P} - e{\bf A})^2}}

The system of equations was solved for $v_i$ using the code
(in there $v1s = v_1^2$, $vs=v^2$ and $P1 = P_1 - eA_1$)::

    >>> from sympy import var, solve
    >>> var("P1 P2 P3 m c v1s v2s v3s")
    (P1, P2, P3, m, c, v1s, v2s, v3s)
    >>> vs = v1s+v2s+v3s
    >>> solve([P1**2*(1-vs/c**2) -v1s*m**2,
    ...        P2**2*(1-vs/c**2) -v2s*m**2,
    ...        P3**2*(1-vs/c**2) -v3s*m**2], [v1s, v2s, v3s])
    {v1s: P1**2*c**2/(P1**2 + P2**2 + P3**2 + c**2*m**2),
     v2s: P2**2*c**2/(P1**2 + P2**2 + P3**2 + c**2*m**2),
     v3s: P3**2*c**2/(P1**2 + P2**2 + P3**2 + c**2*m**2)}

And the absolute value was removed by using the fact, that $v_i$ has the same
sign as $p_i = P_i - e A_i$ which follows from the second equation.

The Hamiltonian is:

.. math::

    H({\bf x}, {\bf P}, t) = {\bf v} \cdot {\bf P} - L =

        = {\bf v} \cdot {\bf P}
        +m c^2\sqrt{1-{v^2\over c^2}} + e\phi - e{\bf v}\cdot {\bf A} =

        = {\bf v} \cdot ({\bf P}-e{\bf A})
        +m c^2\sqrt{1-{v^2\over c^2}} + e\phi =

        = {c({\bf P} - e{\bf A})\cdot({\bf P}-e{\bf A})\over\sqrt{m^2c^2 +
        ({\bf P} - e{\bf A})^2}}
        +m c^2\sqrt{1-{1\over c^2}\left({c({\bf P} - e{\bf A})\over\sqrt{m^2c^2 + ({\bf P} - e{\bf A})^2}}\right)^2} + e\phi =

        = {c({\bf P} - e{\bf A})^2\over\sqrt{m^2c^2 + ({\bf P} - e{\bf A})^2}}
        +m c^2\sqrt{1-{({\bf P} - e{\bf A})^2\over m^2c^2 + ({\bf P} - e{\bf A})^2}} + e\phi =

        = {c({\bf P} - e{\bf A})^2\over\sqrt{m^2c^2 + ({\bf P} - e{\bf A})^2}}
        +m c^2\sqrt{m^2 c^2 \over m^2c^2 + ({\bf P} - e{\bf A})^2} + e\phi =

        = {c\left(({\bf P} - e{\bf A})^2+m^2c^2\right)\over
            \sqrt{m^2c^2 + ({\bf P} - e{\bf A})^2}} + e\phi =

        = c\sqrt{m^2c^2 + ({\bf P} - e{\bf A})^2} + e\phi

Electromagnetic Stress Tensor
-----------------------------

The stress tensor is calculated from the Lagrangian:

.. math::

    \L = -{1\over 4\mu_0} F_{\alpha\beta} F^{\alpha\beta}
        =-{1\over 2\mu_0}(\partial_\alpha A_\beta \partial^\alpha A^\beta
            -\partial_\beta A_\alpha \partial^\alpha A^\beta)

using the Noether formula:

.. math::

    T^\mu{}_\nu = {\partial\L\over\partial(\partial_\mu A_\alpha)}
                    \partial_\nu A_\alpha
                    -\delta^\mu{}_\nu \L =

        = -{1\over\mu_0} F^{\mu\alpha}
            \partial_\nu A_\alpha+{1\over 4\mu_0}\delta^\mu{}_\nu
                F_{\alpha\beta} F^{\alpha\beta}

We raise the $\nu$ index:

.. math::

    T^{\mu\nu} = g^{\nu\lambda} T^\mu{}_\lambda
        = -{1\over\mu_0} F^{\mu\alpha}
            \partial^\nu A_\alpha+{1\over 4\mu_0}g^{\mu\nu}
                F_{\alpha\beta} F^{\alpha\beta}

This tensor is not symmetric under the exchange of the $\mu\nu$ indices. To
make it symmetric, we add a total derivative term
$\partial_\alpha K^{\alpha\mu\nu}$, where $K^{\alpha\mu\nu}$ is antisymmetric
in its first two indices. This guarantees that
$\partial_\mu \partial_\alpha K^{\alpha\mu\nu}=0$ so that the new stress energy
tensor is still conserved. We choose
$K^{\alpha\mu\nu}={1\over\mu_0} F^{\mu\alpha} A^\nu$ and get:

.. math::

    T^{\mu\nu} +\partial_\alpha K^{\alpha\mu\nu}
        = -{1\over\mu_0} F^{\mu\alpha}
            \partial^\nu A_\alpha+{1\over 4\mu_0}g^{\mu\nu}
                F_{\alpha\beta} F^{\alpha\beta}
                +{1\over\mu_0}\partial_\alpha ( F^{\mu\alpha} A^\nu) =

        = {1\over\mu_0}F^{\mu\alpha}
                (\partial_\alpha A^\nu - \partial^\nu A_\alpha)
            +{1\over 4\mu_0}g^{\mu\nu}
                F_{\alpha\beta} F^{\alpha\beta}
                +{1\over\mu_0}(\partial_\alpha F^{\mu\alpha}) A^\nu =

        = {1\over\mu_0}F^{\mu\alpha} F_\alpha{}^\nu
            +{1\over 4\mu_0}g^{\mu\nu}
                F_{\alpha\beta} F^{\alpha\beta} =

        = -{1\over\mu_0}\left(F^{\mu\alpha} F^\nu{}_\alpha
            -{1\over 4}g^{\mu\nu}
                F_{\alpha\beta} F^{\alpha\beta}\right)

where we used $\partial_\alpha F^{\mu\alpha} = 0$.

Another way to derive the stress energy tensor is from general relativity using
the formula:

.. math::

    T_{\mu\nu} = - {2\over\sqrt{ |\det g| }}{\delta S_{EM}\over
            \delta g^{\mu\nu}}

So we write the action:

.. math::

    S_{EM} = -\int {1\over 4\mu_0} F_{\alpha\beta} F^{\alpha\beta}
        \sqrt{ |\det g| }\d^4 x
        = -\int {1\over 4\mu_0} g^{\alpha\lambda} g^{\beta\rho} F_{\alpha\beta}
            F_{\lambda\rho}
        \sqrt{ |\det g| }\d^4 x

And vary with respect to $g^{\mu\nu}$:

.. math::

    \delta S_{EM}
        = -\delta \int {1\over 4\mu_0} g^{\alpha\lambda} g^{\beta\rho}
            F_{\alpha\beta} F_{\lambda\rho} \sqrt{ |\det g| }\d^4 x =

        = -{1\over 4\mu_0} \int  \left(\delta (g^{\alpha\lambda} g^{\beta\rho})
            F_{\alpha\beta} F_{\lambda\rho} \sqrt{ |\det g| }
            + g^{\alpha\mu} g^{\beta\rho}
            F_{\alpha\beta} F_{\lambda\rho} \left(\delta \sqrt{ |\det g| }
            \right)
            \right)\d^4 x =

        = -{1\over 4\mu_0} \int  \left(2(\delta g^{\alpha\lambda}) g^{\beta\rho}
            F_{\alpha\beta} F_{\lambda\rho} \sqrt{ |\det g| }
            + g^{\alpha\lambda} g^{\beta\rho}
            F_{\alpha\beta} F_{\lambda\rho} \left(-\half \sqrt{ |\det g| }
            g_{\mu\nu} (\delta g^{\mu\nu})
            \right)
            \right)\d^4 x =

        = -{1\over 4\mu_0} \int  \left(2(\delta g^{\alpha\lambda})
            F_{\alpha\beta} F_\lambda{}^\beta
            -\half F_{\alpha\beta} F^{\alpha\beta}
            g_{\mu\nu} (\delta g^{\mu\nu})
            \right) \sqrt{ |\det g| } \d^4 x =

        = -{1\over 2\mu_0} \int  \left(
            F_{\mu\beta} F_\nu{}^\beta
            -{1\over 4} F_{\alpha\beta} F^{\alpha\beta}
            g_{\mu\nu}
            \right) (\delta g^{\mu\nu}) \sqrt{ |\det g| } \d^4 x

And we get:

.. math::

    T_{\mu\nu} = {1\over \mu_0} \left(
            F_{\mu\beta} F_\nu{}^\beta
            -{1\over 4} F_{\alpha\beta} F^{\alpha\beta}
            g_{\mu\nu} \right)


Examples
--------

Biot-Savart Law
~~~~~~~~~~~~~~~

Maxwell's equations in Lorenz gauge :eq:`Aeq1`:

.. math::

    \partial_\alpha\partial^\alpha A^\beta = \mu_0 j^\beta

have the solution for the vector potential :eq:`Avec_sol`:

.. math::

    {\bf A}({\bf x}, t) = {\mu_0\over 4\pi}\int
         {{\bf j}({\bf y},t-{ |{\bf x} - {\bf y}| \over c})
            \over |{\bf x} - {\bf y}| }\d^3 y

Assuming ${ |{\bf x} - {\bf y}| \over c} \ll t$:

.. math::

    {\bf A}({\bf x}, t) = {\mu_0\over 4\pi}\int
         {{\bf j}({\bf y},t) \over |{\bf x} - {\bf y}| }\d^3 y

The magnetic field is then:

.. math::

    {\bf B}({\bf x}, t) = \nabla \times {\bf A}({\bf x}, t)
         =\nabla \times {\mu_0\over 4\pi}\int
         {{\bf j}({\bf y},t) \over |{\bf x} - {\bf y}| }\d^3 y =

         ={\mu_0\over 4\pi}\int \left(\nabla {1\over
                 |{\bf x} - {\bf y}| }\right)\times {\bf j}({\bf y},t)\d^3 y =

         ={\mu_0\over 4\pi}\int \left(-{{\bf x} - {\bf y}\over
                 |{\bf x} - {\bf y}|^3 }\right)\times {\bf j}({\bf y},t)\d^3 y =

         ={\mu_0\over 4\pi}\int {\bf j}({\bf y},t) \times {{\bf x} - {\bf y}
                \over |{\bf x} - {\bf y}|^3 } \d^3 y

If the current can be approximated by an infinitely-narrow wire, we get:

.. math::

    {\bf j}({\bf y},t) \d^3 y = I(t) \d {\bf l}

and:

.. math::

    {\bf B}({\bf x}, t)
         ={\mu_0\over 4\pi}\int I(t)\d{\bf l} \times {{\bf x} - {\bf l}
                \over |{\bf x} - {\bf l}|^3 }

Example: Straight Wire
^^^^^^^^^^^^^^^^^^^^^^

Let's assume infinite straight wire carrying constant current $I$:

.. math::

    {\bf l} = (0, 0, l)

    \d {\bf l} = (0, 0, 1)\d l

    {\bf x} = (x, y, z)

    {\bf x}-{\bf l} = (x, y, z-l)

    {\bf B}({\bf x})
         ={\mu_0 I\over 4\pi}\int \d{\bf l} \times {{\bf x} - {\bf l}
                \over |{\bf x} - {\bf l}|^3 } =

         ={\mu_0 I\over 4\pi} \int_{-\infty}^\infty (0, 0, 1) \times
             {(x, y, z-l) \d l
                \over (x^2 + y^2 + (z-l)^2)^{3\over 2} } =

         =(y, -x, 0) {\mu_0 I \over 4\pi}\int_{-\infty}^\infty {\d l
                \over (x^2 + y^2 + (z-l)^2)^{3\over 2} } =

         =(y, -x, 0) {\mu_0 I \over 4\pi} {2\over x^2+y^2} =

         =(y, -x, 0) {\mu_0 I \over 2\pi} {1\over x^2+y^2}

Where we used the value of the folowing integral:

.. math::

    \int_{-\infty}^\infty {\d l \over (x^2+y^2 + (z - l)^2)^{3\over 2} }
        = \int_{-\infty}^\infty {\d u \over (x^2+y^2 + u^2)^{3\over 2} } =

        = \left[u\over (x^2+y^2) \sqrt{x^2+y^2 + u^2}\right]_{-\infty}^\infty
        = \left[\sign u\over (x^2+y^2) \sqrt{
            \left(x\over u\right)^2 + \left(y\over u\right)^2 + 1}
            \right]_{-\infty}^\infty =

        = {1\over x^2+y^2} - \left(-{1\over x^2+y^2}\right) = {2\over x^2+y^2}


For $y=0$:

.. math::

    {\bf B}(x, 0, z)
         =(0, -x, 0) {\mu_0 I \over 2\pi} {1\over x^2}
         =(0, -1, 0) {\mu_0 I \over 2\pi x}

Example: Circular Loop
^^^^^^^^^^^^^^^^^^^^^^

Let's assume a circular loop:

.. math::

    {\bf l} = (r\cos\phi, r\sin\phi, 0)

    {\d {\bf l}\over\d \phi} = (-r\sin\phi, r\cos\phi, 0)

    {\bf x} = (x, y, z)

    {\bf x}-{\bf l} = (x-r\cos\phi, y-r\sin\phi, z)

    {\bf B}({\bf x})
         ={\mu_0 I\over 4\pi}\int \d{\bf l} \times {{\bf x} - {\bf l}
                \over |{\bf x} - {\bf l}|^3 } =

         ={\mu_0 I\over 4\pi} \int_0^{2\pi} (-r\sin\phi, r\cos\phi, 0) \times
             {(x-r\cos\phi, y-r\sin\phi, z) \d \phi
                \over ((x-r\cos\phi)^2 + (y-r\sin\phi)^2 + z^2)^{3\over 2} } =

         ={\mu_0 I\over 4\pi} \int_0^{2\pi} {
                 (-z\cos\phi, -z\sin\phi, (x-r\cos\phi)\cos\phi+
                    (y-r\sin\phi)\sin\phi)
             r\d \phi
                \over ((x-r\cos\phi)^2 + (y-r\sin\phi)^2 + z^2)^{3\over 2} } =

         ={\mu_0 I\over 4\pi} \int_0^{2\pi} {
                 (-z\cos\phi, -z\sin\phi, x\cos\phi+y\sin\phi-r)
             r\d \phi
                \over (x^2+y^2+z^2+r^2-2xr\cos\phi-2yr\sin\phi)^{3\over 2} }

Due to the symmetry of the problem, we can set $y=0$:

.. math::

    {\bf B}(x, 0, z)
         ={\mu_0 I\over 4\pi} \int_0^{2\pi} {
                 (-z\cos\phi, -z\sin\phi, x\cos\phi-r)
             r\d \phi
                \over (x^2+z^2+r^2-2xr\cos\phi)^{3\over 2} } =

         ={\mu_0 I\over 4\pi} \int_0^{2\pi} {
                 (-z\cos\phi, 0, x\cos\phi-r)
             r\d \phi
                \over (x^2+z^2+r^2-2xr\cos\phi)^{3\over 2} }

In the last equation we used the fact, that $\sin\phi$ is odd and $\cos\phi$ is
even on the interval $(0, 2\pi)$.
For $x=y=0$ we get:

.. math::

    {\bf B}(0, 0, z)
         ={\mu_0 I\over 4\pi} \int_0^{2\pi} {
                 (-z\cos\phi, 0, -r)
             r\d \phi
                \over (r^2 + z^2)^{3\over 2} } =

         =(0, 0, -1) {\mu_0 I\over 4\pi} \int_0^{2\pi} {
             r^2\d \phi
                \over (r^2 + z^2)^{3\over 2} } =

         =(0, 0, -1) {\mu_0 I\over 2} {
             r^2 \over (r^2 + z^2)^{3\over 2} }

Helmholtz Coil
^^^^^^^^^^^^^^

Helmholtz coil is a set of two circular loops of radius $r$, that are $d$
apart, where $d=r$. Let's calculate the magnetic field on the axis.
Magnetic field of the first coil is (see the previous example):

.. math::

    {\bf B}_1(0, 0, z) = (0, 0, -1) {\mu_0 I\over 2} {
             r^2 \over (r^2 + z^2)^{3\over 2} }

Second coil is positioned $d$ above the first one:

.. math::

    {\bf B}_2(0, 0, z) = (0, 0, -1) {\mu_0 I\over 2} {
             r^2 \over (r^2 + (z-d)^2)^{3\over 2} }

The total magnetic field is:

.. math::

    {\bf B}(0, 0, z) = {\bf B}_1(0, 0, z) + {\bf B}_2(0, 0, z) =

    = (0, 0, -1) {\mu_0 I\over 2} {
             r^2 \over (r^2 + z^2)^{3\over 2} }
    + (0, 0, -1) {\mu_0 I\over 2} {
             r^2 \over (r^2 + (z-d)^2)^{3\over 2} } =

    = (0, 0, -1) {\mu_0 I r^2\over 2} \left(
             {1 \over (r^2 + z^2)^{3\over 2} } +
             {1 \over (r^2 + (z-d)^2)^{3\over 2} }\right)

The field in the middle:

.. math::

    {\bf B}(0, 0, {d\over 2})
    = (0, 0, -1) {\mu_0 I r^2\over 2} \left(
             {1 \over (r^2 + \left(d\over 2\right)^2)^{3\over 2} } +
             {1 \over (r^2 + \left(d\over 2\right)^2)^{3\over 2} }\right) =

    = (0, 0, -1) {\mu_0 I r^2
             \over (r^2 + \left(d\over 2\right)^2)^{3\over 2} }

For $r=d$ we get:

.. math::

    {\bf B}(0, 0, {d\over 2})
    = (0, 0, -1) {\mu_0 I r^2
             \over (r^2 + \left(r\over 2\right)^2)^{3\over 2} } =

    = (0, 0, -1) {\mu_0 I
             \over r (1 + \left(1\over 2\right)^2)^{3\over 2} } =

    = (0, 0, -1) {\mu_0 I 4^{3\over 2}
             \over r 5^{3\over 2} } =

    = (0, 0, -1) {8 \over 5 \sqrt 5} {\mu_0 I \over r} =

    = (0, 0, -1) B

where the magnitude of ${\bf B}$ is:

.. math::

    B = {8 \over 5 \sqrt 5} {\mu_0 I \over r}

For $r=0.15\rm\, m$ and $N=130$ turns we get the magnitude of the field as
(we use SI units, so $I$ is in $A$ and $B$ in tesla):

.. math::

    B = {8 \over 5 \sqrt 5} {\mu_0 N I \over r}
      = {8 \over 5 \sqrt 5} {4\pi 10^{-7} \cdot 130 I \over 0.15}
      = 7.79\cdot 10^{-4} I

Code::

    >>> from math import pi, sqrt
    >>> "%e" % (8*4*pi*1e-7*130 / (5*sqrt(5)*0.15))
    '7.792861e-04'

Equation of motion for an electron in this field is:

.. math::

    m {\d^2 {\bf x}\over \d t^2} = e\left({\bf v} \times {\bf B}\right)

    m {\d^2 {\bf x}\over \d t^2} = eB\, (v_y, -v_x, 0)

The general solution is:

.. math::

    {\bf x} = {v m\over eB} \left(x + \cos {eB\over m} (t-t_0),
                y -\sin {eB\over m} (t-t_0),
                z\right)

So the electron is moving in a circle with a center $(x, y, z)$,
$t_0$ depends on the initial direction of the velocity and $v$ is the magnitude
of the initial velocity. There can also be a possible movement in the $z$
direction, but for the following initial conditions there is none:

.. math::

    {\bf x}_0 = (0, 0, 0)

    {\bf v}_0 = (0, -v, 0)

Then we get:

.. math::

    {\bf x} = {v m\over eB} \left(-1+\cos {eB\over m} t,
                -\sin {eB\over m} t,
                0\right)

    {\bf v} = v \left(-\sin {eB\over m} t,
                -\cos {eB\over m} t,
                0\right)

So the radius of the circle is $R = {v m\over eB}$.
Let the electrons by accelerated by the electric potential $V$:

.. math::

    \half m v^2 = e V

So the initial velocity is:

.. math::

    v = \sqrt{2eV\over m}

and we get for the radius:

.. math::

    R = {v m\over eB}
        = {m\over eB} \sqrt{2eV\over m}
        = {1\over B} \sqrt{2mV\over e}

from which the electron charge versus mass ratio is:

.. math::

    {e\over m} = {2V \over R^2 B^2}
        = {2V \over R^2\left({8 \over 5 \sqrt 5} {\mu_0 N I \over r}\right)^2}=

        = {125 V r^2 \over 32 \mu_0^2 R^2 N^2 I^2}

For $r=0.15\rm\, m$, $N=130$, $V=300\rm\,V$, $R=0.05\rm\,m$, $I=1.48\rm\,A$
we get:

.. math::

    {e\over m} = 1.80 \cdot 10^{11}\rm\,C\cdot kg^{-1}

Code::

    >>> from math import pi
    >>> r = 0.15
    >>> N = 130
    >>> V = 300
    >>> R = 0.05
    >>> I = 1.48
    >>> mu0 = 4*pi*1e-7
    >>> "%e" % (125 * V * r**2 / (32 * mu0**2 * R**2 * N**2 * I**2))
    '1.804238e+11'

Reference value is:

.. math::

    {e\over m} = 1.7588 \cdot 10^{11}\rm\,C\cdot kg^{-1}

Code::

    >>> e = 1.6021766e-19
    >>> c = 299792458
    >>> eV = e
    >>> KeV = 1e3 * eV
    >>> m = 510.998910 * KeV / c**2
    >>> m
    9.109382795192204e-31
    >>> "%e" % (e / m)
    '1.758820e+11'

or even simpler (we do not actually need the value of the electron charge
$e$)::

    >>> c = 299792458
    >>> KeV = 1e3
    >>> m = 510.998910 * KeV / c**2
    >>> "%e" % (1/m)
    '1.758820e+11'

We can use the experimental value to calculate the electron rest mass energy:

.. math::

    m c^2 = {c^2 \over 1.804238\cdot 10^{11}}{\rm\, eV}
        = 498.1356 {\rm\, KeV}


Ampère's Force Law
~~~~~~~~~~~~~~~~~~

The force on a wire 1 due to a magnetic field of a wire 2 is:

.. math::

    {\bf F} = I_1 \int \d {\bf l}_1 \times {\bf B}({\bf l}_1)

    {\bf B}({\bf x})
         ={\mu_0\over 4\pi}\int I_2(t)\d{\bf l}_2 \times {{\bf x} - {\bf l}_2
                \over |{\bf x} - {\bf l}_2|^3 }


Where ${\bf B}({\bf x})$ is the magnetic field produced by the wire 2.
Combining these two equations we get:

.. math::

    {\bf F} = I_1 \int \d {\bf l}_1 \times {\bf B}({\bf l}_1) =

        = I_1 \int \d {\bf l}_1 \times \left(
         {\mu_0\over 4\pi}\int I_2(t)\d{\bf l}_2 \times {{\bf l}_1 - {\bf l}_2
                \over |{\bf l}_1 - {\bf l}_2|^3 }\right) =

        = {\mu_o I_1 I_2\over 4\pi} \int \int {\d {\bf l}_1 \times (
         \d{\bf l}_2 \times ({\bf l}_1 - {\bf l}_2))
                \over |{\bf l}_1 - {\bf l}_2|^3 } =

        = {\mu_o I_1 I_2\over 4\pi} \int \int {
            \d {\bf l}_2 (\d {\bf l}_1 \cdot ({\bf l}_1 - {\bf l}_2)) -
            ({\bf l}_1 - {\bf l}_2) (\d {\bf l}_2 \cdot\d {\bf l}_1)
                \over |{\bf l}_1 - {\bf l}_2|^3 }

Parallel Straight Wires
^^^^^^^^^^^^^^^^^^^^^^^

We calculate the force between two parallel straight infinite wires:

.. math::

    {\bf l}_1 = ({d\over 2}, 0, l_1)

    \d{\bf l}_1 = (0, 0, \d l_1)

    {\bf l}_2 = (-{d\over 2}, 0, l_2)

    \d{\bf l}_2 = (0, 0, \d l_2)

    {\bf l}_1 - {\bf l}_2 = (d, 0, l_1-l_2)

    \d {\bf l}_2 (\d {\bf l}_1 \cdot ({\bf l}_1 - {\bf l}_2)) -
    ({\bf l}_1 - {\bf l}_2) (\d {\bf l}_2 \cdot\d {\bf l}_1)
        = (0, 0, \d l_2) (l_1-l_2)\d l_1 - (d, 0, l_1-l_2)\d l_2 \d l_1
        = (-d, 0, 0)\d l_1 \d l_2

    {\bf F}
        = {\mu_o I_1 I_2\over 4\pi} \int \int {
            \d {\bf l}_2 (\d {\bf l}_1 \cdot ({\bf l}_1 - {\bf l}_2)) -
            ({\bf l}_1 - {\bf l}_2) (\d {\bf l}_2 \cdot\d {\bf l}_1)
                \over |{\bf l}_1 - {\bf l}_2|^3 } =

        = {\mu_o I_1 I_2\over 4\pi} \int \int {
            (-d, 0, 0)\d l_1 \d l_2
                \over (d^2 + (l_1 - l_2)^2)^{3\over 2} } =

        = (-1, 0, 0){\mu_o I_1 I_2\over 4\pi} \int \d l_1
            \int_{-\infty}^\infty \d l_2 {
            d
                \over (d^2 + (l_1 - l_2)^2)^{3\over 2} } =

        = (-1, 0, 0){\mu_o I_1 I_2\over 4\pi} \int \d l_1
            {2\over d} =

        = (-1, 0, 0){\mu_o I_1 I_2\over 2\pi d} \int \d l_1

Where we used the value of the folowing integral:

.. math::

    \int_{-\infty}^\infty \d l_2 {d \over (d^2 + (l_1 - l_2)^2)^{3\over 2} }
        = \int_{-\infty}^\infty \d x {d \over (d^2 + x^2)^{3\over 2} } =

        = \left[x\over d \sqrt{d^2 + x^2}\right]_{-\infty}^\infty
        = \left[\sign x\over d \sqrt{\left(d\over x\right)^2 + 1}
            \right]_{-\infty}^\infty =

        = {1\over d} - \left(-{1\over d}\right) = {2\over d}

As such, the direction of the force on the first wire (at coordinates $({d\over
2}, 0, 0)$ going in the $z$ direction) will be to the left and the force per
unit length is:

.. math::

    F_m = {\mu_o I_1 I_2\over 2\pi d}

Because the second wire is at the coordinates $(-{d\over
2}, 0, 0)$ and the force on the first wire is in the direction
$(-1, 0, 0)$, the force between the wires is attractive, as long as $I_1$ and
$I_2$ have the same sign (either both currents go up, or both down)
and repulsive if $I_1$ and $I_2$ have opposite signs.

Let $d=1\rm\,m$, $I_1 = I_2 = 1\rm\, A$, then the force is attractive and
(we also use $\mu_0 = 4\pi \cdot 10^{-7}$):

.. math::

    F_m = {4\pi \cdot 10^{-7} \over 2\pi} {\rm\, N \cdot m^{-1}}
        = 2 \cdot 10^{-7} {\rm\, N \cdot m^{-1}}

Perpendicular Straight Wires
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We calculate the force between two perpendicular straight infinite wires:

.. math::

    {\bf l}_1 = ({d\over 2}, 0, l_1)

    \d{\bf l}_1 = (0, 0, \d l_1)

    {\bf l}_2 = (-{d\over 2}, l_2, 0)

    \d{\bf l}_2 = (0, \d l_2, 0)

    {\bf l}_1 - {\bf l}_2 = (d, -l_2, l_1)

    \d {\bf l}_2 (\d {\bf l}_1 \cdot ({\bf l}_1 - {\bf l}_2)) -
    ({\bf l}_1 - {\bf l}_2) (\d {\bf l}_2 \cdot\d {\bf l}_1)
        = (0, \d l_2, 0) l_1\d l_1
        = (0, l_1, 0)\d l_1 \d l_2

    {\bf F}
        = {\mu_o I_1 I_2\over 4\pi} \int \int {
            \d {\bf l}_2 (\d {\bf l}_1 \cdot ({\bf l}_1 - {\bf l}_2)) -
            ({\bf l}_1 - {\bf l}_2) (\d {\bf l}_2 \cdot\d {\bf l}_1)
                \over |{\bf l}_1 - {\bf l}_2|^3 } =

        = {\mu_o I_1 I_2\over 4\pi} \int \int {
            (0, l_1, 0)\d l_1 \d l_2
                \over (d^2 + l_1^2 + l_2^2)^{3\over 2} } =

        = (0, 1, 0){\mu_o I_1 I_2\over 4\pi} \int_{-\infty}^\infty \d l_1
            \int_{-\infty}^\infty \d l_2 {
            l_1
                \over (d^2 + l_1^2 +l_2^2)^{3\over 2} } =

        = (-1, 0, 0){\mu_o I_1 I_2\over 4\pi} \int_{-\infty}^\infty \d l_1
            {2 l_1\over d^2 + l_1^2}
            =

        = 0

The integral is an odd functin of $l_1$, so it is zero.  We used the value of
the folowing integral (but in fact it is already seen before this integral is
needed that the double integral must be zero):

.. math::

    \int_{-\infty}^\infty \d l_2 {l_1 \over (d^2 + l_1^2 + l_2^2)^{3\over 2} }

        = \left[l_1 l_2\over (d^2+l_1^2) \sqrt{d^2 +l_1^2 + l_2^2}
            \right]_{-\infty}^\infty
        = \left[l_1 \sign l_2\over (d^2+l_1^2)
            \sqrt{\left(d\over l_2\right)^2 + \left(l_1\over l_2\right)^2 + 1}
            \right]_{-\infty}^\infty =

        = {l_1\over d^2+l_1^2} - \left(-{l_1\over d^2 + l_1^2}\right)
        = {2 l_1\over d^2 + l_1^2}

As such, there will be no net force.

Infinitely Long Wire and a Square Loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We calculate the net force on a square loop with current $I_1$ of side $a$,
whose center is $d$ far from an infinitely long wire with current $I_2$:

The wire has coordinates $(0, 0, z)$ and the magnetic field from it is (see the
example above):

.. math::

    {\bf B}(x, 0, z) = (0, -1, 0) {\mu_0 I \over 2\pi x}

The four sides of the loop are ($0 \le l_1 \le a$):

.. math::

    {\bf l}_1 = (d-{a\over 2}+l_1, 0, {a\over2})

    {\bf l}_1 = (d+{a\over 2}, 0, {a\over2}-l_1)

    {\bf l}_1 = (d+{a\over 2}-l_1, 0, -{a\over2})

    {\bf l}_1 = (d-{a\over 2}, 0, -{a\over2}+l_1)

and the differentials are:

.. math::

    \d {\bf l}_1 = (1, 0, 0) \d l_1

    \d {\bf l}_1 = (0, 0, -1) \d l_1

    \d {\bf l}_1 = (-1, 0, 0) \d l_1

    \d {\bf l}_1 = (0, 0, 1) \d l_1

The net force on the loop is:

.. math::

    {\bf F} = I_1 \int \d {\bf l}_1 \times {\bf B}
        = I_1 \int \d {\bf l}_1 \times (0, -1, 0) {\mu_0 I_2 \over 2\pi
            ({\bf l}_1)_x} =

        = {\mu_0 I_1 I_2\over 2\pi}\left(
            \int_0^a {(0, 0, 1)\d l_1\over d-{a\over 2} + l_1}
            +\int_0^a {(1, 0, 0)\d l_1\over d+{a\over 2}}
            +\int_0^a {(0, 0, -1)\d l_1\over d+{a\over 2}-l_1}
            +\int_0^a {(-1, 0, 0)\d l_1\over d-{a\over 2}}
            \right) =

        = {\mu_0 I_1 I_2\over 2\pi}\left(
            (0, 0, 1)\left[\log \left| d-{a\over 2} + l_1 \right|
                -\log \left|d + {a\over 2} - l_1\right| \right]_0^a
            +(1, 0, 0)\left({a\over d + {a\over 2}}-{a\over d - {a\over 2}}
                \right)\right) =

        = {\mu_0 I_1 I_2\over 2\pi}\left(
            (0, 0, 1) \cdot 0 +
            (1, 0, 0){a^2\over d^2 - \left({a\over 2}\right)^2}
                \right) =

        = (1, 0, 0){\mu_0 I_1 I_2\over 2\pi}
            {a^2\over d^2 - \left({a\over 2}\right)^2}

Magnetic Dipole
~~~~~~~~~~~~~~~

.. math::

    {\bf A}({\bf r}) = {\mu_0\over 4\pi} {{\bf m}\times{\bf r}\over r^3}

    {\bf B}({\bf r}) = \nabla\times {\bf A}
    = {\mu_0\over 4\pi} \nabla\times
        \left({{\bf m}\times{\bf r}\over r^3}\right) =

    = {\mu_0\over 4\pi} \left({\bf m}\nabla\cdot\left({\bf r}\over r^3\right)
        -{\bf m}\cdot\nabla\left({\bf r}\over r^3\right)
        \right) =

    = {\mu_0\over 4\pi} \left({\bf m}\left(\left(\nabla{1\over r^3}\right)
            \cdot{\bf r}+{1\over r^3}\nabla\cdot{\bf r}\right)
        -{\bf m}\cdot\left(\left(\nabla{1\over r^3}\right)
            {\bf r}+{1\over r^3}\nabla{\bf r}\right)\right)
        =

    = {\mu_0\over 4\pi} \left({\bf m}\left(\left(-{3{\bf r}\over r^5}\right)
            \cdot{\bf r}+{1\over r^3}3\right)
        -{\bf m}\cdot\left(\left(-{3{\bf r}\over r^5}\right)
            {\bf r}+{1\over r^3}\one\right)\right)
        =

    = {\mu_0\over 4\pi} \left({\bf m}\left(-{3\over r^3}+{3\over r^3}\right)
        +{\bf m}\cdot\left({3{\bf r}{\bf r}\over r^5}-{\one\over r^3}\right)
        \right)
        =

    = {\mu_0\over 4\pi} \left({3{\bf r}({\bf m}\cdot{\bf r})\over r^5}
        -{{\bf m}\over r^3}\right)

Bar Magnet
~~~~~~~~~~

A good model of a bar magnet of the length $L$ and width $W$ is a combination
of two magnetic monopoles (that sit inside the magnet, so one cannot actually
see them, just their behavior outside the magnet):

.. math::

    {\bf B}({\bf x}) = {\mu_0 Q_m\over 4\pi} \left(
        {{\bf x}-{\bf p}_1 \over |{\bf x}-{\bf p}_1|^3}
        -
        {{\bf x}-{\bf p}_2 \over |{\bf x}-{\bf p}_2|^3}
        \right)

where:

.. math::

    {\bf p}_1 = (0, 0, d)

    {\bf p}_2 = (0, 0, -d)

    d = {L-W\over 2}

The magnetic moment vector is:

.. math::

    {\bf m} = Q_m ({\bf p}_1 - {\bf p}_2)

and its magnitude then is:

.. math::

    m = 2 Q_m d

The permeability is:

.. math::

    \mu_0 = 4\pi \cdot 10^{-7}{\rm\,H\cdot m^{-1}}
        = 4\pi \cdot 10^{-7}{\rm\,V\cdot s\cdot A^{-1}\cdot m^{-1}}

For a typical bar magnet, we have for example:

.. math::

    L &= 5{\rm\,cm} \\
    W &= 1{\rm\,cm} \\
    Q_m &= 3.3{\rm\,A\cdot m} \\
    d &= {L-W\over2} = 0.02{\rm\,m} \\
    m &= 2 Q_m d = 2\times 3.3\times 0.02{\rm\,A\cdot m^2}
        = 0.132 {\rm\,A\cdot m^2}

The unit of ${\bf B}$ is Tesla: $\rm 1 T = V\cdot s \cdot m^{-2}$.

Bar Magnet in a Coil
~~~~~~~~~~~~~~~~~~~~

We throw a magnet through a coil and calculate the voltage on the coil.
We use two model of the bar magnet: a magnetic dipole and two monopoles $2d$
apart.

Geometry:

.. math::

    {\bf v} = (0, 0, v)

    {\bf l} = (a\cos\phi, a\sin\phi, z)

    {\d{\bf l}\over \d\phi} = (-a\sin\phi, a\cos\phi, 0)

Field of the dipole:

.. math::

    {\bf E} = 0

    {\bf B}({\bf r}) = {\mu_0\over 4\pi} \left({3{\bf r}({\bf m}\cdot{\bf r})\over r^5}
        -{{\bf m}\over r^3}\right)

    {\bf m} = (0, 0, m)

we will need:

.. math::

    {\bf v}\times{\bf B}({\bf l})
    = {\mu_0\over 4\pi}{\bf v}\times
        \left({3{\bf l}({\bf m}\cdot{\bf l})\over l^5}
    -{{\bf m}\over l^3}\right) =

    = {\mu_0\over 4\pi}
        \left({3({\bf v}\times{\bf l})({\bf m}\cdot{\bf l})\over l^5}
    -{{\bf v}\times{\bf m}\over l^3}\right) =

    = {\mu_0\over 4\pi}
        {3({\bf v}\times{\bf l})({\bf m}\cdot{\bf l})\over l^5}
        =

    = {\mu_0\over 4\pi}
        {3(va\sin\theta, -va\cos\theta, 0)mz\over (a^2 + z^2)^{5\over2}} =

    = {3\mu_0 m\over 4\pi}
        {a v z\over (a^2 + z^2)^{5\over2}} (\sin\theta, -\cos\theta, 0)

and

.. math::

    {\bf v}\times{\bf B}\cdot{\d{\bf l}\over \d\phi} =

    = {3\mu_0 m\over 4\pi}
        {a v z\over (a^2 + z^2)^{5\over2}} (\sin\theta, -\cos\theta, 0)
        \cdot
    (-a\sin\phi, a\cos\phi, 0) =

    = -{3\mu_0 m\over 4\pi}
        {a^2 v z\over (a^2 + z^2)^{5\over2}}

Field of two monopoles:

.. math::

    {\bf E} = 0

    {\bf B}({\bf x}) = {\mu_0 Q_m\over 4\pi} \left(
        {{\bf x}-{\bf p}_1 \over |{\bf x}-{\bf p}_1|^3}
        -
        {{\bf x}-{\bf p}_2 \over |{\bf x}-{\bf p}_2|^3}
        \right)

    {\bf p}_1 = (0, 0, d)

    {\bf p}_2 = (0, 0, -d)

    d = {L-W\over 2}

we will need:

.. math::

    {\bf v}\times{\bf B}({\bf l})
        = {\mu_0 Q_m\over 4\pi} \left(
        {{\bf v}\times({\bf l}-{\bf p}_1) \over |{\bf l}-{\bf p}_1|^3}
        -
        {{\bf v}\times({\bf l}-{\bf p}_2) \over |{\bf l}-{\bf p}_2|^3}
        \right) =

        = {\mu_0 Q_m\over 4\pi} \left(
        {(0, 0, v)\times(a\cos\phi, a\sin\phi, z-d) \over
            (a^2+(z-d)^2)^{3\over2}}
        -
        {(0, 0, v)\times(a\cos\phi, a\sin\phi, z+d) \over
            (a^2+(z+d)^2)^{3\over2}}
        \right) =

        = {\mu_0 Q_m a v \over 4\pi} \left(
        {1 \over (a^2+(z-d)^2)^{3\over2}}
        -
        {1 \over (a^2+(z+d)^2)^{3\over2}}
        \right) (\sin\phi, -\cos\phi, 0)

and

.. math::

    {\bf v}\times{\bf B}\cdot{\d{\bf l}\over \d\phi} =

    = {\mu_0 Q_m a v \over 4\pi} \left(
    {1 \over (a^2+(z-d)^2)^{3\over2}}
    -
    {1 \over (a^2+(z+d)^2)^{3\over2}}
    \right) (\sin\phi, -\cos\phi, 0)
        \cdot
    (-a\sin\phi, a\cos\phi, 0) =

    = -{\mu_0 Q_m a^2 v \over 4\pi} \left(
    {1 \over (a^2+(z-d)^2)^{3\over2}}
    -
    {1 \over (a^2+(z+d)^2)^{3\over2}}
    \right)

Now we can calculate the voltage:

.. math::

    V = \oint \left({\bf E} + {\bf v}\times{\bf B}\right) \cdot {\d{\bf l}} =

        = \oint {\bf v}\times{\bf B} \cdot {\d{\bf l}} =

        = \int_0^{2\pi} {\bf v}\times{\bf B} \cdot {\d{\bf l}\over \d\phi}
            \d\phi

for the dipole we get

.. math::

        V = \cdots
        = -\int_0^{2\pi} {3\mu_0 m\over 4\pi}
        {a^2 v z\over (a^2 + z^2)^{5\over2}}
            \d\phi =

        = -{3\mu_0 m\over 2}
        {a^2 v z\over (a^2 + z^2)^{5\over2}}

For two monopoles we get

.. math::

        V = \cdots
        = -\int_0^{2\pi} {\mu_0 Q_m a^2 v \over 4\pi} \left(
            {1 \over (a^2+(z-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z+d)^2)^{3\over2}}
            \right)
            \d\phi =

        = -{\mu_0 Q_m a^2 v \over 2} \left(
            {1 \over (a^2+(z-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z+d)^2)^{3\over2}}
            \right)


For the dipole, the function

.. math::

    {z\over(a^2+z^2)^{5\over 2}}

has a maximum and minimum for:

.. math::

    z = \pm{a\over 2}

with the max value:

.. math::

    {z\over(a^2+z^2)^{5\over 2}} =
    {{a\over 2}\over(a^2+\left({a\over 2}\right)^2)^{5\over 2}} =
    {16\sqrt 5 \over 125 a^4}

Code::

    >>> from sympy import var, solve, S, refine, Q
    >>> var("a z")
    (a, z)
    >>> f = z / (a**2+z**2)**(S(5)/2)
    >>> solve(f.diff(z), z)
    [-a/2, a/2]
    >>> f.subs(z, a/2)
    16*sqrt(5)*a/(125*(a**2)**(5/2))
    >>> refine(f.subs(z, a/2), Q.positive(a))
    16*sqrt(5)/(125*a**4)


So the maximum voltage is:

.. math::

    V = {\mu_0\over 2} {3va^2mz\over (a^2 + z^2)^{5\over2}}
        = {\mu_0\over 2} {3mva^2 {16\sqrt 5 \over 125 a^4}} =

        = {24\sqrt 5\over125} {\mu_0 m v\over a^2}

If we drop the magnet from height $h$ above the coil into it, then its speed
will be $v_0 = \sqrt{2hg}$ in the middle of the coil, when $t=0$. Then:

.. math::

    z = v_0 t + \half g t^2

    v = v_0 + g t

And we get for the voltage dependence for dipole:

.. math::

    V = - {\mu_0\over 2} {3va^2mz\over (a^2 + z^2)^{5\over2}}
        =- {\mu_0\over 2} {3(v_0+gt)a^2m(v_0 t + \half g t^2)\over
             (a^2 + (v_0 t + \half g t^2)^2)^{5\over2}}

The time difference between the maximum and minimum is the time difference
between $z=-{a\over2}$ and $z=+{a\over2}$, so:

.. math::

    \Delta t = \sqrt{2h+a\over g} - \sqrt{2h-a\over g}

The total flux doesn't depend on the particular dependence of $z(t)$ and
$v(t)$:

.. math::

    \Phi = \int_0^\infty V(t) \d t =

        = - {3\mu_0 m\over 2} \int_0^\infty{v(t)a^2z(t)
                \over (a^2 + z(t)^2)^{5\over2}} \d t =

        = - {3\mu_0 m\over 2} \int_0^\infty{{\d z\over\d t}a^2z(t)
                \over (a^2 + z(t)^2)^{5\over2}} \d t =

        = - {3\mu_0 m\over 2} \int_0^\infty{a^2z
                \over (a^2 + z^2)^{5\over2}} \d z =

        = - {3\mu_0 m\over 4} \int_{a^2}^\infty{a^2
                \over u^{5\over2}} \d u =

        = - {3\mu_0 m a^2\over 4} \left(-{2\over 3}\right)
            \left[1\over u^{3\over2}\right]_{a^2}^\infty =

        = - {3\mu_0 m a^2\over 4} \left(-{2\over 3}\right)
            \left[-1\over a^3\right] =

        = - {\mu_0 m \over 2a}

For the voltage dependence of two monopoles, we get:

.. math::

    V = -{\mu_0 Q_m a^2 v \over 2} \left(
            {1 \over (a^2+(z-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z+d)^2)^{3\over2}}
            \right) =

    = -{\mu_0 Q_m a^2 (v_0+gt) \over 2} \left(
            {1 \over (a^2+(v_0 t + \half g t^2-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(v_0 t + \half g t^2+d)^2)^{3\over2}}
            \right)

The total flux doesn't depend on the particular dependence of $z(t)$ and
$v(t)$:

.. math::

    \Phi = \int_0^\infty V(t) \d t =

        =-\int_0^\infty {\mu_0 Q_m a^2 v(t) \over 2} \left(
            {1 \over (a^2+(z(t)-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z(t)+d)^2)^{3\over2}}
            \right)
            \d t =

        =-\int_0^\infty {\mu_0 Q_m a^2 {\d z\over \d t} \over 2} \left(
            {1 \over (a^2+(z(t)-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z(t)+d)^2)^{3\over2}}
            \right)
            \d t =

        =-\int_0^\infty {\mu_0 Q_m a^2 \over 2} \left(
            {1 \over (a^2+(z-d)^2)^{3\over2}}
            -
            {1 \over (a^2+(z+d)^2)^{3\over2}}
            \right)
            \d z =

        =- {\mu_0 Q_m a^2 \over 2} \left(
            \int_0^\infty{1 \over (a^2+(z-d)^2)^{3\over2}} \d z
            -
            \int_0^\infty{1 \over (a^2+(z+d)^2)^{3\over2}} \d z
            \right) =

        =- {\mu_0 Q_m a^2 \over 2} \left(
            {1\over a^2}\left(1 + {d\over\sqrt{a^2 + d^2}}\right)
            -
            {1\over a^2}\left(1 - {d\over\sqrt{a^2 + d^2}}\right)
            \right) =

        =- {\mu_0 Q_m d\over\sqrt{a^2 + d^2}}

Note that in the limit $d\to 0$, we get the magnetic moment $m = 2 d Q_m$ and
the last formula for two monopoles flux becomes the dipole flux.

As a particular example, consider a coil with $N=500$ loops, $a=1.4\rm\,cm$,
$d=1.8\rm\,cm$, $Q_m=43\rm\,A\cdot m$. Then the total flux from the second peak
is:

.. math::

    \Phi =- {N\mu_0 Q_m d\over\sqrt{a^2 + d^2}} = -0.021 \rm\, V\cdot s

Code::

    >>> from math import pi, sqrt
    >>> mu0 = 4*pi*1e-7
    >>> cm = 0.01
    >>> Q_m = 43.
    >>> d = 1.8*cm
    >>> a = 1.4*cm
    >>> N = 500
    >>> -N*mu0*Q_m*d/sqrt(a**2+d**2)
    -0.02132647889395681

For a single loop with $a=1.25\rm\,cm$ we get:

.. math::

    \Phi =- {\mu_0 Q_m d\over\sqrt{a^2 + d^2}} = -4.44\times 10^{-5}
        \rm\, V\cdot s

and for a single loop with $a=1.8\rm\,cm$ we get:

.. math::

    \Phi =- {\mu_0 Q_m d\over\sqrt{a^2 + d^2}} = -3.82\times 10^{-5}
        \rm\, V\cdot s

Code::

    >>> a = 1.25*cm
    >>> -mu0*Q_m*d/sqrt(a**2+d**2)
    -4.438304942066266e-05
    >>> a = 1.8*cm
    >>> -mu0*Q_m*d/sqrt(a**2+d**2)
    -3.820879326816195e-05



RC Circuit
~~~~~~~~~~

Let's consider resistor (with voltage $V=RI$) and capacitor (with voltage
$V={Q\over C}$ and current $I(t) = Q'(t)$) in a series. Voltage on the battery
is $V$, then the equation for the circuit is:

.. math::

    RI(t) + {Q(t)\over C} = V

with initial condition $Q(0) = 0$. We differentiate it:

.. math::

    RI'(t) + {I(t)\over C} = 0

and the initial condition follows from the first equation $I(0) = {V\over R}$.
The solution is:

.. math::

    I(t) = {V\over R} e^{-{t\over RC}}

Now we calculate the charge (using the initial condition for the charge above
for the lower bound of the integral):

.. math::

    Q(t) = \int_0^t I(t') \d t'
         = {V\over R} \int_0^t e^{-{t'\over RC}} \d t'
         = {V\over R} \left[-RC e^{-{t'\over RC}}\right]_0^t =

         = {V\over R} \left[-RC e^{-{t\over RC}}+RC\right]
         = VC \left(1-e^{-{t\over RC}}\right)

The voltage on the resistor is:

.. math::

    R I(t) = R {V\over R} e^{-{t\over RC}} = V e^{-{t\over RC}}

The voltage on the capacitor is:

.. math::

    {Q(t)\over C} = {VC \left(1-e^{-{t\over RC}}\right) \over C}
        = V \left(1-e^{-{t\over RC}}\right)

Half life of the capacitor is defined as the time $\tau$ so that the charge is
half of the total charge, and we get:

.. math::

    Q(\tau) = \half Q(\infty)

    VC \left(1-e^{-{\tau\over RC}}\right) = \half VC

    1-e^{-{\tau\over RC}} = \half

    \half = e^{-{\tau\over RC}}

    \log \half = -{\tau\over RC}

    \tau = -RC \log \half = RC\log 2


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
doping concetration ($C=p_D-n_A$ where $p_D$ is the concentration of ionized
donors, charged positive, and $n_A$ is the concentration of ionized acceptors,
charged negative) and $q$ is the electron charge (positive). We get:

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
generated using ${\bf E}$ and $n$ and $p$. A drift-diffusion model is to assume
a drift current ($q\mu_n n {\bf E}$) and a diffusion ($q D_n \nabla n$),
which gives:

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

    {\partial n\over\partial t} = -R + \nabla\cdot (\mu_n n {\bf E})
        +\nabla\cdot (D_n \nabla n)

    {\partial p\over\partial t} = -R - \nabla\cdot (\mu_p p {\bf E})
        +\nabla\cdot (D_p \nabla p)

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n + C)

And it is usually assumed that the magnetic field is time independent, so
${\bf E}=-\nabla\phi$ and we get:

.. math::
    :label: semicond-eq

    {\partial n\over\partial t} = -R - \nabla\cdot (\mu_n n \nabla\phi)
        +\nabla\cdot (D_n \nabla n)

    {\partial p\over\partial t} = -R + \nabla\cdot (\mu_p p \nabla\phi)
        +\nabla\cdot (D_p \nabla p)

    \nabla\cdot(\varepsilon \nabla\phi) = -q(p-n + C)

These are three nonlinear (due to the terms $\mu_n n \nabla\phi$ and
$\mu_p p \nabla\phi$) equations for three unknown functions $n$, $p$ and $\phi$.

Example 1
~~~~~~~~~

We can substract the first two
equations and we get:

.. math::

    {\partial q(p-n)\over\partial t} = - q\nabla\cdot ((\mu_p p+\mu_n n){\bf E})
        +q\nabla\cdot(D_p \nabla p-D_n\nabla n)

    \nabla\cdot(\varepsilon {\bf E}) = q(p-n+C)

and using $\rho=q(p-n+C)$ and $\sigma=q(\mu_p p+\mu_n n)$, we get:

.. math::

    {\partial \rho\over\partial t} -q{\partial C\over\partial t} =
        - \nabla\cdot (\sigma {\bf E})
        +q\nabla\cdot(D_p \nabla p-D_n\nabla n)

    \nabla\cdot(\varepsilon {\bf E}) = \rho

So far we didn't make any assumptions. Most of the times the net doping
concetration $C$ is time independent, which gives:

.. math::

    {\partial \rho\over\partial t} =
        - \nabla\cdot (\sigma {\bf E})
        +q\nabla\cdot(D_p \nabla p-D_n\nabla n)

    \nabla\cdot(\varepsilon {\bf E}) = \rho

Assuming further $D_p \nabla p-D_n\nabla n=0$, we just get the equation of
continuity and the Gauss law:

.. math::

    {\partial \rho\over\partial t} + \nabla\cdot (\sigma {\bf E}) = 0

    \nabla\cdot(\varepsilon {\bf E}) = \rho

Finally, assuming also that that $\rho$ doesn't depend on
time, we get:

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

Example 3
---------

Let's calculate the 1D pn-junction. We take the equations :eq:`semicond-eq` and
write them in 1D for the stationary state
(${\partial n\over\partial t}={\partial p\over\partial t}=0$):

.. math::

    0 = -R - (\mu_n n \phi')' + (D_n n')'

    0 = -R + (\mu_p p \phi')' + (D_p p')'

    (\varepsilon \phi')' = -q(p-n + C)

We expand the derivatives and assume that $\mu$ and $D$ is constant:

.. math::

    0 = -R - \mu_n n' \phi' - \mu_n n \phi'' + D_n n''

    0 = -R + \mu_p p' \phi' + \mu_p p \phi'' + D_p p''

    \varepsilon \phi'' = -q(p-n + C)

and we put the second derivatives on the left hand side:

.. math::
    :label: 1d-pn-junction1

    n'' = {1\over D_n}(R + \mu_n n' \phi' + \mu_n n \phi'')

    p'' = {1\over D_p}(R - \mu_p p' \phi' - \mu_p p \phi'')

    \phi'' = -{q\over\varepsilon} (p-n + C)

now we introduce the variables $y_i$:

.. math::

    y_0 = n

    y_1 = y_0' = n'

    y_2 = p

    y_3 = y_2' = p'

    y_4 = \phi

    y_5 = y_4' = \phi'

and rewrite :eq:`1d-pn-junction1`:

.. math::

    y_1' = {1\over D_n}(R + \mu_n y_1 y_5 + \mu_n y_0 y_5')

    y_3' = {1\over D_p}(R - \mu_p y_3 y_5 - \mu_p y_2 y_5')

    y_5' = -{q\over\varepsilon} (y_2-y_0 + C)

So we are solving the following six nonlinear first order ODE:

.. math::
    :label: 1d-pn-junction2

    y_5' = -{q\over\varepsilon} (y_2-y_0 + C)

    y_0' = y_1

    y_1' = {1\over D_n}(R + \mu_n y_1 y_5 + \mu_n y_0 y_5')

    y_2' = y_3

    y_3' = {1\over D_p}(R - \mu_p y_3 y_5 - \mu_p y_2 y_5')

    y_4' = y_5
