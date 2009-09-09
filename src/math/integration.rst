Integration
===========

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
