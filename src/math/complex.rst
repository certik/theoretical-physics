.. index:: complex numbers

Complex Numbers
===============

We start by defining $\arg(z)$ by its principal value, then everything else
follows from this definitino.  We could have also used any other branch, but
then most results in this chapter would need to be updated with the new
convention.

Then we define exponential, logarithm, power and so on using simple natural
formulas. Everything else follows directly from those. In the derivation of
each formula, only formulas introduced before (above) are used.

Every formula in this chapter holds for all complex numbers, unless explicitly
specified otherwise.

Real and Imaginary Part
-----------------------

A complex number $z$ can be written using its real and imaginary parts:

.. math::

    z = \Re z + i \Im z

Argument Function
-----------------

Principal value of $\arg(z)$ is defined as

.. math::

    \arg z = \arg(\Re z + i \Im z) = \atan2(\Im z, \Re z)

thus we have $-\pi < \arg z \le \pi$. Few formulas:

.. math::

    \arg ab = \arg a + \arg b + 2\pi
        \left\lfloor \pi-\arg a-\arg b \over 2\pi \right\rfloor

Exponential
-----------

.. math::

    e^z = e^{\Re z + i\Im z} = e^{\Re z} (\cos\Im z + i \sin \Im z)

It holds:

.. math::

    e^{a+b} = e^a e^b

Any complex number can then be written in a polar form:

.. math::

    z = |z| e^{i\arg z}

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

    \arg e^z = \arg e^{\Re z} e^{i\Im z} = \arg e^{i\Im z}
        = \Im z + 2\pi \left\lfloor \pi-\Im z \over 2\pi \right\rfloor

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
