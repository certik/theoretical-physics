Linear Algebra
==============

Scalar Product
==============

Virtually all spaces used in physics are Hilbert spaces (treated in the weak
sense, i.e. equipped with distributions), which means that they have a scalar
product and a norm.

The braket $\braket{f|g}$ in Dirac notation is a scalar product and we are
free to define it anyway we like, as long as it satisfies the following
properties:

.. math::

    \braket{f|g} = \braket{g|f}^*

    \braket{f|ag} = a\braket{f|g}

    \braket{f_1 + f_2|g} = \braket{f_1|g} + \braket{f_2|g}

    \braket{f|f} \ge 0

where $\braket{f|f}=0$ if, and only if, $\ket{f}=0$. Scalar product induces the
norm:

.. math::

    ||\ket{f}|| = \sqrt{\braket{f|f}}

Any norm has to satisfy the following properties:

.. math::

    ||a\ket{f}|| = |a| ||\ket{f}||

    ||\ket{f}+\ket{g}|| \le ||\ket{f}|| + ||\ket{g}||

    ||\ket{f}|| \ge 0

where $||\ket{f}||=0$ if, and only if, $\ket{f}=0$. Those properties are
automatically satisfied by the induced norm.

In general, any of these properties can be weakened, one can study spaces that
have a norm, but not a scalar product, or spaces, that have objects resembling
a norm (or a scalar product), that only satisfy some of the properties of the
norm (or a scalar product). Those are not very important in physics. On the
other hand, it is very important to understand how to work with Hilbert spaces
(in the weak sense). Dirac notation makes it very easy to understand and
remember how to work with such spaces.

Examples
--------

Some examples of frequently used spaces and scalar products follows.

Finite dimensional spaces:

.. math::

    \ket{f} = \left(\begin{array}{c}
        f_1 \\
        f_2 \\
        \vdots \\
        f_n \\
        \end{array}\right)

    \bra{f} =
    \left(\begin{array}{cccc}
        f_1 & f_2 & \cdots & f_n \\
        \end{array}\right)

$R^n$ scalar product:

.. math::

    \braket{f|g} =
    \left(\begin{array}{cccc}
        f_1 & f_2 & \cdots & f_n \\
        \end{array}\right)
    \left(\begin{array}{c}
        g_1 \\
        g_2 \\
        \vdots \\
        g_n \\
        \end{array}\right)
        = f_1 g_2 + f_2 g_2 + \cdots + f_n g_n

Infinite dimensional spaces:

.. math::

    \ket{f} = \left(\begin{array}{c}
        f_1 \\
        f_2 \\
        \vdots \\
        \end{array}\right)

    \bra{f} =
    \left(\begin{array}{ccc}
        f_1 & f_2 & \cdots \\
        \end{array}\right)

$l^2$ scalar product:

.. math::

    \braket{f|g} =
    \left(\begin{array}{ccc}
        f_1 & f_2 & \cdots \\
        \end{array}\right)
    \left(\begin{array}{c}
        g_1 \\
        g_2 \\
        \vdots \\
        \end{array}\right)
        = f_1 g_2 + f_2 g_2 + \cdots

Function spaces:

.. math::

    \ket{f} = f(x)

    \bra{f} = f^*(x)

$L^2$ scalar product:

.. math::

    \braket{f|g} = \int_\Omega f^*(x) g(x) \d x

$H^1$ scalar product:

.. math::

    \braket{f|g} = \int_\Omega f^*(x) g(x) + f'^*(x) g'(x) \d x

$H^2$ scalar product:

.. math::

    \braket{f|g} = \int_\Omega f^*(x) g(x) + f'^*(x) g'(x)
        + f''^*(x) g''(x) \d x

Energy scalar product:

.. math::

    \braket{f|g} = \int_\Omega f^*(x) q(x) g(x) + f'^*(x) p(x) g'(x) \d x

All of these scalar products automatically satisfy all of the properties of the
scalar product, only the energy scalar product doesn't automatically satisfy
$\braket{f|f} \ge 0$, which imposes some conditions on the parameters $p(x)$
and $q(x)$.

Projections
===========

Projection is a linear idempotent operator $P$:

.. math::

    P^2 = P

It takes a vector $\ket{u}$ from $V$ and projects it onto a vector $\ket{w} =
P\ket{u}$ from $W$. Further application of the operator $P$ gains nothing:
$P\ket{w} = P^2\ket{u} = P\ket{u} = \ket{w}$.
It decomposes the space $V$ into a direct sum $V=W\oplus W^\bot$ of
the projection subspace $W$ and its complement $W^\bot$. If $\ket{w}$ is
from $W$ then its complement $\ket{u} - P\ket{u}$ is from $W^\bot$. Given the
space $W$, the operator $P$ is unique.

Orthogonal projection is a projection that is Hermitean:

.. math::

    P^\dag = P

The complement of an orthogonal projection is orthogonal to any vector from $W$:

.. math::

    \braket{u-Pu|w} = \braket{u|w} - \braket{Pu|w} =
        \braket{u|w} - \braket{u|P^\dag|w} =

        =
        \braket{u|w} - \braket{u|P|w} =
        \braket{u|w} - \braket{u|w} = 0



In other words, orthogonal projection projects a vector
$\ket{u}$ from the space $V$ into an orthogonal subspace (projection subspace)
$W$.

If we choose any orthonormal basis $\ket{w_0}$, $\ket{w_1}$,
$\ket{w_2}$, ..., of the subspace $W$, then the orthogonal projection $P$ is:

.. math::

    P = \sum_{k=0}^\infty \ket{w_k}\bra{w_k}

because:


.. math::

    P^2 =
    \sum_{k=0}^\infty \ket{w_k}\bra{w_k}
    \sum_{l=0}^\infty \ket{w_l}\bra{w_l}
    =
    \sum_{k,l=0}^\infty \ket{w_k}\braket{w_k|w_l}\bra{w_l}=

    =\sum_{k,l=0}^\infty \ket{w_k}\delta_{kl}\bra{w_l}
    = \sum_{k=0}^\infty \ket{w_k}\bra{w_k} = P

and

.. math::

    P^\dag = \left(\sum_{k=0}^\infty \ket{w_k}\bra{w_k}\right)^\dag =
    \sum_{k=0}^\infty \left(\ket{w_k}\bra{w_k}\right)^\dag =
    \sum_{k=0}^\infty \ket{w_k}\bra{w_k} = P

$P$ is independent of the basis, i.e $\sum_{k=0}^\infty \ket{w_k}\bra{w_k}
=\sum_{l=0}^\infty \ket{u_l}\bra{u_l}$, as long as $\ket{u_l}$ span the same
subspace as $\ket{w_k}$, because the operator $P$ is unique.


To find the closest vector $\ket{w}$ from $W$ to the vector $\ket{u}$ from $V$,
we need to minimize the norm $||\ket{u}-\ket{w}||$. So we write
$\ket{w} = P\ket{u} + \ket{z}$ for some vector $\ket{z}$ from $W$ and simplify
the norm:

.. math::

    ||\ket{u}-\ket{w}||^2 = \braket{u-w|u-w} =
    \braket{u-Pu-z|u-Pu-z} =

    =
    \braket{u-Pu|u-Pu} + \braket{z|z} - \braket{u-Pu|z}-\braket{z|u-Pu}=

    =
    \braket{u-Pu|u-Pu} + \braket{z|z}

which is minimal for $\ket{z}=0$, so we found out that the closest vector is
$\ket{w} = P\ket{u}$. We used the fact that $\braket{u-Pu|z}=0$, because
$\ket{u-Pu}$ is from the orthogonal complement to the subspace $W$.
In other words, orthogonal projection finds the closest vector from a subspace
onto which it projects.

Nonorthogonal basis
-------------------

In order to project using a nonorthogonal basis $\ket{v_k}$ (for example a
finite element basis), we write:

.. math::

    P\ket{u} = \sum_{k=0}^\infty \ket{v_k}\phi_k

where $\phi_k$ are the projection coefficients that we'd like to calculate.
This holds, because $P\ket{u}$ belongs to the space $W$ and every vector from it
can be expressed as a linear combination of $\ket{v_k}$. Now we multiply by
$\bra{v_l}$ from the left and simplify:

.. math::

    \braket{v_l|P|u} = \sum_{k=0}^\infty \braket{v_l|v_k}\phi_k

    \braket{v_l|u} = \sum_{k=0}^\infty \braket{v_l|v_k}\phi_k

so we need to solve the linear system:

.. math::

    A_{lk}\phi_k = f_l

with:

.. math::

    A_{lk} = \braket{v_l|v_k}

    f_l = \braket{v_l|u}

This works for any basis, it doesn't have to be normalized nor orthogonal.

Examples
--------

$R^n$ projection. Orthogonal basis:

.. math::

    \ket{w_0} =
    \left(\begin{array}{c}
        1 \\
        0 \\
        0 \\
        \end{array}\right)

    \ket{w_1} =
    \left(\begin{array}{c}
        0 \\
        1 \\
        0 \\
        \end{array}\right)

    P = \ket{w_0}\bra{w_0} + \ket{w_1}\bra{w_1} =
    \left(\begin{array}{ccc}
        1 & 0 & 0 \\
        0 & 0 & 0\\
        0 & 0 & 0\\
        \end{array}\right)
    +
    \left(\begin{array}{ccc}
        0 & 0 & 0 \\
        0 & 1 & 0\\
        0 & 0 & 0\\
        \end{array}\right)
    =
    \left(\begin{array}{ccc}
        1 & 0 & 0 \\
        0 & 1 & 0\\
        0 & 0 & 0\\
        \end{array}\right)

Different basis orthogonal basis:

.. math::

    \ket{w_0} = {1\over\sqrt 2}
    \left(\begin{array}{c}
        1 \\
        1 \\
        0 \\
        \end{array}\right)

    \ket{w_1} = {1\over\sqrt 2}
    \left(\begin{array}{c}
        1 \\
        -1 \\
        0 \\
        \end{array}\right)

    P = \ket{w_0}\bra{w_0} + \ket{w_1}\bra{w_1} =
    {1\over 2}
    \left(\begin{array}{ccc}
        1 & 1 & 0 \\
        1 & 1 & 0\\
        0 & 0 & 0\\
        \end{array}\right)
    +
    {1\over 2}
    \left(\begin{array}{ccc}
        1 & -1 & 0 \\
        -1 & 1 & 0\\
        0 & 0 & 0\\
        \end{array}\right)
    =
    \left(\begin{array}{ccc}
        1 & 0 & 0 \\
        0 & 1 & 0\\
        0 & 0 & 0\\
        \end{array}\right)

Lagrange interpolation projection onto the space $\{1, x\}$:

.. math::

    \ket{u} = f(x)

    P\ket{u} = {f(1)+f(-1)\over 2} + x{f(1)-f(-1)\over 2}

$L^2$ projection onto the space $\{1, x\}$. Orthogonal basis:

.. math::

    \ket{u} = f(x)

    \ket{w_0} = {1\over\sqrt2}

    \ket{w_1} = \sqrt{3\over2}x

    P\ket{u} = \ket{w_0}\braket{w_0|u} + \ket{w_1}\braket{w_1|u} =

        = {1\over\sqrt2} \int_{-1}^1 {1\over\sqrt2} f(x) \d x
            + \sqrt{3\over2}x \int_{-1}^1 \sqrt{3\over2}x f(x) \d x
        = {1\over2}\int_{-1}^1 f(x) \d x + {3\over2}x \int_{-1}^1 x f(x) \d x

Different orthogonal basis:

.. math::

    \ket{w_0} = {\sqrt6\over4}(1+x)

    \ket{w_1} = {\sqrt2\over4}(1-3x)

    P\ket{u} = \ket{w_0}\braket{w_0|u} + \ket{w_1}\braket{w_1|u} =

        = {\sqrt6\over4}(1+x) \int_{-1}^1 {\sqrt6\over4}(1+x) f(x) \d x
        + {\sqrt2\over4}(1-3x) \int_{-1}^1 {\sqrt2\over4}(1-3x) f(x) \d x
        = {1\over2}\int_{-1}^1 f(x) \d x + {3\over2}x \int_{-1}^1 x f(x) \d x

Nonorthogonal basis:

.. math::

    \ket{w_0} = 1

    \ket{w_1} = 1 + x

    A_{lk}\phi_k = f_l

    A_{lk} = \left(\begin{array}{cc}
        A_{00} & A_{01} \\
        A_{10} & A_{11} \\
    \end{array}\right)=
    \left(\begin{array}{cc}
        \braket{w_0|w_0} & \braket{w_0|w_1} \\
        \braket{w_1|w_0} & \braket{w_1|w_1} \\
    \end{array}\right)=

    =
    \left(\begin{array}{cc}
        \int_{-1}^1 \d x & \int_{-1}^1 1+x \,\d x \\
        \int_{-1}^1 1+x\,\d x & \int_{-1}^1 (1+x)^2 \,\d x \\
    \end{array}\right)
    =\left(\begin{array}{cc}
        2 & 2 \\
        2 & {8\over3} \\
    \end{array}\right)

    A_{kl}^{-1} =
    \left(\begin{array}{cc}
        2 & -{3\over2} \\
        -{3\over2} & {3\over2} \\
    \end{array}\right)

    f_{l} = \left(\begin{array}{c}
        f_0 \\
        f_1 \\
    \end{array}\right)=
    \left(\begin{array}{c}
        \braket{w_0|u} \\
        \braket{w_1|u} \\
    \end{array}\right)=
    \left(\begin{array}{c}
        \int_{-1}^1 f(x)\, \d x \\
        \int_{-1}^1 (1+x)f(x)\,\d x \\
    \end{array}\right)

    \phi_k =
    \left(\begin{array}{c}
        \phi_0 \\
        \phi_1 \\
    \end{array}\right)=
    A_{kl}^{-1} f_l =
    \left(\begin{array}{cc}
        2 & -{3\over2} \\
        -{3\over2} & {3\over2} \\
    \end{array}\right)
    \left(\begin{array}{c}
        \int_{-1}^1 f(x)\, \d x \\
        \int_{-1}^1 (1+x)f(x)\,\d x \\
    \end{array}\right)=

    =
    \left(\begin{array}{c}
        2\int_{-1}^1 f(x) - {3\over2}(1+x)f(x)\d x \\
        -{3\over2}\int_{-1}^1 f(x) + {3\over2}(1+x)f(x)\d x \\
    \end{array}\right)=

    P\ket{u} = \ket{w_0}\phi_0 + \ket{w_1}\phi_1 =

        = 1 \left(2\int_{-1}^1 f(x) - {3\over2}(1+x)f(x)\d x\right)
        + (1+x)\left(-{3\over2}\int_{-1}^1 f(x) + {3\over2}(1+x)f(x)\d x\right)
        =

        = {1\over2}\int_{-1}^1 f(x) \d x + {3\over2}x \int_{-1}^1 x f(x) \d x

$H^1$ projection. Nonorthogonal basis:

.. math::

    \ket{w_0} = 1

    \ket{w_1} = 1 + x

    A_{lk}\phi_k = f_l

    A_{lk} = \left(\begin{array}{cc}
        A_{00} & A_{01} \\
        A_{10} & A_{11} \\
    \end{array}\right)=
    \left(\begin{array}{cc}
        \braket{w_0|w_0} & \braket{w_0|w_1} \\
        \braket{w_1|w_0} & \braket{w_1|w_1} \\
    \end{array}\right)=

    =
    \left(\begin{array}{cc}
        \int_{-1}^1 \d x & \int_{-1}^1 1+x \,\d x \\
        \int_{-1}^1 1+x\,\d x & \int_{-1}^1 (1+x)^2 + 1 \,\d x \\
    \end{array}\right)
    =\left(\begin{array}{cc}
        2 & 2 \\
        2 & {14\over3} \\
    \end{array}\right)

    A_{kl}^{-1} =
    \left(\begin{array}{cc}
        {7\over8} & -{3\over8} \\
        -{3\over8} & {3\over8} \\
    \end{array}\right)

    f_{l} = \left(\begin{array}{c}
        f_0 \\
        f_1 \\
    \end{array}\right)=
    \left(\begin{array}{c}
        \braket{w_0|u} \\
        \braket{w_1|u} \\
    \end{array}\right)=
    \left(\begin{array}{c}
        \int_{-1}^1 f(x)\, \d x \\
        \int_{-1}^1 (1+x)f(x) + f'(x)\,\d x \\
    \end{array}\right)

    \phi_k =
    \left(\begin{array}{c}
        \phi_0 \\
        \phi_1 \\
    \end{array}\right)=
    A_{kl}^{-1} f_l =
    \left(\begin{array}{cc}
        {7\over8} & -{3\over8} \\
        -{3\over8} & {3\over8} \\
    \end{array}\right)
    \left(\begin{array}{c}
        \int_{-1}^1 f(x)\, \d x \\
        \int_{-1}^1 (1+x)f(x) +f'(x)\,\d x \\
    \end{array}\right)=

    =
    \left(\begin{array}{c}
        \int_{-1}^1  {7\over8}f(x) - {3\over8}(1+x)f(x)- {3\over8}f'(x)\d x \\
        \int_{-1}^1 -{3\over8}f(x) + {3\over8}(1+x)f(x)+ {3\over8}f'(x)\d x \\
    \end{array}\right)=

    P\ket{u} = \ket{w_0}\phi_0 + \ket{w_1}\phi_1 =

        = 1 \left(\int_{-1}^1 {7\over8}f(x) - {3\over8}(1+x)f(x)- {3\over8}f'(x)\d x\right)
        + (1+x)\left(\int_{-1}^1 -{3\over8}f(x) + {3\over8}(1+x)f(x)+ {3\over8}f'(x)\d x\right)
        =

        = \int_{-1}^1 {1\over2}f(x)-{3\over8}f'(x) \d x
        + x \int_{-1}^1 {3\over8}x f(x)+{3\over8}f'(x) \d x=

        = \int_{-1}^1 {1\over2}f(x) \d x + x \int_{-1}^1 {3\over8}x f(x) \d x
            -{3\over8}(f(1)-f(-1)) + {3\over8}x(f(1)-f(-1))=

        = {1\over2}\int_{-1}^1 f(x) \d x + {3\over8}x \int_{-1}^1 x f(x) \d x
            +{3\over8}(-1+x)(f(1)-f(-1))
