.. index:: complex numbers

Complex Numbers
===============

We start by defining $\arg(z)$ by its principal value, then everything else
follows from this definition.  We could have also used any other branch, but
then most results in this chapter would need to be updated with the new
convention.

Then we define exponential, logarithm, power and so on using simple natural
formulas. From these definitions, everything else follows using a very simple
algebra manipulation, all the "messy" features are hidden in the definition and
properties of the real $\atan2$ function. In the derivation of each formula,
only formulas introduced before (above) are used.

Every formula in this chapter holds for all complex numbers, unless explicitly
specified otherwise.

Real and Imaginary Part
-----------------------

A complex number $z$ can be written using its real and imaginary parts:

.. math::

    z = \Re z + i \Im z

The absolute value $|z|$ is defined as:

.. math::

    |z| = \sqrt{\Re^2 z + \Im^2 z}

Argument Function
-----------------

Principal value of $\arg(z)$ is defined as

.. math::

    \arg z = \atan2(\Im z, \Re z)

Thus we have $-\pi < \arg z \le \pi$. All operations with $\arg z$ are then
derived using the properties of the real $\atan2$ function.

Exponential
-----------

Exponential is defined using:

.. math::

    e^z = e^{\Re z + i\Im z} = e^{\Re z} (\cos\Im z + i \sin \Im z)

It follows:

.. math::

    e^{a+b}
        = e^{\Re(a+b)} (\cos\Im(a+b) + i \sin \Im(a+b)) =

        = e^{\Re a}e^{\Re b} \left(
            \cos(\Im a)\cos(\Im b) - \sin(\Im a)\sin(\Im b)
            + i \sin(\Im a)\cos(\Im b) + i\cos(\Im a) \sin(\Im b)\right) =

        = e^{\Re a} (\cos\Im a + i \sin \Im a)
          e^{\Re b} (\cos\Im b + i \sin \Im b) =

        = e^a e^b

Any complex number can be written in a polar form as follows:

.. math::

    z = \Re z + i \Im z = |z| \left( {\Re z \over |z|} + i {\Im z\over
        |z|}\right) =

    = |z| \left( {\Re z \over\sqrt{\Re^2 z + \Im^2 z}}
        + i {\Im z\over\sqrt{\Re^2 z + \Im^2 z}}\right) =

    = |z| \left(\cos\atan2(\Im z, \Re z) + i \sin\atan2(\Im z, \Re z)\right) =

    = |z| \left(\cos\arg z + i \sin\arg z\right) =

    = |z| e^{i\arg z}

The following formula holds:

.. math::

    \arg e^z = \arg e^{\Re z} e^{i\Im z} = \arg e^{i\Im z} =

        = \arg(\cos\Im z + i\sin\Im z) =

        = \atan2(\sin\Im z, \cos\Im z) =

        = \Im z + 2\pi \left\lfloor \pi-\Im z \over 2\pi \right\rfloor

and also:

.. math::

    \arg ab
        = \arg(|a| e^{i\arg a} |b| e^{i\arg b}) =

        = \arg(|a| |b| e^{i(\arg a+\arg b)}) =

        = \arg(e^{i(\arg a+\arg b)}) =

        = \arg(\cos(\arg a+\arg b) + i\sin(\arg a + \arg b)) =

        = \atan2(\sin(\arg a+\arg b), \cos(\arg a + \arg b)) =

        = \arg a + \arg b + 2\pi
            \left\lfloor \pi-\arg a-\arg b\over 2\pi \right\rfloor

and

.. math::

    \arg {1\over z} = -\arg z + 2\pi
            \left\lfloor \pi+\arg z\over 2\pi \right\rfloor

and

.. math::

    \arg {a\over b}
        = \arg\left(|a| e^{i\arg a} \left|{1\over b}\right| e^{i\arg {1\over
            b}}\right) =

        = \arg\left(|a| \left|{1\over b}\right| e^{i(\arg a-\arg b)
            +2\pi i \left\lfloor \pi+\arg b\over 2\pi \right\rfloor }\right) =

        = \arg(e^{i(\arg a-\arg b)}) =

        = \arg(\cos(\arg a-\arg b) + i\sin(\arg a - \arg b)) =

        = \atan2(\sin(\arg a-\arg b), \cos(\arg a - \arg b)) =

        = \arg a - \arg b + 2\pi
            \left\lfloor \pi-\arg a+\arg b\over 2\pi \right\rfloor


Logarithm
---------

The logarithm is defined as:

.. math::
    :label: def_log

    \log z = \log|z| + i \arg z

The motivation is from the following formula:

.. math::

    z = |z| e^{i\arg z} = e^{\log |z|} e^{i\arg z} = e^{\log|z| + i \arg z}

which using our definition becomes:

.. math::
    :label: elog

    z = e^{\log|z| + i \arg z} = e^{\log z}

so a logarithm is an inverse function to an exponential. The formula :eq:`elog`
would be satisfied even if we add a factor of $2\pi i n$ (where $n$ is an
integer) to the right hand side of :eq:`def_log`. However, the convention is to
define logarithm using the equation :eq:`def_log` exactly.

We can now derive a few important formulas:

.. math::

    \log | e^z | = \log | e^{\Re z} e^{i \Im z} | = \log | e^{\Re z} | = \Re z

    \log e^z = \log | e^z | + i \arg e^z = \Re z + i \left(
        \Im z + 2\pi \left\lfloor \pi-\Im z \over 2\pi \right\rfloor
        \right)
        = z + 2\pi i \left\lfloor \pi-\Im z \over 2\pi \right\rfloor

and

.. math::
    :label: log(ab)

    \log ab = \log |ab| + i\arg ab =

    = \log |a| + \log |b| + i\arg a + i\arg b + 2\pi i
            \left\lfloor \pi-\arg a-\arg b \over 2\pi \right\rfloor =

    = \log a + \log b + 2\pi i
            \left\lfloor \pi-\arg a-\arg b \over 2\pi \right\rfloor

and

.. math::
    :label: log(a/b)

    \log {a\over b} = \log \left|{a\over b}\right| + i\arg {a\over b} =

    = \log |a| - \log |b| + i\arg a - i\arg b + 2\pi i
            \left\lfloor \pi-\arg a+\arg b \over 2\pi \right\rfloor =

    = \log a - \log b + 2\pi i
            \left\lfloor \pi-\arg a+\arg b \over 2\pi \right\rfloor


Power
-----

A power of two complex numbers is defined as:

.. math::

    z^a = e^{a\log z}

From above we can also write the power $z^a$ in two different ways:

.. math::

    z^a = \left(e^{\log z}\right)^a = e^{\log z^a}

But these two cannot be used as a definition of a power, because both require
the knowledge of $x^a$, which we are trying to define, where $x=z$ or $x=e^{\log
z}$.

It follows:

.. math::
    :label: log(x^a)

    \log x^a = \log e^{a\log x} = a\log x
        + 2\pi i \left\lfloor \pi-\Im a\log x \over 2\pi \right\rfloor

and

.. math::
    :label: (x^a)^b

    (x^a)^b = e^{b \log x^a} = e^{b \left(
        a\log x
        + 2\pi i \left\lfloor \pi-\Im a\log x \over 2\pi \right\rfloor
    \right)} =

    = e^{a b \log x} e^{
        2\pi i b\left\lfloor \pi-\Im a\log x \over 2\pi \right\rfloor
    } =

    = x^{a b} e^{
        2\pi i b\left\lfloor \pi-\Im a\log x \over 2\pi \right\rfloor
    }

As a special case for $x=e$ one gets:

.. math::
    :label: (e^a)^b

    (e^a)^b = e^{a b} e^{
        2\pi i b\left\lfloor \pi-\Im a \over 2\pi \right\rfloor
    }

Similarly:

.. math::

    (xy)^a = e^{a\log xy}
        = e^{a\log x + a\log y + 2\pi i a
            \left\lfloor \pi-\arg x-\arg y \over 2\pi \right\rfloor
            } =

    = x^a y^a e^{2\pi i a
            \left\lfloor \pi-\arg x-\arg y \over 2\pi \right\rfloor
            }

Examples
--------

For integer $n$ we get from :eq:`(x^a)^b`:

.. math::

    (x^a)^n
    = x^{a n} e^{
        2\pi i n\left\lfloor \pi-\Im a\log x \over 2\pi \right\rfloor
    } = x^{a n}

Using :eq:`(x^a)^b`:

.. math::

    \sqrt{x^2} = (x^2)^{1\over 2} = x^{{1\over 2}\cdot 2}
            e^{
            2\pi i {1\over 2}
            \left\lfloor \pi-\Im 2\log x \over 2\pi \right\rfloor}
        = x e^{
            \pi i
            \left\lfloor \pi-2\arg x \over 2\pi \right\rfloor}
        = (-1)^{\left\lfloor \pi-2\arg x \over 2\pi \right\rfloor} x

Using :eq:`(e^a)^b`:

.. math::

    \sqrt {e^x} = (e^x)^{1\over 2} = e^{x\over 2} e^{
        \pi i\left\lfloor \pi-\Im x \over 2\pi \right\rfloor
    } =
        (-1)^{\left\lfloor \pi-\Im x \over 2\pi \right\rfloor}
        e^{x\over 2}

Using :eq:`log(ab)`:

.. math::

    0 = \log 1 = \log(-1)(-1) =
        \log(-1) + \log(-1) + 2\pi i
            \left\lfloor \pi-\pi-\pi \over 2\pi \right\rfloor =

      = i\pi + i\pi + 2\pi i \left\lfloor-\half\right\rfloor
      = i\pi + i\pi - 2\pi i = 0

Code:

    >>> from math import floor, pi
    >>> from cmath import log
    >>> log((-1)*(-1))
    0j
    >>> log(-1)+log(-1)+2*pi*1j*floor((pi-pi-pi)/(2*pi))
    0j

Another example:

.. math::

    i^i = e^{i \log i} = e^{i^2 \arg i} = e^{-{\pi\over 2}}

Code:

    >>> from math import exp, pi
    >>> 1j**1j
    (0.20787957635076193+0j)
    >>> exp(-pi/2)
    0.20787957635076193

Another example, using :eq:`log(x^a)`:

.. math::

    \log(\sqrt z)
        = \log(z^{1\over2})
        = \half \log z
        + 2\pi i \left\lfloor \pi-\Im {1\over2}\log z \over 2\pi \right\rfloor =

    = \half \log z
    + 2\pi i \left\lfloor \pi-{1\over2}\arg z \over 2\pi \right\rfloor
    = \half \log z

and

.. math::

    \log(z^2)
        = 2 \log z
        + 2\pi i \left\lfloor \pi-\Im 2\log z \over 2\pi \right\rfloor =

    = 2 \log z
    + 2\pi i \left\lfloor \pi-2\arg z \over 2\pi \right\rfloor

and

.. math::

    \log\left({1\over z}\right)
        = \log(z^{-1})
        = - \log z
        + 2\pi i \left\lfloor \pi-\Im (-1)\log z \over 2\pi \right\rfloor =

    = - \log z
    + 2\pi i \left\lfloor \pi+\arg z \over 2\pi \right\rfloor

Another example, following from :eq:`def_log` and :eq:`log(a/b)`:

.. math::

    \arg z = {1\over i}(\log z - \log|z|)
        = {1\over i}\left(\log {z\over|z|}
          - 2\pi i \left\lfloor \pi-\arg z+\arg |z| \over 2\pi \right\rfloor
          \right)
        = {1\over i} \log {z\over|z|}

Complex Conjugate
-----------------

The complex conjugate is defined by:

.. math::

    z = \Re z + i \Im z

    \bar z = \Re z - i \Im z

Now we can solve for $\Re z$ and $\Im z$:

.. math::

    \Re z = {1\over 2}(z + \bar z)

    \Im z = {i\over 2}(-z + \bar z)

Any complex function $f$ can be written using $\Re z$ and $\Im z$, i.e. $f =
f(\Re z, \Im z)$ or using $z$ and $\bar z$, i.e. $f=f(z, \bar z)$.

Examples
~~~~~~~~

.. math::

    |z| = \sqrt{\Re^2 z + \Im^2 z} = \sqrt{
        \left({1\over 2}(z + \bar z)\right)^2 +
        \left({i\over 2}(-z + \bar z)\right)^2}
        =\sqrt{z\bar z}

    |\bar z| = \sqrt{\Re^2 \bar z + \Im^2 \bar z}
        = \sqrt{\Re^2 z + \left(-\Im z\right)^2}
        =|z|

    \arg z = \atan2(\Im z, \Re z)
        =\atan2\left({i\over 2}(-z + \bar z), {1\over 2}(z + \bar z)\right)
        =\atan2\left(i(-z + \bar z), z + \bar z\right)

    \arg \bar z = \atan2(-\Im z, \Re z)
        =-\atan2(\Im z, \Re z) + 2\pi
            \left\lfloor \atan2(\Im z, \Re z)+\pi \over 2\pi \right\rfloor
        =-\arg z + 2\pi \left\lfloor \arg z+\pi \over 2\pi \right\rfloor

    \overline{\log z} = \log|z| -i\arg z
        = \log|\bar z| +i\arg \bar z -2\pi i
            \left\lfloor \arg z+\pi \over 2\pi \right\rfloor
        = \log \bar z -2\pi i
            \left\lfloor \arg z+\pi \over 2\pi \right\rfloor

    \overline{\sqrt z} = \overline{z^\half}
        = \overline{e^{\half\log z}}
        = \overline{e^{\half(\log|z| + i\arg z)}}
        = e^{\half(\log|z| - i\arg z)}
        = e^{\half\left(\log|\bar z| + i\arg \bar z
                - 2\pi i \left\lfloor \arg z+\pi \over 2\pi \right\rfloor
            \right)} =

        = \left(\bar z\right)^\half
            e^{-\pi i \left\lfloor \arg z+\pi \over 2\pi \right\rfloor}
        = (-1)^{\left\lfloor \arg z+\pi \over 2\pi \right\rfloor} \sqrt{\bar z}

Complex Derivatives
-------------------

The complex derivative is defined by

.. math::
    :label: complex_deriv_lim

    {\d f \over \d z}
        = \lim_{h\to0} {f(z+h)-f(z) \over h}

Let's calculate the complex derivative in the direction $\theta$, i.e.
we use $h=te^{i\theta}$ with real $t$ and we introduce $f=f(x, y)$ with $x=\Re
z$, $y=\Im z$ to simplify the notation:

.. math::

    {\d f \over \d z}
        = \lim_{t\to0} {f(z+t e^{i\theta})-f(z) \over t e^{i\theta}} =

        = \lim_{t\to0} {f(x+t\cos\theta, y+t\sin\theta)-f(x, y) \over t}
            e^{-i\theta} =

        = {\d \over \d t} f(x+t\cos\theta, y+t\sin\theta) e^{-i\theta} =

        = \left({\partial f \over \partial x} \cos\theta
        + {\partial f \over \partial y} \sin\theta \right) e^{-i\theta} =

        = \left({\partial f \over \partial x}
            {e^{i\theta}+e^{-i\theta} \over 2}
        + {\partial f \over \partial y} {e^{i\theta}-e^{-i\theta} \over 2i}
            \right) e^{-i\theta} =

        = {\partial f \over \partial x}
            {1+e^{-2i\theta} \over 2}
        + {\partial f \over \partial y} {1-e^{-2i\theta} \over 2i} =

        = \half\left({\partial f \over \partial x}
                   -i {\partial f \over \partial y}\right)
        + \half\left({\partial f \over \partial x}
                   +i {\partial f \over \partial y}\right)e^{-2i\theta} =

        = {\partial f \over \partial z}
            + {\partial f \over \partial \bar z} e^{-2i\theta}

In the last step we have expressed the derivatives with respect to $x$, $y$ in
terms of derivatives with respect to $z$, $\bar z$, using the relations:

.. math::
    :label: dfdz

    {\partial f \over \partial z}
        = {\partial x \over \partial z} {\partial f \over \partial x}
            + {\partial y \over \partial z} {\partial f \over \partial y} =

        = {1\over2} {\partial f \over \partial x}
            - {i\over2} {\partial f \over \partial y} =

        = \half\left( {\partial f \over \partial x}
            - i {\partial f \over \partial y} \right)

.. math::
    :label: dfdconjugate(z)

    {\partial f \over \partial \bar z}
        = {\partial x \over \partial \bar z} {\partial f \over \partial x}
            + {\partial y \over \partial \bar z} {\partial f \over \partial y} =

        = {1\over2} {\partial f \over \partial x}
            + {i\over2} {\partial f \over \partial y} =

        = \half\left( {\partial f \over \partial x}
            + i {\partial f \over \partial y} \right)

Let's repeat the important result:

.. math::
    :label: complex_deriv

    {\d f(z, \bar z) \over \d z}
        = {\partial f(z, \bar z) \over \partial z}
            + {\partial f(z, \bar z) \over \partial \bar z} e^{-2i\theta}

The equation :eq:`complex_deriv` states that the complex derivative along the
direction $\theta$ of any function can be calculated, but the result in general
depends on $\theta$. The derivatives for all possible angles $\theta$ lie on a
circle, with the center ${\partial f \over \partial z}$ and the radius
$\left|{\partial f \over \partial \bar z}\right|$.
When the derivative has different values
for different $\theta$, i.e. when ${\partial f \over \partial \bar z}\neq0$, it
means that the complex limit :eq:`complex_deriv_lim` does not exist. On the
other hand, if the derivative does not depend on $\theta$, i.e.
when ${\partial f \over \partial \bar z}=0$, then the complex limit
:eq:`complex_deriv_lim` exists, and the function has a complex derivative ---
such functions are called analytic. Analytic functions thus do not depend on
$\bar z$ and we can write just $f = f(z)$ for those.

The ${\partial f \over \partial z}$ and ${\partial f \over \partial \bar z}$
are called Wirtinger derivatives.

We can see that the function is analytic (i.e. has a complex derivative) if and
only if:

.. math::

    {\partial f \over \partial \bar z}
        = \half\left( {\partial f \over \partial x}
            + i {\partial f \over \partial y} \right) = 0

We can write $f = u+iv$:

.. math::

    {\partial f \over \partial x} + i {\partial f \over \partial y} = 0

    {\partial (u+iv) \over \partial x}
        + i {\partial (u+iv) \over \partial y} = 0

    \left({\partial u \over \partial x}
    -{\partial v \over \partial y}\right)
        + i \left({\partial u \over \partial y}
          + {\partial v \over \partial x}\right)= 0

both the real and imaginary parts must be equal to zero:

.. math::

    {\partial u \over \partial x} = {\partial v \over \partial y}

    {\partial u \over \partial y} = - {\partial v \over \partial x}

These are called the Cauchy-Riemann equations.

We can derive the chain rule:

.. math::
    :label: chain_rule

    {\d f(g) \over \d z}
        = {\partial f(g) \over \partial z}
            + {\partial f(g) \over \partial \bar z} e^{-2i\theta} =

        = \left({\partial f \over \partial g}{\partial g \over \partial z}
        + {\partial f \over \partial \bar g}{\partial \bar g \over \partial
          z}\right)
        + \left({\partial f \over \partial g}{\partial g \over \partial \bar z}
        + {\partial f \over \partial \bar g}{\partial \bar g \over \partial
          \bar z}\right)
        e^{-2i\theta} =

        = {\partial f \over \partial g}
        \left({\partial g \over \partial z}+{\partial g \over \partial \bar z}
            e^{-2i\theta} \right)
        +
          {\partial f \over \partial \bar g}
        \left({\partial \bar g \over \partial z}+{\partial \bar g \over \partial \bar z}
            e^{-2i\theta} \right) =

        = {\partial f \over \partial g} {\d g \over \d z}
        +
          {\partial f \over \partial \bar g} {\d \bar g \over \d z}

Another useful formula is the derivative of a conjugate function:

.. math::
    :label: deriv_conj

    {\d \bar f \over \d z}
        = {\partial \bar f \over \partial z}
            + {\partial \bar f \over \partial \bar z} e^{-2i\theta}
        = \overline{\partial f \over \partial \bar z}
            + \overline{\partial f \over \partial z} e^{-2i\theta} =

        = \left(\overline{{\partial f \over \partial \bar z} e^{-2i\theta}
            + {\partial f \over \partial z}}\right) e^{-2i\theta}
        = \overline{\d f \over \d z} e^{-2i\theta}

Using :eq:`deriv_conj`, the chain rule :eq:`chain_rule` can also be written as:

.. math::
    :label: chain_rule2

    {\d f(g) \over \d z}
        = {\partial f \over \partial g} {\d g \over \d z}
        + {\partial f \over \partial \bar g} {\d \bar g \over \d z}
        = {\partial f \over \partial g} {\d g \over \d z}
        + {\partial f \over \partial \bar g} \overline {\d g \over \d z}
            e^{-2i\theta}

Which has the advantage that only the ${\d g \over \d z}$ derivative is needed,
the rest is just conjugation and multiplication. If $f$ is analytic, then
${\partial f \over \partial \bar g}=0$, the second term vanishes and the chain
rule is analogous to real functions.

Examples
~~~~~~~~

.. math::

    {\d z \over \d z}
         = {\partial z \over \partial z}
         + {\partial z \over \partial \bar z} e^{-2i\theta}
         = 1

    {\d \bar z \over \d z}
         = {\partial \bar z \over \partial z}
         + {\partial \bar z \over \partial \bar z} e^{-2i\theta}
         = e^{-2i\theta}

    {\d \Re z \over \d z} = {\d {1\over 2}(z + \bar z) \over \d z}
         = {\partial {1\over 2}(z + \bar z) \over \partial z}
         + {\partial {1\over 2}(z + \bar z) \over \partial \bar z} e^{-2i\theta}
         = \half + \half e^{-2i\theta}

    {\d \Im z \over \d z} = {\d {i\over 2}(-z + \bar z) \over \d z}
         = {\partial {i\over 2}(-z + \bar z) \over \partial z}
         + {\partial {i\over 2}(-z + \bar z) \over \partial \bar z}
            e^{-2i\theta}
         = -{i\over2} + {i\over2} e^{-2i\theta}

    {\d |z| \over \d z}
        = {\d \sqrt{z\bar z} \over \d z}
        = {\partial \sqrt{z\bar z} \over \partial z}
        + {\partial \sqrt{z\bar z} \over \partial \bar z} e^{-2i\theta}
        = {\bar z + z e^{-2i\theta}\over 2\sqrt{z\bar z}}
        = {\bar z + z e^{-2i\theta}\over 2|z|}

    {\d |f(z)| \over \d z}
        = {\partial |f| \over \partial f} {\d f \over \d z}
        + {\partial |f| \over \partial \bar f} {\d \bar f \over \d z}
        = {\bar f{\d f\over\d z} + f{\d \bar f\over\d z}\over 2|f|}

    {\d \arg z \over \d z}
        ={\d\, \atan2\left(i(-z + \bar z), z + \bar z\right) \over \d z}
        ={\partial\, \atan2\left(i(-z + \bar z), z + \bar z\right) \over
            \partial z}
        +{\partial\, \atan2\left(i(-z + \bar z), z + \bar z\right) \over
            \partial \bar z} e^{-2i\theta} =

        = {(z+\bar z)(-i)- i(-z+\bar z)\over 4z\bar z}
        + {(z+\bar z)i- i(-z+\bar z)\over 4z\bar z}e^{-2i\theta} =

        = {i\over2}\left( -{1\over z} + {1\over \bar z} e^{-2i\theta} \right)
        = {i\over2}\left( -\bar z + z e^{-2i\theta} \over | z|^2 \right)

    {\d \log|z| \over \d z}
        = {1\over|z|} {\bar z + z e^{-2i\theta}\over 2|z|}
        = {\bar z + z e^{-2i\theta}\over 2|z|^2}

    {\d \log z \over \d z}
        = {\d (\log|z| +i\arg z) \over \d z}
        = {\bar z + z e^{-2i\theta}\over 2|z|^2}
        +i {i\over2}\left( -\bar z + z e^{-2i\theta} \over | z|^2 \right)
        = {\bar z \over | z|^2} = {\bar z\over z\bar z} = {1\over z}

    {\d \overline{\log z} \over \d z}
        = {\partial \overline{\log z} \over \partial z}
        + {\partial \overline{\log z} \over \partial \bar z} e^{-2i\theta}
        = \overline{\partial \log z \over \partial \bar z}
        + \overline{\partial \log z \over \partial z} e^{-2i\theta}
        = {1\over\bar z} e^{-2i\theta}

    {\d |\log z| \over \d z}
        = {\overline{\log z}{\d \log z\over\d z}
            + \log z{\d \overline{\log z}\over\d z}\over 2|\log z|}
        = {{1\over z}\overline{\log z}
            + {1\over\bar z}(\log z) e^{-2i\theta}\over 2|\log z|}
        = {\bar z\overline{\log z}
            + z (\log z) e^{-2i\theta}\over 2z\bar z|\log z|}

Note that if $z$ is real, i.e. $z = \bar z$, we recover the real derivative
results by setting $\theta=0$, i.e. taking the derivative along the $x$-axis:

.. math::

    {\d x \over \d x} = 1

    {\d \Re x \over \d x} = \half + \half = 1

    {\d \Im x \over \d x} = -{i\over2} + {i\over2} = 0

    {\d |x| \over \d x} = {x + x \over 2|x|} = {x \over |x|}

    {\d |f(x)| \over \d x}
        = {f{\d f\over\d x} + f{\d f\over\d z}\over 2|f|}
        = {f{\d f\over\d x} \over |f|}

    {\d \arg x \over \d x} = {i\over2}\left( -{1\over x} + {1\over x}\right) = 0

    {\d \log|x| \over \d x}
        = {x + x \over 2|x|^2}
        = {x \over | x|^2}

    {\d \log x \over \d x} = {1\over x}

    {\d |\log x| \over \d x}
        = {x\log x + x \log x\over 2x^2|\log x|}
        = {\log x\over x|\log x|}

The above approach to first express things in terms of $z$ and $\bar z$ and
then differentiate is probably the easiest, but we can do things in any order
we want. For example the derivative of $|z|$ can also be calculated in this
(arguably more complicated) way:

.. math::

    {\d |z| \over \d z} = {\d \sqrt{\Re^2 z + \Im^2 z} \over \d z}
        = {\Re z {\d \Re z \over \d z} + \Im z {\d \Im z \over \d z} \over |z|}=

        = {\left({1\over 2}(z + \bar z)\right)
            \left(\half + \half e^{-2i\theta}\right)
            + \left({i\over 2}(-z + \bar z)\right)
              \left(-{i\over2} + {i\over2} e^{-2i\theta}\right) \over |z|}=

        = {\bar z + z e^{-2i\theta}\over 2|z|}

Testing Identities Using Computer Code
--------------------------------------

All the complex identities in this chapter can be tested using the following
code (:download:`test_complex.py <code/test_complex.py>`):

.. literalinclude:: code/test_complex.py
