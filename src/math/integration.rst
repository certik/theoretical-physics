.. index:: integration, surface integrals, volume integrals

Integration
===========

This chapter doesn't assume any knowledge about differential geometry. The most
versatile way to do integration over manifolds is explained in the differential
geometry section.

General Case
------------

We want to integrate a function $f$ over a $k$-manifold in $\R^n$, parametrized
as:

.. math::

    \mathbf{\varphi}: \R^k \to \R^n\quad \mathbf{\varphi}(t_1, t_2, \dots, t_k) =
    \mat{\varphi_1(t_1, t_2, \dots, t_k)\cr
        \varphi_2(t_1, t_2, \dots, t_k)\cr
        \vdots \cr
        \varphi_n(t_1, t_2, \dots, t_k)\cr
    }

then the integral of $f(x_1, x_2, \dots, x_n)$ over $\varphi$ is:

.. math::

    \int_M f(x_1, x_2, \dots, x_n)\,\d S = \int_{\R^n} f(\mathbf{\varphi}(t_1,
    t_2, \dots, t_k))\sqrt{\det{\bf G}}\,\d t_1\d t_2\cdots\d t_k

where ${\bf G}$ is called a Gram matrix and ${\bf J}$ is a Jacobian:

.. math::

    ({\bf G})_{ij} = ({\bf J}^T{\bf J})_{ij} = J_{ik}J_{kj} =
    {\partial\varphi_k\over\partial t_i} {\partial\varphi_k\over\partial t_j}

    ({\bf J})_{ij} = {\partial\varphi_i\over\partial t_j} = \mat{
        {\partial\mathbf{\varphi}\over\partial t_1} &
        {\partial\mathbf{\varphi}\over\partial t_2} &
        \cdots &
        {\partial\mathbf{\varphi}\over\partial t_k} \cr
        \vdots & \vdots & \vdots & \vdots \cr
        \vdots & \vdots & \vdots & \vdots \cr
        \vdots & \vdots & \vdots & \vdots \cr
    }

The idea behind this comes from the fact that the volume of the $k$-dimensional
parallelepiped spanned by the vectors

.. math::

    {\partial\mathbf{\varphi}\over\partial t_1}, \dots, {\partial\mathbf{\varphi}\over\partial t_k}

is given by

.. math::

    V = \sqrt{\det {\bf J}^T{\bf J}}

where ${\bf J}$ is an $n\times k$ matrix having those vectors as its column
vectors.

Example
~~~~~~~

Let's integrate a function $f(x, y, z)$ over the surface of a sphere in 3D
(e.g. $k=2$ and $n=3$):

.. math::

    \mathbf{\varphi}(\theta, \phi) = \mat{
        r\sin\theta\cos\phi \cr
        r\sin\theta\sin\phi \cr
        r\cos\theta \cr
    }

    {\bf J} = \mat{
        -r\sin\theta\sin\phi & r\cos\theta\cos\phi \cr
        r\sin\theta\cos\phi & r\cos\theta\sin\phi \cr
        0 & -r\sin\theta \cr
    }

    {\bf G} = {\bf J}^T {\bf J} =
    \mat{
        -r\sin\theta\sin\phi & r\sin\theta\cos\phi & 0 \cr
        r\cos\theta\cos\phi & r\cos\theta\sin\phi & -r\sin\theta \cr
    }
    \mat{
        -r\sin\theta\sin\phi & r\cos\theta\cos\phi \cr
        r\sin\theta\cos\phi & r\cos\theta\sin\phi \cr
        0 & -r\sin\theta \cr
    }
    = \mat {
        r^2\sin^2\theta & 0 \cr
        0 & r^2 \cr
    }

    \det{\bf G} = r^4\sin^2\theta

    \sqrt{\det{\bf G}} = r^2\sin\theta

    \int_M f(x, y, z) \d S = \int_{\R^n} f(r\sin\theta\cos\phi,
    r\sin\theta\sin\phi, r\cos\theta)\, r^2\sin\theta\,\d\theta\,\d\phi
    =

    = \int_0^\pi\d\theta \int_0^{2\pi}\d\phi\, f(r\sin\theta\cos\phi,
    r\sin\theta\sin\phi, r\cos\theta)\, r^2\sin\theta

Let's say we want to calculate the surface area of a sphere, so we set $f(x, y,
z) = 1$ and get:

.. math::

    \int_M \d S
    = \int_0^\pi\d\theta \int_0^{2\pi}\d\phi\, r^2\sin\theta
    = 2\pi r^2\int_0^\pi\d\theta \sin\theta
    = 4\pi r^2

Special Cases
-------------

.. index::
    pair: volume; integration

k = n
~~~~~

.. math::

    \det{\bf G} = \det {\bf J}^R{\bf J} = (\det {\bf J})^2

    \d S = |\det {\bf J}|\,\d t_1\,\d t_2\cdots\d t_k

.. index::
    pair: line; integration

k = 1
~~~~~

.. math::

    \det{\bf G} = \det \left(
        \left({\d\varphi_1\over\d t}\right)^2+
        \left({\d\varphi_2\over\d t}\right)^2+
        \cdots
        \right)
    = \left|{\d\mathbf{\varphi}\over\d t}\right|^2

    \d S = \left|{\d\mathbf{\varphi}\over\d t}\right|\,\d t

.. index::
    pair: surface; integration

k = n - 1
~~~~~~~~~

.. math::

    \det{\bf G} = \det {\bf J}^R{\bf J} =

    =\det(\cdots)^2 + \det(\cdots)^2+\cdots+\det(\dots)^2 =

    =\left|\det\mat{
        {\partial\mathbf{\varphi}\over\partial t_1} &
        {\partial\mathbf{\varphi}\over\partial t_2} &
        \cdots &
        {\partial\mathbf{\varphi}\over\partial t_k} &
        {\bf e}_1 \cr
        \vdots & \vdots & \vdots & \vdots & {\bf e}_2 \cr
        \vdots & \vdots & \vdots & \vdots & \vdots \cr
        \vdots & \vdots & \vdots & \vdots & {\bf e}_n \cr
    }\right|^2 \equiv |\omega_\varphi|^2

    \d S = |\omega_\varphi|\,\d t_1\,\d t_2\cdots\d t_k

$\omega_\varphi$ is a generalization of a vector cross product. The
$\det(\cdots)$ symbol means a determinant of a matrix with one row removed
(first term in the sum has first row removed, second term has second row
removed, etc.).

.. index::
    pair: surface; integration

k = 2, n = 3
~~~~~~~~~~~~

.. math::

    \det{\bf G} = \left|{\partial\mathbf{\varphi}\over\partial t_1}\times
    {\partial\mathbf{\varphi}\over\partial t_2}\right|^2

    \d S = \left|{\partial\mathbf{\varphi}\over\partial t_1}\times
    {\partial\mathbf{\varphi}\over\partial t_2}\right|\,\d t_1\,\d t_2


y = f(x, z)
~~~~~~~~~~~

.. math::

    \det{\bf G} = 1
    +\left({\partial f\over\partial x}\right)^2
    +\left({\partial f\over\partial z}\right)^2

    \d S = \sqrt{1
    +\left({\partial f\over\partial x}\right)^2
    +\left({\partial f\over\partial z}\right)^2
    }\,\d x\,\d z

in general for $x_j = f(x_1, x_2, \dots, x_n)$ we get:

.. math::

    \det{\bf G} = 1
    +\left({\partial f\over\partial x_1}\right)^2
    +\left({\partial f\over\partial x_2}\right)^2
    +\cdots

    \d S = \sqrt{1
    +\left({\partial f\over\partial x_1}\right)^2
    +\left({\partial f\over\partial x_2}\right)^2
    +\cdots
    }\,\d x_1\,\d x_2\cdots\d x_n

The "$x_j$" term is missing in the sums above.

.. index::
    pair: implicit surface; integration

Implicit Surface
~~~~~~~~~~~~~~~~

For a surface given explicitly by

.. math::

    F(x_1, x_2, ..., x_n) = 0

we get:

.. math::

    \d S = |\nabla F| \left|{\partial F\over\partial x_n}\right|\,\d
    x_1\cdots\d x_{n-1}

.. index::
    pair: orthogonal coordinates; integration

Orthogonal Coordinates
~~~~~~~~~~~~~~~~~~~~~~

If the coordinate vectors are orthogonal to each other:

.. math::

    {\partial\mathbf{\varphi}\over\partial t_i} \cdot
    {\partial\mathbf{\varphi}\over\partial t_i} = 0
    \quad\text{for $i\neq j$}

we get:

.. math::

    \d S =
    \left|{\partial\mathbf{\varphi}\over\partial t_1}\right|
    \left|{\partial\mathbf{\varphi}\over\partial t_2}\right|
    \cdots
    \left|{\partial\mathbf{\varphi}\over\partial t_k}\right|
    \d t_1\cdots\d t_k
