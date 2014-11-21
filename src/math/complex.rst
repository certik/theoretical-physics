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

Any complex function can be expressed using $\Re z$ and $\Im z$, or
alternatively using $z$ and $\bar z$.

Examples
~~~~~~~~

.. math::

    |z| = \sqrt{\Re^2 z + \Im^2 z} = \sqrt{
        \left({1\over 2}(z + \bar z)\right)^2 +
        \left({i\over 2}(-z + \bar z)\right)^2}
        =\sqrt{z\bar z}

    \arg z = \atan2(\Im z, \Re z)
        =\atan2\left({i\over 2}(-z + \bar z), {1\over 2}(z + \bar z)\right)
        =\atan2\left(i(-z + \bar z), z + \bar z\right)

Testing Identities Using Computer Code
--------------------------------------

All the complex identities in this chapter can be tested using the following
code (:download:`test_complex.py <code/test_complex.py>`):

.. literalinclude:: code/test_complex.py
