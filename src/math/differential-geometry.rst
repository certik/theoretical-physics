=====================
Differential Geometry
=====================

.. index:: differential geometry, manifolds

Manifolds
=========

.. index:: scalar, vector, tensor

Scalars, Vectors, Tensors
-------------------------


Differentiable manifold $U$ is a space covered by an atlas of maps, each map
covers part of the manifold and is a one to one mapping to an euclidean space
$\R^n$:

.. math::

    \phi:U\to \R^n

Let's have a one-to-one transformation between $x^\mu$ and $x'^\mu$ coordinates
(we simply write $x\equiv x^\mu$, etc.):

.. math::

    x' = x'(x)


.. math::

    x = x(x')

Scalar $\phi(x)$ is such a field that transforms as ($\phi'(x')$ is it's value
in $x'$ coordinates):

.. math::

    \phi'(x')=\phi(x)

One form $p_\alpha(x)$ is such a field that transforms the same as the
gradient $\partial\phi(x)\over\partial x^\mu$ of a scalar, that transforms as 
($\partial\phi'(x')\over\partial x'^\mu$ is it's value in $x'$ coordinates):

.. math::

    {\partial\phi'(x')\over\partial x'^\mu} ={\partial x^\nu\over\partial x'^\mu} {\partial\phi'(x')\over\partial x^\nu} ={\partial x^\nu\over\partial x'^\mu} {\partial\phi(x)\over\partial x^\nu}

so

.. math::

    p'_\mu(x') ={\partial x^\nu\over\partial x'^\mu} p_\nu(x)

Vector $V^\alpha$ is such a field that produces a scalar $\phi=V^\alpha
p_\alpha$ when contracted with a one form and this fact is used to deduce how it
transforms:

.. math::

    \phi' = V'^\alpha p'_\alpha  = V'^\alpha {\partial x^\beta\over\partial x'^\alpha} p_\beta =\phi = V^\beta p_\beta

so we have

.. math::

     V'^\alpha {\partial x^\beta\over\partial x'^\alpha} = V^\beta
 
multiplying by ${\partial x'^\mu\over\partial x^\beta}$ and using the fact that
${\partial x^\beta\over\partial x'^\alpha} {\partial x'^\mu\over\partial x^\beta} = {\partial x'^\mu\over\partial x'^\alpha} =\delta^\mu_\alpha$ we get

.. math::

     V'^\mu = {\partial x'^\mu\over\partial x^\beta} V^\beta
 
Higher tensors are build up and their transformation properties derived from
the fact, that by contracting with either a vector or a form we get a lower
rank tensor that we already know how it transforms.

Having now defined scalar, vector and tensor fields, one may then choose a
basis at each point for each field, the only requirement being that the basis
is not singular. For example for vectors, each point in $U$ has a basis $\vec e_\alpha$, so a vector (field)
$\vec V$ has components $V^\alpha$ with respect to this basis:

.. math::

    \vec V = V^\alpha\vec e_\alpha

.. index::
    pair: covariant; differentiation

Covariant differentiation
-------------------------


The derivative of the basis vector ${\partial \vec
e_\alpha\over\partial x^\beta}$ is a vector, thus it can be written as a linear
combination of the basis vectors:

.. math::

    {\partial \vec e_\alpha\over\partial x^\beta}=\Gamma^\mu_{\alpha\beta} \vec e_\mu

Differentiating a vector is then easy:

.. math::

    {\partial\vec V\over\partial x^\beta}\equiv\nabla_\beta \vec V ={\partial V^\alpha\over\partial x^\beta}\vec e_\alpha+   V^\alpha {\partial \vec e_\alpha\over\partial x^\beta} ={\partial V^\alpha\over\partial x^\beta}\vec e_\alpha+   V^\alpha \Gamma^\mu_{\alpha\beta} \vec e_\mu =\left({\partial V^\alpha\over\partial x^\beta}+   \Gamma^\alpha_{\mu\beta}V^\mu \right) \vec e_\alpha

So we define a covariant derivative:

.. math::

    \nabla_\beta V^\alpha = {\partial V^\alpha\over\partial x^\beta}+   \Gamma^\alpha_{\mu\beta}V^\mu

and write

.. math::

    {\partial\vec V\over\partial x^\beta}=\nabla_\beta \vec V =\left(\nabla_\beta \vec V\right)^\alpha\vec e_\alpha =\left(\nabla_\beta V^\alpha\right)\vec e_\alpha

I.e. we have:

.. math::

    \nabla_\beta \vec V = \nabla_\beta(V^\alpha\vec e_\alpha) = (\nabla_\beta V^\alpha)\vec e_\alpha

We also define:

.. math::

    \nabla_{\vec X} \vec V = \nabla_{X^\beta \vec e_\beta} \vec V \equiv X^\beta\nabla_\beta\vec V = X^\beta(\nabla_\beta V^\alpha)\vec e_\alpha


A scalar doesn't depend on basis vectors, so its covariant derivative is just
its partial derivative

.. math::

    \nabla_\alpha \phi={\partial \phi\over\partial x^\alpha}

Differentiating a one form $p_\alpha$ is done using the fact, that
$\phi=p_\alpha V^\alpha$ is a scalar, thus

.. math::

    \nabla_\beta \phi={\partial p_\alpha V^\alpha\over\partial x^\beta} ={\partial p_\alpha \over\partial x^\beta}V^\alpha+ p_\alpha{\partial  V^\alpha\over\partial x^\beta} ={\partial p_\alpha \over\partial x^\beta}V^\alpha+ p_\alpha\left(\nabla_\beta V^\alpha-   \Gamma^\alpha_{\mu\beta}V^\mu\right)=


.. math::

     =V^\alpha\left({\partial p_\alpha \over\partial     x^\beta}-\Gamma^\mu_{\alpha\beta}p_\mu\right)+     p_\alpha\nabla_\beta V^\alpha =V^\alpha\nabla_\beta p_\alpha+     p_\alpha\nabla_\beta V^\alpha

where we have defined

.. math::

    \nabla_\beta p_\alpha = {\partial p_\alpha \over\partial     x^\beta}-\Gamma^\mu_{\alpha\beta}p_\mu

This is obviously a tensor, because the above equation has a tensor on the left
hand side ($\nabla_\beta \phi$) and tensors on the right hand side
($p_\alpha\nabla_\beta V^\alpha$ and $V^\alpha$). Similarly for the derivative of
the tensor $A^{\mu\nu}$ we use the fact that $V^\mu=A^{\mu\nu}p_\nu$ is a
vector:

.. math::

    \nabla_\beta V^\mu=\nabla_\beta (A^{\mu\nu}p_\nu)=\partial_\beta (A^{\mu\nu}p_\nu)+\Gamma^\mu_{\alpha\beta}A^{\alpha\nu}p_\nu =p_\nu\partial_\beta A^{\mu\nu}+ A^{\mu\nu}\partial_\beta p_\nu+\Gamma^\mu_{\alpha\beta}A^{\alpha\nu}p_\nu=


.. math::

     =p_\nu\partial_\beta A^{\mu\nu}+     A^{\mu\nu}\left(\nabla_\beta p_\nu+\Gamma^\mu_{\nu\beta}p_\mu\right)     +\Gamma^\mu_{\alpha\beta}A^{\alpha\nu}p_\nu =p_\nu\nabla_\beta A^{\mu\nu}+ A^{\mu\nu}\nabla_\beta p_\nu

where we define

.. math::

    \nabla_\beta A^{\mu\nu}=\partial_\beta A^{\mu\nu} +\Gamma^\mu_{\alpha\beta}A^{\alpha\nu} +\Gamma^\nu_{\alpha\beta}A^{\mu\alpha}

and so on for other tensors, for example:

.. math::

    \nabla_\beta A^\mu{}_\nu=\partial_\beta A^\mu{}_\nu +\Gamma^\mu_{\alpha\beta}A^\alpha{}_\nu -\Gamma^\alpha_{\nu\beta}A^\mu{}_\alpha


.. math::

    \nabla_\beta A_{\mu\nu}=\partial_\beta A_{\mu\nu} -\Gamma^\alpha_{\mu\beta}A_{\alpha\nu} -\Gamma^\alpha_{\nu\beta}A_{\mu\alpha}


One can now easily proof some common relations simply by rewriting it to
components and back:

.. math::

    \nabla_{\vec X}(f\vec Y) = (\nabla_{\vec X}f)\vec Y + f\nabla_{\vec X}\vec Y


.. math::

    \nabla_{\vec X}(\vec Y+\vec Z) = \nabla_{\vec X}\vec Y     + \nabla_{\vec X}\vec Z


.. math::

    \nabla_{f\vec X}\vec Y = f\nabla_{\vec X}\vec Y


Change of variable:

.. math::

    \Gamma'^\alpha{}_{\beta\gamma}= {\partial x^\mu\over\partial x'^\beta} {\partial x^\nu\over\partial x'^\gamma} \Gamma^\sigma{}_{\mu\nu} {\partial x'^\alpha\over\partial x^\sigma} + {\partial x'^\alpha\over\partial x^\sigma} {\partial^2 x^\sigma\over\partial x'^\beta\partial x'^\gamma}

.. index::
    pair: parallel; transport

Parallel transport
------------------


If the vectors $\vec V$ at infinitesimally close points of the curve
$x^\mu(\lambda)$ are parallel and of equal length, then $\vec V$ is said to be
parallel transported along the curve, i.e.:

.. math::

    {\d \vec V\over\d\lambda} = 0

So

.. math::

    {\d \vec V\over\d\lambda} = {\d (V^\alpha\vec e_\alpha)\over\d\lambda} =  {\d x^\beta\over\d\lambda}\partial_\beta (V^\alpha\vec e_\alpha) =  {\d x^\beta\over\d\lambda}(\nabla_\beta V^\alpha) \vec e_\alpha = 0

In components (using the tangent vector $U^\beta = {\d x^\beta\over\d\lambda}$):

.. math::

    {\d V^\alpha\over\d\lambda} = U^\beta\nabla_\beta V^\alpha = 0

.. index::
    pair: Fermi-Walker; transport

Fermi-Walker transport
----------------------


In local inertial frame:

.. math::

    U^\lambda_0 = (1, 0, 0, 0)


.. math::

    {\d S^i\over\d t} = 0

We require orthogonality $S_\mu U^\mu = 0$,
in a general frame:

.. math::

    {\d S^\alpha\over\d \tau} = \lambda U^\alpha =  S_\mu {\d U^\mu\over\d \tau} U^\alpha

where $\lambda$ was calculated by differentiating the orthogonality condition.
This is called a Thomas precession. 

For any vector, we define:
the vector $X^\mu$ is Fermi-Walker tranported along the curve if:

.. math::

     {\d X^\mu\over\d\lambda} = X_\alpha{\d U^\alpha\over\d\lambda}U^\mu -X_\alpha U^\alpha{\d U^\mu\over\d\lambda}

If $X^\mu$ is perpendicular to $U^\mu$, the second term is zero and the result
is called a Fermi transport.

Why: the $U^\mu$ is transported by Fermi-Walker and also this is the equation
for gyroscopes, so the natural, nonrotating tetrade is the one with $\vec e^\mu_0
\equiv U^\mu$, which is then correctly transported along any curve (not just
geodesics).

.. index:: geodesics

Geodesics
---------


Geodesics is a curve $x^\alpha(\lambda)$ that locally looks like a line, 
i.e. it parallel
transports its own tangent vector:

.. math::

    U^\beta\nabla_\beta U^\alpha = 0

so

.. math::

    U^\beta\partial_\beta U^\alpha + \Gamma^\alpha_{\beta\gamma}U^\beta U^\gamma  = 0

or equivalently (using the fact $U^\beta\partial_\beta U^\alpha=
{\d x^\beta\over\d\lambda}{\partial\over\partial x^\beta}
{\d x^\alpha\over\d\lambda} = {\d^2 x^\alpha\over\d\lambda^2}$):

.. math::

    {\d^2 x^\alpha\over\d\lambda^2} + \Gamma^\alpha_{\beta\gamma} {\d x^\beta\over\d\lambda}{\d x^\gamma\over\d\lambda} = 0


.. index:: curvature

Curvature
---------


Curvature means that we take a vector $V^\mu$, parallel transport it around
a closed loop (which is just applying a commutator of the covariant derivatives $[\nabla_\alpha, \nabla_\beta]V^\mu$), see how it changes and
that's the curvature:

.. math::

    [\nabla_\alpha, \nabla_\beta]V^\mu\equiv R^\mu{}_{\nu\alpha\beta}V^\nu

That's all there is to it. Expanding the left hand side:

.. math::

    [\nabla_\alpha, \nabla_\beta]V^\mu=\left(\partial_\alpha\Gamma^\mu_{\beta\nu} -\partial_\beta\Gamma^\mu_{\alpha\nu} +\Gamma^\mu_{\alpha\sigma}\Gamma^\sigma_{\beta\nu} -\Gamma^\mu_{\beta\sigma}\Gamma^\sigma_{\alpha\nu}\right)V^\nu

we get

.. math::

    R^\mu{}_{\nu\alpha\beta}=\partial_\alpha\Gamma^\mu_{\beta\nu} -\partial_\beta\Gamma^\mu_{\alpha\nu} +\Gamma^\mu_{\alpha\sigma}\Gamma^\sigma_{\beta\nu} -\Gamma^\mu_{\beta\sigma}\Gamma^\sigma_{\alpha\nu}

.. index::
    pair: Lie; derivative

Lie derivative
--------------


Definition of the Lie derivative of any tensor $T$ is:

.. math::

    \L_{\vec U} T=\lim_{t\to0}{\phi_{t*}T(\phi_t(p))-T(p)\over t}

it can be shown directly from this definition, that the Lie derivative of a
vector is the same as a Lie
bracket:

.. math::

    \L_{\vec U}\vec V \equiv [\vec U, \vec V]

and in components

.. math::

    \L_{\vec U} V^\alpha =  [\vec U, \vec V]^\alpha\equiv U^\beta\nabla_\beta V^\alpha- V^\beta\nabla_\beta U^\alpha = U^\beta\partial_\beta V^\alpha- V^\beta\partial_\beta U^\alpha

Lie derivative of a scalar is

.. math::

    \L_{\vec V} f = V^\mu\partial_\mu f

and of a one form $p_\mu$ is derived using the observation that $f=p_\mu V^\mu$
is a scalar:

.. math::

    \L_{\vec V} p_\mu = V^\nu\nabla_\nu p_\mu+p_\nu\nabla_\mu V^\nu = V^\nu\partial_\nu p_\mu+p_\nu\partial_\mu V^\nu

and so on for other tensors, for example:

.. math::

    \L_{\vec V} g_{\mu\nu} = V^\alpha\nabla_\alpha g_{\mu\nu} +g_{\alpha\nu}\nabla_\mu V^\alpha +g_{\mu\alpha}\nabla_\nu V^\alpha = V^\alpha\partial_\alpha g_{\mu\nu} +g_{\alpha\nu}\partial_\mu V^\alpha +g_{\mu\alpha}\partial_\nu V^\alpha

.. index:: metric

Metric
------


In general, the Christoffel symbols are not symmetric and there is no metric
that generates them. However, if the manifold is equipped with metrics, then
the fundamental theorem of Riemannian geometry states that there is a unique
Levi-Civita connection, for which the metric tensor is preserved by
parallel transport:

.. math::

    \nabla_\mu g_{\alpha\beta}=0

We define the commutation coefficients of the basis $c^\alpha{}_{\mu\nu}$ by

.. math::

    c^\alpha{}_{\mu\nu}\vec e_\alpha = \nabla_{\vec e_\mu}\vec e_\nu- \nabla_{\vec e_\nu}\vec e_\mu

In general these coefficients are not zero (as an example, take the units
vectors in in spherical and cylindrical coordinates), but for coordinate bases
they are.
It can be proven, that

.. math::

    \Gamma^\mu_{\alpha\beta}=\half g^{\mu\sigma} \left(\partial_\beta g_{\sigma\alpha}+\partial_\alpha g_{\sigma\beta}- \partial_\sigma g_{\alpha\beta}+c_{\alpha\sigma\beta}+c_{\beta\sigma\alpha} -c_{\sigma\alpha\beta}\right)

and for coordinate bases $c^\alpha{}_{\mu\nu}=0$, so

.. math::

    \Gamma^\mu_{\alpha\beta}=\Gamma^\mu_{\beta\alpha}


.. math::

    \Gamma^\mu_{\alpha\beta}=\half g^{\mu\sigma} \left(\partial_\beta g_{\sigma\alpha}+\partial_\alpha g_{\sigma\beta}- \partial_\sigma g_{\alpha\beta}\right)

As a special case:

.. math::

    \Gamma^\mu_{\mu\beta}=\half g^{\mu\sigma} \left(\partial_\beta g_{\sigma\mu}+\partial_\mu g_{\sigma\beta}- \partial_\sigma g_{\mu\beta}\right)=\half g^{\mu\sigma}\partial_\beta g_{\sigma\mu}=


.. math::

     =\half \Tr g^{-1}\partial_\beta g =\half \Tr\partial_\beta\log g =\half \partial_\beta\Tr\log g =\half \partial_\beta\log|\det g| =\partial_\beta\log\sqrt{|\det g|} =

.. math::

    ={1\over2\det g}\partial_\beta\det g
    ={1\over\sqrt{|\det g|}}\partial_\beta\sqrt{|\det g|}

All last 3 expressions are used (but the last one is probably the most common).
$g$ is the matrix of coefficients $g_{\mu\nu}$.  At the beginning we used the
usual trick that $g^{\mu\sigma}$ is symmetric but $\partial_\mu
g_{\sigma\beta}- \partial_\sigma g_{\mu\beta}$ is unsymmetric.  Later we used
the identity $\Tr\log g = \log|\det g|$, which follows from the well-known
identity $\det\exp A = \exp\Tr A$ by substituting $A=\log g$ and taking the
logarithm of both sides.

.. index::
    pair: Killing; vector

Symmetries, Killing vectors
---------------------------


We say that a diffeomorphism $\phi$ is a symmetry of some tensor T if the
tensor is invariant after being pulled back under $\phi$:

.. math::

    \phi_*T = T

Let the one-parameter family of symmetries $\phi_t$ be generated by a vector
field $V^\mu(x)$, then the above equation is equivalent to:

.. math::

    \L_{\vec V} T = 0

If $T$ is the metric $g_{\mu\nu}$ then the symmetry is called isometry and
$V^\mu$ is called a Killing vector field and can be calculated from:

.. math::

    \L_{\vec V} g_{\mu\nu} = V^\alpha\nabla_\alpha g_{\mu\nu} +g_{\alpha\nu}\nabla_\mu V^\alpha +g_{\mu\alpha}\nabla_\nu V^\alpha = \nabla_\mu V_\nu +\nabla_\nu V_\mu = 0

The last equality is Killing's equation. If $x^\mu$ is a geodesics with a
tangent vector $U^\mu$ and $V^\mu$ is a Killing vector, then the quantity
$V_\mu U^\mu$ is conserved along the geodesics, because:

.. math::

    {\d (V_\mu U^\mu)\over\d\lambda} =  U^\nu\nabla_\nu(V_\mu U^\mu)=U^\nu U^\mu\nabla_\nu V_\mu +V_\mu U^\nu\nabla_\nu U^\mu = 0

where the first term is both symmetric and antisymmetric in $(\mu, \nu)$, thus
zero, and the second term is the geodesics equation, thus also zero.

.. index::
    pair: divergence; operator

Divergence Operator
-------------------

.. math::

    \nabla_\mu A^\mu
    =\partial_\mu A^\mu+\Gamma^\mu_{\mu\sigma}A^\sigma
    =

    =\partial_\mu A^\mu+{1\over\sqrt{|\det
    g|}}\left(\partial_\sigma\sqrt{|\det g|}\right) A^\sigma
    =

    ={1\over\sqrt{|\det g|}}
    \partial_\mu\left(\sqrt{|\det g|}\, A^\mu\right)

If the metric is diagonal (let's show this in 3D):

.. math::

    g_{ij} =
    \mat{h_1^2 & 0 & 0\cr
    0 & h_2^2 & 0\cr
    0 & 0 & h_3^2\cr}

then

.. math::

    \sqrt{|\det g_{ij}|}=h_1 h_2 h_3

    g^{ij} =
    \mat{{1\over h_1^2} & 0 & 0\cr
    0 & {1\over h_2^2} & 0\cr
    0 & 0 & {1\over h_3^2}\cr}

and

.. math::

    \nabla\cdot{\bf A}=
    \nabla_i A^i
    ={1\over h_1 h_2 h_3}\partial_i
    \left(h_1 h_2 h_3 A^i \right)

.. index::
    pair: laplace; operator

Laplace Operator
----------------

.. math::

    \nabla^2\varphi
    =\nabla_\mu\nabla^\mu\varphi
    =\partial_\mu\nabla^\mu\varphi+\Gamma^\mu_{\mu\sigma}\nabla^\sigma\varphi
    =\partial_\mu\partial^\mu\varphi+\Gamma^\mu_{\mu\sigma}\partial^\sigma\varphi
    =

    =\partial_\mu\partial^\mu\varphi+{1\over\sqrt{|\det
    g|}}\left(\partial_\sigma\sqrt{|\det g|}\right) \partial^\sigma\varphi
    =

    ={1\over\sqrt{|\det g|}}
    \partial_\mu\left(\sqrt{|\det g|}\, \partial^\mu\varphi\right)
    ={1\over\sqrt{|\det g|}}
    \partial_\mu\left(\sqrt{|\det g|}\, g^{\mu\sigma}\partial_\sigma\varphi\right)

If the metric is diagonal (let's show this in 3D):

.. math::

    g_{ij} =
    \mat{h_1^2 & 0 & 0\cr
    0 & h_2^2 & 0\cr
    0 & 0 & h_3^2\cr}

then

.. math::

    \sqrt{|\det g_{ij}|}=h_1 h_2 h_3

    g^{ij} =
    \mat{{1\over h_1^2} & 0 & 0\cr
    0 & {1\over h_2^2} & 0\cr
    0 & 0 & {1\over h_3^2}\cr}

and

.. math::

    \nabla^2\varphi
    =\sum_i{1\over h_1 h_2 h_3}\partial_i
    \left({h_1 h_2 h_3\over h_i^2}\partial_i\varphi \right)

.. index::
    pair: covariant; integration

Covariant integration
---------------------

If $f(x)$ is a scalar, then the integral $\int f(x) \d^4 x$ depends on
coordinates. The correct way to integrate $f(x)$ in any coordinates is:

.. math::

    \int f(x) \sqrt{|g|}\d^4 x

where $g\equiv\det g_{\mu\nu}$. The Gauss theorem in curvilinear coordinates
is:

.. math::

    \int_\Omega \nabla_\mu u^\mu \sqrt{|g|}\d^4 x
    =\int_\Omega {1\over\sqrt{|g|}}\partial_\mu\left(\sqrt{|g|} u^\mu\right) \sqrt{|g|}\d^4 x
    =\int_\Omega \partial_\mu\left(\sqrt{|g|} u^\mu\right)\d^4 x
    =

    =\int_{\partial\Omega} \sqrt{|g|} u^\mu n_\mu\d^3 x
    =\int_{\partial\Omega} u^\mu n_\mu \sqrt{|g|}\d^3 x

where $\partial\Omega$ is the boundary (surface) of $\Omega$ and $n_\nu$ is the
normal vector to this surface.


Examples
========

Weak Formulation of Laplace Equation
------------------------------------

As an example, we write the weak formulation of the Laplace equation in
arbitrary coordintes:

.. math::

    \nabla^2\varphi - f = 0

    \int \left(\nabla^2\varphi v - f v\right)  \sqrt{|g|}d^3 x = 0

    \int \left(
    {1\over\sqrt{|g|}}\partial_i\left(\sqrt{|g|}g^{ij}\partial_j\varphi\right)
    v - f v\right)  \sqrt{|g|}d^3 x = 0

    \int \left(
    \partial_i\left(\sqrt{|g|}g^{ij}\partial_j\varphi\right)
    v - f v\sqrt{|g|}\right)  d^3 x = 0

Now we apply per-partes (assuming the boundary integral vanishes):

.. math::

    \int \left(
    -\sqrt{|g|}g^{ij}\partial_j\varphi
    \partial_i v - f v\sqrt{|g|}\right)  d^3 x = 0

    \int \left(
    -g^{ij}\partial_j\varphi
    \partial_i v - f v\right) \sqrt{|g|} d^3 x = 0

For diagonal metric this evaluates to:

.. math::

    \int \left(
    -\sum_i {1\over h_i^2}\partial_i\varphi \partial_i v
    - f v\right) h_1 h_2 h_3 d^3 x = 0

.. index::
    pair: cylindrical; coordinates

Cylindrical Coordinates
-----------------------



.. math::

    x = \rho\cos\phi


.. math::

    y = \rho\sin\phi


.. math::

    z = z

The transformation matrix is

.. math::

     {\partial (x, y, z)\over\partial(\rho, \phi, z)} =\mat{\cos\phi & -\rho\sin\phi & 0 \cr \sin\phi & \rho\cos\phi & 0 \cr 0 & 0 & 1 \cr}

The metric tensor of the cartesian coordinate system $\hat x^a=(x, y, z)$ is
$\hat g_{ab}={\rm diag}(1, 1, 1)$,
so by transformation we get the metric tensor $g_{ij}$ in the cylindrical
coordinates $x^i=(\rho, \phi, z)$:

.. math::

     g_{ij} =  {\partial \hat x^a\over\partial x^i} {\partial \hat x^b\over\partial x^j} \hat g_{ab} = \left({\partial \hat x\over\partial x}\right)^T \hat g {\partial \hat x\over\partial x} =


.. math::

     = \left({\partial (x, y, z)\over\partial(\rho, \phi, z)}\right)^T \mat{1 & 0 & 0\cr 0 & 1 & 0\cr 0 & 0 & 1\cr} {\partial (x, y, z)\over\partial(\rho, \phi, z)}=


.. math::

    = \mat{\cos\phi &\sin\phi & 0 \cr  -\rho\sin\phi & \rho\cos\phi & 0 \cr 0 & 0 & 1 \cr} \mat{1 & 0 & 0\cr 0 & 1 & 0\cr 0 & 0 & 1\cr} \mat{\cos\phi & -\rho\sin\phi & 0 \cr \sin\phi & \rho\cos\phi & 0 \cr 0 & 0 & 1 \cr}= \mat{1 & 0 & 0\cr 0 & \rho^2 & 0\cr 0 & 0 & 1\cr}


.. math::

     g^{ij} = \mat{1 & 0 & 0\cr 0 & 1\over\rho^2 & 0\cr 0 & 0 & 1\cr}



.. math::

    \det g = \det g_{ij} = \rho^2



.. math::

    \nabla^i\nabla_i\varphi
    ={1\over\sqrt{|\det g|}}
    \partial_i\left(\sqrt{|\det g|}\, g^{ij}\partial_j\varphi\right)
    =

.. math::

    ={1\over\rho}\partial_i\left(\rho g^{ij}\partial_j\varphi\right)
    ={1\over\rho}\partial_\rho\left(\rho \partial_\rho\varphi\right)
    +{1\over\rho}\partial_\phi\left(\rho {1\over\rho^2}\partial_\phi\varphi\right)
    +{1\over\rho}\partial_z\left(\rho \partial_z\varphi\right)=

    ={1\over\rho}\partial_\rho\left(\rho \partial_\rho\varphi\right)
    +{1\over\rho^2}\partial_\phi\partial_\phi\varphi
    +\partial_z\partial_z\varphi=

.. math::

     = \partial_\rho\partial_\rho\varphi
     +{1\over\rho}\partial_\rho\varphi
     +{1\over\rho^2}\partial_\phi\partial_\phi\varphi
     +\partial_z\partial_z\varphi


As a particular example, let's write the Laplace equation with nonconstant
conductivity for axially symmetric field. The Laplace equation is:

.. math::

    \nabla\cdot\sigma\nabla\varphi=0

so we use the formulas above to get:

.. math::

    0=\nabla\cdot\sigma\nabla\varphi=\nabla^i\sigma\nabla_i\varphi = {\partial\over\partial\rho}\sigma{\partial\varphi\over\partial\rho} + {1\over\rho^2} {\partial\over\partial\phi}\sigma{\partial\varphi\over\partial\phi} + {\partial\over\partial z}\sigma{\partial\varphi\over\partial z} + {\sigma\over\rho}{\partial\varphi\over\partial\rho}

but we know that $\varphi=\varphi(\rho, z)$, so
${\partial\varphi\over\partial\phi}=0$
and the final equation is:

.. math::

     {\partial\over\partial\rho}\sigma{\partial\varphi\over\partial\rho} + {\partial\over\partial z}\sigma{\partial\varphi\over\partial z} + {\sigma\over\rho}{\partial\varphi\over\partial\rho} =0

To write the weak formulation for it, we need to integrate covariantly (e.g.
$\rho\,\d\rho\d\phi\d z$ in our case) and
rewrite it using per partes. We did exactly this in the previous example in a
coordinate free maner, so we just use the final formula we got there for a
diagonal metric:

.. math::

    \int\left(
    -\partial_\rho\varphi\partial_\rho v
    -{1\over\rho^2}\partial_\phi\varphi\partial_\phi v
    -\partial_z\varphi\partial_z v
    \right)\sigma\rho\,\d\rho\d\phi\d z=0

and for $\partial_\phi\varphi=0$, we get:

.. math::

    -2\pi\int\left(
    \partial_\rho\varphi\partial_\rho v
    +\partial_z\varphi\partial_z v
    \right)\sigma\rho\,\d\rho\d z=0


Spherical Coordinates
---------------------



.. math::

    x = \rho\sin\theta\cos\phi


.. math::

    y = \rho\sin\theta\sin\phi


.. math::

    z = \rho\cos\theta

The transformation matrix is

.. math::

     {\partial (x, y, z)\over\partial(\rho, \theta, \phi)} = \mat{\sin\theta\cos\phi & \rho\cos\theta\cos\phi & -\rho\sin\theta\sin\phi \cr \sin\theta\sin\phi & \rho\cos\theta\sin\phi & \rho\sin\theta\cos\phi \cr \cos\phi & -\rho\sin\theta & 0 \cr}

The metric tensor of the cartesian coordinate system $\hat x^a=(x, y, z)$ is
$\hat g_{ab}={\rm diag}(1, 1, 1)$,
so by transformation we get the metric tensor $g_{ij}$ in the spherical
coordinates $x^i=(\rho, \theta, \phi)$:

.. math::

     g_{ij} =  {\partial \hat x^a\over\partial x^i} {\partial \hat x^b\over\partial x^j} \hat g_{ab} = \left({\partial \hat x\over\partial x}\right)^T \hat g {\partial \hat x\over\partial x} =


.. math::

     = \left({\partial (x, y, z)\over\partial(\rho, \theta, \phi)}\right)^T \mat{1 & 0 & 0\cr 0 & 1 & 0\cr 0 & 0 & 1\cr} {\partial (x, y, z)\over\partial(\rho, \theta, \phi)}=


.. math::

    = \mat{ \sin\theta\cos\phi & \sin\theta\sin\phi & \cos\theta \cr \rho\cos\theta\cos\phi & \rho\cos\theta\sin\phi & -\rho\sin\theta \cr -\rho\sin\theta\sin\phi & \rho\sin\theta\cos\phi & 0 \cr } \mat{1 & 0 & 0\cr 0 & 1 & 0\cr 0 & 0 & 1\cr} \mat{\sin\theta\cos\phi & \rho\cos\theta\cos\phi & -\rho\sin\theta\sin\phi \cr \sin\theta\sin\phi & \rho\cos\theta\sin\phi & \rho\sin\theta\cos\phi \cr \cos\phi & -\rho\sin\theta & 0 \cr} =


.. math::

     = \mat{1 & 0 & 0\cr 0 & \rho^2 & 0\cr 0 & 0 & \rho^2\sin^2\theta\cr}


.. math::

     g^{ij} = \mat{1 & 0 & 0\cr 0 & 1\over\rho^2 & 0\cr 0 & 0 & 1\over\rho^2\sin^2\theta\cr}



.. math::

    \det g = \det g_{ij} = \rho^4\sin^2\theta



.. math::

    \nabla^i\nabla_i\varphi = \partial^i\partial_i\varphi+{1\over{2\det g}}\partial_j(\det g)\,\, g^{jk}\partial_k\varphi=


.. math::

    = g^{ij}\partial_i\partial_j\varphi+{1\over{2\rho^4\sin^2\theta }}\left( \partial_\rho(\rho^4\sin^2\theta)\,\,g^{\rho \rho}\partial_\rho\varphi + \partial_\theta(\rho^4\sin^2\theta)\,\,g^{\theta \theta}\partial_\theta\varphi \right)


.. math::

     = g^{ij}\partial_i\partial_j\varphi+{2\over\rho}\partial_\rho\varphi +{\cos\theta\over\rho^2\sin\theta}\partial_\theta\varphi =


.. math::

     = \partial_\rho\partial_\rho\varphi
     +{1\over\rho^2}\partial_\theta\partial_\theta\varphi
     +{1\over\rho^2\sin^2\theta}\partial_\phi\partial_\phi\varphi
     +{2\over\rho}\partial_\rho\varphi +{\cos\theta\over\rho^2\sin\theta}\partial_\theta\varphi

.. index:: rotating disk

Rotating Disk
-------------


Let's have a laboratory Euclidean system $x^\mu = (t, x, y, z)$ and
a rotating disk system $x'^\mu = (t', x', y', z')$. The relation between the frames is

.. math::

    \mat{t'\cr x'\cr y'\cr z'\cr}= \mat{1 & 0 & 0 & 0\cr 0 & \cos\omega t & \sin\omega t & 0\cr 0 & -\sin\omega t & \cos\omega t & 0\cr 0 & 0 & 0 & 1\cr} \mat{t\cr x\cr y\cr z\cr} = \mat{t\cr x\cos\omega t+y\sin\omega t\cr -x\sin\omega t+y\cos\omega t\cr z\cr}

The inverse transformation can be calculated by simply inverting the matrix:

.. math::

    \mat{t\cr x\cr y\cr z\cr}= \mat{1 & 0 & 0 & 0\cr 0 & \cos\omega t' & -\sin\omega t' & 0\cr 0 & \sin\omega t' & \cos\omega t' & 0\cr 0 & 0 & 0 & 1\cr} \mat{t'\cr x'\cr y'\cr z'\cr}

so the transformation matrices are:

.. math::

    {\partial x'^\mu\over\partial x^\nu}= \mat{1 & 0 & 0 & 0\cr -x\omega\sin\omega t + y\omega\cos\omega t & \cos\omega t & \sin\omega t & 0\cr -x\omega\cos\omega t - y\omega\sin\omega t & -\sin\omega t & \cos\omega t & 0\cr 0 & 0 & 0 & 1\cr} ={\partial x'\over\partial x}


.. math::

    {\partial x^\nu\over\partial x'^\mu}= \mat{1 & 0 & 0 & 0\cr -x'\omega\sin\omega t' - y'\omega\cos\omega t' & \cos\omega t' & -\sin\omega t' & 0\cr x'\omega\cos\omega t' - y'\omega\sin\omega t' & \sin\omega t' & \cos\omega t' & 0\cr 0 & 0 & 0 & 1\cr} ={\partial x\over\partial x'}

The problem now is that Newtonian mechanics has a degenerated spacetime
metrics (see later). Let's pretend we have the following metrics in the
$x^\mu$ system:

.. math::

    g_{\mu\nu} = \mat{1 & 0 & 0 & 0\cr 0 & 1 & 0 & 0\cr 0 & 0 & 1 & 0\cr 0 & 0 & 0 & 1\cr} =g

and

.. math::

    g'_{\alpha\beta} = {\partial x^\mu\over\partial x'^\alpha} {\partial x^\nu\over\partial x'^\beta} g_{\mu\nu} = \left({\partial x\over\partial x'}\right)^T g \left({\partial x\over\partial x'}\right) = \mat{1 + \omega^2 (x'^2+y'^2) & -\omega y' & \omega x' & 0\cr -\omega y' & 1 & 0 & 0\cr \omega x' & 0 & 1 & 0\cr 0 & 0 & 0 & 1\cr} =g'

However, if we calculate with the correct special relativity metrics:

.. math::

    g_{\mu\nu} = \mat{-c^2 & 0 & 0 & 0\cr 0 & 1 & 0 & 0\cr 0 & 0 & 1 & 0\cr 0 & 0 & 0 & 1\cr} =g

and

.. math::

    g'_{\alpha\beta} = {\partial x^\mu\over\partial x'^\alpha} {\partial x^\nu\over\partial x'^\beta} g_{\mu\nu} = \left({\partial x\over\partial x'}\right)^T g \left({\partial x\over\partial x'}\right) = \mat{-c^2 + \omega^2 (x'^2+y'^2) & -\omega y' & \omega x' & 0\cr -\omega y' & 1 & 0 & 0\cr \omega x' & 0 & 1 & 0\cr 0 & 0 & 0 & 1\cr} =g'

We get the same Christoffel symbols as with the $\diag(1, 1, 1, 1)$ metrics,
because only the derivatives of the metrics are important.
Then the only nonzero Christoffel symbols are

.. math::

    \Gamma^1_{00}=-x'\omega^2


.. math::

    \Gamma^1_{02}=\Gamma^1_{20}=-\omega


.. math::

    \Gamma^2_{00}=-y'\omega^2


.. math::

    \Gamma^2_{01}=\Gamma^2_{10}=\omega

If we want to avoid dealing with metrics, it is possible
to
start with the Christoffel symbols in the $x^\mu$ system:

.. math::

    \Gamma^\sigma_{\mu\nu}=0

and then transforming them to the $x'^\mu$ system using the change of variable
formula:

.. math::

    \Gamma'^\alpha{}_{\beta\gamma}= {\partial x^\mu\over\partial x'^\beta} {\partial x^\nu\over\partial x'^\gamma} \Gamma^\sigma{}_{\mu\nu} {\partial x'^\alpha\over\partial x^\sigma} + {\partial x'^\alpha\over\partial x^\sigma} {\partial^2 x^\sigma\over\partial x'^\beta\partial x'^\gamma} = {\partial x'^\alpha\over\partial x^\sigma} {\partial^2 x^\sigma\over\partial x'^\beta\partial x'^\gamma}

As an example, let's calculate the coefficients above:

.. math::

    \Gamma'^2{}_{00}= {\partial x'^2\over\partial x^\sigma} {\partial^2 x^\sigma\over\partial x'^0\partial x'^0} = {\partial x'^2\over\partial x^\sigma} {\partial \over\partial x'^0} {\partial x^\sigma\over\partial x'^0} =


.. math::

     = \mat{-x\omega\cos\omega t - y\omega\sin\omega t & -\sin\omega t & \cos\omega t & 0\cr} {\partial \over\partial t'} \mat{1\cr -x'\omega\sin\omega t'-y'\omega\cos\omega t'\cr x'\omega\cos\omega t'-y'\omega\sin\omega t'\cr 0\cr} =


.. math::

     = \mat{-x\omega\cos\omega t - y\omega\sin\omega t & -\sin\omega t & \cos\omega t & 0\cr} \mat{0\cr -x'\omega^2\cos\omega t'+y'\omega^2\sin\omega t'\cr -x'\omega^2\sin\omega t'-y'\omega^2\cos\omega t'\cr 0\cr} =-y'\omega^2


.. math::

    \Gamma'^1{}_{00}=-x'\omega^2


.. math::

    \Gamma'^2{}_{01}=\Gamma'^2{}_{10}= {\partial x'^2\over\partial x^\sigma} {\partial^2 x^\sigma\over\partial x'^0\partial x'^1} = {\partial x'^2\over\partial x^\sigma} {\partial \over\partial x'^0} {\partial x^\sigma\over\partial x'^1} =


.. math::

     = \mat{-x\omega\cos\omega t - y\omega\sin\omega t & -\sin\omega t & \cos\omega t & 0\cr} {\partial \over\partial t'} \mat{0\cr \cos\omega t'\cr \sin\omega t'\cr 0\cr} =


.. math::

     = \mat{-x\omega\cos\omega t - y\omega\sin\omega t & -\sin\omega t & \cos\omega t & 0\cr} \mat{0\cr -\omega\sin\omega t'\cr \omega\cos\omega t'\cr 0\cr} =\omega


.. math::

    \Gamma'^1{}_{02}=\Gamma'^1{}_{20}=-\omega

So we got the same results.

Now let's see what we have got.
Later we'll show, that the $\Gamma^i_{00}$ coefficients are just
$\partial_i\phi$ in the Newtonian theory. E.g. in our case we have:

.. math::

    \Gamma'^1_{00} = -x'\omega^2 = \partial_x'\phi


.. math::

    \Gamma'^2_{00} = -y'\omega^2 = \partial_y'\phi


.. math::

    \Gamma'^3_{00} = 0 = \partial_z'\phi

from which:

.. math::

    \phi(t, x, y, z) = -\half(x'^2+y'^2)\omega^2 + C(t)

and the force acting on a test particle is then:

.. math::

    {\bf F} = -m\nabla\phi=m\,(x', y', 0)\,\omega^2=m{\bf r'}\omega^2

where we have defined ${\bf r'} = (x', y', 0)$. This is just the centrifugal
force. Also observe, that we could have read $\phi$ directly from the metrics
itself --- just compare it to the Lorentzian metrics (with gravitation) in the
next chapter.

The other two terms ($\Gamma'^1_{02}$, $\Gamma'^2_{01}$ and the symmetric ones) don't behave as a gravitational force, but
rather only act when we are differentiating (e.g. only act on moving bodies).
Below we show this is just the $-2\boldsymbol\omega\times{\d{\bf r}\over\d t}$ term
(responsible for the Coriolis acceleration).

Let's write the full equations of geodesics:

.. math::

     {\d^2 x^0\over\d\lambda^2}=0


.. math::

     {\d^2 x^1\over\d\lambda^2}+\Gamma^1_{00}\left({\d x^0\over\d\lambda}\right)^2 +2\Gamma^1_{20}{\d x^2\over\d\lambda}{\d x^0\over\d\lambda}=0


.. math::

     {\d^2 x^2\over\d\lambda^2}+\Gamma^2_{00}\left({\d x^0\over\d\lambda}\right)^2 +2\Gamma^2_{10}{\d x^1\over\d\lambda}{\d x^0\over\d\lambda}=0


.. math::

     {\d^2 x^3\over\d\lambda^2}=0

This becomes:

.. math::

     {\d^2 x\over\d t^2}=x\omega^2 +2\omega{\d y\over\d t}


.. math::

     {\d^2 y\over\d t^2}=y\omega^2 -2\omega{\d x\over\d t}


.. math::

     {\d^2 z\over\d t^2}=0

we can define ${\bf r} = (x, y, 0)$ and $\boldsymbol\omega=(0,0,\omega)$. Then the
above equations can be rewritten as:

.. math::

     {\d^2{\bf r}\over\d t^2}={\bf r}\omega^2-2\boldsymbol\omega\times{\d{\bf r}\over\d t}

So we get two fictituous forces, the centrifugal force and the Coriolis force.

Now imagine a static vector in the $x^\mu$ system along the $x$ axis, i.e.

.. math::

    V^\mu = \mat{1\cr 1\cr 0\cr 0\cr} = V

then

.. math::

    V'^\mu = {\partial x'^\mu\over\partial x^\alpha}V^\alpha= {\partial x'\over\partial x}V= \mat{1\cr -x\omega\sin\omega t + y\omega\cos\omega t + \cos\omega t \cr -x\omega\cos\omega t - y\omega\sin\omega t - \sin\omega t\cr 0\cr} = \mat{1\cr y'\omega + \cos\omega t' \cr -x'\omega - \sin\omega t'\cr 0\cr}=V'

In the last equality we transformed from $x^\mu$ to $x'^\mu$ using the
relation between frames.

Differentiating any vector in the $x^\mu$ coordinates
is easy -- it's just a partial derivative (due to the Euclidean metrics).
Let's differentiate any vector in the $x'^\mu$
coordinates with respect to time (since $t=t'$, the time is the same in both
coordinate systems):

.. math::

     \nabla_0V'^{\mu}=\partial_0V'^{\mu}+\Gamma^\mu_{0\alpha}V'^{\alpha}


.. math::

     \nabla_0 \mat{V'^0\cr V'^1 \cr V'^2\cr V'^3\cr} = \mat{\partial_0V'^0\cr \partial_0V'^1 +\Gamma^1_{00}V'^0+\Gamma^1_{02}V'^2\cr \partial_0V'^2 +\Gamma^2_{00}V'^0+\Gamma^2_{01}V'^1\cr \partial_0V'^3\cr} = \mat{\partial_0V'^0\cr \partial_0V'^1 -x'\omega^2V'^0-\omega V'^2\cr \partial_0V'^2 -y'\omega^2V'^0+\omega V'^1\cr \partial_0V'^3\cr}=

.. math::
    :label: vcovar

    =
    \partial_0
    \mat{V'^0\cr V'^1 \cr V'^2\cr V'^3\cr}
    +
    \mat{
    0 & 0 & 0 & 0\cr
    -x'\omega^2 & 0 & -\omega & 0\cr
    -y'\omega^2 & \omega & 0 & 0\cr
    0 & 0 & 0 & 0\cr
    }
    \mat{V'^0\cr V'^1 \cr V'^2\cr V'^3\cr}

For our particular (static) vector this yields:

.. math::

     \nabla_0 \mat{1\cr y'\omega + \cos\omega t' \cr -x'\omega - \sin\omega t'\cr 0\cr} = \mat{0\cr 0\cr 0\cr 0\cr}

as expected, because it was at rest in the $x^\mu$ system.
Let's imagine a static vector in the $x'^\mu$ system along the $x'$ axis, i.e.

.. math::

    W'^\mu = \mat{1\cr 1\cr 0\cr 0\cr}


.. math::

    W^\mu = {\partial x^\mu\over\partial x'^\alpha}W'^\alpha= \mat{1\cr -x'\omega\sin\omega t'-y'\omega\cos\omega t'+\cos\omega t'\cr x'\omega\cos\omega t'-y'\omega\sin\omega t'+\sin\omega t'\cr 0\cr} = \mat{1\cr -y\omega+\cos\omega t\cr x\omega+\sin\omega t\cr 0\cr}

then

.. math::

     \nabla_0W'^\mu= \nabla_0 \mat{1\cr 1\cr 0\cr 0\cr} = \mat{0\cr -x'\omega^2\cr -y'\omega^2+\omega\cr 0\cr}


.. math::

     \nabla_0W^\mu= \partial_0 \mat{1\cr -y\omega+\cos\omega t\cr x\omega+\sin\omega t\cr 0\cr} = \mat{0\cr -\omega\sin\omega t\cr \omega\cos\omega t\cr 0\cr} = \mat{ 0 & 0 & 0 & 0\cr 0 & 0 & -\omega & 0\cr 0 & \omega & 0 & 0\cr 0 & 0 & 0 & 0\cr } \mat{0\cr \cos\omega t\cr \sin\omega t\cr 0\cr} = \boldsymbol\omega\times{\bf W}

Similarly

.. math::

     \nabla_0\nabla_0W'^\mu= = \mat{0\cr -y'\omega^3-\omega^2\cr -x'\omega^3\cr 0\cr}


.. math::

     \nabla_0\nabla_0W^\mu= = \mat{0\cr -\omega^2\cos\omega t\cr -\omega^2\sin\omega t\cr 0\cr}


How can one prove the relation:

.. math::
    :label: vrot

    {\d{\bf A}\over\d t} = \boldsymbol\omega \times {\bf A} + {\d'{\bf A}\over\d t}

that is used for example to derive the Coriolis acceleration etc.?
We need to write it components to understand what it really means:

.. math::

     \nabla_0 \mat{A'^0\cr A'^1\cr A'^2\cr A'^3\cr} = \mat{ 0 & 0 & 0 & 0\cr 0 & 0 & -\omega & 0\cr 0 & \omega & 0 & 0\cr 0 & 0 & 0 & 0\cr } \mat{A'^0\cr A'^1\cr A'^2\cr A'^3\cr} + \partial_0 \mat{A'^0\cr A'^1\cr A'^2\cr A'^3\cr}

Comparing to the covariant derivative above, it's clear that they are equal
(provided that $x'=0$ and $y'=0$, i.e. we are at the center of rotation).


Let's show the derivation by Goldstein. The change in a time $dt$ of a
general vector ${\bf G}$ as seen by an observer in the body system of axes will
differ from the corresponding change as seen by an observer in the space
system:

.. math::

    (d{\bf G})_{\rm space} = (d{\bf G})_{\rm body}+(d{\bf G})_{\rm rot}

Now consider a vector fixed in the rigid body. Then $(d{\bf G})_{\rm body}=0$
and

.. math::

    (d{\bf G})_{\rm rot} = (d{\bf G})_{\rm space} = d\boldsymbol\Omega \times {\bf G}

For an arbitrary vector, the change relative to the space axes is the sum of
the two effects:

.. math::

    (d{\bf G})_{\rm space} = (d{\bf G})_{\rm body}+d\boldsymbol\Omega \times {\bf G}

A more rigorous derivation of the last equation follows from:

.. math::

    G_i = a_{ji}G'_j


.. math::

    dG_i = a_{ji}dG'_j + da_{ji}G'_j

Let's make the space and body instantaneously coincident at time t, then
$a_{ji} = \delta_{ji}$ and
$da_{ji}=-\epsilon_{ijk}d\Omega_k=\epsilon_{ikj}d\Omega_k$, so
we get the same equation as earlier:

.. math::

    dG_i = dG'_i + \epsilon_{ikj}d\Omega_kG'_j

Anyhow, introducing $\boldsymbol\omega$ by:

.. math::

    \boldsymbol\omega = {d\boldsymbol\Omega\over dt}

we get

.. math::

     \left({d{\bf G}\over dt}\right)_{\rm space} = \left({d{\bf G}\over dt}\right)_{\rm body} + \boldsymbol\omega \times {\bf G}

