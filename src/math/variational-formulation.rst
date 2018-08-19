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

    L = \int_a^b \left[ \half u'^2(x) + f(x) u(x) \right] \d x
        - [\hat g(x) u(x)]_a^b\,.

The variational formulation is:

.. math::

    \delta L = 0\,,

which yields:

.. math::
    :label: poisson1

    \delta L &= \int_a^b \left[ u'(x) \delta u'(x)
        + f(x) \delta u(x) \right] \d x
        - [\hat g(x) \delta u(x)]_a^b

             &= \int_a^b \left[-u''(x) \delta u(x)
        + f(x) \delta u(x) \right] \d x
        + [u'(x) \delta u(x)]_a^b
        - [\hat g(x) \delta u(x)]_a^b

             &= \int_a^b \left[-u''(x) + f(x)\right] \delta u(x) \d x
        + [(u'(x) - \hat g(x)) \delta u(x)]_a^b

             &= 0\,,

where we applied integration by parts.
This equation holds for any $\delta u(x)$, and in particular it holds for
$\delta u(x) = 0$ at the boundary (i.e., for $\delta u(a) = 0$ and
$\delta u(b) = 0$). Then the boundary term in :eq:`poisson1` vanishes and we
obtain:

.. math::
    :label: poisson2

    \int_a^b \left[-u''(x) + f(x)\right] \delta u(x) \d x = 0\,,

This equation holds for any $\delta u(x)$ that is zero at the boundary, and
thus it implies:

.. math::
    :label: poisson3

    -u''(x) + f(x) = 0\,.

Now we substitute :eq:`poisson3` into :eq:`poisson1` and obtain:

.. math::
    :label: poisson3_boundary

    [(u'(x) - \hat g(x)) \delta u(x)]_a^b = 0\,.

Thus :eq:`poisson1` implies both :eq:`poisson3` and :eq:`poisson3_boundary`.
The equation :eq:`poisson3_boundary` holds for any $\delta u(x)$ (generally
not zero at the boundary) and thus it implies:

.. math::
    :label: poisson3_boundary2

    u'(x) - \hat g(x) = 0

at the boundary. Thus $\hat g(x)$ imposes the Neumann boundary condition, i.e.,
the value of the derivative $u'(x) = \hat g(x)$ at the boundary. This condition
is imposed variationally.

To impose a Dirichlet boundary condition, we want to impose the value of
$u(x)=\hat u(x)$ at the boundary for some constant $\hat u(x)$. As such, $u(x)$
is not allowed to vary at that part of the boundary, which means that the
variation $\delta u(x) = 0$ at the boundary. So we restrict the variation
$\delta u(x)$ to be zero at the Dirichlet part of the boundary in
:eq:`poisson1` and thus also in :eq:`poisson3_boundary`. This implies that
:eq:`poisson3_boundary2` does not hold at the Dirichlet part of the boundary
and we have to set the value $u(x)$ there directly.

Radial Schrödinger Equation
===========================

The derivation is similar, but we have $\hat g(x) = 0$ based on physical
reasoning (that we cannot set the derivative to a given value, or,
alternatively, that we require the operator to be self-adjoint).
