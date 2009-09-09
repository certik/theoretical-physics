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
$z = z_0 + \epsilon e^{i\varphi}$, $\varphi\in[0, 2\pi)$, so $\d z = i\epsilon
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
