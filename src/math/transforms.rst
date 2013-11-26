Fourier Transform
-----------------

The 1D Fourier transform is:

.. math::

    F[f(x)] \equiv \tilde f(\omega)
        = \int_{-\infty}^{\infty} f(x) e^{-i\omega x}\,\d x

    F^{-1}[\tilde f(\omega)] = f(x)
        = {1\over2\pi}\int_{-\infty}^{\infty}
        \tilde f(\omega) e^{+i\omega x}\,\d \omega

To show that it works:

.. math::

    F^{-1} F [f(x)]
    =
    {1\over2\pi}\int_{-\infty}^{\infty} \left[\int_{-\infty}^{\infty}
        f(x) e^{-i\omega x}\,\d x\right] e^{+i\omega x}\,\d \omega
    =
    {1\over2\pi}\int_{-\infty}^{\infty} \left[\int_{-\infty}^{\infty}
        f(x') e^{-i\omega x'}\,\d x'\right] e^{+i\omega x}\,\d \omega
    =

    =
    \int_{-\infty}^{\infty} f(x') \left[{1\over2\pi}\int_{-\infty}^{\infty}
        e^{i\omega (x- x')}\,\d \omega \right] \,\d x'
    =
    \int_{-\infty}^{\infty} f(x') \delta(x-x') \,\d x'
    =f(x)

If $x$ is time (unit $[\mathrm{s}]$), then $\omega$ is angular frequency (unit
$[\mathrm{rad}/\mathrm{s}]$). One can express the Fourier transform in terms of
ordinary frequency $\nu$ (unit $[1/\mathrm{s}] = [\mathrm{Hz}]$) by
substituting $\omega = 2\pi \nu$:

.. math::

    \tilde f(\omega) = \tilde f(2\pi \nu) \equiv \tilde f'(\nu)
        = \int_{-\infty}^{\infty} f(x) e^{-2\pi i\nu x}\,\d x

    f(x) = \int_{-\infty}^{\infty} \tilde f'(\nu) e^{+2\pi i\nu x}\,\d \nu

Both transformations are equivalent and only differ in whether we
express the transform in terms of $\omega$ or $\nu$,
the conversion
being given by $\tilde f(\omega) = \tilde f(2\pi \nu) \equiv \tilde f'(\nu)$.
Third frequently used convention that is however not equivalent to the above is:

.. math::

    \tilde f(k)
        = {1\over\sqrt{2\pi}}
          \int_{-\infty}^{\infty} f(x) e^{-ik x}\,\d x

    f(x)
        = {1\over\sqrt{2\pi}}
          \int_{-\infty}^{\infty} \tilde f(k) e^{+ik x}\,\d k

The 3D Fourier transform is:

.. math::
    :label: fourier1

    F[f(\mathbf{x})] \equiv \tilde f(\bomega)
        = \int_{-\infty}^{\infty} f(\mathbf{x}) e^{-i\bomega \cdot
            \mathbf{x}}\,\d^3 x

    F^{-1}[\tilde f(\bomega)] = f(\mathbf{x})
        = {1\over(2\pi)^3}\int_{-\infty}^{\infty}
        \tilde f(\bomega) e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega

With obvious analogs for other conventions and dimensions.

The sign convention in the exponentials $e^{\pm i\omega x}$ is arbitrary, one
can as well flip the sign of the direct and inverse transforms. In particular,
one often uses both sign conventions in the same equation. Consider a spacetime
plane-wave $e^{i k\cdot x} = e^{i(\omega t - \mathbf{k}\cdot\mathbf{x})}$. Then
we obtain (using plus sign convention in the $e^{ik \cdot x}$ exponential for
the direct transformation):

.. math::

    F[f(x)] \equiv \tilde f(k)
        = \int_{-\infty}^{\infty} f(x) e^{ik \cdot x}\,\d^4 x
        = \int_{-\infty}^{\infty} f(x)
            e^{i(\omega t - \mathbf{k}\cdot\mathbf{x})}\,\d^4 x

    F^{-1}[f(k)] \equiv f(x)
        = {1\over(2\pi)^4} \int_{-\infty}^{\infty} \tilde f(k)
            e^{-ik \cdot x}\,\d^4 k
        = {1\over(2\pi)^4} \int_{-\infty}^{\infty} \tilde f(k)
            e^{-i(\omega t - \mathbf{k}\cdot\mathbf{x})}\,\d^4 k

Finally, the equation $k\cdot x = \omega t - \mathbf{k}\cdot\mathbf{x}$ depends
on the metric signature, in this case $\diag({1, -1, -1, -1})$.
For a signature $\diag({-1, 1, 1, 1})$ we would get
$k\cdot x = -\omega t + \mathbf{k}\cdot\mathbf{x}$.

Unlike the normalization convention, where one has to be very careful, the sign
convention in Fourier transform is not a problem, one just has to remember to
flip the sign for the inverse transform.

Shift Theorem
~~~~~~~~~~~~~

The Fourier transform of a shifted function, in 3D:

.. math::

    F[f(\mathbf{x}+\mathbf{b})]
        = \int_{-\infty}^{\infty} f(\mathbf{x}+\mathbf{b}) e^{-i\bomega \cdot
            \mathbf{x}}\,\d^3 x =

        = \int_{-\infty}^{\infty} f(\mathbf{x}) e^{-i\bomega \cdot
            (\mathbf{x}-\mathbf{b})}\,\d^3 x =

        = e^{i\bomega\cdot \mathbf{b}} \int_{-\infty}^{\infty} f(\mathbf{x}) e^{-i\bomega \cdot
            \mathbf{x}}\,\d^3 x =

        = e^{i\bomega\cdot \mathbf{b}} F[f(\mathbf{x})]

Radial Fourier Transform
~~~~~~~~~~~~~~~~~~~~~~~~

As a special case when the function $f(\mathbf{x})=f(r)$ is spherically symmetric,
we introduce spherical coordinates such that the $z$-axis is along the
$\bomega$ vector and calculate (we use $r=|\mathbf{x}|$ and $\omega=|\bomega|$):

.. math::

    F[f(\mathbf{x})] \equiv \tilde f(\bomega)
        = \int_{-\infty}^{\infty} f(\mathbf{x}) e^{-i\bomega \cdot
            \mathbf{x}}\,\d^3 x
        = \int_{-\infty}^{\infty} f(r) e^{-i\bomega \cdot
            \mathbf{x}}\,\d^3 x =

        = \int_0^\infty\d r \int_0^\pi\d\theta \int_0^{2\pi}\d\phi f(r)
            e^{-i \omega r \cos\theta}\,r^2\sin\theta =

        = 2\pi \int_0^\infty\d r \int_0^\pi\d\theta f(r)
            e^{-i \omega r \cos\theta}\,r^2\sin\theta =

        = 4\pi \int_0^\infty\d r f(r) {\sin\omega r \over \omega r}\,r^2 =

        = {4\pi\over\omega} \int_0^\infty r\sin(\omega r) f(r) \,\d r

So the transform is real and spherically symmetric, since the result only
depends on $\omega$.

Similarly, for the inverse transform:

.. math::

    F^{-1}[\tilde f(\bomega)] = f(\mathbf{x})
        = {1\over(2\pi)^3}\int_{-\infty}^{\infty}
        \tilde f(\bomega) e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega =

        = {1\over(2\pi)^3}\int_{-\infty}^{\infty}
        \tilde f(\omega) e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega =

        = {1\over(2\pi)^3}
        {4\pi\over r} \int_0^\infty \omega\sin(\omega r) f(\omega) \,\d \omega
        =

        = {1\over 2\pi^2 r}
        \int_0^\infty \omega\sin(\omega r) f(\omega) \,\d \omega


Fourier Transform of a Periodic Function (e.g. in a Crystal)
------------------------------------------------------------

The Fourier transform in :eq:`fourier1` requires the function $f(\mathbf{x})$
to be decaying fast enough in order to converge. In an infinite crystal, on the
other hand, the function $f(\mathbf{x})$ is typically periodic (and thus not
decaying):

.. math::

    f(\mathbf{x}+\mathbf{T}(n_1, n_2, n_3)) = f(\mathbf{x})

where $\mathbf{T}(\mathbf{n})=\mathbf{T}(n_1, n_2,
n_3)=n_1\mathbf{a}_1+n_2\mathbf{a}_2+n_3\mathbf{a}_3$ are the crystal
translation vectors. As such, the Fourier transform in :eq:`fourier1` is
infinite, but it can be made finite by the following definition:

.. math::
    :label: fourier2

    F[f(\mathbf{x})] \equiv \tilde f(\bomega)
        = {1\over\Omega_\mathrm{crystal}}\int_{\Omega_\mathrm{crystal}} f(\mathbf{x}) e^{-i\bomega \cdot
            \mathbf{x}}\,\d^3 x =

        = {1\over\Omega_\mathrm{crystal}} \sum_\mathbf{n} \int_{\Omega_\mathrm{cell}}
        f(\mathbf{x}+\mathbf{T}(\mathbf{n}))
        e^{-i\bomega \cdot (\mathbf{x}+\mathbf{T}(\mathbf{n}))}\,\d^3 x =

        = {1\over\Omega_\mathrm{crystal}} \sum_\mathbf{n} \int_{\Omega_\mathrm{cell}} f(\mathbf{x})
        e^{-i\bomega \cdot (\mathbf{x}+\mathbf{T}(\mathbf{n}))}\,\d^3 x =

        = {1\over\Omega_\mathrm{crystal}} \sum_\mathbf{n} e^{-i\bomega \cdot \mathbf{T}(\mathbf{n})} \int_{\Omega_\mathrm{cell}} f(\mathbf{x})
        e^{-i\bomega \cdot \mathbf{x}}\,\d^3 x =

        = {1\over\Omega_\mathrm{crystal}} N_\mathrm{cell} \int_{\Omega_\mathrm{cell}} f(\mathbf{x})
        e^{-i\bomega \cdot \mathbf{x}}\,\d^3 x =

        = {1\over\Omega_\mathrm{cell}} \int_{\Omega_\mathrm{cell}} f(\mathbf{x})
        e^{-i\bomega \cdot \mathbf{x}}\,\d^3 x

This assumes that the wave vector $\bomega=\mathbf{G}$ is equal to the
reciprocal space vectors $\mathbf{G}$, defined by

.. math::
    :label: G

    e^{i\mathbf{G} \cdot \mathbf{T}(\mathbf{n})} = 1\,,

because then $\sum_\mathbf{n} e^{-i\bomega \cdot \mathbf{T}(\mathbf{n})} =
\sum_\mathbf{n} 1 = N_\mathrm{cell}$.

For $\bomega\neq\mathbf{G}$, the expression ${1\over\Omega_\mathrm{crystal}}
\sum_\mathbf{n} e^{-i\bomega \cdot \mathbf{T}(\mathbf{n})} = 0$ vanishes,
because the sum is bounded, and so dividing by the (infinite) crystal volume
makes the expression vanish, and so $\tilde f(\bomega)=0$.  In other words, the
only non-zero Fourier components $\tilde f(\bomega)$ of any periodic function
$f(\mathbf{x})$ are those with $\bomega=\mathbf{G}$. Equivalently said, if the
Fourier components of a given function are non-zero for some
$\bomega\neq\mathbf{G}$, then the function is not periodic.

Summary: the only difference between the crystal Fourier transform
:eq:`fourier2` and the usual Fourier transform :eq:`fourier1` is the
$\Omega_\mathrm{crystal}$ factor. The Fourier transform :eq:`fourier2` of a
periodic function is nonzero only for $\omega=\mathbf{G}$ and is equal to:

.. math::
    :label: fourier2b

    F[f(\mathbf{x})] \equiv \tilde f(\mathbf{G})
        = {1\over\Omega_\mathrm{cell}} \int_{\Omega_\mathrm{cell}} f(\mathbf{x})
        e^{-i\mathbf{G} \cdot \mathbf{x}}\,\d^3 x

Note: the fact that the sum is bounded follows from:

.. math::

    \left| \sum_{n=-\infty}^\infty e^{ikn} \right|
        = \left| \lim_{N\to\infty} \sum_{n=-N}^N e^{ikn} \right|
        = \left| \lim_{N\to\infty} \left(1+2\sum_{n=1}^N \cos kn\right) \right|=

        = \left| \lim_{N\to\infty} {\cos kN - \cos k(N+1) \over 1-\cos k}
            \right|
        < {2 \over | 1-\cos k | }

Because $| \cos kN - \cos k(N+1) | < 2$.  So for $k\neq 2\pi$ (i.e. the
denominator is non-zero), the sum is bounded (to be precise, the infinite sum
does not converge, because it oscillates, but the point is that the partial sum
is always bounded). For $k=2\pi$, the sum is infinite, because $e^{i2\pi n} =
1$.

Since we divided the direct Fourier transform in :eq:`fourier1` by
$\Omega_\mathrm{crystal}$ to obtain :eq:`fourier2`, we need to multiply the
inverse transform in :eq:`fourier1` by $\Omega_\mathrm{crystal}$:

.. math::
    :label: fourier2b_inv

    F^{-1}[\tilde f(\bomega)] = f(\mathbf{x})
        = {\Omega_\mathrm{crystal}\over(2\pi)^3}\int_{-\infty}^{\infty}
        \tilde f(\bomega) e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega
        = \sum_{\mathbf{G}}
        \tilde f(\mathbf{G}) e^{+i\mathbf{G} \cdot \mathbf{x}}


Discrete Fourier Transform
--------------------------

Starting from

.. math::

    \tilde f(\nu)
        = \int_{-\infty}^{\infty} f(x) e^{-2\pi i\nu x}\,\d x

    f(x) = \int_{-\infty}^{\infty} \tilde f(\nu) e^{+2\pi i\nu x}\,\d \nu

When the $x$ space is discrete, that is $f(x)\to f(x_k)\equiv f_k$, where
$x_k = k\Delta$ and $k=0, 1, \cdots, N-1$, we obtain:

.. math::

    \tilde f(\nu)
        = \int_0^{(N-1)\Delta} f(x) e^{-2\pi i\nu x}\,\d x
        = \sum_{k=0}^{N-1} f_k e^{-2\pi i\nu x_k}
        = \sum_{k=0}^{N-1} f_k e^{-2\pi i\nu k \Delta}

We only need to sample the reciprocal space at the intervals
$\nu = {n\over N \Delta}$ where $n=0, 1, \cdots, N-1$. We finally get:

.. math::

    \tilde f(\nu_n) \equiv \tilde f_n
        = \sum_{k=0}^{N-1} f_k e^{-2\pi i {n\over N} k}

For the inverse transform, we obtain:

.. math::

    f_k
        = {1\over N} \sum_{n=0}^{N-1} \tilde f_n e^{2\pi i {n\over N} k}

Laplace Transform
-----------------

Laplace transform of $f(x)$ is:

.. math::

    L[f(x)] = \int_0^{\infty} f(x) e^{-s x}\,\d x

    L^{-1}[\bar f(s)]
    = {1\over2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
        \bar f(s) e^{s x}\,\d s
    = \sum_{s_0} \res_{s=s_0} (\bar f(s) e^{s x})

The contour integration is over the vertical line $\sigma+i\omega$ and $\sigma$
is chosen large enough so that all residues are to the left of the line (that's
because the Laplace transform $\bar f(s)$ is only defined for $s$ larger than
the residues, so we have to integrate in this range as well).  It can be shown
that the integral over the left semicircle goes to zero:

.. math::

    \left|\int_\Omega e^{sx}g(s) \d s \right|
    =\left|\int_{\pi\over2}^{3\pi\over2} e^{(\sigma + Re^{i\varphi})x}
    g(\sigma+Re^{i\varphi})iRe^{i\varphi}\d\varphi\right|
    \le

    \le R \max_\Omega |g(z)| e^{\sigma x}
        \int_{\pi\over2}^{3\pi\over2}\left| e^{xRe^{i\varphi}}
        \right|\d\varphi
    =

    = R \max_\Omega |g(z)| e^{\sigma x}
        \int_{\pi\over2}^{3\pi\over2}e^{xR \cos \varphi} \d\varphi
    =

    = R \max_\Omega |g(z)| e^{\sigma x}
        \int_0^{\pi}e^{-xR \sin \varphi} \d\varphi
    =

    < {\pi e^{\sigma x}\over x} \max_\Omega |g(z)|

so the complex integral is equal to the sum of all residues of $\bar
f(s)e^{sx}$ in the complex plane.

To show that it works:

.. math::

    L^{-1} L [f(x)]
    =
    {1\over2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
        \left[\int_0^{\infty}
        f(x) e^{-s x}\,\d x\right] e^{s x}\,\d s
    =
    {1\over2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
        \left[\int_0^{\infty}
        f(x') e^{-s x'}\,\d x'\right] e^{s x}\,\d s
    =

    =
    \int_0^{\infty} f(x') \left[{1\over2\pi i}
        \int_{\sigma-i\infty}^{\sigma+i\infty}
        e^{s (x- x')}\,\d s \right] \,\d x'
    =
    \int_0^{\infty} f(x') \delta(x-x') \,\d x'
    =f(x)

where we used:

.. math::

    {1\over2\pi i}
    \int_{\sigma-i\infty}^{\sigma+i\infty} e^{s (x- x')}\,\d s
    =
    {1\over2\pi i}
        \int_{\sigma-i\infty}^{\sigma+i\infty} e^{s (x- x')}\,\d s
    =
    {1\over2\pi i}
        \int_{-\infty}^{\infty} e^{(\sigma+i\omega) (x- x')}\,i\d \omega
    =

    =
    {e^{\sigma (x- x')}\over2\pi}
        \int_{-\infty}^{\infty} e^{i\omega (x- x')}\,\d \omega
    = e^{\sigma (x- x')}\delta(x - x')
    =\delta(x - x')

and it can be derived from the Fourier transform by
transforming a function $U(x)$:

.. math::

    U(x) = \begin{cases}
        f(x)e^{-\sigma x} &\text{for $x\ge0$}\cr
        0 &\text{for $x<0$}\cr
        \end{cases}

and making a substitution $s = \sigma + i\omega$:

.. math::

    L[f(x)] \equiv \bar f(s) = F[U(x)] \equiv \tilde U(\omega)
    = \int_{-\infty}^{\infty} U(x) e^{-i\omega x}\,\d x
    = \int_0^{\infty} f(x) e^{-\sigma x} e^{-i\omega x}\,\d x
    = \int_0^{\infty} f(x) e^{-s x}\,\d x

    L^{-1}[\bar f(s)] \equiv f(x) = U(x) e^{\sigma x}
    = F^{-1}[\tilde U(\omega)]e^{\sigma x}
    = F^{-1}[\bar f(s)]e^{\sigma x}
    = F^{-1}[\bar f(\sigma+i\omega)e^{\sigma x}]

    = {1\over2\pi}\int_{-\infty}^{\infty} \bar f(\sigma + i\omega)e^{\sigma x}
        e^{i\omega x}\,\d \omega
    = {1\over2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}
        \bar f(s) e^{s x}\,\d s
    = \sum_{s_0} \res_{s=s_0} (\bar f(s) e^{s x})

Where the bar ($\bar f$) means the Laplace transform and tilde ($\tilde U$)
means the Fourier transform.
