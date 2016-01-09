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

Scaling
~~~~~~~

For $a>0$:

.. math::

    F[f(ax)](\omega)
        = \int_{-\infty}^{\infty} f(ax) e^{-i\omega x}\,\d x =

        = {1\over a}\int_{-\infty}^{\infty} f(y) e^{-i{\omega\over a} y}\,\d y =

        = {1\over a}F[f(x)]\left({\omega\over a}\right)

Derivative
~~~~~~~~~~

The Fourier transform of a derivative, in 3D:

.. math::

    F[\partial_i f(\mathbf{x})]
        = \int_{-\infty}^{\infty} (\partial_i f(\mathbf{x})) e^{-i\bomega \cdot
            \mathbf{x}}\,\d^3 x =

        = \left[f(\mathbf{x}) e^{-i\bomega \cdot
                \mathbf{x}}\right]_{-\infty}^{\infty}
          -\int_{-\infty}^{\infty} f(\mathbf{x}) \partial_i e^{-i\bomega \cdot
            \mathbf{x}}\,\d^3 x =

        = -\int_{-\infty}^{\infty} f(\mathbf{x}) \partial_i e^{-i\omega_j
            x^j}\,\d^3 x =

        = -(-i\omega_i)\int_{-\infty}^{\infty} f(\mathbf{x})
            e^{-i\bomega \cdot \mathbf{x}}\,\d^3 x =

        = i\omega_i F[f(\mathbf{x})]\,.

An alternative derivation is to start from:

.. math::

    f(\mathbf{x}) = F^{-1}[\tilde f(\bomega)]
        = {1\over(2\pi)^3}\int_{-\infty}^{\infty}
        \tilde f(\bomega) e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega

and differentiate both sides:


.. math::

    \partial_i f(\mathbf{x})
        = {1\over(2\pi)^3}\int_{-\infty}^{\infty}
        \tilde f(\bomega) \partial_i e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega

    \partial_i f(\mathbf{x})
        = {1\over(2\pi)^3}\int_{-\infty}^{\infty}
        i\omega_i \tilde f(\bomega) e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega
        \,,

from which:

.. math::

    F[\partial_i f(\mathbf{x})]
        = i\omega_i \tilde f(\bomega)
        = i\omega_i F[f(\mathbf{x})]\,.

Convolution
~~~~~~~~~~~

The convolution of two functions $f(x)$ and $g(x)$ is defined as:

.. math::

    f(x) * g(x) = \int_{-\infty}^\infty f(y) g(x-y) \,\d y

The Fourier transform of a convolution is:

.. math::

    F[f(x) * g(x)](\omega)
        = \int_{-\infty}^\infty \int_{-\infty}^\infty
            f(y) g(x-y) \,\d y\, e^{-i\omega x}\d x =

        = \int_{-\infty}^\infty \int_{-\infty}^\infty
            g(x-y) e^{-i\omega x} \d x\, f(y) \,\d y =

        = \int_{-\infty}^\infty \int_{-\infty}^\infty
            g(u) e^{-i\omega (u+y)} \d u\, f(y) \,\d y =

        = \int_{-\infty}^\infty g(u) e^{-i\omega u} \d u
        \int_{-\infty}^\infty f(y) e^{-i\omega y} \d y

        = F[f(x)](\omega)\ F[g(x)](\omega)

And for the inverse transform:

.. math::

    F^{-1}[f(\omega) * g(\omega)](x)
        = {1\over 2\pi} \int_{-\infty}^\infty \int_{-\infty}^\infty
            f(y) g(\omega-y) \,\d y\, e^{i\omega x}\d \omega =

        = {1\over 2\pi} \int_{-\infty}^\infty \int_{-\infty}^\infty
            g(\omega-y) e^{i\omega x} \d \omega\, f(y) \,\d y =

        = {1\over 2\pi} \int_{-\infty}^\infty \int_{-\infty}^\infty
            g(u) e^{ix (u+y)} \d u\, f(y) \,\d y =

        = 2\pi {1\over 2\pi} \int_{-\infty}^\infty g(u) e^{ix u} \d u
        {1\over 2\pi}
        \int_{-\infty}^\infty f(y) e^{ix y} \d y

        = 2\pi F^{-1}[f(\omega)](x)\ F^{-1}[g(\omega)](x)

Fourier transform of a function multiplication is:

.. math::

    F [ f g ]
        = F [\ F^{-1}[ F[f] ]\quad  F^{-1}[ F[g] ]\ ]
        = {1\over 2\pi} F [ F^{-1} [ F[f] * F[g] ]]
        = {1\over 2\pi} F[f] * F[g]

and for the inverse transform:

.. math::

    F^{-1} [ f g ]
        = F^{-1} [\ F[ F^{-1}[f] ]\quad  F[ F^{-1}[g] ]\ ]
        = F^{-1} [ F [ F^{-1}[f] * F^{-1}[g] ]]
        = F^{-1}[f] * F^{-1}[g]

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

        = 4\pi \int_0^\infty f(r) \sinc(\omega r) \,r^2 \d r =

        = 4\pi \int_0^\infty f(r) {\sin\omega r \over \omega r}\,r^2 \d r =

        = {4\pi\over\omega} \int_0^\infty r\sin(\omega r) f(r) \,\d r\,,

where we used:

.. math::

    \int_0^\pi e^{-i \omega r \cos\theta}\,\sin\theta \d\theta
        = \int_{-1}^1 e^{i\omega r u} \d u
        = \left[e^{i\omega r u} \over i\omega r\right]_{-1}^1
        = {e^{i\omega r} - e^{-i\omega r} \over i \omega r} =

        = 2 {\sin(\omega r) \over \omega r}
        = 2 \sinc(\omega r) = 2 j_0(\omega r)\,.

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


Examples
~~~~~~~~

Rectangular Function
^^^^^^^^^^^^^^^^^^^^

The rectangular function is defined as:

.. math::

    \Pi(x) = H(x+\half) - H(x-\half)

The Fourier transform is:

.. math::

    F[\Pi(x)] \equiv \tilde \Pi(\omega)
        = \int_{-\infty}^{\infty} \Pi(x) e^{-i\omega x}\,\d x
        = \int_{-\half}^{\half} e^{-i\omega x}\,\d x =

        = \left[e^{-i\omega x} \over -i\omega x\right]_{x=-\half}^\half
        = {e^{i{\omega\over 2}} - e^{-i{\omega \over 2}} \over i
            {\omega\over2}}
        = 2{\sin({\omega \over 2}) \over {\omega \over 2}}
        = 2\sinc\left({\omega\over 2}\right)\,.

Dirichlet Kernel
^^^^^^^^^^^^^^^^

The Dirichlet kernel $D_N(x)$ is a partial sum of complex exponentials:

.. math::

    D_N(x) = {1\over 2\pi}\sum_{n=-N}^N e^{inx} =

    = {1\over 2\pi}\left(1+2\sum_{n=1}^N \cos(nx)\right) =

    = {1\over 2\pi \sin\left(x\over2\right)}\left(\sin\left(x\over2\right)
        +2\sum_{n=1}^N \cos(nx)\sin\left(x\over2\right)\right) =

    = {1\over 2\pi \sin\left(x\over2\right)}\left(\sin\left(x\over2\right)
        +\sum_{n=1}^N\left(
        \sin\left(\left(n+\half\right)x\right)
        -\sin\left(\left(n-\half\right)x\right)
        \right)\right) =

    = {\sin\left(\left(N+\half\right)x\right)
        \over 2\pi \sin\left(x\over2\right)}

From the definition, it is a periodic function with period $2\pi$.

Integral of it is equal to one:

.. math::

    \int_{-\pi}^\pi D_N(x) \d x
    = \int_{-\pi}^\pi {1\over 2\pi}\left(1+2\sum_{n=1}^N \cos(nx)\right) \d x =

    = 1 + {1\over \pi}\sum_{n=1}^N \int_{-\pi}^\pi  \cos(nx)\, \d x = 1

also

.. math::

    \int_{-\pi}^\pi D_N(x-y) \d y = 1

The Dirichlet kernel $D_N(x)$ converges towards a train of delta functions
(called Dirac comb, see the equation :eq:`delta_exp2` in the next section):

.. math::
    :label: delta_exp

    {1\over 2\pi}\sum_{n=-\infty}^\infty e^{inx}
        = \lim_{N\to\infty} {1\over 2\pi}\sum_{n=-N}^N e^{inx}
        = \lim_{N\to\infty} D_N(x) =

        = \lim_{N\to\infty} {\sin\left(\left(N+\half\right)x\right)
            \over 2\pi \sin\left(x\over2\right)}
        = \sum_{n=-\infty}^\infty \delta(x-2\pi n)

Let us do the crucial step in more details using distributions:

.. math::

    \int_{-\infty}^\infty
        \lim_{N\to\infty} {\sin\left(\left(N+\half\right)x\right)
            \over 2\pi \sin\left(x\over2\right)}
        \varphi(x) \,\d x =

    = \sum_{n=-\infty}^\infty \lim_{N\to\infty} \int_{-\pi}^\pi
        {\sin\left(\left(N+\half\right)(x+2\pi n)\right)
            \over 2\pi \sin\left(x+2\pi n\over2\right)}
        \varphi(x+2\pi n) \,\d x =

    = \sum_{n=-\infty}^\infty \varphi(2\pi n) =

    =\int_{-\infty}^\infty \sum_{n=-\infty}^\infty \delta(x-2\pi n)
        \varphi(x)\,\d x

Where we used the fact that

.. math::

    \left[\lim_{N\to\infty} \int_{-\pi}^\pi
        {\sin\left(\left(N+\half\right)(x+2\pi n)\right)
            \over 2\pi \sin\left(x+2\pi n\over2\right)}
        \varphi(x+2\pi n) \,\d x \right] - \varphi(2\pi n) =

    = \left[\lim_{N\to\infty} \int_{-\pi}^\pi
        D_N(x+2\pi n)
        \varphi(x+2\pi n) \,\d x \right] - \varphi(2\pi n) =

    = \lim_{N\to\infty} \int_{-\pi}^\pi
        D_N(x+2\pi n)
        \left(\varphi(x+2\pi n)-\varphi(2\pi n)\right) \,\d x =

    = \lim_{N\to\infty} \int_{-\pi}^\pi
        {\varphi(x+2\pi n)-\varphi(2\pi n)
        \over 2\pi\sin\left(x+2\pi n\over 2\right)}
        \sin\left(\left(N+\half\right)(x+2\pi n)\right)
        \,\d x =

    = 0

Dirac Comb (Shah) Function
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Dirac comb function, also called the Shah function, is defined as:

.. math::

    \Sh(x) = \sum_{n=-\infty}^\infty \delta(x-n)

It has the following scaling property:

.. math::

    \Sh(ax) = \sum_{n=-\infty}^\infty \delta(ax-n)
    = \sum_{n=-\infty}^\infty \delta\left(a\left(x-{n\over a}\right)\right)
    = \sum_{n=-\infty}^\infty {1\over|a|}\delta\left(x-{n\over a}\right)

and for $a={1\over L}$ with $L>0$:

.. math::

    \Sh\left({x\over L}\right) = \sum_{n=-\infty}^\infty L\delta(x-nL)

From which a train of delta functions $L$ distance apart is expressed using a
Dirac comb as:

.. math::

    \sum_{n=-\infty}^\infty \delta(x-nL) = {1\over L}\Sh\left({x\over L}\right)

Using the identity :eq:`delta_exp`, the infinite sum of complex exponentials is
also equal to a Dirac comb:

.. math::
    :label: delta_exp2

    {1\over 2\pi}\sum_{n=-\infty}^\infty e^{inx}
        = \lim_{N\to\infty} {1\over 2\pi}\sum_{n=-N}^N e^{inx}
        = \lim_{N\to\infty} D_N(x) =

        = \lim_{N\to\infty} {\sin\left(\left(N+\half\right)x\right)
            \over 2\pi \sin\left(x\over2\right)}
        = \sum_{n=-\infty}^\infty \delta(x-2\pi n)
        = {1\over 2\pi}\Sh\left({x\over 2\pi}\right)

Using :eq:`delta_exp2` we can now calculate the Fourier transform:

.. math::

    F[\Sh(x)](\omega) \equiv \tilde \Sh(\omega)
        = \int_{-\infty}^{\infty} \Sh(x) e^{-i\omega x}\,\d x =

        = \int_{-\infty}^{\infty} \sum_{n=-\infty}^\infty \delta(x-n)
            e^{-i\omega x}\,\d x =

        = \sum_{n=-\infty}^\infty \int_{-\infty}^{\infty} \delta(x-n)
            e^{-i\omega x}\,\d x =

        = \sum_{n=-\infty}^\infty e^{-i\omega n} =

        = 2\pi \sum_{n=-\infty}^\infty \delta(\omega-2\pi n) =

        = \Sh\left({\omega\over 2\pi}\right)

For the inverse Fourier transform we get (using the previous result):

.. math::

    F^{-1}[\Sh(\omega)](x)
        = F^{-1}\left[\ \Sh\left({(2\pi\omega)\over2\pi}\right) \ \right](x)
        = F^{-1}[\ F[\Sh(x)](2\pi\omega) \ ](x)
        = F^{-1}\left[\ F\left[{1\over2\pi}\Sh\left({x\over2\pi}\right)\right](\omega) \ \right](x)
        = {1\over2\pi}\Sh\left({x\over2\pi}\right)

Periodic Summation
^^^^^^^^^^^^^^^^^^

The convolution $f(x) * g(x) = \int_{-\infty}^\infty f(y) g(x-y) \,\d y$ of a
Dirac comb $\Sh(x)$ and an arbitrary function $f(x)$ is called a periodic
summation:

.. math::

    f(x) * \Sh(x)
        = \int_{-\infty}^\infty f(y) \Sh(x-y) \,\d y
        = \int_{-\infty}^\infty f(y)
            \sum_{n=-\infty}^\infty \delta(x-y-n) \,\d y =

        = \sum_{n=-\infty}^\infty f(x-n)
        = \sum_{n=-\infty}^\infty f(x+n)

because the result is a periodic function with period 1:

.. math::

    (f * \Sh)(x+1)
        = \sum_{n=-\infty}^\infty f(x+n+1)
        = \sum_{m=-\infty}^\infty f(x+m)
        = (f * \Sh)(x)

Poisson Summation Formula
^^^^^^^^^^^^^^^^^^^^^^^^^

The Poisson summation formula:

.. math::
    :label: poisson_summation_formula

    \sum_{n=-\infty}^\infty f(2\pi n)
        = {1\over 2\pi} \sum_{n=-\infty}^\infty \tilde f(n)

can be derived using a Dirac comb:

.. math::

    \sum_{n=-\infty}^\infty f(2\pi n)
        = \int_{-\infty}^\infty f(x) \sum_{n=-\infty}^\infty
            \delta(x-2\pi n) \,\d x =

        = \int_{-\infty}^\infty f(x) {1\over 2\pi}
            \Sh\left(x\over2\pi\right) \,\d x =

        = {1\over 2\pi} \int_{-\infty}^\infty f(x) \cdot
            F[\Sh(\omega)](x) \,\d x =

        = {1\over 2\pi} \int_{-\infty}^\infty F[f(x)](\omega) \cdot
            \Sh(\omega) \,\d \omega =

        = {1\over 2\pi} \int_{-\infty}^\infty \tilde f(\omega) \cdot
            \sum_{n=-\infty}^\infty \delta(\omega-n) \,\d \omega =

        = {1\over 2\pi} \sum_{n=-\infty}^\infty \tilde f(x)

An alternative derivation using Fourier series (see next sections):

.. math::

    \sum_{n=-\infty}^\infty f(x+2\pi n)
        = g(x)
        = \sum_{n=-\infty}^\infty {1\over 2\pi}\int_{-\pi}^\pi
            g(y) e^{-iny} \d y\,  e^{inx} =

        = \sum_{n=-\infty}^\infty {1\over 2\pi}\int_{-\pi}^\pi
            \sum_{m=-\infty}^\infty f(y+2\pi m)
            e^{-iny} \d y\,  e^{inx} =

        = \sum_{n=-\infty}^\infty {1\over 2\pi}
            \sum_{m=-\infty}^\infty
            \int_{-\pi}^\pi
            f(y+2\pi m)
            e^{-in(y+2\pi m)} \d y\,  e^{inx} =

        = \sum_{n=-\infty}^\infty {1\over 2\pi}
            \int_{-\infty}^\infty
            f(y) e^{-iny} \d y\,  e^{inx} =

        = \sum_{n=-\infty}^\infty {1\over 2\pi}
            \tilde f(n) \,  e^{inx}

And setting $x=0$ we get the Poisson summation formula
:eq:`poisson_summation_formula`.

The last derivation can actually also be done using a Dirac comb function as
follows:

.. math::

    \sum_{n=-\infty}^\infty f(x+2\pi n)
        = f(x) * {1\over2\pi}\Sh\left(x \over 2\pi \right ) =

        = F^{-1}\left[\ F\left[f(x) * {1\over2\pi}\Sh\left(x \over
            2\pi \right ) \right](\omega)\ \right](x) =

        = F^{-1}\left[\ F[f(x)](\omega)\ F\left[{1\over2\pi}\Sh\left(x \over
            2\pi \right )\right](\omega)\ \right](x) =

        = F^{-1}[\ F[f(x)](\omega)\ \Sh(\omega)\ ](x) =

        = {1\over 2\pi} \int_{-\infty}^\infty
            F[f(x)](\omega) \Sh(\omega) e^{i\omega x} \d x =

        = \sum_{n=-\infty}^\infty {1\over 2\pi}
            F[f(x)](n) \,  e^{inx}

Fourier Series
^^^^^^^^^^^^^^

Consider a periodic function on an interval $[-\pi, \pi]$:

.. math::
    :label: fs1

    f(x) = \sum_{n=-\infty}^\infty f_n e^{inx}

To calculate the Fourier coefficients $f_n$, we multiply both sides of
:eq:`fs1` by $e^{-imx}$ and integrate:

.. math::

    \int_{-\pi}^\pi f(x) e^{-imx} \d x
        = \int_{-\pi}^\pi \sum_{n=-\infty}^\infty f_n e^{inx} e^{-imx} \d x =

        = \sum_{n=-\infty}^\infty f_n \int_{-\pi}^\pi e^{i(n-m)x} \d x =

        = \sum_{n=-\infty}^\infty f_n 2\pi\delta_{nm} =

        = 2\pi f_m \,,

so

.. math::
    :label: fs2

    f_n = {1\over2\pi} \int_{-\pi}^\pi f(x) e^{-inx} \d x


From Fourier transform: we define a new function $f_0(x)=f(x)$ in the
the $[-\pi, \pi]$ interval and zero otherwise. Then:

.. math::

    f(x) = f_0(x) * {1\over 2\pi}\Sh\left(x\over2\pi\right)
        = \sum_{n=-\infty}^\infty f_0(x+2\pi n)

Apply Fourier transform:

.. math::
    :label: ffrelation

    F[f(x)](\omega)
        = F\left[f_0(x)
            * {1\over 2\pi}\Sh\left(x\over2\pi\right)\right](\omega) =

        = F[f_0(x)](\omega)\ F\left[{1\over 2\pi}\Sh\left(x\over2\pi\right)\                    \right](\omega)
        = F[f_0(x)](\omega)\ \Sh(\omega) =

        = \sum_{n=-\infty}^\infty F[f_0(x)](n) \ \delta(\omega-n)=

        = \sum_{n=-\infty}^\infty
            \int_{-\pi}^\pi f(x) e^{-i n x} \d x \ \delta(\omega-n) =

        = 2\pi \sum_{n=-\infty}^\infty f_n \delta(\omega-n)

We can see that the Fourier transform is zero for $\omega \neq n$. For
$\omega=n$ it is equal to a delta function times a $2\pi$ multiple of a Fourier
series coefficient.

Equation :eq:`ffrelation` provides the relation between a Fourier transform and
a Fourier series. For example for $f(x) = \sin(x)$, the only nonzero Fourier
coefficients are $f_{-1} = {i\over2}$ and $f_1 = -{i\over2}$. The Fourier
transform then is:

.. math::

    F[\sin(x)](\omega)
        = 2\pi\left(f_{-1}\delta(\omega-(-1)) + f_1\delta(\omega-1)\right) =

        = 2\pi\left({i\over 2}\delta(\omega+1))
            -{i\over2}\delta(\omega-1)\right)
        = i\pi\delta(\omega+1) - i\pi\delta(\omega-1)

For $f(x) = 1$ the only nonzero Fourier coefficient is $f_0=1$, the Fourier
transform then is:

.. math::

    F[1](\omega)
        = 2\pi f_0 \delta(\omega-0)
        = 2\pi \delta(\omega)

For $f(x) = e^{3ix}$ the only nonzero Fourier coefficient is $f_3=1$, the
Fourier transform then is:

.. math::

    F[e^{3ix}](\omega)
        = 2\pi f_3 \delta(\omega-3)
        = 2\pi \delta(\omega-3)

For $f(x) = \sum_{n=-\infty}^\infty \delta(x-2\pi n)$ the Fourier coefficients
are all equal to $f_n={1\over 2\pi}$ and the Fourier transform is:

.. math::

    F[f(x)](\omega)
        = 2\pi \sum_{n=-\infty}^\infty f_n \delta(\omega-n)
        = \sum_{n=-\infty}^\infty \delta(\omega-n)

Convergence of Fourier Series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To see what conditions the function $f(x)$ must satisfy in order for the
Fourier series to converge towards it, we can do the following analysis.
Substituting :eq:`fs2` into :eq:`fs1` yields:


.. math::

    f(x) = \sum_{n=-\infty}^\infty {1\over 2\pi}\int_{-\pi}^\pi
        f(y) e^{-iny} \d y\,  e^{inx} =

    = \lim_{N\to\infty} \int_{-\pi}^\pi
        {1\over 2\pi}\sum_{n=-N}^N e^{in(x-y)} f(y) \d y =

    = \lim_{N\to\infty} \int_{-\pi}^\pi D_N(x-y) f(y) \d y

We can now calculate the difference between the Fourier series and the function
value:

.. math::

    \lim_{N\to\infty} \int_{-\pi}^\pi D_N(x-y) f(y) \d y - f(x) =

    = \lim_{N\to\infty} \int_{-\pi}^\pi D_N(x-y) \left(f(y)-f(x)\right) \d y =

    = \lim_{N\to\infty} \int_{-\pi}^\pi
        {\sin\left(\left(N+\half\right)(x-y)\right)
            \over 2\pi \sin\left(x-y\over2\right)}
        \left(f(y)-f(x)\right) \d y =

    = \lim_{N\to\infty} \int_{-\pi}^\pi {f(y)-f(x)\over
        2\pi\sin\left(x-y\over 2\right)}
        \sin\left(\left(N+\half\right)(x-y)\right) \d y =

    = \lim_{N\to\infty} \int_{x-\pi}^{x+\pi} {f(x-u)-f(x)\over
        2\pi\sin\left(u\over 2\right)}
        \sin\left(\left(N+\half\right)u\right) \d u =

    = \lim_{N\to\infty} \int_{x-\pi}^{x+\pi} h(u)
        \sin\left(\left(N+\half\right)u\right) \d u = 0

where $h(u)$ is finite and well behaved at the origin $u=0$:

.. math::

    h(u) = {f(x-u)-f(x)\over 2\pi\sin\left(u\over 2\right)}
        = - {f'(x)\over \pi} + {f''(x)\over 2\pi} u + O(u^2)

The integral is zero because the more and more oscillating $\sin$ function
cancels the contributions of positive and negative parts of the integrand. This
can be proven explicitly as follows using the fact that $h(x)$, $h'(x)$ and
$\cos(Nx)$ is bounded as $N\to\infty$:

.. math::

    \lim_{N\to\infty} \int_a^b h(x) \sin(Nx)\,\d x =

    = \lim_{N\to\infty}{1\over N} \left(\left[-h(x)\cos(Nx)\right]_a^b
    + \int_a^b h'(x) \cos(Nx)\,\d x \right) = 0

The conditions that we used are that the function $h(u)$ can be integrated,
which is satisfied if e.g. $f(x)$ has derivatives. These conditions can be
loosened in various ways.

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
        =

        = {\Omega_\mathrm{cell}N_\mathrm{cell}\over(2\pi)^3}\int_{-\infty}^{\infty}
        \tilde f(\bomega) e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega
        =

        = {N_\mathrm{cell}\over\Omega_\mathrm{BZ}}
        \sum_{\mathbf{G}}
        \int_{\Omega_\mathrm{BZ}}
        \tilde f(\mathbf{G}+\bomega)
            e^{+i(\mathbf{G}+\bomega) \cdot \mathbf{x}}\,\d^3 \omega
        =

        = {N_\mathrm{cell}\over\Omega_\mathrm{BZ}}
        \sum_{\mathbf{G}} e^{+i\mathbf{G} \cdot \mathbf{x}}
        \int_{\Omega_\mathrm{BZ}}
        \tilde f(\mathbf{G}+\bomega)
            e^{+i\bomega \cdot \mathbf{x}}\,\d^3 \omega
        =

        =
        \sum_{\mathbf{G}} \tilde f(\mathbf{G}) e^{+i\mathbf{G} \cdot \mathbf{x}}
        \int_{\Omega_\mathrm{BZ}}
        \delta(\boldsymbol\omega)
            e^{+i\boldsymbol\omega \cdot \mathbf{x}}\,d^3 \omega
        =

        =
        \sum_{\mathbf{G}} \tilde f(\mathbf{G}) e^{+i\mathbf{G} \cdot \mathbf{x}}

where we used the fact that:

.. math::

    {N_\mathrm{cell}\over\Omega_\mathrm{BZ}}\tilde f(\mathbf{G}+\boldsymbol\omega)
    =\tilde f(\mathbf{G})\delta(\boldsymbol\omega) \,.

Alternatively, if one is only interested to show that the inverse
transformation works, one can directly substitute the direct formula
:eq:`fourier2b` into :eq:`fourier2b_inv` as follows:

.. math::

    F^{-1}[\tilde f(\mathbf{G})] = \sum_{\mathbf{G}}
        \tilde f(\mathbf{G}) e^{+i\mathbf{G} \cdot \mathbf{x}} =

    = \sum_{\mathbf{G}}
        \left({1\over\Omega_\mathrm{cell}} \int_{\Omega_\mathrm{cell}}
        f(\mathbf{x'})
        e^{-i\mathbf{G} \cdot \mathbf{x'}}\,d^3 x'\right)
        e^{+i\mathbf{G} \cdot \mathbf{x}} =

    = {1\over\Omega_\mathrm{cell}} \int_{\Omega_\mathrm{cell}} f(\mathbf{x'})
        \sum_{\mathbf{G}} e^{i\mathbf{G}
         \cdot (\mathbf{x}-\mathbf{x'})}\,d^3 x' =

    = {1\over\Omega_\mathrm{cell}} \int_{\Omega_\mathrm{cell}} f(\mathbf{x'})
        (2\pi)^3
        \delta\left({(2\pi)^3\over\Omega_\mathrm{cell}}
            (\mathbf{x}-\mathbf{x'})\right) \,d^3 x' =

    = {1\over\Omega_\mathrm{cell}} \int_{\Omega_\mathrm{cell}} f(\mathbf{x'})
        (2\pi)^3 {\Omega_\mathrm{cell}\over (2\pi)^3}
        \delta(\mathbf{x}-\mathbf{x'}) \,d^3 x' =

    =f(\mathbf{x})\,,

where we used the fact that:

.. math::

    \sum_{n=-\infty}^\infty e^{inx} = 2\pi\delta(x)\,.

Thus we have shown that $F^{-1}[\tilde f(\mathbf{G})] = f(\mathbf{x})$.


One Dimension (Fourier Series)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In one dimension with a periodic function $f(x+L)=f(x)$,
the volume of a unit cell is $\Omega_\mathrm{cell}=L$
and the reciprocal space vectors $G$ are defined using
$e^{iGL}=1$ from which $G_k = {2\pi\over L} k$.
The equation :eq:`fourier2b` then becomes:

.. math::
    :label: fourier2b_1d

    F[f(x)] \equiv \tilde f(G_k) \equiv c_k
        = {1\over L} \int_{-{L\over2}}^{L\over2} f(x)
        e^{-i G_k x}\,\d x
        = {1\over L} \int_{-{L\over2}}^{L\over2} f(x)
        e^{-i(2\pi k x/L)}\,\d x

This is exactly the definition of a Fourier series ($c_k$ are the Fourier
coefficients). The inverse transform follows from :eq:`fourier2b_inv`:

.. math::
    :label: fourier2b_1d_inv

    f(x) = \sum_{k=-\infty}^\infty \tilde f(G_k) e^{i G_k x}
        = \sum_{k=-\infty}^\infty c_k e^{i(2\pi kx/L)}


Discrete Fourier Transform
--------------------------

In the discrete case, we only have a finite
number $N$ of reciprocal points:

.. math::

    k=0, 1, \dots, N/2-1, -N/2, -N/2+1, \dots, -1 \quad\mbox{if $N$ is even}

    k=0, 1, \dots, (N-1)/2, -(N-1)/2, -(N-1)/2+1, \dots, -1 \quad\mbox{if $N$ is odd}

E.g. for:

.. math::

    N=8 \quad \mbox{we get} \quad k=0, 1, 2, 3, -4, -3, -2, -1

    N=9 \quad \mbox{we get} \quad k=0, 1, 2, 3, 4, -4, -3, -2, -1

The real space function $f(x)$ is sampled at points $x_n={L\over N}n$ for
$n=-N/2,\dots,N/2-1$ and the equation :eq:`fourier2b_1d` becomes:

.. math::

    c_k
        = {1\over L} \int_{-{L\over2}}^{L\over2} f(x)
        e^{-i(2\pi k x/L)}\,\d x =

        = \lim_{N\to\infty}
        {1\over L}\sum_{n=-N/2}^{N/2-1}
        f(x_n)
        e^{-i(2\pi k x_n/L)}\,{L\over N} =

        = \lim_{N\to\infty}
        {1\over N}\sum_{n=-N/2}^{N/2-1}
        f(x_n)
        e^{-2\pi i {k\over N} n}

The equation :eq:`fourier2b_1d_inv` becomes:

.. math::

    f(x_n) = \sum_{k=-\infty}^\infty c_k e^{i(2\pi kx_n/L)} =

        = \lim_{N\to\infty}
        \sum_{k=-N/2}^{N/2-1} c_k e^{i(2\pi kx_n/L)} =

        = \lim_{N\to\infty}
        \sum_{k=-N/2}^{N/2-1} c_k e^{2\pi i {k\over N} n}

Using the fact

.. math::

    x_n + L = {L\over N}n + L = {L\over N}(n + N) = x_{n+N}\,,

we can express the periodicity $f(x_n+L)=f(x_n)$ as $f(x_{n+N})=f(x_n)$. The
sums can then be rearranged:

.. math::

    c_k
        = \lim_{N\to\infty}
        {1\over N}\sum_{n=-N/2}^{N/2-1}
        f(x_n)
        e^{-2\pi i {k\over N} n} =

        = \lim_{N\to\infty} {1\over N} \left(
        \sum_{n=-N/2}^{-1}
        f(x_n)
        e^{-2\pi i {k\over N} n}
            +
        \sum_{n=0}^{N/2-1}
        f(x_n)
        e^{-2\pi i {k\over N} n} \right) =

        = \lim_{N\to\infty} {1\over N} \left(
        \sum_{n=N/2}^{N-1}
        f(x_{n-N})
        e^{-2\pi i {k\over N} (n-N)}
            +
        \sum_{n=0}^{N/2-1}
        f(x_n)
        e^{-2\pi i {k\over N} n} \right) =

        = \lim_{N\to\infty} {1\over N}
        \sum_{n=0}^{N-1} f(x_n) e^{-2\pi i {k\over N} n}

and if we drop the limit and consider a finite $N$ only:

.. math::

    f(x_n)
        = \sum_{k=-N/2}^{N/2-1} c_k e^{2\pi i {k\over N} n} =

        = \left(
        \sum_{k=-N/2}^{-1} c_k e^{2\pi i {k\over N} n}
        +
        \sum_{k=0}^{N/2-1} c_k e^{2\pi i {k\over N} n}
        \right) =

        = \left(
        \sum_{k=N/2}^{N-1} c_{k-N} e^{2\pi i {(k-N)\over N} n}
        +
        \sum_{k=0}^{N/2-1} c_k e^{2\pi i {k\over N} n}
        \right) =

        = \sum_{k=0}^{N-1} c_k e^{2\pi i {k\over N} n}

Summary, the direct transform:

.. math::
    :label: dft

    c_k
        = {1\over N} \sum_{n=0}^{N-1} f(x_n) e^{-2\pi i {k\over N} n}

and inverse transform:

.. math::
    :label: idft

    f(x_n)
        = \sum_{k=0}^{N-1} c_k e^{2\pi i {k\over N} n}\,,

with $x_n={L\over N}n$. In the limit $N\to\infty$, the equation :eq:`dft`
becomes :eq:`fourier2b_1d` and equation :eq:`idft` becomes
:eq:`fourier2b_1d_inv` and as we increase $N$, the discrete Fourier
transform numerically converges towards the Fourier series results.

The ${1\over N}$ factor is sometimes moved from the direct to the inverse
transform, but then the correspondence with Fourier series is broken (one has
to divide and multiply by $N$ appropriately to recover it).

Fast Fourier Transform (FFT)
----------------------------

We write the discrete Fourier transform :eq:`dft` using a notation more commonly
used for FFTs:

.. math::

    X(k) = \sum_{n=0}^{N-1} x(n) W_N^{kn}

where:

.. math::

    W_N = e^{-2\pi i / N}

Similarly, the inverse discrete Fourier transform :eq:`idft` becomes:

.. math::

    x(n) = {1\over N} \sum_{k=0}^{N-1} X(k) W_N^{-kn}

Decimation In Frequency (DIF)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We start with radix-4:

.. math::

    X(k) = \sum_{n=0}^{N-1} x(n) W_N^{kn} =

    =\sum_{n=0}^{{N\over4}-1} x(n) W_N^{kn}
    +\sum_{n={N\over4}}^{{2N\over4}-1} x(n) W_N^{kn}
    +\sum_{n={2N\over4}}^{{3N\over4}-1} x(n) W_N^{kn}
    +\sum_{n={3N\over4}}^{{4N\over4}-1} x(n) W_N^{kn} =

    =\sum_{n=0}^{{N\over4}-1} \left[ x(n) W_N^{kn}
    +x\left(n+{N\over4}\right) W_N^{k\left(n+{N\over4}\right)}
    +x\left(n+{2N\over4}\right) W_N^{k\left(n+{2N\over4}\right)}
    +x\left(n+{3N\over4}\right) W_N^{k\left(n+{3N\over4}\right)}
    \right] =

    =\sum_{n=0}^{{N\over4}-1} \left[ x(n)
    +x\left(n+{N\over4}\right) W_N^{kN\over4}
    +x\left(n+{2N\over4}\right) W_N^{2kN\over4}
    +x\left(n+{3N\over4}\right) W_N^{3kN\over4}
    \right] W_N^{kn} =

    =\sum_{n=0}^{{N\over4}-1} \left[ x(n)
    +x\left(n+{N\over4}\right) (-i)^k
    +x\left(n+{2N\over4}\right) (-1)^k
    +x\left(n+{3N\over4}\right) i^k
    \right] W_N^{kn}

Now we subdivide the $X(k)$ sequence into 4 subsequences:

.. math::

    X(4k) = \sum_{n=0}^{{N\over4}-1} \left[ x(n)
    +x\left(n+{N\over4}\right) (-i)^{4k}
    +x\left(n+{2N\over4}\right) (-1)^{4k}
    +x\left(n+{3N\over4}\right) i^{4k}
    \right] W_N^{4kn} =

    = \sum_{n=0}^{{N\over4}-1} \left[ x(n)
    +x\left(n+{N\over4}\right)
    +x\left(n+{2N\over4}\right)
    +x\left(n+{3N\over4}\right)
    \right] W_{N\over4}^{kn}

Similarly:

.. math::

    X(4k+1) = \sum_{n=0}^{{N\over4}-1} \left[ x(n)
    -i x\left(n+{N\over4}\right)
    -x\left(n+{2N\over4}\right)
    +i x\left(n+{3N\over4}\right)
    \right] W_N^{n} W_{N\over4}^{kn}

    X(4k+2) = \sum_{n=0}^{{N\over4}-1} \left[ x(n)
    -x\left(n+{N\over4}\right)
    +x\left(n+{2N\over4}\right)
    -x\left(n+{3N\over4}\right)
    \right] W_N^{2n} W_{N\over4}^{kn}

    X(4k+3) = \sum_{n=0}^{{N\over4}-1} \left[ x(n)
    +i x\left(n+{N\over4}\right)
    -x\left(n+{2N\over4}\right)
    -i x\left(n+{3N\over4}\right)
    \right] W_N^{3n} W_{N\over4}^{kn}

This has a form of a DFT of length ${N\over4}$:

.. math::

    X(4k) = \sum_{n=0}^{{N\over4}-1} F_0(n) W_{N\over4}^{kn}

    X(4k+1) = \sum_{n=0}^{{N\over4}-1} F_1(n) W_{N\over4}^{kn}

    X(4k+2) = \sum_{n=0}^{{N\over4}-1} F_2(n) W_{N\over4}^{kn}

    X(4k+3) = \sum_{n=0}^{{N\over4}-1} F_3(n) W_{N\over4}^{kn}

where

.. math::

    \begin{pmatrix}
    F_0(n) \\
    F_1(n) \\
    F_2(n) \\
    F_3(n) \\
    \end{pmatrix} =
    \begin{pmatrix}
    x(n)
    +x\left(n+{N\over4}\right)
    +x\left(n+{2N\over4}\right)
    +x\left(n+{3N\over4}\right) \\
    x(n)
    -i x\left(n+{N\over4}\right)
    -x\left(n+{2N\over4}\right)
    +i x\left(n+{3N\over4}\right) \\
    x(n)
    -x\left(n+{N\over4}\right)
    +x\left(n+{2N\over4}\right)
    -x\left(n+{3N\over4}\right) \\
    x(n)
    +i x\left(n+{N\over4}\right)
    -x\left(n+{2N\over4}\right)
    -i x\left(n+{3N\over4}\right)
    \end{pmatrix} =

    =\begin{pmatrix}
    1 &  1 &  1 &  1 \\
    1 & -i & -1 &  i \\
    1 & -1 &  1 & -1 \\
    1 &  i & -1 & -i
    \end{pmatrix}
    \begin{pmatrix}
    x(n) \\
    x\left(n+{N\over4}\right) \\
    x\left(n+{2N\over4}\right) \\
    x\left(n+{3N\over4}\right)
    \end{pmatrix}

This coefficient matrix for various radix-n schemes can be generated by::

    >>> from sympy import exp, I, pi, pprint, Matrix
    >>> n = 2
    >>> Matrix(n, n, lambda i, j: exp(-2*pi*I*i*j/n))
    [1  1]
    [1 -1]
    >>> n = 3
    >>> Matrix(n, n, lambda i, j: exp(-2*pi*I*(i*j % n)/n))
    [1,              1,              1]
    [1, exp(-2*I*pi/3), exp(-4*I*pi/3)]
    [1, exp(-4*I*pi/3), exp(-2*I*pi/3)]
    >>> n = 4
    >>> Matrix(n, n, lambda i, j: exp(-2*pi*I*i*j/n))
    [1  1  1  1]
    [1 -I -1  I]
    [1 -1  1 -1]
    [1  I -1 -I]
    >>> n = 5
    >>> Matrix(n, n, lambda i, j: exp(-2*pi*I*(i*j % n)/n))
    [1,              1,              1,              1,              1]
    [1, exp(-2*I*pi/5), exp(-4*I*pi/5), exp(-6*I*pi/5), exp(-8*I*pi/5)]
    [1, exp(-4*I*pi/5), exp(-8*I*pi/5), exp(-2*I*pi/5), exp(-6*I*pi/5)]
    [1, exp(-6*I*pi/5), exp(-2*I*pi/5), exp(-8*I*pi/5), exp(-4*I*pi/5)]
    [1, exp(-8*I*pi/5), exp(-6*I*pi/5), exp(-4*I*pi/5), exp(-2*I*pi/5)]
    >>> n = 8
    >>> Matrix(n, n, lambda i, j: exp(-2*pi*I*(i*j % n)/n))
    [1,              1,  1,              1,  1,              1,  1,              1]
    [1,   exp(-I*pi/4), -I, exp(-3*I*pi/4), -1, exp(-5*I*pi/4),  I, exp(-7*I*pi/4)]
    [1,             -I, -1,              I,  1,             -I, -1,              I]
    [1, exp(-3*I*pi/4),  I,   exp(-I*pi/4), -1, exp(-7*I*pi/4), -I, exp(-5*I*pi/4)]
    [1,             -1,  1,             -1,  1,             -1,  1,             -1]
    [1, exp(-5*I*pi/4), -I, exp(-7*I*pi/4), -1,   exp(-I*pi/4),  I, exp(-3*I*pi/4)]
    [1,              I, -1,             -I,  1,              I, -1,             -I]
    [1, exp(-7*I*pi/4),  I, exp(-5*I*pi/4), -1, exp(-3*I*pi/4), -I,   exp(-I*pi/4)]


One then recursively solves the smaller problems. This approach is used for
example in FFTPACK. There are also other approaches how to decompose the DFT,
used in various other libraries.


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
