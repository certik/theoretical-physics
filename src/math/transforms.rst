Fourier Transform
-----------------

The Fourier transform is:

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
