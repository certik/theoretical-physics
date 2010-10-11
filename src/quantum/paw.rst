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

We introduce smooth wavefunctions (we'll use "\~" for smooth functions) by
a linear transformation operator $T$:

.. math::

    \ket{\psi_n} = T \ket{\tilde\psi_n}

We construct augmentation spheres $|{\bf r} - {\bf R}^a| < r_c^a$ around each
atom $a$ (one can imagine a muffin-tin), where $r_c^a$ is a cut-off radius, $a$
is the atom index, ${\bf R}^a$ is the atom position.

We write $T$ as:

.. math::

    T = \one + \sum_a T^a

where $T^a$ only acts in the augmentation sphere. We choose a complete basis
$\ket{\phi_i^a}$ inside the sphere. The smooth functions can be obtained using
the $T$ operator:

.. math::

    \ket{\phi_i^a}
        = T\ket{\tilde\phi_i^a}
        = \left(1+\sum_{a'} T^{a'}\right) \ket{\tilde\phi_i^a}

        = (1+T^a) \ket{\tilde\phi_i^a}

Because $T^a$ only acts in the sphere, it follows that

.. math::

        \ket{\phi_i^a} = \ket{\tilde\phi_i^a}\quad\quad
            \mbox{for $r>r_c^a$}

outside the sphere (i.e.
$\braket{{\bf r} | \phi_i^a} = \braket{{\bf r} | \tilde\phi_i^a}$
for $r>r_c^a$).
