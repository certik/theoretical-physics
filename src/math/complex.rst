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

    \log ab = \log |ab| + i\arg ab =

    = \log |a| + \log |b| + i\arg a + i\arg b + 2\pi i
            \left\lfloor \pi-\arg a-\arg b \over 2\pi \right\rfloor =

    = \log a + \log b + 2\pi i
            \left\lfloor \pi-\arg a-\arg b \over 2\pi \right\rfloor

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

    \log x^a = \log e^{a\log x} = a\log x
        + 2\pi i \left\lfloor \pi-\Im a\log x \over 2\pi \right\rfloor

and

.. math::

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
