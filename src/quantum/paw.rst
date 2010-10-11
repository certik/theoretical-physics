Projector Augmented-Wave Method (PAW)
=====================================

We can use the Density Functional Theory (DFT) to reduce the many body problem
to solve a single particle Schrödinger equation:

.. math::

    H\ket{\psi_n} = \epsilon_n\ket{\psi_n}

The wavefunctions contain cusps (and are oscillatory around each nucleus), also
one needs to solve this for all core states.

Next step is to use the known behavior around each atom and take advantage of
the known physics somehow.  There are two general approaches, either one can
incorporate the known physic in the basis (for example the partition of unity
in the finite element method), or into the equations. PAW method uses the
latter approach.

Projectors, Augmentation Spheres and Smooth Wavefunctions
---------------------------------------------------------

We introduce *smooth wavefunctions* (we'll use "\~" for smooth functions) by
a linear transformation operator $T$:

.. math::

    \ket{\psi_n} = T \ket{\tilde\psi_n}

We construct *augmentation spheres* $|{\bf r} - {\bf R}^a| < r_c^a$ around each
atom $a$ (one can imagine a muffin-tin), where $r_c^a$ is a cut-off radius, $a$
is the atom index, ${\bf R}^a$ is the atom position.

We write $T$ as:

.. math::

    T = \one + \sum_a T^a

where $T^a$ only acts in the augmentation sphere. We choose a complete basis
$\ket{\phi_i^a}$ (also called *partial waves*) inside the sphere. The smooth
partial waves can be obtained using the $T$ operator:

.. math::

    \ket{\phi_i^a}
        = T\ket{\tilde\phi_i^a}
        = \left(\one+\sum_{a'} T^{a'}\right) \ket{\tilde\phi_i^a}

        = (\one+T^a) \ket{\tilde\phi_i^a}

Because $T^a$ only acts in the sphere, it follows that

.. math::

        \ket{\phi_i^a} = \ket{\tilde\phi_i^a}\quad\quad
            \mbox{for $r>r_c^a$}

outside the sphere (i.e.
$\braket{{\bf r} | \phi_i^a} = \braket{{\bf r} | \tilde\phi_i^a}$
for $r>r_c^a$). We can now expand the smooth wavefunctions using the partial
waves basis:

.. math::
    :label: smooth-partial-waves

    \ket{\tilde\psi_n} = \sum_i P_{ni}^a\ket{\tilde \phi_i^a}

inside the augmentation sphere. Multiplying both sides by $T$:

.. math::
    :label: non-smooth-partial-waves

    T\ket{\tilde\psi_n} = T\sum_i P_{ni}^a\ket{\tilde \phi_i^a}

    T\ket{\tilde\psi_n} = \sum_i P_{ni}^a\, T\ket{\tilde \phi_i^a}

    \ket{\psi_n} = \sum_i P_{ni}^a \ket{\phi_i^a}

So both smooth and non-smooth wavefunctions have the same expansion
coefficients $P_{ni}^a$. We choose smooth *projector functions*
$\ket{\tilde p_i^a}$ satisfying the following
orthogonality and completeness relations inside the augmentation spheres (no
restrictions are imposed outside the spheres, so we just define
$\braket{{\bf r} | \tilde p_i^a} = 0$):

.. math::
    :label: projector-functions

    \braket{\tilde p_i^a | \tilde \phi_j^a} = \delta_{ij}

    \sum_i \ket{\tilde \phi_i^a}\bra{\tilde p_i^a}  = \one

then multiplying :eq:`smooth-partial-waves` by $\bra{\tilde p_i^a}$
and using :eq:`projector-functions`:

.. math::

    \braket{\tilde p_i^a | \tilde \psi_n }
        = \sum_j P_{nj}^a\braket{\tilde p_i^a | \tilde \phi_j^a}
        = \sum_j P_{nj}^a\delta_{ij}
        = P_{ni}^a

we can rewrite :eq:`smooth-partial-waves` and :eq:`non-smooth-partial-waves`:

.. math::
    :label: partial-waves

    \ket{\tilde\psi_n} = \sum_i \braket{\tilde p_i^a | \tilde \psi_n }
        \ket{\tilde \phi_i^a}

    \ket{\psi_n} = \sum_i \braket{\tilde p_i^a | \tilde \psi_n }
        \ket{\phi_i^a}

Let's write $T^a$ using the projectors:

.. math::

    T^a
        = T^a \one
        = T^a \sum_i \ket{\tilde \phi_i^a}\bra{\tilde p_i^a}
        = \sum_i (T^a\ket{\tilde \phi_i^a})\bra{\tilde p_i^a}
        = \sum_i (\ket{\phi_i^a} - \ket{\tilde \phi_i^a})\bra{\tilde p_i^a}

Note that the right hand side is zero outside the augmentation sphere. Thus

.. math::

    T
        = \one + \sum_a T^a
        = \one + \sum_a \sum_i (\ket{\phi_i^a} - \ket{\tilde \phi_i^a})\bra{\tilde p_i^a}

In other words, the transformation operator $T$ is completely defined using the
smooth and non-smooth partial waves and the projector functions. In terms of
the wavefunction:

.. math::

    \ket{\psi_n} = T\ket{\tilde\psi_n}
        =\ket{\tilde\psi_n} + \sum_a \sum_i
            (\ket{\phi_i^a} - \ket{\tilde \phi_i^a})
            \braket{\tilde p_i^a | \tilde\psi_n} =

        =\ket{\tilde\psi_n} + \sum_a\left(
            \sum_i \ket{\phi_i^a}\braket{\tilde p_i^a | \tilde\psi_n}
            - \sum_i\ket{\tilde \phi_i^a}\braket{\tilde p_i^a | \tilde\psi_n}
              \right)

In words, the wavefunction can be decomposed as the sum of the smooth
wavefunction and sum over atoms (centers), at each atom we have "1-center all
electron" minus "1-center pseudo".

The projection functions can always be written as

.. math::

    \bra{\tilde p_i^a}
        = \sum_j\left\{\braket{f_k^a | \tilde\phi_l^a}\right\}_{ij}^{-1}
            \bra{f_j^a}

where $\ket{f_k^a}$ is any set of linearly independent functions.

Note: the $n$ above means all states of interest --- either all states, or only
the valence states.

Frozen Core Approximation
-------------------------

One can either calculate all electrons in the eigenproblem, or only calculate
the valence electrons and treat the core states separately. The simplest option
is to introduce a *frozen core approximation*, where

.. math::

    \ket{\psi_n} = \ket{\phi_\alpha^{a,\mbox{core}}}

for all core states $n$, here $n$ runs over $(a, \alpha)$, where $a$ is the
atom index and $\alpha$ are the core states of an atom. This approximation
can also be relaxed in various ways.

Expectation Values of Local Operators
-------------------------------------

In the frozen core approximation:

.. math::

    \braket{O} = \sum_n^{\mbox{val}} f_n \braket{\psi_n | O | \psi_n}
        + \sum_a \sum_\alpha^{\mbox{core}}
        \braket{\phi_\alpha^{a,\mbox{core}} | O | \phi_\alpha^{a,\mbox{core}}}
        = \cdots =

      =\sum_n^{\mbox{val}} f_n \braket{\tilde \psi_n | O | \tilde \psi_n}
      +\sum_a \sum_{i, j} \left(
        \braket{\phi_i^a | O | \phi_j^a} - \braket{\tilde \phi_i^a | O | \tilde
        \phi_j^a}\right) D_{ij}^a
        +
        \sum_a \sum_\alpha^{\mbox{core}}
        \braket{\phi_\alpha^{a,\mbox{core}} | O | \phi_\alpha^{a,\mbox{core}}}

where the tensor $D_{ij}^a$ is:

.. math::

    D_{ij}^a = \sum_n f_n \braket{\tilde \psi_n|\tilde p_i^a}
        \braket{\tilde p_j^a|\tilde\psi_n}

Density
~~~~~~~

.. math::

    n({\bf r})
        = \sum_n f_n |\psi_n({\bf r})|^2
        = \sum_n f_n \braket{\psi_n | {\bf r} }\braket{{\bf r} | \psi_n}
        = \Big< \ket{\bf r}\bra{\bf r} \Big> =

      =\sum_n^{\mbox{val}} f_n |\tilde\psi_n({\bf r})|^2
      +\sum_a \sum_{i, j} \left(
        \phi_i^a \phi_j^a - \tilde \phi_i^a \tilde \phi_j^a\right) D_{ij}^a
        +
        \sum_a \sum_\alpha^{\mbox{core}}
        |\phi_\alpha^{a,\mbox{core}}|^2

The functions $\phi_\alpha^{a,\mbox{core}}$ are not strictly localized withing
the augmentation sphere.

Kohn Sham Equations
-------------------

We multiply the original equations by $T^\dag$ from the left and use the smooth
wavefunctions:

.. math::

    H\ket{\psi_n} = \epsilon_n\ket{\psi_n}

    T^\dag H\ket{\psi_n} = \epsilon_n T^\dag\ket{\psi_n}

    T^\dag H T\ket{\tilde\psi_n} = \epsilon_n T^\dag T \ket{\tilde\psi_n}

The overlap operator $T^\dag T$ can be written as:

.. math::

    T^\dag T = \cdots = \one + \sum_a \sum_{i,j}
        \ket{\tilde p_i^a}\left(
            \braket{\phi_i^a | \phi_j^a}
            -\braket{\tilde \phi_i^a | \tilde\phi_j^a}
        \right)\bra{\tilde p_j^a}
