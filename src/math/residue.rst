.. index:: residue theorem, contour integration

Residue Theorem
===============

The Residue Theorem says that a contour integral of an analytic function $f$
over a closed curve $\gamma$ (loop) is equal to the sum of residues
$\res_{z_k}f(z)$ of the function at all singularities $z_k$ inside the loop:

.. math::

    \int_\gamma f(z) \d z = 2\pi i \sum_{z_k} \res_{z=z_k} f(z)

Residue $\res_{z_0}f(z)$ is defined as the contour integral around $z_0$
divided by $2\pi i$:

.. math::

    \res_{z=z_0} f(z) = {1\over 2\pi i}\int_{|z - z_0| = \epsilon} f(z) \d z

and it is equal to the coefficient of $1\over z-z_0$ in the
Laurent series of $f(z)$ around the point $z_0$, as can be easily calculated:

.. math::

    \res_{z=z_0} f(z) = {1\over 2\pi i}\int\limits_{|z - z_0| = \epsilon} f(z) \d z
    = {1\over 2\pi i}\int\limits_{|z - z_0| = \epsilon} \sum_{n=-\infty}^\infty c_n
    (z-z_0)^n \d z
    =

    = \sum_{n=-\infty}^\infty c_n {1\over 2\pi i}\int\limits_{|z - z_0| = \epsilon}
    (z-z_0)^n \d z
    = \sum_{n=-\infty}^\infty c_n \delta_{n, -1} = c_{-1}

where we used the result of the following integral (we integrate over the curve
$z = z_0 + \epsilon e^{i\varphi}$, $0\le\varphi<2\pi$, so $\d z = i\epsilon
e^{i\varphi}\d\varphi$):

.. math::

    {1\over 2\pi i}\int\limits_{|z - z_0| = \epsilon} (z-z_0)^n \d z
    =
    {1\over 2\pi i}\int\limits_0^{2\pi} (z_0+\epsilon e^{i\varphi}-z_0)^n
    i\epsilon e^{i\varphi}\d\varphi
    =
    {\epsilon^{n+1}\over 2\pi}\int\limits_0^{2\pi} e^{i\varphi (n + 1)}
    \d\varphi
    =

    =\begin{cases}{
    \epsilon^{n+1}\over 2\pi} \left[ {e^{i\varphi (n + 1)}\over i(n+1)}
    \right]_0^{2\pi}=0\quad\text{for $n\neq-1$}\cr
    {1\over 2\pi}\int\limits_0^{2\pi} \d\varphi=1\quad\text{for $n=-1$}\cr
    \end{cases}
    =\delta_{n, -1}

.. index::
    pair: residue; computation

Computation of Residues
-----------------------

One has to calculate the $c_{-1}$ coefficient in the Laurent series. One way to
do that is to write $f(z)$ as:

.. math::

    f(z) = {H(z)\over (z-z_0)^m}

where $H(z)$ is analytic in the vicinity of $z_0$, e.g. $f(z)$ has a pole of
order $m$ at $z_0$. Then:

.. math::

    \res_{z=z_0} f(z) = c_{-1} = {1\over(m-1)!}
    \left.{\d^m H(z)\over\d z^m}\right|_{z = z_0}

in particular for $m=1$:

.. math::

    \res_{z=z_0} f(z) = H(z_0) = \lim_{z\to z_0}(z-z_0) f(z)

for $m=2$:

.. math::

    \res_{z=z_0} f(z) = H'(z_0) = \lim_{z\to z_0}{\d\over\d z}[(z-z_0)^2 f(z)]

$f$ has a pole of order 1 at $z_0$, $g$ is analytic at $z_0$:

.. math::

    \res_{z=z_0} f(z)g(z) = \lim_{z\to z_0}(z-z_0) f(z)g(z)
    = g(z_0)\lim_{z\to z_0}(z-z_0) f(z) = g(z_0)\res_{z=z_0}f(z)

$f(z_0) = 0$, but $f'(z_0) \neq 0$ and $g$ is analytic at $z_0$:

.. math::

    \res_{z=z_0} {g(z)\over f(z)} = g(z_0)\lim_{z\to z_0}{z-z_0\over f(z)}
    = g(z_0)\lim_{z\to z_0}{z-z_0\over f(z)-f(z_0)}
    = {g(z_0)\over f'(z_0)}

Useful Formulas
---------------

.. index:: Jordan's Lemma

Jordan's Lemma
~~~~~~~~~~~~~~

For estimating integrals over semicircles $\Omega$ ($z = Re^{i\varphi}$,
$0\le\varphi\le\pi$), we can use the following estimates:

.. math::

    \left|\int_\Omega g(z) \d z \right| \le \pi R \max_\Omega |g(z)|

    \left|\int_\Omega e^{i\alpha z}g(z) \d z \right| \le {\pi\over\alpha}
    \max_\Omega |g(z)|\quad\text{for $\alpha>0$}

(In the first case the integration path can be extended to the full circle if
needed ($0\le\varphi\le2\pi$), in the second case the semicircle is the maximum
path. Also if $\alpha<0$, we need to integrate over the lower semicircle.)
These formulas can be used to make sure the integral over the semicircle goes to
zero as $R\to\infty$. Intuitively speaking, in the first case $g(z)$ must
vanish faster than $1\over R$ (e.g. $1\over R^2$ is ok), in the second case
it's enough if $g(z)$ just goes to 0 (no matter how fast).

The estimates can be proved easily:

.. math::

    \left|\int_\Omega g(z) \d z \right|
    = \left|\int_0^\pi g(Re^{i\varphi})iRe^{i\varphi} \d\varphi \right|
    \le \int_0^\pi \left|g(Re^{i\varphi})\right|R \d\varphi
    \le R\max_\Omega |g(z)| \int_0^\pi \d\varphi
    = \pi R \max_\Omega |g(z)|

and

.. math::

    \left|\int_\Omega e^{i\alpha z}g(z) \d z \right|
    =\left|\int_0^\pi e^{i\alpha
    Re^{i\varphi}}g(Re^{i\varphi})iRe^{i\varphi}\right|
    \le

    \le\int_0^\pi e^{-\alpha R\sin\varphi}\left|g(Re^{i\varphi})\right| R \d\varphi
    \le R \max_\Omega |g(z)| \int_0^\pi e^{-\alpha R\sin\varphi}\d\varphi
    <

    < R \max_\Omega |g(z)| 2\int_0^{\pi\over2} e^{-\alpha R{2\over\pi}\varphi}\d\varphi
    = {\pi\over\alpha} \max_\Omega |g(z)|(1-e^{-\alpha R})
    =

    < {\pi\over\alpha} \max_\Omega |g(z)|

Other
~~~~~

Sometimes it is useful to integrate over the arc $z = z_0 + \epsilon
e^{i\varphi}$, $\varphi_0 \le \varphi \le \varphi_0 + \alpha$, and let
$\epsilon\to0$ at the end. If the function is analytic, the result is $0$. If the
function has a pole of order $n > 1$, the result is infinity, unless it's a full
circle (in which case the result is 0). The remaining case is if the function
has a pole of order one, e.g. it can be written ($H(z)$ is analytic at $z_0$):

.. math::

    f(z) = {H(z)\over z - z_0}

Then:

.. math::

    \int_\Omega f(z) \d z =
    \int_\Omega {H(z)\over z - z_0} \d z = \int_{\varphi_0}^{\varphi_0+\alpha}{H(z_0 +
    \epsilon e^{i\varphi})\over z_0 + \epsilon e^{i\varphi} - z_0}\epsilon i
    e^{i\varphi} \d \varphi
    =

    =\int_{\varphi_0}^{\varphi_0+\alpha}H(z_0 + \epsilon e^{i\varphi}) i \d \varphi
    \to\int_{\varphi_0}^{\varphi_0+\alpha}H(z_0) i \d \varphi = i\alpha H(z_0)
    = i\alpha \res_{z = z_0}f(z)
