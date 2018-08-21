===============================
Variational Formulation of PDEs
===============================

Not every equation allows a variational formulation (e.g., Navier-Stokes or
Euler equations do not have such a formulation), but many equations have one,
and we explain how it works on several examples.

Poisson Equation
================

The Lagrangian for Poisson equation is:

.. math::
    :label: poisson0

    L[u] = \int_a^b \left[ \half u'^2(x) - f(x) u(x) \right] \d x
        - [g(x) u(x)]_a^b\,.

Important note: technically, as we will see below, this imposes the Neumann
boundary condition and 1D Poisson equation with two Neumann boundary conditions
does not have a unique solution. At least one Dirichlet boundary condition is
needed for a unique solution. For example with $u(a) = u_0$ and $u'(b) = g$ the
boundary term becomes just $-gu(b)$. However, for simplicity, we will show the
derivation with two Neumann boundary conditions first and we will discuss how
to impose the Dirichlet boundary condition later.

The variational formulation is:

.. math::

    \delta L = 0\,,

which yields:

.. math::
    :label: poisson1

    \delta L &= \int_a^b \left[ u'(x) \delta u'(x)
        - f(x) \delta u(x) \right] \d x
        - [g(x) \delta u(x)]_a^b

             &= \int_a^b \left[-u''(x) \delta u(x)
        - f(x) \delta u(x) \right] \d x
        + [u'(x) \delta u(x)]_a^b
        - [g(x) \delta u(x)]_a^b

             &= \int_a^b \left[-u''(x) - f(x)\right] \delta u(x) \d x
        + [(u'(x) - g(x)) \delta u(x)]_a^b

             &= 0\,,

where we applied integration by parts.
This equation holds for any $\delta u(x)$, and in particular it holds for
$\delta u(x) = 0$ at the boundary (i.e., for $\delta u(a) = 0$ and
$\delta u(b) = 0$). Then the boundary term in :eq:`poisson1` vanishes and we
obtain:

.. math::
    :label: poisson2

    \int_a^b \left[-u''(x) - f(x)\right] \delta u(x) \d x = 0\,,

This equation holds for any $\delta u(x)$ that is zero at the boundary, and
thus it implies:

.. math::
    :label: poisson3

    u''(x) + f(x) = 0\,.

Now we substitute :eq:`poisson3` into :eq:`poisson1` and obtain:

.. math::
    :label: poisson3_boundary

    [(u'(x) - g(x)) \delta u(x)]_a^b = 0\,.

Thus :eq:`poisson1` implies both :eq:`poisson3` and :eq:`poisson3_boundary`.
The equation :eq:`poisson3_boundary` holds for any $\delta u(x)$ (generally
not zero at the boundary) and thus it implies:

.. math::
    :label: poisson3_boundary2

    u'(x) - g(x) = 0

at the boundary. Thus $g(x)$ imposes the Neumann boundary condition, i.e.,
the value of the derivative $u'(x) = g(x)$ at the boundary. This condition
is imposed variationally.

To impose a Dirichlet boundary condition, we want to impose the value of
$u(x)=u_0(x)$ at the boundary for some constant $u_0(x)$. As such, $u(x)$
is not allowed to vary at that part of the boundary, which means that the
variation $\delta u(x) = 0$ at the boundary. So we restrict the variation
$\delta u(x)$ to be zero at the Dirichlet part of the boundary in
:eq:`poisson1` and thus also in :eq:`poisson3_boundary`. This implies that
:eq:`poisson3_boundary2` does not hold at the Dirichlet part of the boundary
and we have to set the value $u(x)$ there directly.

As a particular example, let $u(a) = u_0$ and $u'(b) = g$. Then the Lagrangian
:eq:`poisson0` becomes:

.. math::

    L[u] = \int_a^b \left[ \half u'^2(x) - f(x) u(x) \right] \d x - g u(b)\,.

The governing equation :eq:`poisson3` is the same:

.. math::

    u''(x) + f(x) = 0\,.

The boundary term :eq:`poisson3_boundary` becomes:

.. math::

    (u'(b) - g(b)) \delta u(b) = 0\,.

Which implies $u'(b) = g(b)$.
The Dirichlet boundary condition is part of the definition of the function
space $U := \{u : u \in H^1(a,b), u(a)=u_0\}$, so all trial functions $u$ that
one can choose (admissible) and substitute in $L[u]$ must lie in $U$. Since
the value of $u(a)$ is fixed, we always have $\delta u(a) = 0$. On the other
hand, since $u(b)$ is not fixed, in general we have $\delta u(b) \ne 0$.

Radial Schrödinger Equation
===========================

The derivation is similar as for the Poisson equation, except that we have
$g(x) = 0$ based on physical reasoning (that we cannot set the derivative
to a given value, or, alternatively, that we require the operator to be
self-adjoint).

The Lagrangian for the radial Schrödinger equation is:

.. math::
    :label: schr_radial0

    L[R] = \int_0^\infty \left[\half R'^2(r)
        + \left(V(r) + {l(l+1)\over 2 r^2}\right) R^2(r) \right] r^2 \,\d r\,.

We minimize the Lagrangian subject to the normalization condition
$N[R] = \int_0^\infty R^2(r) r^2\, \d r = 1$ as follows:

.. math::
    :label: schr_radial1

    0 &= \delta (L - \epsilon (N-1))

    &= \delta \int_0^\infty \left[ \half r^2 R'^2
    + (r^2 V + \half l(l+1)) R^2 - \epsilon r^2R^2 \right] \,\d r =

    &= 2\int_0^\infty \left[ \half r^2 R'(\delta R)'
    + (r^2 V + \half l(l+1)) R\delta R - \epsilon r^2 R\delta R \right]
      \,\d r =

    &= 2\int_0^\infty \left[ -\half (r^2 R')'
    + (r^2 V + \half l(l+1)) R - \epsilon r^2 R\right]\delta R \,\d r
      + [r^2 R' \delta R]_0^\infty

This equation holds for any $\delta R(r)$, and so it also holds when we
restrict $\delta R(r) = 0$ on the boundary and the boundary term vanishes. Then
it implies the radial Schrödinger equation:

.. math::
    :label: schr_radial2

    -\half (r^2 R'(r))' + (r^2 V(r) + \half l(l+1)) R(r) = \epsilon r^2 R(r)

Substituting :eq:`schr_radial2` into :eq:`schr_radial1` we obtain:

.. math::
    :label: schr_radial_boundary

      [r^2 R' \delta R]_0^\infty = 0

And we can see that :eq:`schr_radial1` implies both the equation
:eq:`schr_radial2` and the boundary term :eq:`schr_radial_boundary`. The
boundary term is zero for $r=0$, so it reduces to:

.. math::
    :label: schr_radial_boundary2

    \lim_{r\to\infty} r^2 R'(r) \delta R(r) = 0

We can see that there is no natural condition at $r=0$, and for $r=\infty$ we
only have two possible options. Either we impose $\delta R(\infty) = 0$ and
obtain the Dirichlet condition and the boundary term
:eq:`schr_radial_boundary2` vanishes. Or we allow $\delta R(\infty)$ to vary,
and then :eq:`schr_radial_boundary2` implies $R'(\infty) = 0$.

Unlike for the Poisson equation we are not allowed to set $R'(\infty)$ to
anything other than zero, and that's why :eq:`schr_radial0` has no surface
term.
