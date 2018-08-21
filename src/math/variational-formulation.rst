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

Example
-------

As a particular example, let $u(a) = u_0$ and $u'(b) = g$. Then the Lagrangian
:eq:`poisson0` becomes:

.. math::
    :label: poisson_example_L

    L[u] = \int_a^b \left[ \half u'^2(x) - f(x) u(x) \right] \d x - g u(b)\,.

We can explicitly define the space $U$ of all trial functions $u \in U$ that
one can choose (admissible) and substitute in :eq:`poisson_example_L` as
follows. We have to impose the Dirichlet condition $u(a) = u_0$ on the space
itself, and we also have to choose how smooth functions we want. For finite
element applications one typically chooses $H^1$ (i.e., values and first
derivatives are from $L^2$) and we obtain:

.. math::
    :label: poisson_example_UU

    U := \{u : u \in H^1(a,b), u(a)=u_0\}

Now we derive what space the variation $\delta u(x)$ belongs to. Let
$u_\textrm{min}$ be the solution (the extremum of the functional
:eq:`poisson_example_L`). Then from calculus of variations:

.. math::
    :label: poisson_example_u

    u = u_\textrm{min} + \varepsilon \delta u(x)

Here $u$ is called the trial function and $\delta u(x)$ is called the test
function. Both $u$ and $u_\textrm{min}$ are from the space $U$. Thus we can
compute:

.. math::

    \delta u(a) = {u(a) - u_\textrm{min}(a) \over \varepsilon}
    = {u_0 - u_0 \over \varepsilon} = 0\,.

In addition, both $u,u_\textrm{min}\in H^1(a,b)$, so also their difference
$u(x) - u_\textrm{min}(x)$ and thus also $\delta u(x)={u(x) - u_\textrm{min}(x)
\over \varepsilon}$ is from $H^1(a,b)$. There are no other conditions ($u(b)$
and $u_\textrm{min}(b)$ are generally different, so in general $\delta u(b) \ne
0$) and so $\delta u(x) \in U_0$ where the space $U_0$ is:

.. math::
    :label: poisson_example_U0

    U_0 := \{w : w \in H^1(a,b), w(a)=0\}\,.

The definition of the space $U_0$ in :eq:`poisson_example_U0` is derived from
the definition of the space $U$ in :eq:`poisson_example_UU`.

To compute the variation of $L$, we substitute :eq:`poisson_example_u` into
:eq:`poisson_example_L`, differentiate with respect to $\varepsilon$ and then
set $\varepsilon=0$ using :eq:`functional_deriv`:

.. math::

    \delta L[u] = \left.{\d\over\d\varepsilon}L[u_\textrm{min}+\varepsilon
        \delta u] \right|_{\varepsilon=0}

as was done in :eq:`poisson1` and one obtains the weak form (below we drop the
label $\textrm{min}$ from $u_\textrm{min}$ and just use $u$):

.. math::
    :label: poisson_example_weak_form

    \delta L[u] =
    \int_a^b \left[ u'(x) \delta u'(x) - f(x) \delta u(x) \right] \d x
        - g \delta u(b) = 0\,.

The task is to find such function $u\in U$ so that
:eq:`poisson_example_weak_form` holds for all $\delta u \in U_0$.  From
:eq:`poisson_example_weak_form` one obtains (as in :eq:`poisson1`):

.. math::
    :label: poisson_example_2

    \int_a^b \left[-u''(x) - f(x)\right] \delta u(x) \d x
        + (u'(b) - g) \delta u(b) = 0\,.

The governing equation :eq:`poisson3` is the same:

.. math::
    :label: poisson_example_strong

    u''(x) + f(x) = 0\,.

The boundary term :eq:`poisson3_boundary` becomes (see
:eq:`poisson_example_2`):

.. math::

    (u'(b) - g) \delta u(b) = 0\,.

Which implies $u'(b) = g$.

The Dirichlet boundary condition is part of the definition of the function
space :eq:`poisson_example_UU`, so all trial functions $u$ that one can choose
(admissible) and substitute in $L[u]$ must lie in $U$. From the derivation of
the space $U_0$ in :eq:`poisson_example_U0` we can see that since the value of
$u(a)$ is fixed, we always have $\delta u(a) = 0$; on the other hand, since
$u(b)$ is not fixed, in general we have $\delta u(b) \ne 0$.

The Neumann boundary condition is imposed variationally due to the surface term
in the weak form :eq:`poisson_example_weak_form`.

Summary
~~~~~~~

We have shown above that there are three equivalent formulations which
fully and uniquely determine the solution and boundary conditions (both
Dirichlet and Neumann):

1. Define the functional $L[u]$ in :eq:`poisson_example_L` and the space $U$
   for the trial functions $u\in U$ in :eq:`poisson_example_UU`.
2. Define the weak form :eq:`poisson_example_weak_form` and the two spaces $U$
   and $U_0$, where $u\in U$ and $\delta u \in U_0$.
3. Define the strong form :eq:`poisson_example_strong` and the boundary
   conditions $u(a) = u_0$ and $u'(b) = g$.

Let us write down the three formulations in detail.

Variational Formulation
~~~~~~~~~~~~~~~~~~~~~~~

The variational formulation is the formulation 1. above.

.. math::

    L[u] = \int_a^b \left[ \half u'^2(x) - f(x) u(x) \right] \d x - g u(b)\,.

The task is to find such $u\in U$ that extremizes this functional
($\delta L[u] = 0$), where:

.. math::

    U := \{u : u \in H^1(a,b), u(a)=u_0\}\,.

Weak Formulation
~~~~~~~~~~~~~~~~

Weak formulation is the formulation 2. above, and it is customary to
write $w(x) \equiv \delta u(x)$ in the weak form
:eq:`poisson_example_weak_form`:

.. math::
    :label: poisson_example_weak_form2

    \int_a^b \left[ u'(x) w'(x) - f(x) w(x) \right] \d x - g w(b) = 0\,.

The task is to find such $u\in U$ so that :eq:`poisson_example_weak_form2`
holds for all $w\in U_0$, where

.. math::

    U   & := \{u : u \in H^1(a,b), u(a)=u_0\}\,,

    U_0 & := \{w : w \in H^1(a,b), w(a)=0\}\,.

We can also define:

.. math::

    a(u,w) &= \int_a^b u'(x) w'(x) \d x\,,

    b(w)   &= \int_a^b f(x) w(x) \d x + g w(b)

and write :eq:`poisson_example_weak_form2` as:

.. math::

    a(u,w) = b(w)\,.

Strong Formulation
~~~~~~~~~~~~~~~~~~

Strong formulation is the formulation 3. above. We are solving the equation:

.. math::

    u''(x) + f(x) = 0

subject to boundary conditions $u(a) = u_0$ and $u'(b) = g$.

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
