=========
Operators
=========

Introduction
============

The domain of the operator $A$ is $D(A)$, a subspace of the Hilbert space
$\mathscr{H}$.
Linear operator is:

.. math::

    A (\alpha \ket{u} + \beta \ket{v}) = \alpha A \ket{u} + \beta A \ket{v}

for all $\ket{u}, \ket{v} \in D(A)$.
Symmetric operator is:

.. math::

    \braket{u|Av} = \braket{Au|v}

for all $\ket{u}, \ket{v} \in D(A)$ dense in $\mathscr{H}$.
If $D(A)$ is dense in $\mathscr{H}$, then the adjoint operator $A^\dag$ is
defined by

.. math::

    \braket{u|A^\dag v} = \braket{Au|v}

for all $\ket{u} \in D(A)$. The domain $D(A^\dag)$ is given by all
$\ket{v}$ for which the above relation holds. It can be shown that
$D(A) \subset D(A^\dag)$.

Operator $A$ is self-adjoint if $A = A^\dag$.
Symmetric operator is self-adjoint only if $D(A) = D(A^\dag)$. (Bounded
symmetric operator is always self-adjoint.)
Hermitean operator is a bounded symmetric operator.

Hermitian implies self-adjoint implies symmetric, but all converse implications
are false.
Below, we need the operator to be self-adjoint (we assume
unbounded by default).

Spectrum
========

To obtain a spectrum of the operator $A$, we need to solve the following
problem:

.. math::

    A \ket{\lambda} = \lambda \ket{\lambda}

Those values of $\lambda$ for which the solution $\ket{\lambda}\in\mathscr{H}$
belong to the discrete part of the spectrum. $\lambda$ are called eigenvalues
and $\ket{\lambda}$ eigenvectors.
Those values of $\lambda$ for which $\ket{\lambda}$ can be normalized
to a delta function:

.. math::

   \braket{\lambda|\kappa} = \delta(\lambda-\kappa)

belong to the continuous part of the spectrum (note that in this case
$\ket{\lambda}\notin\mathscr{H}$).

Eigenvectors belonging to the continous part of the spectrum obey the
completeness relation:

.. math::

    \int \ket{\lambda}\bra{\lambda} \d \lambda = \one

Eigenvectors belonging to the discrete part obey the following completeness
relation:

.. math::

    \sum_\lambda \ket{\lambda}\bra{\lambda} \d \lambda = \one

The sum or integral runs over the whole spectrum (if the spectrum contains both
discrete and continous part, we simply combine sums and integrals).

Spectrum of a self-adjoint operator is real, because

.. math::

    \braket{\lambda|A|\lambda} = \lambda \braket{\lambda|\lambda} =
        \lambda^* \braket{\lambda|\lambda}


The eigenvectors are orthogonal:

.. math::

    \braket{\lambda|A|\kappa} = \kappa \braket{\lambda|\kappa} =
        \lambda \braket{\lambda|\kappa}

    (\kappa-\lambda) \braket{\lambda|\kappa} = 0

So for $\kappa\ne\lambda$ we get $\braket{\lambda|\kappa}=0$,
for $\kappa=\lambda$ the $\braket{\lambda|\lambda}$ is equal to 1 if
$\lambda$ belongs to the discrete spectrum and we get:

.. math::

    \braket{\lambda|\kappa} = \delta_{\lambda\kappa}

or it is normalized as a delta function if it belongs to the continous part:

.. math::

    \braket{\lambda|\kappa} = \delta(\lambda-\kappa)


As such, eigenvectors of a self-adjoint operator are complete and orthogonal
in the above sense. Thus any function from the space can then be expanded into
the series:

.. math::

    f(x) = \braket{x|f} = \sum_\lambda \braket{x|\lambda}\braket{\lambda|f}

where $\braket{x|\lambda}$ are the eigenvectors and the
coefficients $\braket{\lambda|f}$ are given by:

.. math::

    \braket{\lambda|f} = \int \braket{\lambda|x}\braket{x|f} \d x
        = \int \braket{\lambda|x} f(x) \d x

The sum over $\lambda$ runs over the whole spectrum (i.e. it becomes an
integral over the continuos parts). Also the coefficients $\braket{\lambda|f}$
are either discrete or continous depending on the part of the spectrum.
The series converges in the norm, i.e. the following norm goes to zero as we
sum over $\lambda$:

.. math::

    \left\| f(x) - \sum_\lambda \braket{x|\lambda}\braket{\lambda|f} \right\|
        \to 0

.. _deriv_operator:

Derivative Operator
===================

We have the eigenvalue problem

.. math::

    A u = \lambda u

where

.. math::

    A = -i {\d \over \d x}

The operator $A$ is unbounded.
$A$ is self-adjoint if:

.. math::

    \int_a^b u^*(x) A v(x) \d x = \int_a^b (A u(x))^* v(x) \d x

So

.. math::

    \int_a^b u^*(x) A v(x) \d x
        = \int_a^b u^*(x) \left(-i {\d \over \d x}\right) v(x) \d x =

        = \int_a^b \left(i {\d \over \d x} u^*(x) \right) v(x) \d x
            -i[u^*(x) v(x)]^b_a =

        = \int_a^b \left(-i {\d \over \d x} u(x) \right)^* v(x) \d x
            -i[u^*(x) v(x)]^b_a =

        = \int_a^b (A u(x))^* v(x) \d x -i[u^*(x) v(x)]^b_a


The operator is self-adjoint if and only if $[u^*(x) v(x)]^b_a=0$.
Few boundary conditions that satisfy this condition:

* Dirichlet boundary conditions

.. math::

    u(a) = 0, \quad u(b) = 0

* Periodic boundary conditions

.. math::

    u(a) = u(b)

* Antiperiodic boundary conditions

.. math::

    u(a) = -u(b)

Solving the eigenproblem:

.. math::

    A u = \lambda u

    -i {\d \over \d x} u = \lambda u

    u(x) = e^{i\lambda x}


Fourier Series
--------------

We restrict our space to periodic functions.
Applying the periodic boundary condition:

.. math::

    u(a) = e^{i\lambda a} = u(b) = e^{i\lambda b}

so

.. math::

    e^{i\lambda (b-a)} = 1

    \lambda = {2\pi n\over b-a}\quad\quad{\mbox{for $n=0, \pm 1, \pm 2, \dots$}}

The normalized eigenvectors are:

.. math::

    u_n(x) = {1\over\sqrt{b-a}} e^{i {2\pi n\over b-a} x}

These eigenvectors belong to our space and as such all
$\lambda = {2\pi n\over b-a}$ form a discrete spectrum. Other solutions
do not satisfy the periodic boundary condition and so there is no continous
part in the spectrum.

The eigenvectors must be orthogonal, as we can check:

.. math::

    \int_a^b u_n^*(x) u_m(x) \d x =

    = \int_a^b
        {1\over\sqrt{b-a}} e^{-i {2\pi n\over b-a} x}
        {1\over\sqrt{b-a}} e^{i {2\pi m\over b-a} x}
        \d x =

    = {1\over b-a} \int_a^b
        e^{i {2\pi (m-n)\over b-a} x}
        \d x =

    = \begin{cases}
        {1\over b-a} \int_a^b e^{0} \d x & \mbox{for } m = n \\
        {1\over i 2\pi (m-n) } \left[e^{i {2\pi (m-n)\over b-a} x}\right]^b_a &
            \mbox{for } m \ne n \\
      \end{cases} =

    = \begin{cases}
        1 & \mbox{for } m = n \\
        {1\over i 2\pi (m-n) } \left(
            e^{i {2\pi (m-n)\over b-a} b}-e^{i {2\pi (m-n)\over b-a} a}\right) &
            \mbox{for } m \ne n \\
      \end{cases} =

    = \begin{cases}
        1 & \mbox{for } m = n \\
        {e^{i {2\pi (m-n)\over b-a} a}\over i 2\pi (m-n)} \left(
            e^{i {2\pi (m-n)\over b-a} (b-a)}-1\right) &
            \mbox{for } m \ne n \\
      \end{cases} =

    = \begin{cases}
        1 & \mbox{for } m = n \\
        0 & \mbox{for } m \ne n \\
      \end{cases} =
      \delta_{mn}

The eigenvectors must be complete:

.. math::

    \sum_{n=-\infty}^\infty \ket{n}\bra{n} = \one

    \sum_{n=-\infty}^\infty \braket{x|n}\braket{n|x'} = \braket{x|x'}

    \sum_{n=-\infty}^\infty u_n(x) u_n^*(x') \d x = \delta(x-x')

Any function $f(x)$ can then be expanded on the interval $[a, b]$ into the
Fourier series:

.. math::

    f(x) = \braket{x|f} = \sum_{n=-\infty}^\infty \braket{x|n}\braket{n|f}
    = \sum_{n=-\infty}^\infty c_n' u_n(x)
    = \sum_{n=-\infty}^\infty c_n' {1\over\sqrt{b-a}} e^{i {2\pi n\over b-a} x}
    = \sum_{n=-\infty}^\infty c_n e^{i {2\pi n\over b-a} x}

    c_n = c_n' {1\over\sqrt{b-a}}
        = \braket{n|f} {1\over\sqrt{b-a}}
        = {1\over\sqrt{b-a}} \int_a^b \braket{n|x}\braket{x|f} \d x
        = {1\over\sqrt{b-a}} \int_a^b u_n^*(x) f(x) \d x
        = {1\over b-a} \int_a^b e^{-i {2\pi n\over b-a} x} f(x) \d x

Equivalently, this can be written using $\sin$ and $\cos$ directly:

.. math::

    f(x)
        = \sum_{n=-\infty}^\infty c_n
            e^{i {2\pi n\over b-a} x} =

        = \sum_{n=-\infty}^\infty c_n
            \cos \left({2\pi n\over b-a} x\right)
        + \sum_{n=-\infty}^\infty i c_n
            \sin \left({2\pi n\over b-a} x\right) =

        = c_0 + \sum_{n=1}^\infty (c_n + c_{-n})
            \cos \left({2\pi n\over b-a} x\right)
        + \sum_{n=1}^\infty i (c_n - c_{-n})
            \sin \left({2\pi n\over b-a} x\right)

By introducing the coefficients $a_n$ and $b_n$:

.. math::

    a_n &= c_n + c_{-n}      \quad\quad {\mbox{for } n = 0, 1, 2, \dots} \\
    b_n &= i(c_n - c_{-n})   \quad\quad {\mbox{for } n = 1, 2, \dots}

we can write the series as:

.. math::

    f(x)
        = {a_0\over 2} + \sum_{n=1}^\infty a_n
            \cos \left({2\pi n\over b-a} x\right)
        + \sum_{n=1}^\infty b_n \sin \left({2\pi n\over b-a} x\right)

we get:

.. math::

    a_n = c_n + c_{-n}
        = {1\over b-a} \int_a^b \left(
            e^{-i {2\pi n\over b-a} x} + e^{i {2\pi n\over b-a} x}\right)
            f(x) \d x
        = {2\over b-a} \int_a^b \cos \left({2\pi n\over b-a} x\right)
            f(x) \d x

    b_n = i(c_n - c_{-n})
        = {i\over b-a} \int_a^b \left(
            e^{-i {2\pi n\over b-a} x} - e^{i {2\pi n\over b-a} x}\right)
            f(x) \d x
        = {2\over b-a} \int_a^b \sin \left({2\pi n\over b-a} x\right)
            f(x) \d x

Fourier Transform
-----------------

Our domain is $(-\infty, \infty)$, so the solution of the eigen problem is:

.. math::

    A u = \lambda u

    -i {\d \over \d x} u = \lambda u

    u(x) = e^{i\lambda x}

The normalized eigenfunctions are:

.. math::

    u_\lambda(x) = {1\over\sqrt{2\pi}} e^{i\lambda x}

We calculate the normalization:

.. math::

    \int_{-\infty}^\infty u_\lambda^*(x) u_\kappa(x) \d x =

    = \int_{-\infty}^\infty
        {1\over\sqrt{2\pi}} e^{-i\lambda x}
        {1\over\sqrt{2\pi}} e^{i\kappa x}
        \d x =

    = {1\over 2\pi} \int_{-\infty}^\infty e^{i(\kappa-\lambda) x} \d x =

    = \delta(\kappa-\lambda)

So the spectrum is continous. The eigenvectors must be complete:

.. math::

    \int_{-\infty}^\infty \ket{\lambda}\bra{\lambda} \d \lambda = \one

    \int_{-\infty}^\infty \braket{x|\lambda}\braket{\lambda|x'} \d \lambda
        = \braket{x|x'}

    \int_{-\infty}^\infty u_\lambda(x) u_\lambda^*(x') \d \lambda = \delta(x-x')

Any function $f(x)$ can then be written as:

.. math::

    f(x) = \braket{x|f}
    = \int_{-\infty}^\infty \braket{x|\lambda}\braket{\lambda|f} \d \lambda
    = \int_{-\infty}^\infty u_\lambda(x) \hat f(\lambda) \d \lambda
    = {1\over\sqrt{2\pi}} \int_{-\infty}^\infty e^{i\lambda x}
        \hat f(\lambda) \d \lambda

where $\hat f(\lambda)$ is called the Fourier transform of $f(x)$:

.. math::

    \hat f(\lambda) = \braket{\lambda|f}
    = \int_{-\infty}^\infty \braket{\lambda|x}\braket{x|f} \d x
    = \int_{-\infty}^\infty u_\lambda^*(x) f(x) \d x
    = {1\over\sqrt{2\pi}}\int_{-\infty}^\infty
        e^{-i\lambda x} f(x) \d x

Sturm–Liouville Operator
========================

The Sturm-Liouville operator $L$ is:

.. math::

    L u(x)  = {1 \over w(x)} \left(-{\d\over \d x}
        \left(p(x){\d u(x)\over dx}\right) +q(x) u(x) \right)

Everything is real.
The scalar product is weighted by $w(x)$. The operator is self-adjoint if:

.. math::

    \int_a^b u(x) L v(x) w(x) \d x = \int_a^b (L u(x)) v(x) w(x) \d x

so

.. math::

    \int_a^b u(x) L v(x) w(x) \d x =

    = \int_a^b u(x) {1 \over w(x)} \left(-{\d\over \d x}
        \left(p(x){\d v(x)\over dx}\right) +q(x) v(x) \right)
        w(x) \d x =

    = \int_a^b \left(-u(x) {\d\over \d x}
        \left(p(x){\d v(x)\over dx}\right) + u(x) q(x) v(x) \right)
        \d x =

    = \int_a^b \left({\d u(x)\over\d x} p(x){\d v(x)\over dx}
        + u(x) q(x) v(x) \right) \d x
          -\left[u(x)p(x){\d v(x)\over dx}\right]^b_a
          =

    = \int_a^b \left(-{\d\over \d x} \left(p(x) {\d u(x)\over\d x}\right) v(x)
        + u(x) q(x) v(x) \right) \d x
          -\left[u(x)p(x){\d v(x)\over dx}-{\d u(x)\over dx}p(x)v(x)\right]^b_a
          =

    = \int_a^b \left(L u(x)\right) v(x) w(x) \d x
          -\left[u(x)p(x){\d v(x)\over dx}-{\d u(x)\over dx}p(x)v(x)\right]^b_a

And the operator $L$ is self-adjoint if and only if:

.. math::

    \left[u(x)p(x)v'(x)-u'(x)p(x)v(x)\right]^b_a = 0

This condition can be satisfied by various boundary conditions.
For example:

* Dirichlet boundary conditions

.. math::

    u(a) = 0, \quad u(b) = 0

* Neumann boundary conditions

.. math::

    u'(a) = 0, \quad u'(b) = 0

* Periodic boundary conditions

.. math::

    u(a)  &= u(b) \\
    u'(a) &= u'(b)

* Antiperiodic boundary conditions

.. math::

    u(a)  &= -u(b) \\
    u'(a) &= -u'(b)

or mixtures of these, e.g. Dirichlet at $x=a$ and Neumann at $x=b$.

Legendre Polynomials
--------------------

Legendre polynomials $P_n(x)$ are solutions of the Sturm–Liouville problem on
the interval $[-1, 1]$ with $p(x)=1-x^2$, $q(x)=0$, $w(x)=1$ and
$\lambda=n(n+1)$:

.. math::

    L u(x)  = n(n+1) u(x)

    L u(x)  = -{\d\over \d x} \left((1-x^2){\d u(x)\over dx}\right)

The operator $L$ is self-adjoint due to vanishing $p(x)$ at
the endpoints:

.. math::

    \left[(u(x)v'(x)-u'(x)v(x))p(x)\right]_{-1}^1
        = \left[(u(x)v'(x)-u'(x)v(x))(1-x^2)\right]_{-1}^1 = 0

We restrict our space to bounded functions. The solutions of the eigenvalue
problem for integer $n$ are Legendre polynomials $P_n(x)$, the normalized
eigenvectors $u_n(x)$ are:

.. math::

    u_n(x) = \sqrt{2n+1\over 2} P_n(x)

Solutions for non
integer $n$ are Legendre functions that are singular at the end points and as
such are not solutions that we want. As such, the spectrum is discrete and the
Legendre polynomials form a complete orthogonal basis for functions
on the interval $[-1, 1]$:

.. math::

    \int_{-1}^1 u_n(x) u_m(x)
    = {2n+1\over 2} \int_{-1}^1 P_n(x) P_m(x)
    = \delta_{n m}

    \sum_{n=0}^\infty u_n(x) u_n(x')
    = {2n+1\over 2} \sum_{n=0}^\infty P_n(x) P_n(x')
    = \delta(x-x')

any function $f(x)$ on the interval $[-1, 1]$ can be expanded as:

.. math::

    f(x) = \sum_{n=0}^\infty f_n' u_n(x)
        = \sum_{n=0}^\infty f_n' \sqrt{2n+1\over 2} P_n(x)
        = \sum_{n=0}^\infty f_n P_n(x)

    f_n = f_n' \sqrt{2n+1\over 2}
        = \sqrt{2n+1\over 2} \int_{-1}^1 u_n(x) f(x)
        = {2n+1\over 2} \int_{-1}^1 P_n(x) f(x)

Angular Momentum Operator
=========================

The angular momentum operators $L_1$, $L_2$ and $L_3$ are given by:

.. math::

    L_j = -i \epsilon_{jkl} x_k \partial_l

in spherical coordinates:

.. math::

    L_1 &= i \left(\sin \phi \ \partial_\theta
         + \cot \theta \cos \phi \ \partial_\phi\right) \\
    L_2 &= i \left(-\cos\phi \ \partial_\theta
        + \cot \theta \sin \phi \ \partial_\phi\right) \\
    L_3 &= -i \partial_\phi

and

.. math::

    L^2 = L_1^2 + L_2^2 + L_3^2 =
         - \left( {1\over\sin\theta} \partial_\theta
                \left(\sin\theta \ \partial_\theta \right)
         + {1\over \sin^2\theta}\partial_\phi^2\right)

The eigenproblem is:

.. math::
    :label: Ylm_eig

    L^2 \ket{lm} &= l(l+1) \ket{lm} \\
    L_3 \ket{lm} &= m \ket{lm}

Using Condon & Shortley phase convention, it can be shown that:

.. math::
    :label: ladder

    (L_1 \pm i L_2) \ket{l, m} = \sqrt{(l \mp m)(l\pm m + 1)} \ket{l,m \pm 1}

and by repeated application:

.. math::

    (L_1 \pm i L_2)^k \ket{l, m} =

        = \sqrt{(l \mp m)(l \mp m-1)\cdots(l\mp m -k+1)
            (l\pm m + 1)(l\pm m + 2)\cdots(l\mp m + k)} \ket{l,m \pm k} =

        = \sqrt{{(l\mp m)!\over (l\pm m)!} {(l\pm m + k)!\over (l\mp m - k)!}}
            \ket{l,m \pm k}

where

.. math::

    L_1 + i L_2 = i \sin \phi \ \partial_\theta
         + i \cot \theta \cos \phi \ \partial_\phi
        \pm \left(\cos\phi \ \partial_\theta
        - \cot \theta \sin \phi \ \partial_\phi\right) =

    = e^{\pm i\phi} \left(\pm \partial_\theta + i \cot\theta \partial_\phi
        \right)

The solution of :eq:`Ylm_eig` is of the form:

.. math::
    :label: Ylm_form

    \braket{\theta \phi | l m} = Y_{lm}(\theta, \phi)
        = \Theta_{lm}(\theta) \Phi_m(\phi)

and we get from :eq:`Ylm_eig`:

.. math::

    -i {\d\over\d\phi} \Phi_m(\phi) = m \Phi_m(\phi)

on the interval $[0, 2 \pi]$ with the boundary condition $\Phi_m(0) =
\Phi_m(2\pi)$. From
:ref:`deriv_operator` the eigenvalues are all integer $m$
and the normalized eigenvector is:

.. math::
    :label: Phi_sol

    \Phi_m(\phi) = {1\over\sqrt{2\pi}} e^{im\phi}

Substituting :eq:`Phi_sol` into :eq:`Ylm_form` we get from
:eq:`Ylm_eig` an ordinary second order differential equation for
$\Theta_{lm}(\theta)$:

.. math::

    L^2 \ket{lm} = l(l+1) \ket{lm}

    - \left( {1\over\sin\theta} \partial_\theta
                \left(\sin\theta \ \partial_\theta \right)
         + {1\over \sin^2\theta}\partial_\phi^2\right)
        {1\over\sqrt{2\pi}} e^{im\phi} \Theta_{lm}
        = l(l+1) {1\over\sqrt{2\pi}} e^{im\phi} \Theta_{lm}

    {1\over\sin\theta} {\d\over\d \theta}
                \left(\sin\theta {\d\over\d \theta} \Theta_{lm}\right)
                +
            \left( l(l+1) - {m^2\over \sin^2\theta} \right) \Theta_{lm} = 0

    {\d\over\d \cos\theta} \left((1-\cos^2\theta)
        {\d\over\d \cos \theta} \Theta_{lm}\right)
                +
            \left( l(l+1) - {m^2\over 1-\cos^2\theta} \right) \Theta_{lm} = 0

    {\d\over\d z} \left((1-z^2) {\d \Theta_{lm}\over\d z}\right)
        + \left(l (l+1) - {m^2\over 1-z^2}\right)\Theta_{lm} = 0

where

.. math::

    z = \cos\theta

This equation can be solved using the following approach.
From :eq:`ladder` we get:

.. math::

    (L_1\pm iL_2)Y_{lm}(\theta, \phi)
    = (L_1\pm iL_2)\Theta_{lm}(\theta)\Phi_m(\phi) =

    = e^{\pm i\phi} \left(\pm \partial_\theta + i \cot\theta \partial_\phi
        \right) \Theta_{lm}(\theta) {1\over\sqrt{2\pi}} e^{im\phi} =

    = {1\over\sqrt{2\pi}} e^{i(m\pm1)\phi}
        \left(\pm {\d\over\d \theta} -m \cot\theta \right) \Theta_{lm}(\theta) =

    = \mp {1\over\sqrt{2\pi}} e^{i(m\pm1)\phi}
        \left(\sin\theta {\d\over\d \cos \theta} \mp m
            {\d\sin\theta\over\d \cos\theta} \right) \Theta_{lm}(\theta) =

    = \mp {1\over\sqrt{2\pi}} e^{i(m\pm1)\phi}
        \sin^{1\pm m}\theta \left({\d\over\d \cos \theta}
        \sin^{\mp m}\theta\ \Theta_{lm}(\theta) \right) =

    = \mp \Phi_{m\pm 1}(\phi)
        \sin^{1\pm m}\theta \left({\d\over\d \cos \theta}
        \sin^{\mp m}\theta\ \Theta_{lm}(\theta) \right)


and by repeated application we get:

.. math::

    (L_1\pm iL_2)^k Y_{lm}(\theta, \phi)
    = (\mp 1)^k \Phi_{m\pm k}(\phi)
        \sin^{k\pm m}\theta \left({\d^k\over(\d \cos \theta)^k}
        \sin^{\mp m}\theta\ \Theta_{lm}(\theta) \right) =

    = \sqrt{{(l\mp m)!\over (l\pm m)!} {(l\pm m + k)!\over (l\mp m - k)!}}
        \Phi_{m \pm k}(\phi) \Theta_{l,m\pm k}(\theta)

from which we obtain:

.. math::
    :label: Theta_lmpmk

    \Theta_{l,m\pm k}(\theta) =
        \sqrt{{(l\pm m)!\over (l\mp m)!} {(l\mp m - k)!\over (l\pm m + k)!}}
            (\mp 1)^k
        \sin^{k\pm m}\theta \left({\d^k\over(\d \cos \theta)^k}
        \sin^{\mp m}\theta\ \Theta_{lm}(\theta) \right)

As a special case for $m=0$ and $k=m>0$ we get:

.. math::
    :label: Theta_lpmm

    \Theta_{l,\pm m}(\theta) =
            (\mp 1)^m
        \sqrt{{(l - m)!\over (l + m)!}}
        \sin^{m}\theta \left({\d^m\over(\d \cos \theta)^m}
        \Theta_{l0}(\theta) \right)

and for $m=l$ and $k=l-m$ we get (we only use the $\Theta_{l,m- k}$ branch):

.. math::
    :label: Theta_ll

    \Theta_{lm}(\theta) =
    \Theta_{l,l-(l-m)}(\theta) =

        = \sqrt{{(l- l)!\over (l+ l)!} {(l+ l - (l-m))!\over (l- l +
        l-m)!}}
            (+ 1)^{l-m}
        \sin^{l-m- l}\theta \left({\d^{l-m}\over(\d \cos \theta)^{l-m}}
        \sin^{+ l}\theta\ \Theta_{ll}(\theta) \right) =

        = \sqrt{{1\over (2l)!} {(l+m)!\over (l-m)!}}
        {1\over\sin^m\theta} \left({\d^{l-m}\over(\d \cos \theta)^{l-m}}
        \sin^l\theta\ \Theta_{ll}(\theta) \right)

From
:eq:`ladder` we get:

.. math::

    (L_1 + i L_2) Y_{ll}
        = \sqrt{(l - l)(l + l + 1)} Y_{ll} = 0

Using :eq:`Phi_sol` this gives us a first order differential equation:

.. math::

    (L_1 + i L_2) \Theta_{ll} \Phi_l = 0

    e^{i\phi} \left(\partial_\theta + i \cot\theta \partial_\phi
        \right) \Theta_{ll} {1\over\sqrt{2\pi}} e^{i l\phi} = 0

    {\partial \Theta_{ll}\over\partial \theta} - l \cot \theta \ \Theta_{ll} = 0

from which

.. math::
    :label: Theta_ll_form

    \Theta_{ll}(\theta) = (-1)^l \sqrt{(2l+1)!\over 2} {1\over 2^l l!}
        \sin^l \theta

It is normalized as:

.. math::

    \int_0^\pi \Theta_{ll}^2 \sin\theta\ \d\theta = 1

We used the value of the integral:

.. math::

    \int_0^\pi \sin^{2l+1}\theta\ \d\theta = {\sqrt\pi\ \Gamma(l+1)
        \over \Gamma(l+{3\over2})}
     = {\sqrt\pi\  2^{l+1} l! \over (2l+1)!! \sqrt\pi}
     = {2^{l+1} l! \over (2l+1)!!}
     = {2^{2l+2} (l+1)! l! \over (2l+2)!} =

     = {(2^{l+1} l!)^2 (l+1) \over (2l+2)!}
     = {4 (2^l l!)^2 (l+1) \over (2l+1)! 2 (l+1)}
     = {2 (2^l l!)^2 \over (2l+1)!}

Using :eq:`Theta_ll_form` in :eq:`Theta_ll` we get:

.. math::

    \Theta_{lm}(\theta)
        = (-1)^l \sqrt{{2l+1\over 2}{(l+m)!\over (l-m)!}}
        {1\over 2^l l!}
        {1\over\sin^m\theta} {\d^{l-m}\over(\d \cos \theta)^{l-m}}
        \sin^{2l}\theta

for $m=0$ we obtain:

.. math::

    \Theta_{l0}(\theta)
        = (-1)^l \sqrt{{2l+1\over 2}}
        {1\over 2^l l!}
        {\d^l\over(\d \cos \theta)^l}
        \sin^{2l}\theta =

        = \sqrt{{2l+1\over 2}}
        {1\over 2^l l!}
        {\d^l\over(\d \cos \theta)^l}
        (\cos^2\theta-1)^l =

        = \sqrt{{2l+1\over 2}} P_l(\cos\theta)

where

.. math::

    P_l(z) = {1\over 2^l l!} {\d^l\over\d z^l} (z^2-1)^l

is the Rodrigues' formula for Legendre polynomials.
We substitute $\Theta_{l0}$ into :eq:`Theta_lpmm` and get:

.. math::

    \Theta_{l,\pm m}(\theta) =
            (\mp 1)^m
        \sqrt{{2l+1\over 2}{(l - m)!\over (l + m)!}}
        \sin^{m}\theta \left({\d^m\over(\d \cos \theta)^m}
        P_l(\cos\theta) \right)

Hence $\Theta_{lm} = (-1)^m \Theta_{l,-m}$.
Using associated Legendre polynomials, we can write:

.. math::

    \Theta_{lm}(\theta) = \sqrt{{2l+1\over 2}{(l-m)!\over (l+m)!}}
        P_l^m(\theta)

where (for all $m$):

.. math::

        P_l^m(\theta)
        = (-1)^l {(l+m)!\over (l-m)!} {1\over 2^l l!}
        {1\over\sin^m\theta} {\d^{l-m}\over(\d \cos \theta)^{l-m}}
        \sin^{2l}\theta =

        = {(l+m)!\over (l-m)!} {1\over 2^l l!}
        {1\over\sin^m\theta} {\d^{l-m}\over(\d \cos \theta)^{l-m}}
        (\cos^2\theta-1)^l =

        = (-1)^m {1\over 2^l l!}
        {(1-\cos^2)^m\theta\over\sin^m\theta}
            {\d^{l+m}\over(\d \cos \theta)^{l+m}}
        (\cos^2\theta-1)^l =

        = (-1)^m {1\over 2^l l!}
        \sin^m\theta {\d^{l+m}\over(\d \cos \theta)^{l+m}}
        (\cos^2\theta-1)^l =

        = (-1)^m {1\over 2^l l!}
        (1-z^2)^{m\over 2} {\d^{l+m}\over \d z^{l+m}} (z^2-1)^l

hence $P^{-m}_l(z) = (-1)^m {(l-m)!\over (l+m)!} P_l^m(z)$.
For $m \ge 0$:

.. math::

        P_l^{\pm m}(\cos \theta) =
            (\mp 1)^m
        \sin^{m}\theta {\d^m\over(\d \cos \theta)^m} P_l(\cos\theta)

        P_l^{\pm m}(z) =
            (\mp 1)^m
        (1-z^2)^{m\over2} {\d^m\over\d z^m} P_l(z)

Finally, we get (for all $m$):

.. math::

    Y_{lm}(\theta, \phi)
        = \Theta_{lm}(\theta) \Phi_m(\phi)
        = \sqrt{{2l+1\over 4\pi}{(l-m)!\over (l+m)!}}
        P_l^m(\theta) e^{im\phi}
