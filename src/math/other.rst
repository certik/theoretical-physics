Delta Function
--------------


Delta function $\delta(x)$ is defined such that this relation holds:

.. math::
    :label: deltadef

       \int f(x)\delta(x-t)\d x=f(t)

No such function exists, but one can find many sequences "converging" to a delta function:

.. math::
    :label: deltalim

       \lim_{\alpha\to\infty}\delta_\alpha(x) = \delta(x)

more precisely:

.. math::
    :label: deltaprec

       \lim_{\alpha\to\infty}\int f(x)\delta_\alpha(x)\d x = \int f(x)\lim_{\alpha\to\infty}\delta_\alpha(x)\d x = f(0)

one example of such a sequence is:

.. math::

       \delta_\alpha(x) = {1\over\pi x}\sin(\alpha x)

It's clear that :eq:`deltaprec` holds for any well behaved function $f(x)$.
Some mathematicians like to say that it's incorrect to use such a notation when
in fact the integral :eq:`deltadef` doesn't "exist", but we will not follow
their approach, because it is not important if something "exists" or not,
but rather if it is clear what we mean by our notation: :eq:`deltadef` is a
shorthand for :eq:`deltaprec` and :eq:`deltalim` gets a mathematically rigorous
meaning when you integrate both sides and use :eq:`deltadef` to arrive at
:eq:`deltaprec`.  Thus one uses the relations :eq:`deltadef`, :eq:`deltalim`,
:eq:`deltaprec` to derive all properties of the delta function.

Let's give an example. Let ${\bf\hat r}$ be the unit vector in 3D and we can label it using spherical coordinates ${\bf\hat r}={\bf\hat r}(\theta,\phi)$. We can also express it in cartesian coordinates as ${\bf\hat r}(\theta,\phi)=(\cos\phi\sin\theta,\sin\phi\sin\theta,\cos\theta)$.



.. math::
    :label: deltar

       f({\bf\hat r'})=\int\delta({\bf\hat r}-{\bf\hat r'})f({\bf\hat r})\,\d {\bf\hat r}

Expressing $f({\bf\hat r})=f(\theta,\phi)$ as a function of $\theta$ and $\phi$ we have

.. math::
    :label: deltaangles

       f(\theta',\phi')=\int\delta(\theta-\theta')\delta(\phi-\phi') f(\theta,\phi)\,\d\theta\d\phi

Expressing :eq:`deltar` in spherical coordinates we get

.. math::

       f(\theta',\phi')=\int\delta({\bf\hat r}-{\bf\hat r'}) f(\theta,\phi)\sin\theta\,\d\theta\d\phi

and comparing to :eq:`deltaangles` we finally get

.. math::

       \delta({\bf\hat r}-{\bf\hat r'})={1\over\sin\theta} \delta(\theta-\theta')\delta(\phi-\phi')

In exactly the same manner we get

.. math::

       \delta({\bf r}-{\bf r'})=\delta({\bf\hat r}-{\bf\hat r'}) {\delta(\rho-\rho')\over\rho^2}

See also :eq:`functionalderdel` for an example of how to deal with more complex expressions involving the delta function like $\delta^2(x)$.

When integrating over finite interval, this formula is very useful:

.. math::

    \int_a^b f(x)\delta(x-t)\d x = f(t) \theta(b-t) \theta(t-a)

in other words, the integral vanishes unless $a < t < b$. In the limit $a\to
-\infty$ and $b\to\infty$ we get:

.. math::

    \theta(b-t) \to \theta(\infty - t) = 1

    \theta(t-a) \to \theta(t - (-\infty)) = \theta(t+\infty) = 1

Distributions
-------------

Some mathematicians like to use distributions and a mathematical notation for
that, which I think is making things less clear, but nevertheless it's
important to understand it too, so the notation is explained in this section,
but I discourage to use it -- I suggest to only use the physical notation as
explained below. The math notation below is put into quotation marks, so that
it's not confused with the physical notation.

The distribution is a functional and each function $f(x)$ can be identified
with a distribution $\mathnot{T_f}$ that it generates using this definition ($\varphi(x)$
is a test function):

.. math::

    \mathnot{T_f(\phi(x))} \equiv \int f(x)\varphi(x) \d x \equiv
    \mathnot{f(\varphi(x))} \equiv \mathnot{(f(x), \varphi(x))}

besides that, one can also define distributions that can't be identified with
regular functions, one example is a delta distribution (Dirac delta function):

.. math::

    \mathnot{\delta(\phi(x))} \equiv \phi(0) \equiv \int \delta(x) \phi(x) \d x

The last integral is not used in mathematics, in physics on the other hand, the
first expressions ($\mathnot{\delta(\phi(x))}$) is not used, so $\delta(x)$ always means
that you have to integrate it, as explained in the previous section, so it
behaves like a regular function (except that such a function doesn't exist and
the precise mathematical meaning is only after you integrate it, or through the
identification above with distributions).

One then defines common operations via acting on the generating function, then
observes the pattern and defines it for all distributions. For example
differentiation:

.. math::

    \mathnot{{\d\over\d x}T_f(\varphi)} =
    \mathnot{T_{f'}(\varphi)} =
    \int f'\varphi \d x =
    -\int f\varphi' \d x =
    \mathnot{-T_f(\varphi')}

so:

.. math::

    \mathnot{{\d\over\d x}T(\varphi)} =
    \mathnot{-T(\varphi')}


Multiplication:

.. math::

    \mathnot{gT_f(\varphi)} =
    \mathnot{T_{gf}(\varphi)} =
    \int gf\varphi \d x =
    \mathnot{T_f(g\varphi)}

so:

.. math::

    \mathnot{gT(\varphi)} =
    \mathnot{T(g\varphi)}

Fourier transform:

.. math::

    \mathnot{FT_f(\varphi)} =
    \mathnot{T_{Ff}(\varphi)} =
    \int F(f)\varphi \d x =

    =\int\left[\int e^{-ikx} f(k) \d k\right] \varphi(x) \d x
    =\int f(k)\left[\int e^{-ikx} \varphi(x) \d x\right] \d k
    =\int f(x)\left[\int e^{-ikx} \varphi(k) \d k\right] \d x
    =

    =
    \int f F(\varphi) \d x =
    \mathnot{T_f(F\varphi)}

so:

.. math::

    \mathnot{FT(\varphi)} =
    \mathnot{T(F\varphi)}

But as you can see, the notation is just making things more complex, since it's
enough to just work with the integrals and forget about the rest. One can then
even omit the integrals, with the understanding that they are implicit.

Some more examples:

.. math::

    \int \delta(x-x_0)\varphi(x) \d x = \int \delta(x)\varphi(x+x_0) \d x
    = \varphi(x_0) \equiv \mathnot{\delta(\varphi(x+x_0))}

Proof of $\delta(-x) = \delta(x)$:

.. math::

    \int_{-\infty}^\infty \delta(-x)\varphi(x)\d x =
    -\int_{\infty}^{-\infty} \delta(y)\varphi(-y)\d y =
    \int_{-\infty}^\infty \delta(x)\varphi(-x)\d x
    \equiv \mathnot{\delta(\varphi(-x))} = \varphi(0)
    =\mathnot{\delta(\phi(x))}
    \equiv
    \int_{-\infty}^\infty \delta(x)\varphi(x)\d x

Proof of $x\delta(x) = 0$:

.. math::

    \int x\delta(x)\varphi(x)\d x = \mathnot{\delta(x\varphi(x))}
    = 0 \cdot \varphi(0) = 0

Proof of $\delta(cx) = {\delta(x)\over |c|}$:

.. math::

    \int \delta(cx)\varphi(x)\d x = {1\over|c|}\int\delta(x)\varphi\left({x\over
    c}\right)\d x
    =\mathnot{\delta\left(\varphi\left({x\over c}\right)\over|c|\right)}
    ={\delta(0)\over|c|}
    =\mathnot{{\delta(\varphi(x))\over|c|}}
    =
    \int {\delta(x)\over |c|}\varphi(x)\d x


.. index:: variation, functional derivative

Variations and Functional Derivatives
-------------------------------------


Functional derivatives are a common source of confusion and especially the
notation. The reason is similar to the delta function --- the definition is
operational, i.e. it tells you what operations you need to do to get a
mathematically precise formula. The notation below is commonly used in physics
and in our opinion it is perfectly precise and exact, but some mathematicians
may not like it.

Let's have $\x=(x_1,x_2,\dots,x_N)$. The function $f(\x)$ assigns a number to each $\x$. We define a differential of $f$ as

.. math::

       \d f\equiv \left.{\d\over\d\varepsilon}f(\x+\varepsilon\h) \right|_{\varepsilon=0} =\lim_{\varepsilon\to0} {f(\x+\varepsilon\h)-f(\x)\over\varepsilon}=\a\cdot\h

The last equality follows from the fact, that $\left.{\d\over\d\varepsilon}f(\x+\varepsilon\h) \right|_{\varepsilon=0}$ is a linear function of $\h$. We define ${\partial f\over\partial x_i}$ as

.. math::

       \a\equiv\left({\partial f\over\partial x_1},{\partial f\over\partial x_2}, \dots,{\partial f\over\partial x_N}\right)

This also gives a formula for computing ${\partial f\over\partial x_i}$: we set $h_j=\delta_{ij}h_i$ and

.. math::

       {\partial f\over\partial x_i}=a_i=\a\cdot\h=\left.{\d\over\d\varepsilon} f(\x+\varepsilon(0,0,\dots,1,\dots,0))\right|_{\varepsilon=0}=


.. math::

       =\lim_{\varepsilon\to0} {f(x_1,x_2,\dots,x_i+\varepsilon,\dots,x_N)-f(x_1,x_2,\dots,x_i,\dots,x_N) \over\varepsilon}

But this is just the way the partial derivative is usually defined. Every variable can be treated as a function (very simple one):

.. math::

       x_i=g(x_1,\dots,x_N)=\delta_{ij}x_j

and so we define

.. math::

       \d x_i\equiv\d g=\d(\delta_{ij}x_j)=h_i

and thus we write $h_i=\d x_i$ and $\h=\d\x$ and

.. math::

       \d f={\d f\over\d x_i}\d x_i

So $\d\x$ has two meanings --- it's either $\h=\x-\x_0$ (a finite change in the independent variable $\x$) or a differential, depending on the context. Even mathematicians use this notation.

Functional $F[f]$ assigns a number to each function $f(x)$. The variation is defined as

.. math::

       \delta F[f]\equiv\left.{\d\over\d\varepsilon}F[f+\varepsilon h] \right|_{\varepsilon=0}=\lim_{\epsilon\to0}{F[f+\epsilon h]-F[f]\over\epsilon}= \int a(x)h(x)\d x

We define ${\delta F\over\delta f(x)}$ as

.. math::

       a(x)\equiv{\delta F\over\delta f(x)}

This also gives a formula for computing ${\delta F\over\delta f(x)}$: we set $h(y)=\delta(x-y)$ and

.. math::

       {\delta F\over\delta f(x)}=a(x)=\int a(y)\delta(x-y)\d y= \left.{\d\over\d\varepsilon}F[f(y)+\varepsilon\delta(x-y)] \right|_{\varepsilon=0}=


.. math::

       =\lim_{\varepsilon\to0} {F[f(y)+\varepsilon\delta(x-y)]-F[f(y)]\over\varepsilon}

Every function can be treated as a functional (although a very simple one):

.. math::

       f(x)=G[f]=\int f(y)\delta(x-y)\d y

and so we define

.. math::

       \delta f\equiv\delta G[f]= \left.{\d\over\d\varepsilon}G[f(x)+\varepsilon h(x)] \right|_{\varepsilon=0}= \left.{\d\over\d\varepsilon}(f(x)+\varepsilon h(x)) \right|_{\varepsilon=0}= h(x)

thus we write $h=\delta f$ and

.. math::

       \delta F[f]=\int {\delta F\over\delta f(x)}\delta f(x)\d x

so $\delta f$ have two meanings --- it's either
$h(x)=\left.{\d\over\d\varepsilon}(f(x)+\varepsilon h(x))
\right|_{\varepsilon=0}$ (a finite change in the function $f$) or a variation
of a functional, depending on the context. Some mathematicians don't like to
write $\delta f$ in the meaning of $h(x)$, they prefer to write the latter, but
it is in fact perfectly fine to use $\delta f$, because it is completely analogous to $\d\x$.


The correspondence between the finite and infinite dimensional case can be summarized as:

.. math::
    :nowrap:

    \begin{eqnarray*} f(x_i) \quad&\Longleftrightarrow&\quad F[f] \\ \d f=0 \quad&\Longleftrightarrow&\quad \delta F=0 \\ {\partial f\over\partial x_i}=0 \quad&\Longleftrightarrow&\quad {\delta F\over\delta f(x)}=0 \\ f \quad&\Longleftrightarrow&\quad F \\ x_i \quad&\Longleftrightarrow&\quad f(x) \\ x \quad&\Longleftrightarrow&\quad f \\ i \quad&\Longleftrightarrow&\quad x \\ \end{eqnarray*}


More generally, $\delta$-variation can by applied to any function $g$ which contains the function $f(x)$ being varied, you just need to replace $f$ by $f+\epsilon h$ and apply ${\d\over\d\epsilon}$ to the whole $g$, for example (here $g=\partial_\mu\phi$ and $f=\phi$):

.. math::

    \delta\partial_\mu\phi
        = \left.{\d\over\d\varepsilon}\partial_\mu(\phi+\varepsilon h) \right|_{\varepsilon=0}
        = \partial_\mu\left.{\d\over\d\varepsilon}(\phi+\varepsilon h) \right|_{\varepsilon=0}
        =\partial_\mu h
        =\partial_\mu \delta\phi


This notation allows us a very convinient computation, as shown in the following examples. First, when computing a variation of some integral, when can interchange $\delta$ and $\int$:

.. math::

       F[f]=\int K(x) f(x) \d x


.. math::

       \delta F=\delta \int K(x) f(x) \d x = \left.{\d\over\d\varepsilon}\int K(x) (f+\varepsilon h)\d x\right|_{\varepsilon=0}= \left.\int{\d\over\d\varepsilon} (K(x) (f+\varepsilon h))\d x\right|_{\varepsilon=0}=


.. math::

       =\int\delta(K(x) f(x))\d x

In the expression $\delta(K(x) f(x))$ we must understand from the context if we are treating it as a functional of $f$ or $K$. In our case it's a functional of $f$, so we have $\delta(K f)=K\delta f$.

A few more examples:

.. math::

       {\delta\over\delta f(t)}\int\d t'f(t')g(t')= \left.{\d\over\d\varepsilon}\int\d t'(f(t')+\varepsilon\delta(t-t'))g(t') \right|_{\varepsilon=0}=g(t)


.. math::

       {\delta f(t')\over\delta f(t)}= \left.{\d\over\d\varepsilon}(f(t')+\varepsilon\delta(t-t')) \right|_{\varepsilon=0}=\delta(t-t')


.. math::

       {\delta f(t_1)f(t_2)\over\delta f(t)}= \left.{\d\over\d\varepsilon}(f(t_1)+\varepsilon\delta(t-t_1)) (f(t_2)+\varepsilon\delta(t-t_2)) \right|_{\varepsilon=0}=\delta(t-t_1)f(t_2)+f(t_1)\delta(t-t_2)


.. math::

       {\delta\over\delta f(t)}\half\int\d t_1\d t_2K(t_1,t_2)f(t_1)f(t_2)= \half\int\d t_1\d t_2K(t_1,t_2){\delta f(t_1)f(t_2)\over\delta f(t)}=


.. math::

       =\half\left(\int\d t_1 K(t_1,t)f(t_1)+\int\d t_2 K(t,t_2)f(t_2)\right) =\int\d t_2 K(t,t_2)f(t_2)

The last equality follows from $K(t_1,t_2)=K(t_2,t_1)$ (any antisymmetrical part of a $K$ would not contribute to the symmetrical integration).

Another example is the derivation of Euler-Lagrange equations for the
Lagrangian density $\L=\L(\eta_\rho, \partial_\nu \eta_\rho, x^\nu)$:

.. math::

    0 = \delta I = \delta \int \L \,\d^4x^\mu
    = \int \delta \L \,\d^4x^\mu
    = \int { \partial \L\over\partial \eta_\rho}\delta\eta_\rho
        +
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \delta(\partial_\nu\eta_\rho)
        \,\d^4x^\mu
    =

    = \int { \partial \L\over\partial \eta_\rho}\delta\eta_\rho
        +
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \partial_\nu(\delta\eta_\rho)
        \,\d^4x^\mu
    =

    = \int { \partial \L\over\partial \eta_\rho}\delta\eta_\rho
        -
        \partial_\nu\left(
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \right)
        \delta\eta_\rho
        \,\d^4x^\mu
        +\int \partial_\nu \left(
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \delta\eta_\rho
        \right)
        \,\d^4x^\mu
    =

    = \int \left[{ \partial \L\over\partial \eta_\rho}
        -
        \partial_\nu\left(
        { \partial \L\over\partial (\partial_\nu \eta_\rho)}
        \right)
        \right]
        \delta\eta_\rho
        \,\d^4x^\mu

Another example:

.. math::

       {\delta\over\delta f(t)}\int f^3(x)\d x= \left.{\d\over\d\varepsilon}\int(f(x)+\varepsilon\delta(x-t))^3\d x \right|_{\varepsilon=0}=


.. math::

       =\left.\int3(f(x)+\varepsilon\delta(x-t))^2\delta(x-t)\d x \right|_{\varepsilon=0}=\int3f^2(x)\delta(x-t)\d x=3f^2(t)

Some mathematicians would say the above calculation is incorrect, because
$\delta^2(x-t)$ is undefined. But that's not exactly true, because in case of
such problems the above notation automatically implies working with some
sequence $\delta_\alpha(x) \to \delta(x)$ (for example $\delta_\alpha(x) =
{1\over\pi x}\sin(\alpha x)$) and taking the limit $\alpha\to\infty$:

.. math::

       {\delta\over\delta f(t)}\int f^3(x)\d x= \left.\lim_{\alpha\to\infty}{\d\over\d\varepsilon}\int(f(x)+\varepsilon\delta_\alpha(x-t))^3\d x \right|_{\varepsilon=0}=


.. math::

       =\left.\lim_{\alpha\to\infty}\int3(f(x)+\varepsilon\delta_\alpha(x-t))^2\delta_\alpha(x-t)\d x \right|_{\varepsilon=0}=\lim_{\alpha\to\infty}\int3f^2(x)\delta_\alpha(x-t)\d x=


.. math::
    :label: functionalderdel

       =\int3f^2(x)\lim_{\alpha\to\infty}\delta_\alpha(x-t)\d x= \int3f^2(x)\delta(x-t)\d x=3f^2(t)

As you can see, we got the same result, with the same rigor, but using an obfuscating notation. That's why such obvious manipulations with $\delta_\alpha$ are tacitly implied.

Another example with a metric as a function of coordinates
$g_{\mu\nu} = g_{\mu\nu}(x^\mu)$:

.. math::

    \delta g_{\mu\nu}
        = \delta g_{\mu\nu}(x^\mu)
        = \left.{\d\over\d\varepsilon} g_{\mu\nu}(x^\mu+\varepsilon
                (\delta x^\mu)) \right|_{\varepsilon=0}
        = \left.{\d\over\d\varepsilon}
                (x^\sigma+\varepsilon(\delta x^\sigma)) \right|_{\varepsilon=0}
            \partial_\sigma g_{\mu\nu}
        = (\delta x^\sigma) \partial_\sigma g_{\mu\nu}

And an example of varying with respect to a metric:

.. math::

    \delta \sqrt{ |\det g_{\mu\nu}| }
        =\sqrt{ |\det g_{\mu\nu}| }\, \delta \log \sqrt{ |\det g_{\mu\nu}| }
        =\half \sqrt{ |\det g_{\mu\nu}| }\, \delta \log |\det g_{\mu\nu}| =

        =\half \sqrt{ |\det g_{\mu\nu}| }\, \delta \Tr \log g_{\mu\nu}
        =\half \sqrt{ |\det g_{\mu\nu}| }\, \Tr \delta \log g_{\mu\nu} =

        =\half \sqrt{ |\det g_{\mu\nu}| }\, \Tr g^{\mu\nu} \delta g_{\mu\nu}
        =\half \sqrt{ |\det g_{\mu\nu}| }\, g^{\mu\nu} \delta g_{\mu\nu} =

        =-\half \sqrt{ |\det g_{\mu\nu}| }\, g_{\mu\nu} \delta g^{\mu\nu}

.. index:: dirac notation

Dirac Notation
--------------


The Dirac notation allows a very compact and powerful way of writing equations that describe a function expansion into a basis, both discrete (e.g. a fourier series expansion) and continuous (e.g. a fourier transform) and related things. The notation is designed so that it is very easy to remember and it just guides you to write the correct equation.

Let's have a function $f(x)$. We define

.. math::
    :nowrap:

    \begin{eqnarray*} \braket{x|f}&\equiv& f(x) \\ \braket{x'|f}&\equiv& f(x') \\ \braket{x'|x}&\equiv&\delta(x'-x) \\ \int\ket{x}\bra{x}\d x&\equiv&\one \\ \end{eqnarray*}

The following equation

.. math::

       f(x')=\int\delta(x'-x)f(x)\d x

then becomes

.. math::

       \braket{x'|f}=\int\braket{x'|x}\braket{x|f}\d x

and thus we can interpret $\ket{f}$ as a vector, $\ket{x}$ as a basis and $\braket{x|f}$ as the coefficients in the basis expansion:

.. math::

       \ket{f}=\one\ket{f}=\int\ket{x}\bra{x}\d x\ket{f}= \int\ket{x}\braket{x|f}\d x

That's all there is to it. Take the above rules as the operational definition
of the Dirac notation. It's like with the delta function - written alone it
doesn't have any meaning, but there are clear and non-ambiguous rules to
convert any expression with $\delta$ to an expression which even mathematicians
understand (i.e. integrating, applying test functions and using other relations
to get rid of all $\delta$ symbols in the expression -- but the result is
usually much more complicated than the original formula). It's the same with
the ket $\ket{f}$: written alone it doesn't have any meaning, but you can
always use the above rules to get an expression that make sense to everyone
(i.e. attaching any bra to the left and rewriting all brackets $\braket{a|b}$
with their equivalent expressions) -- but it will be more complex and harder to
remember and -- that is important -- less general.

Now, let's look at the spherical harmonics:

.. math::

       Y_{lm}({\bf\hat r})\equiv\braket{{\bf\hat r}|lm}

on the unit sphere, we have

.. math::

       \int\ket{\bf\hat r}\bra{\bf\hat r}\d{\bf\hat r}= \int\ket{\bf\hat r}\bra{\bf\hat r}\d\Omega=\one


.. math::

       \delta({\bf\hat r}-{\bf\hat r'})=\braket{{\bf\hat r}|{\bf\hat r'}}

thus

.. math::

       \int_0^{2\pi}\int_0^{\pi} Y_{lm}(\theta,\phi)\,Y^*_{l'm'}(\theta,\phi)\sin\theta\,\d\theta\,\d\phi = \int\braket{l'm'|{\bf\hat r}}\braket{{\bf\hat r}|lm}\d\Omega= \braket{l'm'|lm}

and from :eq:`Yorto` we get

.. math::

       \braket{l'm'|lm}=\delta_{mm'}\delta_{ll'}

now

.. math::

       \sum_{lm}Y_{lm}(\theta,\phi)Y_{lm}^*(\theta',\phi')= \sum_{lm}\braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r'}}

from :eq:`Ycomplete` we get

.. math::

       \sum_{lm}\braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r'}}= \braket{{\bf\hat r}|{\bf\hat r'}}

so we have

.. math::

       \sum_{lm}\ket{lm}\bra{lm}=\one

so $\ket{lm}$ forms an orthonormal basis. Any function defined on the sphere $f({\bf\hat r})$ can be written using this basis:

.. math::

       f({\bf\hat r}) =\braket{{\bf\hat r}|f} =\sum_{lm}\braket{{\bf\hat r}|lm}\braket{lm|f} =\sum_{lm}Y_{lm}({\bf\hat r})f_{lm}

where

.. math::

       f_{lm}=\braket{lm|f}=\int\braket{lm|{\bf\hat r}}\braket{{\bf\hat r}|f}\d\Omega =\int Y_{lm}^*({\bf\hat r}) f({\bf\hat r})\d\Omega

If we have a function $f({\bf r})$ in 3D, we can write it as a function of $\rho$ and ${\bf\hat r}$ and expand only with respect to the variable ${\bf\hat r}$:

.. math::

       f({\bf r})=f(\rho{\bf\hat r})\equiv g(\rho,{\bf\hat r})= \sum_{lm}Y_{lm}({\bf\hat r})g_{lm}(\rho)

In Dirac notation we are doing the following: we decompose the space into the angular and radial part

.. math::

       \ket{{\bf r}}=\ket{{\bf\hat r}}\otimes\ket{\rho} \equiv\ket{{\bf\hat r}}\ket{\rho}

and write

.. math::

       f({\bf r})=\braket{{\bf r}|f}=\bra{{\bf\hat r}}\braket{\rho|f}= \sum_{lm}Y_{lm}({\bf\hat r})\bra{lm}\braket{\rho|f}

where

.. math::

       \bra{lm}\braket{\rho|f}= \int\braket{lm|{\bf\hat r}}\bra{{\bf\hat r}}\braket{\rho|f}\d\Omega =\int Y_{lm}^*({\bf\hat r}) f({\bf r})\d\Omega

Let's calculate $\braket{\rho|\rho'}$

.. math::

       \braket{{\bf r}|{\bf r'}}=\bra{\bf\hat r}\braket{\rho|\rho'}\ket{{\bf\hat r'}} =\braket{{\bf\hat r}|{\bf\hat r'}}\braket{\rho|\rho'}

so

.. math::

       \braket{\rho|\rho'} ={\braket{{\bf r}|{\bf r'}}\over\braket{{\bf\hat r}|{\bf\hat r'}}} ={\delta(\rho-\rho')\over\rho^2}

We must stress that $\ket{lm}$ only acts in the $\ket{{\bf\hat r}}$ space (not the $\ket\rho$ space) which means that

.. math::

       \braket{{\bf r}|lm} =\bra{\bf\hat r}\braket{\rho|lm} =\braket{{\bf\hat r}|lm}\bra{\rho} =Y_{lm}({\bf\hat r})\bra{\rho}

and $V\ket{lm}$ leaves $V\ket\rho$ intact. Similarly,

.. math::

       \sum_{lm} \ket{lm}\bra{lm}=\one

is a unity in the $\ket{\bf\hat r}$ space only (i.e. on the unit sphere).

Let's rewrite the equation :eq:`lsum`:

.. math::

       \sum_m\braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r'}}= {4\pi\over 2l+1} \braket{{\bf\hat r}\cdot{\bf\hat r'}|P_l}

Using the completeness relation :eq:`Lorto`:

.. math::

       \sum_l {2l+1\over2}\braket{x'|P_l}\braket{P_l|x}=\braket{x'|x}


.. math::

       \sum_l \ket{P_l}{2l+1\over2}\bra{P_l}=\one

we can now derive a very important formula true for every function $f({\bf\hat r}\cdot{\bf\hat r'})$:



.. math::

       f({\bf\hat r}\cdot{\bf\hat r'})=\braket{{\bf\hat r}\cdot{\bf\hat r'}|f}= \sum_l \braket{{\bf\hat r}\cdot{\bf\hat r'}|P_l}{2l+1\over2}\braket{P_l|f}= \sum_{lm}\braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r'}}{(2l+1)^2\over8\pi} \braket{P_l|f}=


.. math::

       =\sum_{lm}\braket{{\bf\hat r}|lm}f_l \braket{lm|{\bf\hat r'}}

where

.. math::

       f_l={(2l+1)^2\over8\pi}\braket{P_l|f} ={(2l+1)^2\over8\pi}\int_{-1}^1 \braket{P_l|x}\braket{x|f}\d x ={(2l+1)^2\over8\pi}\int_{-1}^1 P_l(x)f(x)\d x

or written explicitly

.. math::
    :label: fylm

       f({\bf\hat r}\cdot{\bf\hat r'})= \sum_{l=0}^\infty\sum_{m=-l}^l Y_{lm}({\bf\hat r}) f_l Y_{lm}^*({\bf\hat r'})

.. index:: homogeneous functions

Homogeneous functions
---------------------

A function of several variables $f(x_1, x_2, \dots) \equiv f(x_i)$ is
homogeneous of degree $k$ if

.. math::

    f(\lambda x_i) = \lambda^k f(x_i)

By differentiating with respect to $\lambda$:

.. math::

    x_i {\partial f(\lambda x_i)\over\partial x_i} = k\lambda^{k-1} f(x_i)

and setting $\lambda=1$ we get the so called Euler equation:

.. math::

    x_i {\partial f(x_i)\over\partial x_i} = k f(x_i)

in 3D this can also be written as:

.. math::

    {\bf x} \cdot \nabla f({\bf x}) = k f({\bf x})

Example 1
~~~~~~~~~

The function $f(x, y, z) = {xy\over z}$ is homogeneous of degree 1, because:

.. math::

    f(\lambda x, \lambda y, \lambda z) = {\lambda x\lambda y\over \lambda z}
    = \lambda {xy\over z}
    = \lambda f(x, y, z)

and the Euler equation is:

.. math::

    x{\partial f\over\partial x} +
    y{\partial f\over\partial y} +
    z{\partial f\over\partial z}
    =
    f

or

.. math::

    x{y\over z} +
    y{x\over z} +
    z\left(-{xy\over z^2}\right)
    ={xy\over z}

Which is true.

Example 2
~~~~~~~~~

The function $V(r) = -{Z \over r}$ is homogeneous of degree -1, because:

.. math::

    V(\lambda r) = -{Z\over \lambda r} = \lambda^{-1} V(r)

and the Euler equation is:

.. math::

    r{\d V\over\d r} = -V

or

.. math::

    r{Z\over r^2} = -\left(-{Z\over r}\right)

Which is true.


Green Functions
---------------

Green functions are an excellent tool for working with a solution to any ODE or
PDE. In this text we explain how it works and then show how one can calculate
them using FEM.

Introduction
~~~~~~~~~~~~

Let's put any ODE or PDE in the form:

.. math::
    :label: pde

    Lu(x)=f(x)

Here $L$ is a differential operator and $x$ can have any dimension, e.g. 1D
(ODE), 2D, 3D or more (PDE). Then we can express the solution as

.. math::
    :label: solution

    u(x) = L^{-1}f(x) = \int G(x, x')f(x')\d x'

where $G(x, x')$ is a Green function, that needs to satisfy the equation:

.. math::
    :label: green

    LG(x, x')=\delta(x-x')

Remember, that $L$ acts on $x$ only, so we can check, that :eq:`solution`
indeed solves the PDE :eq:`pde`:

.. math::

    Lu(x)
    = L\int G(x, x')f(x')\d x'
    = \int LG(x, x')f(x')\d x'
    = \int \delta(x-x')f(x')\d x'
    = f(x)

Boundary Conditions
~~~~~~~~~~~~~~~~~~~

The equation :eq:`green` doesn't determine the Green function uniquely,
because one can add to it any solution of the homogeneous equation $Lu(x)=0$.
We can use this freedom to solve :eq:`green` for any boundary condition.
So we prescribe a boundary condition
and find the Green function (by solving :eq:`green`) that satisfies the
boundary condition. It can be shown, that $u(x)$ determined from
:eq:`solution` then also needs to satisfy the same boundary condition.

Symmetry
~~~~~~~~

We write the equation for Green functions at two different points $x_1$
and $x_2$:

.. math::

    L G(x, x_1) = \delta(x-x_1)

    L G(x, x_2) = \delta(x-x_2)

and multiply the first equation by $G(x, x_2)$, second by $G(x, x_1)$:

.. math::

    G(x, x_2) L G(x, x_1) = \delta(x-x_1) G(x, x_2)

    G(x, x_1) L G(x, x_2) = \delta(x-x_2) G(x, x_1)

substract them and integrate over $x$:

.. math::

    G(x, x_2) L G(x, x_1) - G(x, x_1) L G(x, x_2)
        = \delta(x-x_1) G(x, x_2) - \delta(x-x_2) G(x, x_1)

    \int \left(G(x, x_2) L G(x, x_1) - G(x, x_1) L G(x, x_2) \right) \d x
        = \int \left(\delta(x-x_1) G(x, x_2) - \delta(x-x_2) G(x, x_1)
            \right)\d x

    \int \left(G(x, x_2) L G(x, x_1) - G(x, x_1) L G(x, x_2) \right) \d x
        = G(x_1, x_2) - G(x_2, x_1)

Assuming that the operator $L$ is Hermitean, we get:

.. math::

    \int \left((L G(x, x_2)) G(x, x_1) - G(x, x_1) L G(x, x_2) \right) \d x
        = G(x_1, x_2) - G(x_2, x_1)

    0 = G(x_1, x_2) - G(x_2, x_1)

So the Green function is symmetric for Hermitean operators $L$.

Examples
~~~~~~~~

Poisson Equation in 1D
^^^^^^^^^^^^^^^^^^^^^^

Poisson equation:

.. math::

    -{\d^2\over\d x^2} u(x) = f(x)

We calculate the Green function using the Fourier transform:

.. math::

    -{\partial^2\over\partial x^2} G(x, x') = \delta(x-x')

    -(ik)^2 \tilde G(k, x') = {e^{ikx'}\over\sqrt{2\pi}}

    \tilde G(k, x') = {e^{ikx'}\over\sqrt{2\pi}\,k^2}

    G(x, x') = -\half (x-x') \sign(x-x')
        = -\half (x-x') (2H(x-x')-1)
        = H(x-x') (x'-x) +\half(x-x')

Check:

.. math::

    {\partial\over\partial x} G(x, x')
        = \delta(x-x') (x'-x) + H(x-x') (-1) + \half
        = - H(x-x') + \half

    {\partial^2\over\partial x^2} G(x, x')
        = - \delta(x-x')

Then:

.. math::

    u(x) = \int G(x, x') f(x') \d x'
        = \int \left(H(x-x') (x'-x) +\half(x-x')\right) f(x') \d x'

The green function can also be written using $x_<=\min(x, x')$ and
$x_> = \max(x, x')$:

.. math::

    G(x, x') = H(x-x') (x'-x) +\half(x-x')
        = \half(x_< - x_>)

Radial Poisson Equation
^^^^^^^^^^^^^^^^^^^^^^^

Let's write $r_>$ and $r_<$ using the Heaviside step function:

.. math::

    r_> = \max(r, r')
        =
    \begin{cases}
    r&\quad\mbox{for $r>r'$}\cr
    r'&\quad\mbox{for $r<r'$}\cr
    \end{cases}
    = H(r-r') r + H(r'-r)r' =

    = H(r-r') r + (1-H(r-r'))r'
    = H(r-r') (r-r') + r'

and:

.. math::

    r_< = \min(r, r')
        =
    \begin{cases}
    r'&\quad\mbox{for $r>r'$}\cr
    r&\quad\mbox{for $r<r'$}\cr
    \end{cases}
    = H(r-r') r' + H(r'-r)r =

    = H(r-r') r' + (1-H(r-r'))r
    = H(r-r') (r'-r) + r

Then we can differentiate:

.. math::

    {\partial\over\partial r} r_>
        = \delta(r-r')(r-r') + H(r-r')
        = H(r-r')

    {\partial^2\over\partial r^2} r_>
        = \delta(r-r')

    {\partial\over\partial r} r_<
        = \delta(r-r')(r'-r) - H(r-r') + 1
        = 1-H(r-r') = H(r'-r)

    {\partial^2\over\partial r^2} r_<
        = -\delta(r-r')

Given:

.. math::
    :label: rad_integral_u

    u(r) = \int_0^\infty {f(r') r'^2 \over r_>} \d r'

The Green function is

.. math::

    G(r, r') = {r'^2\over r_>}

Let's differentiate:

.. math::

    {\partial\over\partial r} G(r, r') = -{r'^2\over r_>^2}
            {\partial\over\partial r} r_>
    = -{r'^2\over r_>^2} H(r-r')
    = -{r'^2\over r^2} H(r-r')

and

.. math::

    {\partial^2\over\partial r^2} G(r, r') = +{2\over r}{r'^2\over r^2}
        H(r-r') -{r'^2\over r^2} \delta(r-r')

So we get:

.. math::

    -{\partial^2\over\partial r^2} G(r, r')
        -{2\over r}{\partial\over\partial r} G(r, r')
        =-{2\over r}{r'^2\over r^2} H(r-r') +{r'^2\over r^2} \delta(r-r')
            +{2\over r}{r'^2\over r^2} H(r-r')
        ={r'^2\over r^2} \delta(r-r') = \delta(r-r')

So $u(r)$ from :eq:`rad_integral_u` is a solution to the radial Poisson
equation:

.. math::

    -{\d^2\over\d r^2} u(r) - {2\over r}{\d\over\d r}u(r) = f(r)

Helmholtz Equation in 1D
^^^^^^^^^^^^^^^^^^^^^^^^

.. math::

    \left({\d^2\over\d x^2}+1\right)u(x)=f(x)

    \left({\d^2\over\d x^2}+1\right)G(x, x')=\delta(x-x')

with boundary conditions $u(0)=u({\pi\over2})=0$.
We use the Fourier transform:

.. math::

    \left((ik)^2+1\right)\tilde G(k, x')={e^{ikx'}\over\sqrt{2\pi}}

    \tilde G(k, x')={e^{ikx'}\over \sqrt{2\pi} (1-k^2)}

    G(x, x') = \half\sign(x-x')\sin(x-x')

Check:

.. math::

    {\partial\over\partial x} G(x, x') = \delta(x-x')\sin(x-x')
        +\half\sign(x-x')\cos(x-x') =

        = \half\sign(x-x')\cos(x-x')

    {\partial^2\over\partial x^2} G(x, x') = \delta(x-x')\cos(x-x')
        -\half\sign(x-x')\sin(x-x') =

        = -\half\sign(x-x')\sin(x-x') + \delta(x-x')

    {\partial^2\over\partial x^2} G(x, x')
    +{\partial\over\partial x} G(x, x') = \delta(x-x')

The general solution of the homogeneous equation is:

.. math::

    u(x) = C_1 \sin x + C_2 \cos x

so the general Green function is:

.. math::

    G(x, x') = \half\sign(x-x')\sin(x-x') + C_1 \sin (x+x')
        + C_2 \cos (x+x')

Satisfying the boundary conditions (for all $x' \ne 0$):

.. math::

    G(0, x') = G({\pi\over 2}, x') = 0

we get:

.. math::

    C_1 & = -\half \\
    C_2 & = 0

and:

.. math::

    G(x, x') = \half\sign(x-x')\sin(x-x') -\half \sin (x+x') =

    =-H(x'-x)\sin x\cos x' - H(x - x') \cos x \sin x' =

    =
    \begin{cases}
    -\sin x\cos x'&\quad x<x'\cr
    -\cos x\sin x'&\quad x>x'\cr
    \end{cases}
    =-\sin x_< \cos x_>

and

.. math::

     u(x) = \int G(x, x')f(x')\d x'
    =-\cos x\int_0^xf(x')\sin x'\d x'
    -\sin x\int_x^{\pi\over2}f(x')\cos x'\d x'

To show that this really works, let's take for example $f(x)=3\sin2x$. Then

.. math::

    u(x)
    =-\cos x\int_0^x3\sin 2x'\sin x'\d x'
    -\sin x\int_x^{\pi\over2}3\sin 2x'\cos x'\d x'

We can use SymPy to evaluate the integrals::

    In [1]: u = -cos(x)*integrate(3*sin(2*y)*sin(y), (y, 0, x)) - \
        sin(x)*integrate(3*sin(2*y)*cos(y), (y, x, pi/2))

    In [2]: u
    Out[2]:
    -(cos(x)*sin(2*x) - 2*cos(2*x)*sin(x))*cos(x) - (sin(x)*sin(2*x)
        + 2*cos(x)*cos(2*x))*sin(x)

    In [3]: simplify(u)
    Out[3]:
         2                  2
    - cos (x)*sin(2*x) - sin (x)*sin(2*x)

    In [4]: trigsimp(_)
    Out[4]: -sin(2*x)

And we get

.. math::

    u(x)=-\sin 2x

We can easily check, that $u''+u=3\sin2x$::

    >>> u = -sin(2*x)
    >>> u.diff(x, 2) + u
    3*sin(2*x)

and since $f(x) = 3\sin2x$, we have verified, that $u(x)=-\sin 2x$ is the correct
solution.

Poisson Equation in 2D
^^^^^^^^^^^^^^^^^^^^^^

Let ${\bf x}=(x, y)$ and we want to solve:

.. math::

    \nabla^2u({\bf x})=f({\bf x})

So we have:

.. math::

    \nabla^2G({\bf x}, {\bf x'})=\delta({\bf x}-{\bf x'})

The solution is:

.. math::

    G({\bf x}, {\bf x'})
    ={1\over2\pi}\log|{\bf x}-{\bf x'}|
    ={1\over4\pi}\log|{\bf x}-{\bf x'}|^2
    ={1\over4\pi}\log((x-x')^2+(y-y')^2)

Poisson Equation in 3D
^^^^^^^^^^^^^^^^^^^^^^

.. math::

    \nabla^2u(x)=f(x)

    \nabla^2G(x, x')=\delta(x-x')

with boundary condition $G(x) = 0$ at infinity. Then:

.. math::

    G(x, x')=-{1\over4\pi}{1\over|x-x'| }

and

.. math::

    u(x) = -{1\over4\pi}\int {f(x')\over|x-x'| }\d x'

Helmholtz Equation in 3D
^^^^^^^^^^^^^^^^^^^^^^^^

.. math::

    (\nabla^2+k^2)u(x)=f(x)

    (\nabla^2+k^2)G(x, x')=\delta(x-x')

with boundary condition $G(x) = 0$ at infinity. Then:

.. math::

    G(x, x')=-{1\over4\pi}{e^{ik|x-x'| }\over|x-x'| }

    u(x) = -{1\over4\pi}\int {f(x')e^{ik|x-x'| }\over|x-x'| }\d x'


Finite Element Method
^^^^^^^^^^^^^^^^^^^^^

Let's show it on the Laplace equation. We want to solve:

.. math::

    \nabla^2G(x, x')=\delta(x-x')

We will treat $x'$ as a parameter, so we define $g_{x'}(x)\equiv G(x, x')$:

.. math::

    \nabla^2g_{x'}(x)=\delta(x-x')

We set $g_{x'}(x)=0$ on the boundary and we get:

.. math::

    -\int\nabla g_{x'}(x) \cdot \nabla v(x) \d x = \int v(x)\delta(x-x')\d x

    -\int\nabla g_{x'}(x) \cdot \nabla v(x) \d x = v(x')

So we choose $x'$ and then solve for $g_{x'}(x)$ using FEM and we get the
Green function $G(x, x')$ for all $x$ and one particular $x'$. We can then
evaluate the integral :eq:`solution` numerically -- one would have to use FEM
for all $x'$ that are needed in the integral, so that is not efficient, but it
should work. One will then be able to play with Green functions and be able to
calculate them numerically for any boundary condition (which is not possible
analytically).



Binomial Coefficients
---------------------

For $n$ and $k$ integers, the binomial coefficients are defined by:

.. math::

    \binom{n}{k} = {n!\over k! (n-k)!} =
        {n (n-1) \cdots (n-k+1)\over k!}

For $r$ real, one just uses the second formula as a definition:

.. math::

    \binom{r}{k} = {r (r-1) \cdots (r-k+1)\over k!}

Example:

.. math::

    \binom{-n}{k}
        = {(-n) (-n-1) \cdots (-n-k+1)\over k!}
        = (-1)^{k} {n (n+1) \cdots (n+k-1)\over k!}
        = (-1)^{k}\binom{n+k-1}{k}

The binomial formula is for $n$ integer:

.. math::

    (x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}

and for $r$ real and $|x| < |y|$ this can be generalized to:

.. math::

    (x+y)^r = \sum_{k=0}^\infty \binom{r}{k} x^k y^{r-k}

Example: (for $|x| < 1$)

.. math::

    (1 + x)^{-n} = \sum_{k=0}^\infty \binom{-n}{k} x^k
        = \sum_{k=0}^\infty (-1)^k\binom{n+k-1}{k} x^k
        = \sum_{k=0}^\infty \binom{n+k-1}{k} (-x)^k

so:

.. math::

    (1 - x)^{-n} = \sum_{k=0}^\infty \binom{n+k-1}{k} x^k

    (1 - x)^{-1} = \sum_{k=0}^\infty \binom{1+k-1}{k} x^k
        = \sum_{k=0}^\infty \binom{k}{k} x^k
        = \sum_{k=0}^\infty x^k

Triangle Inequality
-------------------

Triangle inequality (condition) means that none of the three
quantities $a$, $b$, $c$ is greater than the sum of the other two:

.. math::
    :label: trig_three

    a + b \ge c

    b + c \ge a

    c + a \ge b

This is equivalent to just one equation:

.. math::
    :label: trig_one

    |a-b| \le c \le a+b

we can do any permutation of the symbols, i.e. the above equation is equivalent
to any of these:

.. math::

    |b-c| \le a \le b+c

    |c-a| \le b \le c+a

So instead of stating the three inequalities :eq:`trig_three` it is more
convenient to just write :eq:`trig_one`, using any permutation that we like.

To show, that :eq:`trig_three` implies :eq:`trig_one` we rewrite
:eq:`trig_three`:

.. math::

    a + b \ge c

    c \ge a-b

    c \ge b-a

so

.. math::

    a + b \ge c

    c \ge |a-b|

and we get :eq:`trig_one`.
To show, that :eq:`trig_one` implies :eq:`trig_three` we rewrite
:eq:`trig_one` for $a\ge b$ first:

.. math::

    a \ge b

    |a-b| \le c \le a+b

so:

.. math::

    a \ge b

    a-b \le c \le a+b

rearranging:

.. math::

    a + b \ge c

    b + c \ge a

    a \ge b

since $c$ is positive, if $a\ge b$ then also $c+a\ge b$ and we get
:eq:`trig_three`. Finally, for $a < b$:

.. math::

    a < b

    |a-b| \le c \le a+b

so:

.. math::

    a < b

    -(a-b) \le c \le a+b

rearranging:

.. math::

    a + b \ge c

    b > a

    c + a \ge b


since $c$ is positive, if $b > a$ then also $b+c\ge a$ and we get
:eq:`trig_three`.

Gamma Function
--------------

Gamma function $\Gamma(z)$ is defined as:

.. math::

    \Gamma(z) = \int_0^\infty t^{z-1} e^{-t} \d t

Integrating by parts we get:

.. math::

    \Gamma(z)
        = \int_0^\infty t^{z-1} e^{-t} \d t
        = (z-1)\int_0^\infty t^{z-2} e^{-t} \d t-[t^{z-1}e^{-t}]_0^\infty
        = (z-1)\Gamma(z-1)

So for integer $n$ we get:

.. math::
    :label: gamma_fact

    \Gamma(n+1) = n\Gamma(n) = n(n-1)\Gamma(n-1)
        = n(n-1)(n-2)\cdots 2\cdot1\cdot\Gamma(1) =

        = n(n-1)(n-2)\cdots 1
        = n!

and

.. math::
    :label: gamma_double_fact

    \Gamma(n+\half) = (n-\half)\Gamma(n-\half)
        = (n-\half)(n-1-\half)\Gamma(n-1-\half)
        = (n-\half)(n-1-\half)\cdots\half\Gamma(\half) =

        = {2n-1\over2}{2n-3\over2}{2n-5\over2}\cdots{1\over2}\Gamma(\half)
        = {(2n-1)!!\over 2^n}\Gamma(\half)
        = {(2n-1)!!\over 2^n}\sqrt\pi

Where we used:

.. math::

    \Gamma(1)
        = \int_0^\infty t^{1-1} e^{-t} \d t
        = \int_0^\infty e^{-t} \d t
        = [-e^{-t}]_0^\infty
        = 1

    \Gamma(\half)
        = \int_0^\infty t^{{1\over2}-1} e^{-t} \d t
        = \int_0^\infty {e^{-t}\over\sqrt t} \d t
        = \int_0^\infty {e^{-x^2}\over x} 2x\, \d x
        = 2\int_0^\infty e^{-x^2} \d x =

        = \int_{-\infty}^\infty e^{-x^2} \d x
        = \sqrt{
            \int_{-\infty}^\infty e^{-x^2} \d x
            \int_{-\infty}^\infty e^{-y^2} \d y
            }
        = \sqrt{2\pi \int_0^\infty e^{-r^2} r\d r} =

        = \sqrt{2\pi \int_0^\infty e^{-u} \half\d u}
        = \sqrt\pi

Factorial
---------

The factorial $n!$ is defined as

.. math::

    n! = n(n-1)(n-2)\cdots 3\cdot2\cdot 1

By :eq:`gamma_fact` it can be written using the Gamma function as:

.. math::

    n! = \Gamma(n+1)

Double Factorial
----------------

The double factorial $n!!$ is defined as:

.. math::

    n!! = \begin{cases}
        n(n-2)(n-4)(n-6)\cdots 5\cdot3\cdot1\quad\quad\mbox{for odd $n=2k+1$} \\
        n(n-2)(n-4)(n-6)\cdots 6\cdot4\cdot2\quad\quad\mbox{for even $n=2k$}
    \end{cases}

One can rewrite double factorial using a factorial as:

.. math::

    (2k)!! = 2\cdot4\cdot6\cdots (2k)
        = 2^k (1\cdot2\cdot3\cdots k)
        = 2^k k!

    (2k-1)!!
        = 1\cdot3\cdot5\cdots(2k-1)
        = {1\cdot2\cdot3\cdot4\cdot5\cdots(2k) \over 2\cdot4\cdot6\cdots (2k)}
        = {(2k)!\over (2k)!!} = {(2k)!\over 2^k k!}

For odd $n$ it can be written using the Gamma function, see :eq:`gamma_double_fact`:

.. math::

    (2k-1)!! = {1\over\sqrt\pi} 2^k \Gamma\left(k+\half\right)

Example
~~~~~~~

.. math::

    A(n) = {1\cdot3\cdot5 \cdot \dots \cdot (2n-1) \over
        1\cdot 2\cdot 3\cdot \dots \cdot n}
        = {(2n-1)!!\over n!}
        = {(2n)!\over 2^n (n!)^2}
        = {1\over 2^n}\binom{2n}{n}

    B(n) = {1\cdot3\cdot5 \cdot \dots \cdot (2n-1) \over
        2\cdot 4\cdot\cdot6 \dots \cdot 2n}
        = {(2n-1)!!\over (2n)!!}
        = {(2n)!\over (2^n n!)^2}
        = {1\over 4^n}\binom{2n}{n}
