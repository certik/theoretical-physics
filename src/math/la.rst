Linear Algebra
==============

Scalar Product
--------------

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
~~~~~~~~

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
