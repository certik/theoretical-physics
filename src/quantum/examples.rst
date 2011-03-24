========
Examples
========

Two Particles in Harmonic Potential
===================================

It is a 1D, two-body problem with an interacting Hamiltonian

.. math::

    H(x_1, x_2) = -\half{\partial^2\over\partial x_1^2}
    -\half{\partial^2\over\partial x_2^2}
        +{1\over|x_1 - x_2|} + \half\omega^2 x_1^2 + \half\omega^2 x_2^2

and it can be solved analytically. The Schrödinger equation is

.. math::

    \left(-\half{\partial^2\over\partial x_1^2} -\half{\partial^2\over\partial x_2^2}
        +{1\over|x_1 - x_2|} + \half\omega^2 x_1^2 + \half\omega^2 x_2^2
    \right)\Psi(x_1, x_2) = E \Psi(x_1, x_2)

we use the substitution:

.. math::

    u = {1\over\sqrt2}(x_1 - x_2)

    v = {1\over\sqrt2}(x_1 + x_2)

then

.. math::

    {\partial^2\over\partial x_1^2} + {\partial^2\over\partial x_2^2}=
    {\partial^2\over\partial u^2} + {\partial^2\over\partial v^2}

    |x_1 - x_2| = \sqrt2|u|

    x_1^2 + x_2^2 = u^2 + v^2

and

.. math::

    \left(-\half{\partial^2\over\partial u^2} -\half{\partial^2\over\partial v^2}
        +{1\over\sqrt2 |u|} + \half\omega^2 u^2 + \half\omega^2 v^2
    \right)\Psi(u, v) = E \Psi(u, v)

Note also the symmetry of the Hamiltonian $H(x_1, x_2) = H(x_2, x_1)$ which
after substitution is equivalent to $H(u, v) = H(-u, v)$.
Now we can separate the equation:

.. math::

    \Psi(u, v) = f(u)g(v)

    \left(-\half{\d^2\over\d u^2} +{1\over\sqrt2 |u|} + \half\omega^2 u^2
    \right)f_k(u) = \epsilon_k f_k(u)

    \left(-\half{\d^2\over\d v^2} + \half\omega^2 v^2
    \right)g_l(v) = \epsilon_l g_l(v)

    E_{kl} = \epsilon_k + \epsilon_l

the solution of the second equation is:

.. math::

    g_l(v) = {1\over\sqrt{2^l l!}} \left(\omega\over\pi\right)^{1\over4}
        e^{-{\omega v^2\over2}} H_l(\sqrt\omega v)

    \epsilon_l = \omega(l+\half)\quad\mbox{for $l=0, 1, 2, \dots$}

where $H_n(x)$ are the Hermite polynomials:

.. math::

    H_n(x) = (-1)^n e^{x^2} {\d^n\over\d x^n} e^{-x^2}

The solution to the first equation can be approximated around the minimum of
the potential, which occurs at point $u=u_0$ (since the potential is symmetric
with respect to $u$, we only treat the branch $u>0$):

.. math::

    V(u) = {1\over\sqrt2 |u|} + \half\omega^2 u^2 =
        \left(2^{-{1\over 3}} + 2^{-{4\over3}}\right) \omega^{2\over3}
        +{3\over 2}\omega^2(u-u_0)^2
        +O\left((u-u_0)^3\right)

    u_0 = 2^{-{1\over6}}\omega^{-{2\over3}}

So the first few states can be approximated by the harmonic oscillator
solution with frequency $\sqrt3\omega$:

.. math::

    f_k(u) = {1\over\sqrt{2^k k!}} \left(\sqrt3\omega\over\pi\right)^{1\over4}
        e^{-{\sqrt3\omega (u-u_0)^2\over2}} H_k(3^{1\over4}\sqrt\omega (u-u_0))

    \epsilon_k =
        \left(2^{-{1\over 3}} + 2^{-{4\over3}}\right) \omega^{2\over3}
        +
        \sqrt3\omega(k+\half)\quad\mbox{for $k=0, 1, 2, \dots$}

The final solution is then:

.. math::

    \Psi_{kl}(u, v) = f_k(u) g_l(v) =

        =
        {1\over\sqrt{2^k k!}} \left(\sqrt3\omega\over\pi\right)^{1\over4}
        e^{-{\sqrt3\omega (u-u_0)^2\over2}} H_k(3^{1\over4}\sqrt\omega (u-u_0))
        {1\over\sqrt{2^l l!}} \left(\omega\over\pi\right)^{1\over4}
        e^{-{\omega v^2\over2}} H_l(\sqrt\omega v)

    E_{kl} = \epsilon_k + \epsilon_l =
        \left(2^{-{1\over 3}} + 2^{-{4\over3}}\right) \omega^{2\over3}
        +
        \sqrt3\omega(k+\half)
        +
        \omega(l+\half)


Quantum Harmonic Oscillator
===========================


The quantum
harmonic oscillator for one particle in 1D is:

.. math::

     i\hbar{\partial\over\partial t}\psi(x, t)= -{\hbar^2\over2m}{\partial^2\over\partial x^2}\psi(x,t)+V(x)\psi(x,t)


.. math::

     V(x)={1\over2}m\omega^2x^2

This is a partial differential equation for the time evolution of the wave
function $\psi(x, t)$, but one method to solve it is the
eigenvalues expansion:

.. math::

    \psi(x,t) = \sum_E c_E\psi_E(x)e^{-{i\over\hbar}Et}

where the sum goes over the whole spectrum (for continuous spectrum the sum
turns into an integral), the $c_E$ coefficients are determined from the initial condition
and $\psi_E(x)$ satisfies the one dimensional one particle time independent
Schrödinger equation:

.. math::

     -{\hbar^2\over2m}{\d^2\over\d x^2}\psi_E(x)+V(x)\psi_E(x)=E\psi_E(x)

and this is just an ODE and thus can be solved with Hermes1D. There can be many
types of boundary conditions for this equation, depending on the physical
problem, but in our case we simply have $\lim_{x\to\pm\infty}\psi_E(x)=0$ and
the normalization condition $\int_{-\infty}^\infty|\psi_E(x)|^2\d x=1$.

We can set $m=\hbar=1$ and from now on we'll just write $\psi(x)$ instead of
$\psi_E(x)$:

.. math::

     -{1\over2}{\d^2\over\d x^2}\psi(x)+V(x)\psi(x)=E\psi(x)

and we will solve it on the interval $(a, b)$ with the boundary condition
$\psi(a)=\psi(b)=0$. The weak formulation is

.. math::

     \int_a^b{1\over2}{\d\psi(x)\over\d x}{\d v(x)\over\d x}+V(x)\psi(x)v(x)\,\d x -\left[{\d\psi(x)\over\d x}v(x)\right]^a_b =E\int_a^b\psi(x)v(x)\,\d x

but due to the boundary condition $v(a)=v(b)=0$ so
$\left[\psi'(x)v(x)\right]^a_b=0$ and we get

.. math::

     \int_a^b{1\over2}{\d\psi(x)\over\d x}{\d v(x)\over\d x}+V(x)\psi(x)v(x)\,\d x =E\int_a^b\psi(x)v(x)\,\d x

And the finite element formulation is then $\psi(x)=\sum_j y_j\phi_j(x)$ and
$v=\phi_i(x)$:

.. math::

     \left(\int_a^b{1\over2}\phi_i'(x)\phi_j'(x)+V(x)\phi_i(x)\phi_j(x)\,\d x\right) y_j =E\int_a^b\phi_i(x)\phi_j(x)\,\d x\ y_j

which is a generalized eigenvalue problem:

.. math::

     A_{ij}y_j=EB_{ij}y_j

with

.. math::

     A_{ij}=\int_a^b{1\over2}\phi_i'(x)\phi_j'(x)+V(x)\phi_i(x)\phi_j(x)\,\d x


.. math::

     B_{ij}=\int_a^b\phi_i(x)\phi_j(x)\,\d x



Radial Schrödinger Equation
=============================


Another important example is the three dimensional one particle time
independent Schrödinger equation for a spherically symmetric potential:

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

The solution is then:

.. math::

    \psi({\bf x})=\sum_{nlm}c_{nlm}R_{nl}(r)Y_{lm}\left({\bf x}\over r\right)

where $R_{nl}(r)$ satisfies the radial Schrödinger equation (from now on we
just write $R(r)$):

.. math::

    -{1\over2}R''(r)-{1\over r}R'(r)+\left(V+{l(l+1)\over2r^2}\right)R(r)=ER(r)

Again there are many types of boundary conditions, but the most common case is
$\lim_{r\to\infty}R(r)=0$ and $R(0)=1$ or $R(0)=0$. One solves this equation on
the interval $(0, a)$ for large enough $a$.

The procedure is similar to the previous example, only we need to remember that
we always have to use covariant integration (in the previous example the
covariant integration was the same as the coordinate integration),
in this case $r^2\sin\theta \d
r\d\theta\d\phi$, so the weak formulation is:

.. math::

    \int \left(-{1\over2}R''(r)-{1\over r}R'(r)+\left(V+{l(l+1)\over2r^2}\right)R(r)\right)v(r)r^2\sin\theta \d r\d\theta\d\phi=


.. math::

     =\int ER(r) v(r)r^2\sin\theta \d r\d\theta\d\phi

Integrating over the angles gives $4\pi$ which we cancel out at both sides and
we get:

.. math::

    \int_0^a \left(-{1\over2}R''(r)-{1\over r}R'(r)+\left(V+{l(l+1)\over2r^2}\right)R(r)\right)v(r)r^2 \d r=


.. math::

     =E\int_0^a R(r) v(r)r^2 \d r

We apply per partes to the first two terms on the left hand side:

.. math::

    \int_0^a \left(-{1\over2}R''(r)-{1\over r}R'(r)\right)v(r)r^2 \d r =\int_0^a -{1\over2r^2}\left(r^2 R'(r)\right)'v(r)r^2 \d r=


.. math::

     =\int_0^a -{1\over2}\left(r^2 R'(r)\right)'v(r) \d r =\int_0^a {1\over2}r^2 R'(r)v'(r) \d r-{1\over2} [r^2R'(r)v(r)]_0^a=


.. math::

     =\int_0^a {1\over2} R'(r)v'(r) r^2\d r -{1\over2} a^2R'(a)v(a)

We used the fact that $\lim_{r\to0} r^2 R'(r) = 0$. If we also prescribe the
boundary condition $R'(a)=0$, then the boundary term vanishes completely. The
weak formulation is then:

.. math::

    \int_0^a {1\over2}R'(r)v'(r)r^2+ \left(V+{l(l+1)\over2r^2}\right)R(r)v(r)r^2\,\d r = E\int_0^aR(r)v(r)r^2\,\d r

or

.. math::

    \int_0^a {1\over2}R'(r)v'(r)r^2+ V(r)R(r)v(r)r^2+{l(l+1)\over2} R(r)v(r)\,\d r = E\int_0^aR(r)v(r)r^2\,\d r

Another approach
~~~~~~~~~~~~~~~~

Another (equivalent) approach is to write a weak formulation for
the 3D problem in cartesian coordinates:

.. math::

     \int_\Omega{1\over2}\nabla\psi({\bf x})\nabla v({\bf x})+V(r)\psi({\bf x})v({\bf x})\,\d^3 x =E\int_\Omega\psi({\bf x})v({\bf x})\,\d^3 x

and only then transform to spherical coordinates:

.. math::

     \int_0^{2\pi}\d\varphi\int_0^\pi\d\theta\int_0^a\d r \left({1\over2}\nabla\psi({\bf x})\nabla v({\bf x})+V(r)\psi({\bf x})v({\bf x})\right)r^2\sin\theta=


.. math::

     = E\int_0^{2\pi}\d\varphi\int_0^\pi\d\theta\int_0^a\d r\, \psi({\bf x})v({\bf x})r^2\sin\theta

The 3d eigenvectors $\psi({\bf x})$ however are not spherically symmetric.
Nevertheless we can still proceed by choosing our basis as

.. math::

    v_{ilm}({\bf x})=\phi_{il}(r)Y_{lm}(\theta, \varphi)

and seek our solution as

.. math::

    \psi({\bf x})=\sum_{jlm}y_{jlm}\phi_{jl}(r)Y_{lm}(\theta, \varphi)

Using the properties of spherical harmonics and the gradient:

.. math::

    \int Y_{lm} Y_{l'm'} \sin\theta\,\d\theta\,\d\varphi= \delta_{ll'}\delta_{mm'}


.. math::

    \int r^2\nabla Y_{lm} \nabla Y_{l'm'} \sin\theta\,\d\theta\,\d\varphi= l(l+1)\delta_{ll'}\delta_{mm'}


.. math::

    \nabla f = {\partial f\over \partial r}\boldsymbol{\hat r} + {1\over r} {\partial f\over\partial\theta}\boldsymbol{\hat\theta}+{1\over r\sin\theta} {\partial f\over\partial\phi}\boldsymbol{\hat\phi}

the weak formulation becomes:

.. math::

     \left(\int_0^a {1\over2}r^2\phi_{il}'(r)\phi_{jl}'(r)+ {1\over2}X+ {l(l+1)\over2}\phi_{il}(r)\phi_{jl}(r)+ r^2V(r)\phi_{il}(r)\phi_{jl}(r)\,\d r\right)y_{jlm}=


.. math::

     = E\int_0^ar^2 \phi_{il}(r)\phi_{jl}(r)\,\d r\ y_{jlm}

where both $l$ and $m$ indices are given by the indices of the particular base
function $v_{ilm}$. The $X$ term is (schematically):

.. math::

    X=\int r^2\sin\theta(r)Y_{lm}(\theta,\varphi) (\phi_{il}\nabla\phi_{jl}+\nabla\phi_{il}\phi_{jl}) \nabla Y_{lm}

There is an interesting identity:

.. math::

    \int r{\bf \hat r} Y_{lm} \nabla Y_{l'm'} \sin\theta\,\d\theta\,\d\varphi= 0

But it cannot be applied, because we have one more $r$ in the expression.
Nevertheless the term is probably zero, as can be seen when we compare the weak
formulation to the one we got directly from the radial equation.

How Not To Derive The Weak Formulation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


If we forgot that we have to integrate covariantly, this section is devoted
to what happens if we integrate using the coordinate integration. We would get:

.. math::

    \int_0^a {1\over2}R'(x)v'(x)-{1\over r}R'(x)v(x)+ \left(V+{l(l+1)\over2r^2}\right)R(x)v(x)\,\d x = E\int_0^aR(x)v(x)\,\d x

Notice the matrix on the left hand side is not symmetric. There is another way
of writing the weak formulation by applying per-partes to the $R'(r)v(r)$ term:

.. math::

    -\int_0^a{1\over r}R'(x)v(x)\d x=


.. math::

     =\int_0^a{1\over r}R(x)v'(x)\d x -\int_0^a{1\over r^2}R(x)v(x)\d x -\left[{1\over r}R'(x)v'(x)\right]_0^a +\left[{1\over r^2}R'(x)v(x)\right]_0^a

We can use $v(a)=0$ and $R'(a)=0$ to simplify a bit:

.. math::

    -\int_0^a{1\over r}R'(x)v(x)\d x=


.. math::

     =\int_0^a{1\over r}R(x)v'(x)\d x -\int_0^a{1\over r^2}R(x)v(x)\d x +\lim_{r\to0}\left({R'(x)v'(x)\over r}-{R'(x)v(x)\over r^2}\right)

Since $R(x)\sim r^l$ near $r=0$, we can see that for $l\ge3$ the limits
on the right hand side are zero, but for $l=0, 1, 2$ they are not zero and need
to be taken into account. Let's assume $l\ge3$ for now, then our weak formulation looks like:

.. math::

    \int_0^a {1\over2}R'(x)v'(x)+{1\over r}R(x)v'(x)+ \left(V+{l(l+1)\over2r^2}-{1\over r^2}\right)R(x)v(x)\,\d x = E\int_0^aR(x)v(x)\,\d x

or

.. math::

    \int_0^a {1\over2}R'(x)v'(x)+{1\over r}R(x)v'(x)+ \left(V+{(l-2)(l+1)\over2r^2}\right)R(x)v(x)\,\d x = E\int_0^aR(x)v(x)\,\d x

The left hand side is also not symmetric, however we can now take an average of
our both weak formulations to get a symmetric weak formulation:

.. math::

    \int_0^a {1\over2}R'(x)v'(x)+{R(x)v'(x)-R'(x)v(x)\over 2r}+ \left(V+{l(l+1)-1\over2r^2}\right)R(x)v(x)\,\d x =


.. math::

     = E\int_0^aR(x)v(x)\,\d x

Keep in mind, that this symmetric version is only correct for $l\ge3$. For
$l<3$ we need to use our first nonsymmetric version.

As you can see, this is something very different to what we got in the previous
section. First there were lots of technical difficulties and second the final
result is wrong, since it doesn't correspond to the 3D Schrödinger equation.

Scattering in radial potential
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If $V=0$, the radial equation is:

.. math::

    -{1\over2}R_{El}''(r)-{1\over r}R_{El}'(r)+{l(l+1)\over2r^2} R_{El}(r)
        = E R_{El}(r)

The general solution is a linear combination of the spherical Bessel functions
$j_l(kr)$ and $n_l(kr)$:

.. math::

    R_{El}(r) = A_l j_l(kr) + B_l n_l(kr)

where $k=\sqrt{2E}$ and $E > 0$ is a continuous spectrum. The asymptotic expansion for $r\to\infty$ is:

.. math::

    j_l(kr)\to{1\over kr}\sin\left(kr-{l\pi\over 2}\right)

    n_l(kr)\to{1\over kr}\cos\left(kr-{l\pi\over 2}\right)

so we get for large $r$:

.. math::

    R_{El}(r) = A_l j_l(kr) + B_l n_l(kr) \to

    \to A_l {1\over kr}\sin\left(kr-{l\pi\over 2}\right)
        + B_l{1\over kr}\cos\left(kr-{l\pi\over 2}\right) =

    = \sqrt{A_l^2 + B_l^2} {1\over kr}\sin\left(kr-{l\pi\over 2}
        +\atan2(B_l, A_l)\right)
    = C_l {1\over kr}\sin\left(kr-{l\pi\over 2}-\delta_l\right)

where

.. math::

    \delta_l = -\atan2(B_l, A_l) = \atan2(-B_l, A_l)

    C_l = \sqrt{A_l^2 + B_l^2}

The $C_l$ and $\delta_l$ are physical variables, so we express $A_l$ and $B_l$
using them:

.. math::

    A_l = C_l \cos\delta_l

    B_l = -C_l \sin\delta_l

and write the exact solution $R_{El}$ as:

.. math::

    R_{El}(r) = C_l (\cos\delta_l\, j_l(kr) - \sin\delta_l\, n_l(kr))


We can then compare this to $\phi \approx e^{ikz} + f(\theta, \phi)
{e^{ikr}\over r}$, by expanding $e^{ikz} = e^{ikr\cos\theta}=
\sum (2l+1) i^l j_l(kr)P_l(\cos\theta)$:

.. math::

    C_l = {e^{i\delta_l}\over k}

    f(\theta, \phi) = {1\over 2ik} \sum (2l+1)(e^{2i\delta_l}-1)P_l(\cos\theta)

Since $\sigma(\theta) = |f(\theta)|^2$ and integrating over $\omega$ we get the
total cross section:

.. math::

    \sigma = {4\pi\over k}\sum (2l+1)\sin^2\delta_l

In order to find the phase shifts $\delta_l$, we solve the radial equation for
the full potential

.. math::

    -{1\over2}R_{nl}''(r)-{1\over r}R_{nl}'(r)+\left(V+{l(l+1)\over2r^2}\right)
        R_{nl}(r)=ER_{nl}(r)

and then fit it to the above asymptotic solution for V=0. We require that the
value and the slope must be continuous. In particular, we take the logarithmic
derivative ($(\log u)'={u'\over u}$) at the point $r=a$:

.. math::

    \gamma_l \equiv \left.{\d\over\d r} \log u\right|_{r=a}
    = \left.{\d\over\d r} \log R_l(kr)\right|_{r=a}
    = {\left.{\d R_l(kr)\over\d r} \right|_{r=a}\over R_l(kr)}

expressing $R_{El}(kr)$ and $R_{El}'(kr)$ using $\delta_l$:

.. math::

    R_{El}(r) = C_l (\cos\delta_l\, j_l(kr) - \sin\delta_l\, n_l(kr))

    R_{El}'(r) = C_l k (\cos\delta_l\, j_l'(kr) - \sin\delta_l\, n_l'(kr))

calculating $\gamma_l$:

.. math::

    \gamma_l = {R_{El}'(a)\over R_{El}(a)}
        = {C_l k (\cos\delta_l\, j_l'(ka) - \sin\delta_l\, n_l'(ka)) \over
                C_l (\cos\delta_l\, j_l(ka) - \sin\delta_l\, n_l(ka)) }
        =

        = k {j_l'(ka) - \tan\delta_l\, n_l'(ka) \over
                j_l(ka) - \tan\delta_l\, n_l(ka)) }

and solving for $\delta$ we get:

.. math::

    \tan\delta_l
        = {k j_l'(ka) - \gamma_l j_l(ka)\over k n_l'(ka)-\gamma_l n_l(ka)}
        = {-k j_{l+1}(ka) +kl{j_l(ka)\over ka} - \gamma_l j_l(ka)
            \over -k n_{l+1}(ka)+kl{n_l(ka)\over ka} - \gamma_l n_l(ka)}
        =

        = {ka j_{l+1}(ka) -l j_l(ka) + a j_l(ka) \gamma_l
            \over ka n_{l+1}(ka) -l n_l(ka) + a n_l(ka) \gamma_l}

where we used the following relations:

.. math::

    j_l'(z) = -j_{l+1}(z) + l{j_l(z)\over z}

    n_l'(z) = -n_{l+1}(z) + l{n_l(z)\over z}

Now we can use these $\delta_l$ in the formula for the total cross section. We
can define a reduced phase-shift $\eta_l$ by

.. math::

    \delta_l = (n-l-1) \pi + \eta_l

where $n-l-1$ is the number of radial nodes and $0 \le \eta_l \le \pi$.

The problem can now be formulated in two ways. Either to solve the radial
equation for a potential with finite reach and then "measure" those phase
shifts in the solution. Or by prescribing those phase shifts and we now need to
calculate the solutions (e.g. the energies) from the radial equation.
