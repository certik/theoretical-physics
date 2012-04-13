Hartree-Fock (HF) Method
========================

Derivation
----------

The interacting Hamiltonian for many body Schrödinger equation
is (see the general QFT notes for derivation):

.. math::

    i\hbar\partial_t\ket{\Psi(t)} = \hat H\ket{\Psi(t)}

    \hat H = \hat T + \hat V = \sum_{ij} c_i^\dag\braket{i|T|j}c_j +
        \half \sum_{ijkl} c_i^\dag c_j^\dag\braket{ij|V|kl}c_l c_k

where $\ket{i}$ are spin orbitals (thus the integration over $\omega$ below)
and:

.. math::

    \braket{i|T|j} = \int \chi_i^*({\bf x}) \left(
        -\half\nabla^2 - \sum_n {Z_n\over | {\bf x} -{\bf R}_n | }\right)
            \chi_j({\bf x})\d^3 x\, \d\omega

    \braket{ij|V|kl} = \int \chi_i^*({\bf x}) \chi_j^*({\bf y})
        {1\over | {\bf x} - {\bf y} | } \chi_k({\bf x}) \chi_l({\bf y})
            \d^3 x\, \d\omega_x\,
            \d^3 y\, \d\omega_y

We would like to minimize the energy $E = \braket{\Psi | \hat H | \Psi }$ using
the following basis for $Z$ electrons:

.. math::

    \ket{\Psi} = c_1^\dag c_2^\dag \cdots c_Z^\dag\ket{0}

We express the energy $E$ in this basis:

.. math::

    E = \braket{\Psi | \hat H | \Psi } =

    = \bra{0}c_Z\cdots c_2 c_1 \hat H
        c_1^\dag c_2^\dag \cdots c_Z^\dag\ket{0} =

    = \bra{0}c_Z\cdots c_2 c_1
    \left(\sum_{i,j=1}^Z c_i^\dag\braket{i|T|j}c_j +
        \half \sum_{i,j,k,l=1}^Z c_i^\dag c_j^\dag\braket{ij|V|kl}c_l c_k\right)
        c_1^\dag c_2^\dag \cdots c_Z^\dag\ket{0} =

    = \sum_{i=1}^Z \braket{i|T|i} +
        \half \sum_{i,j=1}^Z \left(\braket{ij|V|ij}-\braket{ij|V|ji}\right)

We minimize it with the constrain $\braket{i|j} = \delta_{ij}$:

.. math::

    \delta \left(E - \sum_{i,j=1}^Z \epsilon_{ij} \braket{i|j}\right) = 0

We obtain:

.. math::
    :label: hfeq0

    T \ket{i} + \sum_{j=1}^Z \left(\braket{j|V|ij}-\braket{j|V|ji}\right)
        = \epsilon_i \ket{i}

in the $x$-representation:

.. math::

    \braket{{\bf x} | T | i}
        + \sum_{j=1}^Z \left(\bra{{\bf x}}\braket{j|V|ij}-
            \bra{{\bf x}}\braket{j|V|ji}\right)
        = \epsilon_i \braket{{\bf x} | i}

    \braket{{\bf x} | T | i}
        + \sum_{j=1}^Z \left(\braket{j{\bf x}|V|ij}-
            \braket{j{\bf x}|V|ji}\right)
        = \epsilon_i \braket{{\bf x} | i}

And writing the individual terms explicitly (in this section, all orbitals are
*spin* orbitals):

.. math::

    \braket{{\bf x} | i} = \psi_i({\bf x})

    \braket{{\bf x} | T | i}
        = \left(-\half \nabla^2 -\sum_n {Z_n\over | {\bf x} -{\bf R}_n | }
            \right)\psi_i({\bf x})

    \braket{j{\bf x}|V|ij}
        = \int \psi_j^*({\bf y}){1\over|{\bf x}-{\bf y}|}
            \psi_i({\bf x})\psi_j({\bf y}) \d^3 y
        = \int {|\psi_j({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_i({\bf x})

    \braket{j{\bf x}|V|ji}
        = \int \psi_j^*({\bf y}){1\over|{\bf x}-{\bf y}|}
            \psi_j({\bf x})\psi_i({\bf y}) \d^3 y
        = \int {\psi_i({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_j({\bf x})

we get the Hartree-Fock equations:

.. math::
    :label: hfeq

    \left(-\half \nabla^2 -{Z\over |{\bf x}|}
    +
    \int {\sum_{j=1}^Z|\psi_j({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y\right)\psi_i({\bf x})
    - \sum_{j=1}^Z\int {\psi_i({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_j({\bf x})
    =
    \epsilon_i \psi_i({\bf x})

Let's introduce the number density $n({\bf x})$, Hartree potential $V_H({\bf
x})$ and nonlocal exchange potential $V_x$ with its kernel $U({\bf x}, {\bf
y})$:

.. math::

    n({\bf x}) = \sum_{j=1}^Z|\psi_j({\bf y})|^2

    V_H({\bf x}) = \int {\sum_{j=1}^Z|\psi_j({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y
        = \int {n({\bf y})\over|{\bf x}-{\bf y}|} \d^3 y

    \hat V_x f({\bf x}) =
    - \sum_{j=1}^Z\int {f({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_j({\bf x})
    = \int U({\bf x}, {\bf y}) f({\bf y}) \d^3 y

    U({\bf x}, {\bf y}) =
    - \sum_{j=1}^Z {\psi_j({\bf x})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}

then we can write the HF equations as:

.. math::

    \left(-\half \nabla^2 -{Z\over |{\bf x}|} + V_H({\bf x})
        + \hat V_x
        \right)\psi_i({\bf x})
    =
    \epsilon_i \psi_i({\bf x})

    \left(-\half \nabla^2 -{Z\over |{\bf x}|} + V_H({\bf x})
        \right)\psi_i({\bf x})
    + \int U({\bf x}, {\bf y}) \psi_i({\bf y}) \d^3 y
    =
    \epsilon_i \psi_i({\bf x})

The Hartree potential can be calculated by solving the Poisson equation:

.. math::

    \nabla^2V_H({\bf x}) = -4\pi n({\bf x})

where:

.. math::

    n({\bf x}) = \sum_{i=1}^Z |\psi_i({\bf x})|^2

The application of the exchange potential $\hat V_x$ on any function
$f({\bf x})$ can be calculated by:

.. math::

    \hat V_x f({\bf x}) = - \sum_{j=1}^Z W_{fj}({\bf x})\psi_j({\bf x})

    W_{fj}({\bf x}) = \int {f({\bf y})\psi_j^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y

    \nabla^2 W_{fj}({\bf x}) = -4\pi f({\bf x})\psi_j^*({\bf x})

Roothaan Equations For Closed Shell Systems
-------------------------------------------

Starting from :eq:`hfeq0` and integrating over spins we get (here
$i$, $k$ are spatial orbitals, not spin orbitals):

.. math::
    :label: hfeq01

    T \ket{i} + \sum_{k=1}^{N/2}
        \left(2\braket{k|V|ik}-\braket{k|V|ki}\right) = \epsilon_i \ket{i}

We introduce basis functions $\ket{\mu}$ by (below the greek letters are basis
functions, latin letters are spatial orbitals):

.. math::

    \ket{i} = \sum_\nu C_{\nu i} \ket{\nu}

substitute into :eq:`hfeq01` and multiply by $\bra{\mu}$ from the left:

.. math::
    :label: hfeq02

    \sum_\nu \braket{\mu | T | \nu} C_{\nu i}
        + \sum_\nu\sum_{k=1}^{N/2} \left(2\braket{\mu k|V|\nu k}
            -\braket{\mu k|V|k\nu}\right) C_{\nu i}
        = \epsilon_i \sum_\nu \braket{\mu | \nu} C_{\nu i}

Now we expand the functions $\ket{k}$:

.. math::
    :label: hfeq03

    \sum_\nu \braket{\mu | T | \nu} C_{\nu i}
        + \sum_\nu \sum_{\alpha\beta}
            \left(2\sum_{k=1}^{N/2} C_{\alpha k} C_{\beta k}^* \right)
            \left(\braket{\mu \beta|V|\nu \alpha}
                -\half\braket{\mu \beta|V|\alpha \nu}\right) C_{\nu i}
        = \epsilon_i \sum_\nu \braket{\mu | \nu} C_{\nu i}

we introduce the density matrix:

.. math::

    \hat\rho
        = 2 \sum_{k=1}^{N/2} \ket{k}\bra{k}
        = \sum_{\alpha\beta} \ket{\alpha} 2 \sum_{k=1}^{N/2}
            C_{\alpha k} C_{\beta k}^*\bra{\beta}
        = \sum_{\alpha\beta} \ket{\alpha}P_{\alpha\beta}\bra{\beta}

    P_{\alpha\beta} = 2 \sum_{k=1}^{N/2} C_{\alpha k} C_{\beta k}^*

and get:

.. math::
    :label: hfeq04

    \sum_\nu \left( \braket{\mu | T | \nu}
        + \sum_{\alpha\beta}
            P_{\alpha\beta}
            \left(\braket{\mu \beta|V|\nu \alpha}
                -\half \braket{\mu \beta|V|\alpha \nu}\right) \right) C_{\nu i}
        = \epsilon_i \sum_\nu \braket{\mu | \nu} C_{\nu i}

introducing:

.. math::

    F_{\mu\nu} = H_{\mu\nu}^{\mbox{core}} + G_{\mu\nu}

    H_{\mu\nu}^{\mbox{core}} = \braket{\mu | T | \nu}

    G_{\mu\nu} = \sum_{\alpha\beta} P_{\alpha\beta}
            \left(\braket{\mu \beta|V|\nu \alpha}
                -\half \braket{\mu \beta|V|\alpha \nu}\right)

    S_{\mu\nu} = \braket{\mu | \nu}

the equation :eq:`hfeq04` is:

.. math::
    :label: roothaan1

    \sum_\nu F_{\mu\nu} C_{\nu i}
        = \epsilon_i \sum_\nu S_{\mu\nu} C_{\nu i}

These are the Roothaan equations. It is a generalized eigenvalue problem.

The same thing can be derived in $x$-representation
starting from :eq:`hfeq` and introducing spatial orbitals:

.. math::
    :label: hfeq2

    \left(-\half \nabla^2 -{Z\over |{\bf x}|}
    +
    \int {2\sum_{k=1}^{N/2}|\psi_k({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y\right)\psi_i({\bf x})
    - \sum_{k=1}^{N/2}\int {\psi_i({\bf y})\psi_k^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_k({\bf x})
    =
    \epsilon_i \psi_i({\bf x})

We introduce basis functions $\phi_\mu$:

.. math::

    \psi_i({\bf x}) = \sum_\nu C_{\nu i} \phi_\nu({\bf x})

substitute into :eq:`hfeq2` and also multiply the whole equation by
$\phi_\mu^*$ and integrate over ${\bf x}$:

.. math::
    :label: hfeq3

    \sum_\nu
    \int
    \phi_\mu^*({\bf x})
    \left(-\half \nabla^2 -{Z\over |{\bf x}|}
    +
    \int {2\sum_{k=1}^{N/2}|\psi_k({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y\right)\phi_\nu({\bf x}) \d^3 x\, C_{\nu i}

    -\sum_\nu
    \int
    \phi_\mu^*({\bf x})
    \sum_{k=1}^{N/2}\int {\phi_\nu({\bf y})\psi_k^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_k({\bf x})\d^3 x\, C_{\nu i}
    =
    \epsilon_i
    \sum_\nu
    \int \phi_\mu^*({\bf x}) \phi_\nu({\bf x})\d^3 x
    \, C_{\nu i}

This can be written as:

.. math::

    \sum_\nu F_{\mu\nu} C_{\nu i} = \epsilon_i \sum_\nu S_{\mu\nu} C_{\nu i}

    F_{\mu\nu} = H_{\mu\nu}^{\mbox{core}} + G_{\mu\nu}
        = T_{\mu\nu} + V_{\mu\nu} + G_{\mu\nu}

where:

.. math::

    T_{\mu\nu} =
            \int \phi_\mu^*({\bf x}) \left(-\half \nabla^2 \right)
            \phi_\nu({\bf x}) \d^3 x
        =
            \half \int \nabla \phi_\mu^*({\bf x}) \cdot
                \nabla \phi_\nu({\bf x}) \d^3 x

    V_{\mu\nu} =
        \int \phi_\mu^*({\bf x}) \left(-{Z\over |{\bf x}|}\right)
        \phi_\nu({\bf x}) \d^3 x

    G_{\mu\nu} =
        \int \phi_\mu^*({\bf x}) \left(
    \int {2\sum_{k=1}^{N/2}|\psi_k({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y\right)\phi_\nu({\bf x}) \d^3 x
    -\int
    \phi_\mu^*({\bf x})
    \sum_{k=1}^{N/2}\int {\phi_\nu({\bf y})\psi_k^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\psi_k({\bf x})\d^3 x


    S_{\mu\nu} = \int \phi_\mu^*({\bf x}) \phi_\nu({\bf x})\d^3 x

Introducing the density matrix and density:

.. math::

    \rho({\bf x}, {\bf y}) = \braket{{\bf x} | \hat \rho | {\bf y}}
    = \sum_{\alpha\beta} \braket{{\bf x}|\alpha}P_{\alpha\beta}
        \braket{\beta|{\bf y}}
    = \sum_{\alpha\beta} \phi_\alpha({\bf x}) P_{\alpha\beta}
        \phi_\beta^*({\bf y})


    P_{\alpha\beta} = 2 \sum_{k=1}^{N/2} C_{\alpha k} C_{\beta k}^*

    \rho({\bf x}) = 2 \sum_{k=1}^{N/2} | \psi_k({\bf x})|^2
        = 2 \sum_{k=1}^{N/2} | \braket{{\bf x}|k}|^2
        = 2 \sum_{k=1}^{N/2} \braket{{\bf x}|k}\braket{k|{\bf x}}
        = \braket{{\bf x}|\hat \rho|{\bf x}}
        = \sum_{\alpha\beta} \phi_\alpha({\bf x}) P_{\alpha\beta}
            \phi_\beta^*({\bf x})

Expanding the $\psi_k$ functions and using the density matrix we get for
$G_{\mu\nu}$:

.. math::

    G_{\mu\nu} =
        \sum_{\alpha\beta} P_{\alpha\beta}
        \int \phi_\mu^*({\bf x}) \left(
    \int {\phi_\beta^*({\bf y})\phi_\alpha({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\right)\phi_\nu({\bf x}) \d^3 x
    -\half \sum_{\alpha\beta} P_{\alpha\beta}
    \int
    \phi_\mu^*({\bf x})
    \int {\phi_\nu({\bf y})\phi_\beta^*({\bf y})\over|{\bf x}-{\bf y}|}
            \d^3 y\,\,\phi_\alpha({\bf x})\d^3 x

or

.. math::

    G_{\mu\nu} =
        \sum_{\alpha\beta} P_{\alpha\beta}
        \int {\phi_\mu^*({\bf x}) \phi_\nu({\bf x}) \phi_\beta^*({\bf y})
                \phi_\alpha({\bf y})
            -\half
            \phi_\mu^*({\bf x}) \phi_\alpha({\bf x}) \phi_\beta^*({\bf y})
                \phi_\nu({\bf y}) \over
                        | {\bf x}-{\bf y}|}
            \d^3 x\, \d^3 y

        \equiv \sum_{\alpha\beta} P_{\alpha\beta}
            \left(\braket{\mu \beta|{1\over r_{12}}|\nu \alpha}
                -\half \braket{\mu \beta|{1\over r_{12}}|\alpha \nu}\right)

In physical and chemistry notation this is written as:

.. math::

    G_{\mu\nu} = \sum_{\alpha\beta} P_{\alpha\beta}
            \left(\braket{\mu \beta|\nu \alpha}
                -\half \braket{\mu \beta|\alpha \nu}\right)
        = \sum_{\alpha\beta} P_{\alpha\beta}
            \left((\mu \nu|\beta \alpha) -\half (\mu \alpha|\beta \nu)\right)

Note that this notation implicitly assumes the ${1\over r_{12}}$ factor, so
for example $\braket{\mu \beta|\nu \alpha}$ actually means
$\braket{\mu \beta|{1\over r_{12}}|\nu \alpha}$ and one has to understand this
from the context.

General Matrix Elements in Spherical Symmetry
---------------------------------------------

Overlap
~~~~~~~

The overlap matrix element is:

.. math::

    S_{ij} = \int \phi_i^*({\bf x}) \phi_j({\bf x})\d^3 x

We will use the following functions:

.. math::

    \phi_i({\bf x}) = {P_{n_1l_1}(r)\over r} Y_{l_1m_1}(\Omega)

    \phi_j({\bf x}) = {P_{n_2l_2}(r)\over r} Y_{l_2m_2}(\Omega)

and we get:

.. math::

    S_{ij} = \int {P_{n_1l_1}(r)\over r} Y_{l_1m_1}^*(\Omega)
        {P_{n_2l_2}(r)\over r} Y_{l_2m_2}(\Omega) r^2 \d r \d \Omega =

    = \delta_{l_1 l_2} \delta_{m_1 m_2} \int P_{n_1l_1}(r) P_{n_2l_2}(r) \d r

Potential
~~~~~~~~~

The potential matrix element is:

.. math::

    V_{ij} =
        \int \phi_i^*({\bf x}) \left(-{Z\over |{\bf x}|}\right)
        \phi_j({\bf x}) \d^3 x

We will use the following functions:

.. math::

    \phi_i({\bf x}) = {P_{n_1l_1}(r)\over r} Y_{l_1m_1}(\Omega)

    \phi_j({\bf x}) = {P_{n_2l_2}(r)\over r} Y_{l_2m_2}(\Omega)

and we get:

.. math::

    V_{ij} = \int {P_{n_1l_1}(r)\over r} Y_{l_1m_1}^*(\Omega)
        \left(-{Z\over r}\right)
        {P_{n_2l_2}(r)\over r} Y_{l_2m_2}(\Omega) r^2 \d r \d \Omega =

    = \delta_{l_1 l_2} \delta_{m_1 m_2} \int P_{n_1l_1}(r)
        \left(-{Z\over r}\right) P_{n_2l_2}(r) \d r

Kinetic
~~~~~~~

The kinetic matrix element is:

.. math::

    T_{ij} =
            \int \phi_i^*({\bf x}) \left(-\half \nabla^2 \right)
            \phi_j({\bf x}) \d^3 x

We will use the following functions:

.. math::

    \phi_i({\bf x}) = {P_{n_1l_1}(r)\over r} Y_{l_1m_1}(\Omega)

    \phi_j({\bf x}) = {P_{n_2l_2}(r)\over r} Y_{l_2m_2}(\Omega)

and we get:

.. math::

    T_{ij}
        = \int {P_{n_1l_1}(r)\over r} Y_{l_1m_1}^*(\Omega)
            \left(\left(-\half \nabla^2\right)
            {P_{n_2l_2}(r)\over r} Y_{l_2m_2}(\Omega) \right) r^2 \d r \d
            \Omega =

        = \int {P_{n_1l_1}(r)\over r} Y_{l_1m_1}^*(\Omega)
            \left(\left(-\half {\partial^2\over\partial r^2}
                -{1\over r}{\partial\over\partial r}
                +{l_2 (l_2+1)\over 2r^2}\right)
            {P_{n_2l_2}(r)\over r} Y_{l_2m_2}(\Omega) \right) r^2 \d r \d
            \Omega =

        = \delta_{l_1 l_2} \delta_{m_1 m_2}
        \int {P_{n_1l_1}(r)\over r}
            \left(\left(-\half {\partial^2\over\partial r^2}
                -{1\over r}{\partial\over\partial r}
                +{l_2 (l_2+1)\over 2r^2}\right)
            {P_{n_2l_2}(r)\over r} \right) r^2 \d r =

        = \delta_{l_1 l_2} \delta_{m_1 m_2}
        \int {P_{n_1l_1}(r)\over r}
            \left(\left(-{1\over 2r} {\partial^2\over\partial r^2}r
                +{l_2 (l_2+1)\over 2 r^2}\right)
            {P_{n_2l_2}(r)\over r} \right) r^2 \d r =

        = \delta_{l_1 l_2} \delta_{m_1 m_2}
        \int P_{n_1l_1}(r)
            \left(-\half {\partial^2\over\partial r^2}
                +{l_2 (l_2+1)\over 2 r^2}\right)
            P_{n_2l_2}(r) \d r =

        = \delta_{l_1 l_2} \delta_{m_1 m_2}
        \int \left( -\half P_{n_1l_1}(r) P_{n_2l_2}''(r)
                +P_{n_1l_1}(r) {l_2 (l_2+1)\over 2 r^2} P_{n_2l_2}(r) \right)
            \d r =

        = \delta_{l_1 l_2} \delta_{m_1 m_2}
        \int \left( \half P_{n_1l_1}'(r) P_{n_2l_2}'(r)
                +P_{n_1l_1}(r) {l_2 (l_2+1)\over 2 r^2} P_{n_2l_2}(r) \right)
            \d r

Hartree Potential (Direct Term)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The direct (Hartree) term is given by:

.. math::

    J_{\mu\nu} = \int \phi_\mu^*({\bf x}) V_H({\bf x}) \phi_\nu({\bf x}) \d^3 x

where the Hartree potential $V_H({\bf x})$ is given by:

.. math::

    V_H({\bf x}) = \int {2\sum_{k=1}^{N/2}|\psi_k({\bf y})|^2\over
            |{\bf x}-{\bf y}|} \d^3 y
        = \int {n({\bf y})\over
            |{\bf x}-{\bf y}|} \d^3 y

where the number density $n({\bf x})$ is given by:

.. math::

    n({\bf x}) = 2 \sum_{k=1}^{N/2} | \psi_k({\bf x})|^2
        = \sum_{\alpha\beta} \phi_\alpha({\bf x}) P_{\alpha\beta}
            \phi_\beta^*({\bf x})

All together we get:

.. math::
    :label: hartree1

    J_{\mu\nu} = \sum_{\alpha\beta} P_{\alpha\beta}
        \int {\phi_\mu^*({\bf x}) \phi_\alpha({\bf y})
                \phi_\beta^*({\bf y}) \phi_\nu({\bf x}) \over
                |{\bf x}-{\bf y}| } \d^3 x \d^3 y
        = \sum_{\alpha\beta} P_{\alpha\beta}
            \braket{\mu \beta|\nu \alpha}
        = \sum_{\alpha\beta} P_{\alpha\beta}
            (\mu \nu|\beta \alpha)

In spherical symmetry, we get (see :ref:`hartree_spherical` for derivation):

.. math::
    :label: hartree2

    J_{\mu\nu} = \int P_\mu V_H(r) P_\nu \d r  = \sum_{k} 2(2l_k+1)
        R^0(\mu, k, \nu, k)

Here we sum over the occupied radial orbitals $k$. This sum is already carried
out in $P_{\alpha\beta}$ in :eq:`hartree1`. On the other hand, :eq:`hartree2`
has the sum over the magnetic number $m$ carried out (thus the $2l+1$ term),
while in :eq:`hartree1` this sum is part of the sum over $\alpha=(n, l, m)$.

Two particle
~~~~~~~~~~~~

The two particle matrix element is:

.. math::
    :label: twoint

    (ij|kl) = \braket{ik|jl} =
        \int {\psi_i^*({\bf x})\psi_j({\bf x})\psi_k^*({\bf x}')\psi_l({\bf x}')
            \over | {\bf x} - {\bf x}' |} \d^3 x \d^3 x'

The $\braket{ik|jl}$ is called the physicists' notation because
the $\ket{jl}$ and $\ket{ik}$ kets are:

.. math::

    \ket{jl}=\psi_j({\bf x})\psi_l({\bf x}')

    \ket{ik}=\psi_i({\bf x})\psi_k({\bf x}')

The $(ij|kl)$ is called the chemists' notation. From :eq:`twoint` the
symmetries of $(ij|kl)$ are exchange of $i$ with $j$ or $k$ with $l$ or the
$ij$ and $kl$ pairs:

.. math::

    (ij|kl) = (ji|kl) = (ij|lk) = (ji|lk) =

    = (kl|ij) = (lk|ij) = (kl|ji) = (lk|ji)

So if we view $(ij|kl)$ as two boxes $(\cdot | \cdot )$ then we can permute the
labels in the given box "$\cdot$", as well as exchange the boxes (the only
thing we cannot do is to take one particle from one box and put it into the
other). As such the box "$\cdot$" is a pair of two electrons (in any order) and
the two electron integral assigns a unique number to a pair of such boxes (in
any order). The symmetries of the $\braket{ik|jl}$ symbol are:

.. math::

    \braket{ik|jl} = \braket{jk|il} = \braket{il|jk} = \braket{jl|ik} =

    = \braket{ki|lj} = \braket{li|kj} = \braket{kj|li} = \braket{lj|ki}


We use the following functions for $\psi$:

.. math::

    \psi_i({\bf x}) = {P_{n_1l_1}(r)\over r} Y_{l_1m_1}(\Omega)

    \psi_j({\bf x}) = {P_{n_1'l_1'}(r)\over r} Y_{l_1'm_1'}(\Omega)

    \psi_k({\bf x}) = {P_{n_2l_2}(r)\over r} Y_{l_2m_2}(\Omega)

    \psi_l({\bf x}) = {P_{n_2'l_2'}(r)\over r} Y_{l_2'm_2'}(\Omega)

And the multipole expansion:

.. math::

    {1\over |{\bf x}-{\bf x}'|}
        = \sum_{k,q}{r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}Y_{kq}(\Omega)Y_{kq}^*(\Omega')

And we get:

.. math::

    (ij|kl) = \braket{ik|jl} = \braket{l_1 m_1 l_2 m_2 |
        {1\over |{\bf x} - {\bf x}'|} | l_1' m_1' l_2' m_2'} =

    =\int {\psi_i^*({\bf x})\psi_j({\bf x})\psi_k^*({\bf x}')\psi_l({\bf x}')
        \over |{\bf x} - {\bf x}'|} \d^3 x \d^3 x' =

    = \int
        {P_{n_1l_1}(r)\over r} Y_{l_1m_1}^*(\Omega)
        {P_{n_1'l_1'}(r)\over r} Y_{l_1'm_1'}(\Omega)
        {P_{n_2l_2}(r')\over r'} Y_{l_2m_2}^*(\Omega')
        {P_{n_2'l_2'}(r')\over r'} Y_{l_2'm_2'}(\Omega')

        \sum_{k,q}{r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}Y_{kq}(\Omega)Y_{kq}^*(\Omega')
        r^2 r'^2 \d r \d r' \d \Omega \d \Omega' =

    =
    \sum_{k,q}
    \int
        Y_{l_1m_1}^*(\Omega)
        Y_{l_1'm_1'}(\Omega)
        Y_{kq}(\Omega)
        \d \Omega
      \int
        Y_{l_2m_2}^*(\Omega')
        Y_{l_2'm_2'}(\Omega')
        Y_{kq}^*(\Omega')
        \d \Omega'

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r' =

    =
    \sum_{k,q}
    (-1)^{m_1+m_2+q}
    \int
        Y_{l_1,-m_1}(\Omega)
        Y_{l_1'm_1'}(\Omega)
        Y_{kq}(\Omega)
        \d \Omega
      \int
        Y_{l_2,-m_2}(\Omega')
        Y_{l_2'm_2'}(\Omega')
        Y_{k,-q}(\Omega')
        \d \Omega'

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r' =

    =
    \sum_{k,q}
    (-1)^{m_1+m_2+q}
    \sqrt{(2l_1+1)(2l_1'+1)(2k+1)\over 4\pi}
            \begin{pmatrix} l_1 & l_1' & k \\ 0 & 0 & 0 \end{pmatrix}
                    \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & q
                    \end{pmatrix}

    \sqrt{(2l_2+1)(2l_2'+1)(2k+1)\over 4\pi}
            \begin{pmatrix} l_2 & l_2' & k \\ 0 & 0 & 0 \end{pmatrix}
                    \begin{pmatrix} l_2 & l_2' & k \\ -m_2 & m_2' & -q
                    \end{pmatrix}

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r' =

    =
    \sum_k
    \sqrt{(2l_1+1)(2l_1'+1)(2l_2+1)(2l_2'+1)}
    \begin{pmatrix} l_1 & l_1' & k \\ 0 & 0 & 0 \end{pmatrix}
    \begin{pmatrix} l_2 & l_2' & k \\ 0 & 0 & 0 \end{pmatrix}

    \sum_{q=-k}^k (-1)^{m_1+m_2+q}
        \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & q \end{pmatrix}
        \begin{pmatrix} l_2 & l_2' & k \\ -m_2 & m_2' & -q \end{pmatrix}

      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r' =

    =
    \sum_{k=\max(| l_1-l_1'| ,| l_2-l_2'| , | m_1-m_1'| )}^{
        \min(l_1+l_1', l_2+l_2')
    }\!\!\!\!\!\!\!\!\!\!\!\!
    \sqrt{(2l_1+1)(2l_1'+1)(2l_2+1)(2l_2'+1)}

    (-1)^{m_1+m_2'} \delta_{m_1+m_2- m_1'-m_2', 0}
    \begin{pmatrix} l_1 & l_1' & k \\ 0 & 0 & 0 \end{pmatrix}
    \begin{pmatrix} l_2 & l_2' & k \\ 0 & 0 & 0 \end{pmatrix}

        \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & m_1-m_1' \end{pmatrix}
        \begin{pmatrix} l_2 & l_2' & k \\ -m_2 & m_2' & m_2-m_2' \end{pmatrix}

      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r'

In the last step we used the fact that the $3j$ symbols are zero unless
$-m_1+m_1'+q=0$
and $-m_2+m_2'-q=0$, from which it follows
that $q=m_1-m_1'=-m_2+m_2'$ and so one of the $3j$ symbols is zero
unless $m_1+m_2-m_1'-m_2'=0$, which is expressed by
$\delta_{m_1+m_2- m_1'-m_2', 0}$.
Given this condition, the sum over $q$ must be such
that one $q$ is equal to $m_1-m_1'=-m_2+m_2'$, which means that
$k \ge |m_1 - m_1'| = |m_2 - m_2'|$ otherwise the $3j$ symbols will be zero.
Finally, $k$ must also satisfy the conditions
$|l_1-l_1'| \le k \le l_1+l_1'$ and $|l_2-l_2'| \le k \le l_2+l_2'$.
The sign factor
$(-1)^{m_1+m_2+q} = (-1)^{m_1+m_2+m_1-m_1'} =(-1)^{m_1+m_2-m_2+m_2'}$
is equal to both $(-1)^{m_1+m_2'}$ and $(-1)^{m_2-m_1'}$ so we just used the
former.

We can write this using the $c^k$ symbols as:

.. math::

    (ij|kl) =
    \sum_{k=\max(| l_1-l_1'| ,| l_2-l_2'| , | m_1-m_1'| )}^{
        \min(l_1+l_1', l_2+l_2')
    }\!\!\!\!\!\!\!\!\!\!\!\!
    \sqrt{(2l_1+1)(2l_1'+1)(2l_2+1)(2l_2'+1)}

    (-1)^{m_2-m_2'} (-1)^{-m_1} (-1)^{-m_2} \delta_{m_1+m_2- m_1'-m_2', 0}
    \begin{pmatrix} l_1 & l_1' & k \\ 0 & 0 & 0 \end{pmatrix}
    \begin{pmatrix} l_2 & l_2' & k \\ 0 & 0 & 0 \end{pmatrix}

        \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & m_1-m_1' \end{pmatrix}
        \begin{pmatrix} l_2 & l_2' & k \\ -m_2 & m_2' & m_2-m_2' \end{pmatrix}

      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r' =

    =
    \sum_{k=\max(| l_1-l_1'| ,| l_2-l_2'| , | m_1-m_1'| )}^{
        \min(l_1+l_1', l_2+l_2')
    }\!\!\!\!\!\!\!\!\!\!\!\!
    c^k(l_1, m_1, l_1', m_1')
    c^k(l_2, m_2, l_2', m_2')

    (-1)^{m_2-m_2'} \delta_{m_1+m_2- m_1'-m_2', 0}

      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r'

    =
    \sum_{k=\max(| l_1-l_1'| ,| l_2-l_2'| , | m_1-m_1'| )}^{
        \min(l_1+l_1', l_2+l_2')
    }\!\!\!\!\!\!\!\!\!\!\!\!
    c^k(l_1, m_1, l_1', m_1')
    c^k(l_2', m_2', l_2, m_2)

    \delta_{m_1+m_2- m_1'-m_2', 0}

      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r'

We can also couple the angular momenta as follows:

.. math::

    \ket{l_1 l_2 LM} = \sum_{m_1 m_2} (l_1 m_1 l_2 m_2 | LM)
        \ket{l_1 m_1} \ket{l_2 m_2} =

    = \sum_{m_1 m_2} (-1)^{l_1-l_2+M}\sqrt{2L+1}
        \begin{pmatrix} l_1 & l_2 & L \\ m_1 & m_2 & -M \end{pmatrix}
        \ket{l_1 m_1} \ket{l_2 m_2}

and we get for the matrix elements:

.. math::

    \braket{l_1 l_2 LM  | {1\over |{\bf x} - {\bf x}'|} | l_1' l_2' L' M'} =

    = \sum_{m_1 m_2} \sum_{m_1' m_2'} (-1)^{l_1-l_2+l_1'-l_2'+M+M'}
        \sqrt{(2L+1)(2L'+1)}

        \begin{pmatrix} l_1 & l_2 & L \\ m_1 & m_2 & -M \end{pmatrix}
        \begin{pmatrix} l_1' & l_2' & L' \\ m_1' & m_2' & -M' \end{pmatrix}

        \bra{l_1 m_1} \bra{l_2 m_2}
        {1\over |{\bf x} - {\bf x}'|}
        \ket{l_1' m_1'} \ket{l_2 m_2'} =

    = \sum_{m_1 m_2} \sum_{m_1' m_2'} (-1)^{l_1-l_2+l_1'-l_2'+M+M'}
        \sqrt{(2L+1)(2L'+1)}

        \begin{pmatrix} l_1 & l_2 & L \\ m_1 & m_2 & -M \end{pmatrix}
        \begin{pmatrix} l_1' & l_2' & L' \\ m_1' & m_2' & -M' \end{pmatrix}

        (ij|kl) =

    = \sum_{m_1 m_2} \sum_{m_1' m_2'} (-1)^{l_1-l_2+l_1'-l_2'+M+M'}
        \sqrt{(2L+1)(2L'+1)}

        \begin{pmatrix} l_1 & l_2 & L \\ m_1 & m_2 & -M \end{pmatrix}
        \begin{pmatrix} l_1' & l_2' & L' \\ m_1' & m_2' & -M' \end{pmatrix}

    \sum_k
    \sqrt{(2l_1+1)(2l_1'+1)(2l_2+1)(2l_2'+1)}
    \begin{pmatrix} l_1 & l_1' & k \\ 0 & 0 & 0 \end{pmatrix}
    \begin{pmatrix} l_2 & l_2' & k \\ 0 & 0 & 0 \end{pmatrix}

    \sum_{q=-k}^k (-1)^{m_1+m_2+q}
        \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & q \end{pmatrix}
        \begin{pmatrix} l_2 & l_2' & k \\ -m_2 & m_2' & -q \end{pmatrix}

      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r' =

    = \sum_{m_1 m_2} \sum_{m_1' m_2'} (-1)^{l_1-l_2+l_1'-l_2'}
        (2L+1)

        \delta_{MM'}\delta_{LL'}
        \begin{pmatrix} l_1 & l_2 & L \\ m_1 & m_2 & -M \end{pmatrix}
        \begin{pmatrix} l_1' & l_2' & L \\ m_1' & m_2' & -M \end{pmatrix}

    \sum_k
    \sqrt{(2l_1+1)(2l_1'+1)(2l_2+1)(2l_2'+1)}
    \begin{pmatrix} l_1 & l_1' & k \\ 0 & 0 & 0 \end{pmatrix}
    \begin{pmatrix} l_2 & l_2' & k \\ 0 & 0 & 0 \end{pmatrix}

    \sum_{q=-k}^k (-1)^{m_1+m_2+q}
        \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & q \end{pmatrix}
        \begin{pmatrix} l_2 & l_2' & k \\ -m_2 & m_2' & -q \end{pmatrix}

      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r' =

    = (-1)^{l_1-l_2+l_1'-l_2'} (2L+1)

    \sum_k
    \sqrt{(2l_1+1)(2l_1'+1)(2l_2+1)(2l_2'+1)}
    \begin{pmatrix} l_1 & l_1' & k \\ 0 & 0 & 0 \end{pmatrix}
    \begin{pmatrix} l_2 & l_2' & k \\ 0 & 0 & 0 \end{pmatrix}

        \delta_{MM'}\delta_{LL'} (-1)^{l_1+l_1'+L}
    \begin{Bmatrix} l_1 & l_2 & L \\ l_2' & l_1' & k \end{Bmatrix}

      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r' =

    = \sum_k
      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r'

        (-1)^{L-l_2-l_2'} (2L+1)
        \delta_{MM'}\delta_{LL'}\sqrt{(2l_1+1)(2l_1'+1)(2l_2+1)(2l_2'+1)}

    \begin{pmatrix} l_1 & l_1' & k \\ 0 & 0 & 0 \end{pmatrix}
    \begin{pmatrix} l_2 & l_2' & k \\ 0 & 0 & 0 \end{pmatrix}
    \begin{Bmatrix} l_1 & l_2 & L \\ l_2' & l_1' & k \end{Bmatrix} =

    = \sum_k
      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{n_1l_1}(r)
        P_{n_1'l_1'}(r)
        P_{n_2l_2}(r')
        P_{n_2'l_2'}(r')
        \d r \d r'

        (-1)^{l_1 + l_1' + L} (2L+1)

        \delta_{LL'}\delta_{MM'}\sqrt{(2l_1+1)(2l_1'+1)(2l_2+1)(2l_2'+1)}

    \begin{pmatrix} l_1 & k & l_1' \\ 0 & 0 & 0 \end{pmatrix}
    \begin{pmatrix} l_2 & k & l_2' \\ 0 & 0 & 0 \end{pmatrix}
    \begin{Bmatrix} l_1 & l_2 & L \\ l_2' & l_1' & k \end{Bmatrix}




Where we used the $6j$ symbol:

.. math::

    \begin{Bmatrix} l_1 & l_2 & L \\ l_2' & l_1' & k \end{Bmatrix}
    =\sum_{m_1 m_2 m_1' m_2' M q} (-1)^{l_1+l_2+l_1'+l_2'+L+k
        -m_1-m_2-m_1'-m_2'-M-q}

    \begin{pmatrix} l_1 & l_2 & L \\ m_1 & m_2 & -M \end{pmatrix}
    \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & q \end{pmatrix}
    \begin{pmatrix} l_2' & l_1' & L \\ m_2' & -m_1' & M \end{pmatrix}
    \begin{pmatrix} l_2' & l_2 & k \\ -m_2' & -m_2 & -q \end{pmatrix}
    =

    =\sum_{m_1 m_2 m_1' m_2' M q} (-1)^{l_1+l_2+l_1'+l_2'+L+k
        -m_1-m_2-m_1'-m_2'-M-q}

    \begin{pmatrix} l_1 & l_2 & L \\ m_1 & m_2 & -M \end{pmatrix}
    \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & q \end{pmatrix}
    \begin{pmatrix} l_1' & l_2' & L \\ m_1' & -m_2' & -M \end{pmatrix}
    (-1)^{l_2+l_2'+k}
    \begin{pmatrix} l_2 & l_2' & k \\ -m_2 & -m_2' & -q \end{pmatrix}
    =

    =\sum_{m_1 m_2 m_1' m_2' q} \delta_{M, m_1' + m_2'}
        (-1)^{l_1+l_1'+L} (-1)^{m_1+m_2+q}

    \begin{pmatrix} l_1 & l_2 & L \\ m_1 & m_2 & -M \end{pmatrix}
    \begin{pmatrix} l_1 & l_1' & k \\ -m_1 & m_1' & q \end{pmatrix}
    \begin{pmatrix} l_1' & l_2' & L \\ m_1' & +m_2' & -M \end{pmatrix}
    \begin{pmatrix} l_2 & l_2' & k \\ -m_2 & +m_2' & -q \end{pmatrix}

Where we have renamed $-m_2'$ to $m_2'$.

Slater Type Orbitals (STO)
--------------------------

In this section we express the matrix elements in the STO basis.
It turns out that all integrals that we need can be expressed in terms
of the following simple integral (where $n,\zeta \ge 0$):

.. math::
    :label: slater_basic

    \int_0^\infty r^n e^{-\zeta r} \d r
        =\int_0^\infty \left(x\over\zeta\right)^n e^{-r} {\d r\over\zeta}
        ={1\over\zeta^{n+1}} \int_0^\infty x^n e^{-r} \d r
        ={\Gamma(n+1)\over\zeta^{n+1}}
        ={n!\over\zeta^{n+1}}

The STO basis function for the radial Schrödinger equation for $P(r)$ is:

.. math::
    :label: sto_P

    P_{n\zeta}(r) = N_{n\zeta} r^n e^{-\zeta r}

Where the normalization constant $N_{n\zeta}$ is such that the STO orbital is
normalized as the radial wavefunction $P(r)$:

.. math::

    1 = \int_0^\infty P_{n\zeta}^2(r) \d r
        = N_{n\zeta}^2 \int_0^\infty r^{2n} e^{-2\zeta r} \d r
        = N_{n\zeta}^2 {(2n)!\over (2\zeta)^{2n+1}}

from which we get:

.. math::

    N_{n\zeta} = \sqrt{(2\zeta)^{2n+1}\over (2n)!}

Note that for $R(r)={P(r)\over r}$ we get the following STO basis function:

.. math::
    :label: sto_R

    R_{n\zeta}(r) = {P_{n\zeta}(r)\over r} = N_{n\zeta} r^{n-1} e^{-\zeta r}

One uses either :eq:`sto_P` or :eq:`sto_R` depending on whether one solves the
radial Schrödinger equation for $P$ or for $R={P\over r}$.

Overlap
~~~~~~~

.. math::

    \int P_{n_i \zeta_i}(r) P_{n_j \zeta_j}(r) \d r =

        = \int
            N_{n_i\zeta_i} r^{n_i} e^{-\zeta_i r}
            N_{n_j\zeta_j} r^{n_j} e^{-\zeta_j r}
         \d r =

        = N_{n_i\zeta_i} N_{n_j\zeta_j} \int
             r^{n_i + n_j} e^{-(\zeta_i+\zeta_j) r}
         \d r =

        = N_{n_i\zeta_i} N_{n_j\zeta_j}
            {(n_i + n_j)! \over  (\zeta_i+\zeta_j)^{n_i+n_j+1}}

Potential
~~~~~~~~~

.. math::

    \int P_{n_i\zeta_i}(r) \left(-{Z\over r}\right) P_{n_j\zeta_j}(r) \d r =

    = \int
        N_{n_i\zeta_i} r^{n_i} e^{-\zeta_i r}
        \left(-{Z\over r}\right)
        N_{n_j\zeta_j} r^{n_j} e^{-\zeta_j r}
        \d r =

    = -Z N_{n_i\zeta_i} N_{n_j\zeta_j} \int
         r^{n_i+n_j-1} e^{-(\zeta_i+\zeta_j) r}
        \d r =

    = -Z N_{n_i\zeta_i} N_{n_j\zeta_j}
        {(n_i + n_j - 1)! \over  (\zeta_i+\zeta_j)^{n_i+n_j}}

Kinetic
~~~~~~~

.. math::

    \int \left( \half P_{n_i\zeta_i}'(r) P_{n_j\zeta_j}'(r)
            +P_{n_i\zeta_i}(r) {l (l+1)\over 2 r^2} P_{n_j\zeta_j}(r) \right)
        \d r =

    = \half N_{n_i\zeta_i}N_{n_j\zeta_j}\int \left(
            {\d\over\d r}(r^{n_i} e^{-\zeta_i r})
            {\d\over\d r}(r^{n_j} e^{-\zeta_j r})
            +r^{n_i} e^{-\zeta_i r} {l (l+1)\over r^2}
                r^{n_j} e^{-\zeta_j r}
            \right)
        \d r =

    = \half N_{n_i\zeta_i}N_{n_j\zeta_j}\int \left(
            (n_i r^{n_i-1} e^{-\zeta_i r}
                            -\zeta_i r^{n_i} e^{-\zeta_i r})
                        (n_j r^{n_j-1} e^{-\zeta_j r}
                            -\zeta_j r^{n_j} e^{-\zeta_j r})
            +l (l+1) r^{n_i+n_j-2} e^{-(\zeta_i+\zeta_j) r}
            \right)
        \d r =

    = \half N_{n_i\zeta_i}N_{n_j\zeta_j}\int \left(
        \left(
                    {n_i n_j\over r^2}
                   -{n_i \zeta_j+n_j\zeta_i \over r}
                   +\zeta_i \zeta_j
                \right) r^{n_i+n_j} e^{-(\zeta_i+\zeta_j) r}
            +l (l+1) r^{n_i+n_j-2} e^{-(\zeta_i+\zeta_j) r}
            \right)
        \d r =

    = \half N_{n_i\zeta_i}N_{n_j\zeta_j}\int \left(
        (n_i n_j + l(l+1))       r^{n_i+n_j-2} e^{-(\zeta_i+\zeta_j) r}
       -(n_i \zeta_j+n_j\zeta_i) r^{n_i+n_j-1} e^{-(\zeta_i+\zeta_j) r}
       +\zeta_i \zeta_j          r^{n_i+n_j  } e^{-(\zeta_i+\zeta_j) r}
            \right)
        \d r =

    = \half N_{n_i\zeta_i}N_{n_j\zeta_j}\left(
        (n_i n_j + l(l+1))
            {(n_i + n_j - 2)! \over  (\zeta_i+\zeta_j)^{n_i +n_j - 1}}
       -(n_i \zeta_j+n_j\zeta_i)
            {(n_i + n_j - 1)! \over  (\zeta_i+\zeta_j)^{n_i +n_j    }}
       +\zeta_i \zeta_j
            {(n_i + n_j    )! \over  (\zeta_i+\zeta_j)^{n_i +n_j + 1}}
            \right)

Two particle
~~~~~~~~~~~~

In this section we also need the following integrals:

.. math::

    \int_u^\infty r^n e^{-\zeta r} \d r = {n!\over \zeta^{n+1}}
        e^{-\zeta u} \sum_{\nu=0}^n {u^\nu \zeta^\nu \over \nu!}

    \int_0^u r^n e^{-\zeta r} \d r = \int_0^\infty r^n e^{-\zeta r} \d r
        -\int_u^\infty r^n e^{-\zeta r} \d r =
    {n!\over \zeta^{n+1}}\left(1-
        e^{-\zeta u} \sum_{\nu=0}^n {u^\nu \zeta^\nu \over \nu!}\right)

The Slater integral is given by:

.. math::

    R^k(i, j, k, l) = \int_0^\infty {r_<^k\over r_>^{k+1}} P_i(r) P_k(r)
        P_j(r') P_l(r') \d r \d r' =

        = \int_0^\infty P_i(r) P_k(r) {Y^k(P_j P_l, r)\over r} \d r

where

.. math::

    Y^k(f(r), r) = r \int_0^\infty {r_<^k\over r_>^{k+1}} f(r') \d r'
        = {1\over r^k} \int_0^r r'^k f(r') \d r' + r^{k+1} \int_r^\infty
            {1\over r'^{k+1}} f(r') \d r'

and we get:

.. math::

    Y^k(P_j(r) P_l(r), r)
        = {1\over r^k} \int_0^r r'^k P_j(r') P_l(r') \d r'
            + r^{k+1} \int_r^\infty {1\over r'^{k+1}} P_j(r') P_l(r') \d r' =

        = {N_{n_j \zeta_j}N_{n_l \zeta_l}\over r^k} \int_0^r r'^k
                r'^{n_j}e^{-\zeta_j r'}
                r'^{n_l}e^{-\zeta_l r'} \d r'
            + N_{n_j \zeta_j}N_{n_l \zeta_l} r^{k+1}
                \int_r^\infty {1\over r'^{k+1}}
                r'^{n_j}e^{-\zeta_j r'}
                r'^{n_l}e^{-\zeta_l r'} \d r' =

        = {N_{n_j \zeta_j}N_{n_l \zeta_l}\over r^k} \int_0^r
                r'^{n_j+n_l+k}e^{-(\zeta_j+\zeta_l) r'} \d r'
            + N_{n_j \zeta_j}N_{n_l \zeta_l} r^{k+1}
                \int_r^\infty
                r'^{n_j+n_l-k-1}e^{-(\zeta_j+\zeta_l) r'} \d r' =

        = {N_{n_j \zeta_j}N_{n_l \zeta_l}\over r^k}
            {(n_j+n_l+k)!\over(\zeta_j+\zeta_l)^{n_j+n_l+k+1}} \left(
                1 - e^{-(\zeta_j+\zeta_l)r} \sum_{\nu=0}^{n_j+n_l+k}
                    { r^\nu(\zeta_j+\zeta_l)^\nu \over \nu! }
                \right) +

            + N_{n_j \zeta_j}N_{n_l \zeta_l} r^{k+1}
                {(n_j+n_l-k-1)!\over (\zeta_j+\zeta_l)^{n_j+n_l-k}}
                    e^{-(\zeta_j+\zeta_l)r}
                \sum_{\nu=0}^{n_j+n_l-k-1}{r^\nu(\zeta_j+\zeta_l)^\nu\over \nu!}

Putting everything together we get:

.. math::

    R^k(i, j, k, l)
        = N_{n_i \zeta_i}N_{n_j \zeta_j}N_{n_k \zeta_k}N_{n_l \zeta_l}
            \int_0^\infty
            r^{n_i}e^{-\zeta_i r}
            r^{n_k}e^{-\zeta_k r}
            {1\over r}
            \left(
        {1\over r^k}
            {(n_j+n_l+k)!\over(\zeta_j+\zeta_l)^{n_j+n_l+k+1}} \left(
                1 - e^{-(\zeta_j+\zeta_l)r} \sum_{\nu=0}^{n_j+n_l+k}
                    { r^\nu(\zeta_j+\zeta_l)^\nu \over \nu! }
                \right) + \right.

        \left.  + r^{k+1}
                {(n_j+n_l-k-1)!\over (\zeta_j+\zeta_l)^{n_j+n_l-k}}
                    e^{-(\zeta_j+\zeta_l)r}
                \sum_{\nu=0}^{n_j+n_l-k-1}{r^\nu(\zeta_j+\zeta_l)^\nu\over \nu!}
            \right)
            \d r =

        = N_{n_i \zeta_i}N_{n_j \zeta_j}N_{n_k \zeta_k}N_{n_l \zeta_l}
            \left(
            {(n_j+n_l+k)!\over(\zeta_j+\zeta_l)^{n_j+n_l+k+1}}
            \int_0^\infty
            r^{n_i+n_k-k-1}e^{-(\zeta_i+\zeta_k) r}
            \left(
                1 - e^{-(\zeta_j+\zeta_l)r} \sum_{\nu=0}^{n_j+n_l+k}
                    { r^\nu(\zeta_j+\zeta_l)^\nu \over \nu! }
                \right) \d r + \right.

        \left.  +
            \int_0^\infty
            e^{-(\zeta_i+\zeta_j+\zeta_k+\zeta_l) r}
                {(n_j+n_l-k-1)!\over (\zeta_j+\zeta_l)^{n_j+n_l-k}}
                \sum_{\nu=0}^{n_j+n_l-k-1}{
                    r^{n_i+n_k+k+\nu}(\zeta_j+\zeta_l)^\nu\over \nu!}
            \d r
            \right) =

        = N_{n_i \zeta_i}N_{n_j \zeta_j}N_{n_k \zeta_k}N_{n_l \zeta_l}
            \left(
            {(n_j+n_l+k)!\over(\zeta_j+\zeta_l)^{n_j+n_l+k+1}}
            \left(
                {(n_i+n_k-k-1)!\over (\zeta_i+\zeta_k)^{n_i+n_k-k}}
                - \sum_{\nu=0}^{n_j+n_l+k}
                    {(\zeta_j+\zeta_l)^\nu (n_i+n_k-k+\nu-1)! \over \nu!
                    (\zeta_i+\zeta_j+\zeta_k+\zeta_l)^{n_i+n_k-k+\nu}}
                \right) + \right.

        \left.  +
                {(n_j+n_l-k-1)!\over (\zeta_j+\zeta_l)^{n_j+n_l-k}}
                \sum_{\nu=0}^{n_j+n_l-k-1}{
                    (n_i+n_k+k+\nu)! (\zeta_j+\zeta_l)^\nu\over
                    \nu!(\zeta_i+\zeta_j+\zeta_k+\zeta_l)^{n_i+n_k+k+\nu+1}}
            \right) =

        = N_{n_i \zeta_i}N_{n_j \zeta_j}N_{n_k \zeta_k}N_{n_l \zeta_l}
            \left(
            {(n_j+n_l+k)!\over(\zeta_j+\zeta_l)^{n_j+n_l+k+1}}
            \left(
                {(n_i+n_k-k-1)!\over (\zeta_i+\zeta_k)^{n_i+n_k-k}}
                - H^{-k-1}_{jilk}
                \right) + \right.

        \left.  +
                {(n_j+n_l-k-1)!\over (\zeta_j+\zeta_l)^{n_j+n_l-k}}
                H^k_{jilk}
            \right) =

        = N_{n_i \zeta_i}N_{n_j \zeta_j}N_{n_k \zeta_k}N_{n_l \zeta_l}
            \left(
                {(n_i+n_k-k-1)!\over (\zeta_i+\zeta_k)^{n_i+n_k-k}}
                H^k_{ijkl}
            +
                {(n_j+n_l-k-1)!\over (\zeta_j+\zeta_l)^{n_j+n_l-k}}
                H^k_{jilk}
            \right)

where:

.. math::

    H^k_{ijkl} =
                \sum_{\nu=0}^{n_i+n_k-k-1}{
                    (n_j+n_l+k+\nu)! (\zeta_i+\zeta_k)^\nu\over
                    \nu!(\zeta_i+\zeta_j+\zeta_k+\zeta_l)^{n_j+n_l+k+\nu+1}}

Exchange Integral in Spherical Symmetry
---------------------------------------

Let's calculate the exchange integral

.. math::

    \int {\psi_i^*({\bf x})\psi_j({\bf x})\psi_j^*({\bf x}')\psi_i({\bf x}')
        \over |{\bf x} - {\bf x}'|} \d^3 x \d^3 x'

for the particular choice of the functions $\psi$:

.. math::

    \psi_i({\bf x}) = {P_{nl}(r)\over r} Y_{lm}(\Omega)

    \psi_j({\bf x}) = {P_{n'l'}(r)\over r} Y_{l'm'}(\Omega)

We use multipole expansion:

.. math::

    {1\over |{\bf x}-{\bf x}'|}
        = \sum_{k,q}{r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}Y_{kq}(\Omega)Y_{kq}^*(\Omega')

And we get:

.. math::

    \int {\psi_i^*({\bf x})\psi_j({\bf x})\psi_j^*({\bf x}')\psi_i({\bf x}')
        \over |{\bf x} - {\bf x}'|} \d^3 x \d^3 x' =

    = \int
        {P_{nl}(r)\over r} Y_{lm}^*(\Omega)
        {P_{n'l'}(r)\over r} Y_{l'm'}(\Omega)
        {P_{n'l'}(r')\over r'} Y_{l'm'}^*(\Omega')
        {P_{nl}(r')\over r'} Y_{lm}(\Omega')

        \sum_{k,q}{r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}Y_{kq}(\Omega)Y_{kq}^*(\Omega')
        r^2 r'^2 \d r \d r' \d \Omega \d \Omega' =

    =
    \sum_{k,q}
    \int
        Y_{lm}^*(\Omega)
        Y_{l'm'}(\Omega)
        Y_{kq}(\Omega)
        \d \Omega
      \int
        Y_{l'm'}^*(\Omega')
        Y_{lm}(\Omega')
        Y_{kq}^*(\Omega')
        \d \Omega'

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k,q}
    \int
        Y_{lm}^*(\Omega)
        Y_{l'm'}(\Omega)
        Y_{kq}(\Omega)
        \d \Omega
        (-1)^{m+m'+q}
      \int
        Y_{l',-m'}(\Omega')
        Y_{l,-m}^*(\Omega')
        Y_{k,-q}(\Omega')
        \d \Omega'

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k}
        c^k(l, m, l', m') \sqrt{2k+1\over 4\pi}
        (-1)^{m+m'+m-m'}
        c^k(l, -m, l', -m') \sqrt{2k+1\over 4\pi}

      \int {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k}
        c^k(l, m, l', m')
        c^k(l, -m, l', -m')
      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k}
        c^k(l, m, l', m')
        c^k(l, m, l', m')
      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r' =

    =
    \sum_{k=|l-l'|}^{l+l'}
        \left(
        c^k(l, m, l', m')
        \right)^2
      \int {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r)
        P_{n'l'}(r)
        P_{n'l'}(r')
        P_{nl}(r')
        \d r \d r'

Occupation Numbers
------------------

We have a sum over $N$ electron states like this:

.. math::

    \sum_{i=1}^N A_i({\bf x}) = \sum_{nlms} A_{nlms}({\bf x})

where $A_{nlms}({\bf x})$ are some functions that depend on the state numbers
(for example squares of the wavefunctions). Then there are two options ---
either there is a way to sum over the $m$ and $s$ degrees of freedom, so that
the sum can be written exactly as:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) = \sum_{nlms} B_{nl}({\bf x})

where $B_{nl}$ (that don't depend on $m$ and $s$) will in general be different
to $A_{nlms}$, but the sum will be the same. Or we have to approximate the sum
(for example by averaging over the angles, or in some other way) as:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) \to \sum_{nlms} B_{nl}({\bf x})

In either case, the occupation numbers $f_{nl}$ are simply the number of times
the functions $B_{nl}({\bf x})$ appear in the sum for the given $n$ and $l$:

.. math::

    \sum_{nlms} B_{nl}({\bf x}) = \sum_{nl} f_{nl} B_{nl}({\bf x})

So for closed shells atoms, it is always:

.. math::

    f_{nl} = 2(2l+1)

because there are two spins, and $2l+1$ possibilities for $m$, for open shell
atoms, $f_{nl}$ is anything between $0$ and $2l+1$.

Example I
~~~~~~~~~

As an example, let's say that after some calculation for closed shell systems
we get exactly:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) = \sum_{nl} 2(2l+1) B_{nl}({\bf x})

Then because there are exactly $2(2l+1)$ states in the $nl$ shell, we write the
above as:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) = \sum_{nl} 2(2l+1) B_{nl}({\bf x})
        = \sum_{nl} f_{nl} B_{nl}({\bf x})

Then we do similar calculation for the open shell system, and we have to use
some approximations to get the following formula, where the $B_{nl}({\bf x})$
happen to be exactly the same as for the closed shell system:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) \to \sum_{nlm} 2 B_{nl}({\bf x})

Then we denote by $f_{nl}$ the number of electrons in the shell $nl$ (at least
one of them will be open, for which $nl$ we have $f_{nl} < 2(2l+1)$), and we
can write the above as:

.. math::

    \sum_{nlms} A_{nlms}({\bf x}) \to \sum_{nlm} 2 B_{nl}({\bf x})
        = \sum_{nl} f_{nl} B_{nl}({\bf x})

Example II
~~~~~~~~~~

The usual chemical occupation numbers for the Uranium atom are:

.. math::

    f_{1l} & = 2 (2l+1)    \\
    f_{2l} & = 2 (2l+1)    \\
    f_{3l} & = 2 (2l+1)    \\
    f_{4l} & = 2 (2l+1)    \\
    f_{5l} & = 2 (2l+1)\quad\quad\mbox{for $l\le2$}    \\
    f_{53} & = 3    \\
    f_{60} & = 2    \\
    f_{61} & = 6    \\
    f_{62} & = 1    \\
    f_{70} & = 2    \\

So the $n=5$, $l=3$ and $n=6$, $l=2$ shells are open, all others are closed.
By summing all these $f_{nl}$, we get 92 states as expected:

.. math::

    \sum_{nl} f_{nl} = 2 + (2+6) + (2+6+10) + (2+6+10+14) + (2+6+10) +

        + 3 + 2 + 6 + 1 + 2 = 92

Code::

    def f_nl(n, l):
        if n < 5 or (n == 5 and l <= 2):
            return 2*(2*l+1)
        else:
            d = {
                (5, 3): 3,
                (6, 0): 2,
                (6, 1): 6,
                (6, 2): 1,
                (7, 0): 2,
                }
            if (n, l) in d:
                return d[n, l]
            else:
                return 0

    print "Sum f_nl =", sum([f_nl(n, l) for n in range(8) for l in range(n)])

prints::

    Sum f_nl = 92

Hartree Screening Functions
---------------------------

Hartree screening function $Y^k(f, r)$ is defined as:

.. math::

    Y^k(f, r) = r
    \int_0^\infty
    {r_{<}^k\over r_{>}^{k+1}}
    f(r')
    \d r'

and it occurs in many formulas in the Hartree Fock theory, so this section shows
how to calculate it. It depends on $k$ and a function $f(r)$.

We first do the integral:

.. math::

    Y^k(f, r) = r
    \int_0^\infty
    {r_{<}^k\over r_{>}^{k+1}}
    f(r')
    \d r'
    = r
    \int_0^r
    {r'^k\over r^{k+1}}
    f(r')
    \d r'
    +
    r \int_r^\infty
    {r^k\over r'^{k+1}}
    f(r')
    \d r'
    =

    =
    {1\over r^k}
    \int_0^r
    {x^k}
    f(x)
    \d x
    +
    r^{k+1}
    \int_r^\infty
    {1\over x^{k+1}}
    f(x)
    \d x
    =Z^k(r)
    +
    r^{k+1}
    \int_r^\infty {1\over x^{k+1}} f(x) \d x

where:

.. math::

    Z^k(r) =
    {1\over r^k}
    \int_0^r
    {x^k}
    f(x)
    \d x

    {\d Z^k(r) \over \d r}= -{k\over r} Z^k(r) + f(r)

    Z^k(0) = 0

Now we differentiate $Y^k(r)$:

.. math::

    {\d Y^k(r) \over \d r} = {\d Z^k(r) \over \d r}
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} f(x) \d x
        -f(r)
    =

    =
    -{k\over r} Z^k(r) + f(r)
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} f(x) \d x
        -f(r) =

    =
    -{k\over r} Z^k(r)
        + {k+1\over r} r^{k+1}
        \int_r^\infty {1\over x^{k+1}} f(x) \d x =

    =
    -{k\over r} Z^k(r)
        + {k+1\over r} (Y^k(r) - Z^k(r)) =

    =
    -{2k+1\over r} Z^k(r) + {k+1\over r} Y^k(r)

Also $Y^k(\infty) = Z^k(\infty)$, so we get the following set of first order
differential equations with boundary conditions:

.. math::

    \left({\d\over\d r} - {k+1\over r}\right) Y^k(r) = -{2k+1\over r} Z^k(r)

    \left({\d\over\d r} + {k\over r}\right) Z^k(r) = f(r)

    Y^k(\infty) = Z^k(\infty)

    Z^k(0) = 0

One way to calculate the Hartree screening function is to integrate the second
equation from the left using the boundary condition $Z^k(0) = 0$ and then
integrate the first equation from the right, using the boundary condition
$Y^k(\infty) = Z^k(\infty)$.

Another way is to obtain one second order equation. Expressing $Z^k$ from the
first equation:

.. math::

    Z^k(r) = -{r\over 2k+1}\left({\d\over\d r} - {k+1\over r}\right) Y^k(r) =

    =-{r\over 2k+1}{\d Y^k(r)\over \d r} + {k+1\over 2k+1} Y^k(r)

and substituting into the second equation we get:

.. math::

    -\left({\d\over\d r} + {k\over r}\right)
        \left({r\over 2k+1}{\d Y^k(r)\over \d r} + {k+1\over 2k+1} Y^k\right)
        = f(r)

    -{r\over 2k+1}\left({\d^2\over\d r^2} - {k(k+1)\over r^2}\right)
        Y^k(r)
        = f(r)

    \left(-{\d^2\over\d r^2} + {k(k+1)\over r^2}\right) Y^k(r)
        = {2k+1\over r} f(r)

With boundary condition on the left:

.. math::

    Z^k(0) = {k+1\over 2k+1} Y^k(0) = 0

    Y^k(0) = 0

and on the right:

.. math::

    Z^k(r)
        =-{r\over 2k+1}{\d Y^k(r)\over \d r} + {k+1\over 2k+1} Y^k(r)
        = Y^k(r)

    -{r\over 2k+1}{\d Y^k(r)\over \d r} - {k\over 2k+1} Y^k(r) = 0

    {\d Y^k(r)\over \d r} + {k\over r} Y^k(r) = 0

which for $r\to\infty$ becomes:

.. math::

    \left.{\d Y^k(r)\over \d r}\right|_{r=\infty} = 0

but in practise, it's better to use the former Newton (Robin) boundary
condition. We have obtained one second order equation for $Y^k(r)$

.. math::

    \left(-{\d^2\over\d r^2} + {k(k+1)\over r^2}\right) Y^k(r)
        = {2k+1\over r} f(r)

with boundary conditions:

.. math::

    Y^k(0) = 0

    {\d Y^k(r)\over \d r} + {k\over r} Y^k(r) = 0

The
weak formulation is:

.. math::

    \int_0^{r_{max}} Y^k{}'(r) v'(r) + {k(k+1)\over r^2} Y^k(r) v(r) \d r
        -[Y^k{}'(r)v(r)]_0^{r_{max}}
        = \int_0^{r_{max}} {2k+1\over r}f(r)v(r) \d r

The boundary term can be simplified using the boundary conditions as:

.. math::

        -[Y^k{}'(r)v(r)]_0^{r_{max}}
        = -Y^k{}'(r_{max})v(r_{max}) + Y^k{}'(0) v(0)
        = -Y^k{}'(r_{max})v(r_{max})
        = {k\over r_{max}} Y^k(r_{max})v(r_{max})

so we get

.. math::

    \int_0^{r_{max}} Y^k{}'(r) v'(r) + {k(k+1)\over r^2} Y^k(r) v(r) \d r
        + {k\over r_{max}} Y^k(r_{max})v(r_{max})
        = \int_0^{r_{max}} {2k+1\over r}f(r)v(r) \d r

where the test functions $v(r)$ have the constrain $v(0)=0$ on the left
boundary and no constrain on the right.

.. _hartree_spherical:

Hartree Potential in Spherical Symmetry
---------------------------------------

For both open and closed shell atoms we get exactly:

.. math::

    V_H({\bf x})
        = \int {n({\bf y})\over|{\bf x}-{\bf y}|} \d^3 y
        = \int {\sum_{j=1}^Z|\psi_j({\bf y})|^2\over|{\bf x}-{\bf y}|}
            \d^3 y =

        = 2\sum_{nlm}\int {|Y_{lm}(\Omega')|^2 P_{nl}^2(r')\over
            |{\bf x}-{\bf y}|} \d\Omega' \d r' =

        = 2\sum_{nlm}\sum_{l'm'}\int {r_<^{l'}\over r_>^{l'+1}}
            {4\pi\over 2l'+1}
            Y_{lm}^*(\Omega')Y_{lm}(\Omega')
            Y_{l'm'}^*(\Omega)Y_{l'm'}(\Omega') P_{nl}^2(r') \d\Omega' \d r' =

        = 2\sum_{nlm}\sum_{l'}\int {r_<^{l'}\over r_>^{l'+1}}
            {4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega) \sqrt{2l'+1\over 4\pi}
                c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = 2\sum_{nl}\sum_{l'=0}^{2l}\int {r_<^{l'}\over r_>^{l'+1}}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)
                \sum_m c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = 2\sum_{nl}\int {1\over r_>}
            \sqrt{4\pi}
            Y_{00}^*(\Omega)
                \sum_m c^0(l, m, l, m) P_{nl}^2(r') \d r' +

        + 2\sum_{nl}\sum_{l'=1}^{2l}\int {r_<^{l'}\over r_>^{l'+1}}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)
                \sum_m c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = \sum_{nl}2\sum_m c^0(l, m, l, m) \int {1\over r_>}
                 P_{nl}^2(r') \d r' +

        + 2\sum_{nl}\sum_{l'=1}^{2l}\int {r_<^{l'}\over r_>^{l'+1}}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)
                \sum_m c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = \sum_{nl}2\sum_m \int {1\over r_>}
                 P_{nl}^2(r') \d r' +

        + 2\sum_{nl}\sum_{l'=1}^{2l}\int {r_<^{l'}\over r_>^{l'+1}}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)
                \sum_m c^{l'}(l, m, l, m) P_{nl}^2(r') \d r' =

        = \sum_{nl} f_{nl} \int {1\over r_>} P_{nl}^2(r') \d r' +

        + 2\sum_{nl}\sum_{l'=1}^{2l}
            \sqrt{4\pi\over 2l'+1}
            Y_{l'0}^*(\Omega)\sum_m c^{l'}(l, m, l, m)
          \int {r_<^{l'}\over r_>^{l'+1}} P_{nl}^2(r') \d r'

For closed shell atoms we use the fact, that

.. math::

        \sum_{m=-l}^l c^{l'}(l, m, l, m) = (2l+1) \delta_{l' 0}

and the second term disappears, and for open shell atoms
we have to use the central field approximation: we average
the integral for $V_H$ over the angles:

.. math::

    V_H({\bf x}) \to V_H(r) = {1\over 4\pi} \int V_H({\bf x})\, \d \Omega

and using the fact, that

.. math::

    \int Y_{l'0}^*(\Omega)\, \d \Omega = \sqrt{4\pi} \delta_{l' 0}

the second term disappears as well. We got the same expression for both open
shell (with central field approximation) and closed shell (no approximation)
atoms.  The radial charge density is:

.. math::

    n(r) = {1\over 4\pi} \sum_{nl} f_{nl} \left(P_{nl}(r)\over r\right)^2

So we got:

.. math::

    V_H(r) =
       \sum_{nl} f_{nl} \int {1\over r_>} P_{nl}^2(r') \d r'
       =\int {4\pi n(r') r'^2 \over r_>} \d r'
       = {Y^0(4\pi n(r) r^2, r) \over r}

The Hartree screening function $Y^0(4\pi n(r) r^2, r)$ is given by the equation:

.. math::

    -{\d^2\over\d r^2} Y^0(r) = {1\over r} 4\pi n(r) r^2

So $V_H(r)$ satisfies the radial Poisson equation:

.. math::

    (V_H(r) r)'' = -{1\over r} 4\pi n(r) r^2

    V_H''(r) r + 2V_H'(r) = - 4\pi n(r) r

    V_H''(r) + {2\over r}V_H'(r) = -4\pi n(r)

Nonlocal Exchange Potential in Spherical Symmetry
-------------------------------------------------

Similarly, we calculate:

.. math::

    \sum_{j=1}^Z\int {\psi_i({\bf x'})\psi_j^*({\bf x'})\over|{\bf x}-{\bf x'}|}
            \d^3 x'\,\,\psi_j({\bf x}) =

    = \sum_{n'l'm'}\sum_{k,q}\int
        {P_{nl}(r')\over r'} Y_{lm}(\Omega')
        {P_{n'l'}(r')\over r'} Y_{l'm'}^*(\Omega')
        {P_{n'l'}(r)\over r} Y_{l'm'}(\Omega)

        {r_{<}^k\over r_{>}^{k+1}}
            {4\pi\over 2k+1}Y_{kq}(\Omega)Y_{kq}^*(\Omega')
        r'^2 \d r' \d \Omega' =

    = \sum_{n'l'm'}\sum_{k,q}
            {P_{n'l'}(r)\over r}
            {4\pi\over 2k+1}
        \int Y_{lm}(\Omega') Y_{l'm'}^*(\Omega') Y_{kq}^*(\Omega')
            Y_{l'm'}(\Omega)
            Y_{kq}(\Omega)
            \d \Omega'
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'  =

    = \sum_{n'l'}\sum_{k}
            {P_{n'l'}(r)\over r}
            {4\pi\over 2k+1}
            {2k+1\over 4\pi}
                \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
                Y_{lm}(\Omega)
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'  =

    =
    {Y_{lm}(\Omega)\over r}
    \sum_{n'l'}\sum_{k=|l-l'|}^{k=l+l'}
            \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'\,
            P_{n'l'}(r) =

    =
    {Y_{lm}(\Omega)\over r}
    \sum_{n'l'}\sum_{k=|l-l'|}^{k=l+l'}
        (2l'+1)
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'\,
            P_{n'l'}(r) =

    =
    {Y_{lm}(\Omega)\over r}
    \sum_{n'l'} f_{n'l'} \sum_{k=|l-l'|}^{k=l+l'}
        \half
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        \int
        {r_{<}^k\over r_{>}^{k+1}}
        P_{nl}(r')
        P_{n'l'}(r')
        \d r'\,
            P_{n'l'}(r)

Functions with different spins don't contribute to the sum, so there is no
multiplication by 2. We assumed closed shells atoms (we summed over all $m'$ in
the above). We used the result of the integral in
:ref:`five_spherical_harmonics` and also:

.. math::
    :label: using3j

    \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
        = \sqrt{2l'+1\over 2l+1}
            \sqrt{(2l'+1)(2l+1)}
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        = (2l'+1)
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2


Radial Hartree-Fock Equations
-----------------------------

Using the above integrals, the HF equations become:

.. math::

    -\half P_{nl}''(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)P_{nl}(r) +

            -\sum_{n'l'}
                f_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int
                {r_{<}^k\over r_{>}^{k+1}}
                P_{nl}(r')
                P_{n'l'}(r')
                \d r'\,
                    P_{n'l'}(r)
        = \epsilon_{nl} P_{nl}(r)

with:

.. math::

    V_H(r) =
       \sum_{nl} f_{nl} \int {1\over r_>} P_{nl}^2(r') \d r'

Using the Hartree screening functions, the HF equations are:

.. math::

    -\half P_{nl}''(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)P_{nl}(r) +

            -\sum_{n'l'}
                f_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                {Y^k(P_{nl}(r) P_{n'l'}(r), r) \over r}
                P_{n'l'}(r)
        = \epsilon_{nl} P_{nl}(r)

with:

.. math::

    V_H(r) = \sum_{nl} f_{nl} {Y^0(P_{nl}^2(r), r) \over r}
        = {Y^0(4\pi n(r) r^2, r) \over r}

Total Energy
------------

The total energy is:

.. math::

    E = \sum_a 2(2l_a+1) \left( \epsilon_a
        -\sum_b (2l_b+1) \left( R_0(a, b, a, b)-\sum_l
            \half \begin{pmatrix} l_a & l & l_b \\ 0 & 0 & 0 \end{pmatrix}^2
            R_l(a, b, b, a)\right) \right) =

      = \sum_{nl} f_{nl} \left( \epsilon_{nl}
        -\sum_{n'l'} \half f_{n'l'} \left( R_0(nl, n'l', nl, n'l')-\sum_k
            \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
            R_l(nl, n'l', n'l', nl)\right) \right) =

      = \sum_{nl} f_{nl} \epsilon_{nl}
        -\sum_{nl}\sum_{n'l'} \half f_{nl} f_{n'l'}
            \left(
        \int_0^\infty P_{nl}^2(r) {Y^0(P_{n'l'}^2(r), r)\over r} \d r
            -\sum_k
            \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int_0^\infty P_{nl}(r) P_{n'l'}(r)
                        {Y^l(P_{nl}(r) P_{n'l'}(r), r)\over r} \d r
            \right) =

      = \sum_{nl} f_{nl} \epsilon_{nl}
        -\half
        \int_0^\infty 4\pi n(r) r^2 {Y^0(4\pi n(r) r^2, r)\over r} \d r +

            +\sum_{nl}\sum_{n'l'} \half f_{nl} f_{n'l'} \sum_k
            \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int_0^\infty P_{nl}(r) P_{n'l'}(r)
                        {Y^l(P_{nl}(r) P_{n'l'}(r), r)\over r} \d r
            =

      = \sum_{nl} f_{nl} \epsilon_{nl}
        -2\pi \int_0^\infty V_H(r) n(r) r^2 \d r
            +\sum_{nl}\sum_{n'l'} \half f_{nl} f_{n'l'} \sum_k
            \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int_0^\infty P_{nl}(r) P_{n'l'}(r)
                        {Y^l(P_{nl}(r) P_{n'l'}(r), r)\over r} \d r

where:

.. math::

    R_l(a, b, c, d) = \int_0^\infty P_a(r) P_c(r) {Y^l(P_b(r) P_d(r), r)\over r} \d r

Example: Helium
~~~~~~~~~~~~~~~

For Helium atom, the only nonzero occupation numbers are:

.. math::

    f_{10} = 2

and the sum over $n'l'$ simplifies to:

.. math::

    \sum_{n'l'}
        f_{n'l'}
        \sum_{k=|l-l'|}^{k=l+l'}
        \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
    = f_{10} \half \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}^2
    = f_{10} \half = 1

so we only need to solve for the $1s$ state and we get:

.. math::

    -\half P_{10}''(r) +
        \left(-{Z\over r} + V_H(r)\right)P_{10}(r)
            -{Y^0(P_{10}(r) P_{10}(r), r) \over r}
                P_{10}(r)
        = \epsilon_{10} P_{10}(r)

with:

.. math::

    V_H(r) = 2 {Y^0(P_{10}^2(r), r) \over r}
        = {Y^0(4\pi n(r) r^2, r) \over r}

We can combine the equations:

.. math::

    -\half P_{10}''(r) +
        \left(-{Z\over r} + 2 {Y^0(P_{10}^2(r), r) \over r}\right)P_{10}(r)
            -{Y^0(P_{10}^2(r), r) \over r}
                P_{10}(r)
        = \epsilon_{10} P_{10}(r)

and we obtain:

.. math::

    -\half P_{10}''(r) +
        \left(-{Z\over r} + {Y^0(P_{10}^2(r), r) \over r}\right)P_{10}(r)
        = \epsilon_{10} P_{10}(r)

FEM
---

The weak formulation is ($u(r) = P_{nl}(r)$):

.. math::

    \int_0^\infty \left( \half u'(r) v'(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)u(r)v(r)
            \right) \d r+

            -\sum_{n'l'}
                f_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int_0^\infty
                v(r)
                P_{n'l'}(r)
                {Y^k(u(r) P_{n'l'}(r), r)\over r}
                \d r
        = \epsilon \int_0^\infty u(r)v(r)\d r

for closed shell atoms:

.. math::

    \int_0^\infty \left( \half u'(r) v'(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)u(r)v(r)
            \right) \d r+

            -\sum_{n'l'}
                2(2l'+1)
                \sum_{k=|l-l'|}^{k=l+l'}
                \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \int_0^\infty
                v(r)
                P_{n'l'}(r)
                {Y^k(u(r) P_{n'l'}(r), r)\over r}
                \d r
        = \epsilon \int_0^\infty u(r)v(r)\d r

or (here $i,j$ runs over all spatial orbitals $nl$, but for the given $l$, only
a subset of $i, j$ corresponding to this $l$ is varied below)

.. math::

    \int_0^\infty \left( \half u_i'(r) v_j'(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)u_i(r)v_j(r)
            \right) \d r+

            -\sum_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \sqrt{2l'+1\over 2l+1}c^k(l, 0, l', 0)
                \int_0^\infty
                v_j(r)
                P_{n'l'}(r)
                {Y^k(u_i(r) P_{n'l'}(r), r)\over r}
                \d r
        = \epsilon \int_0^\infty u_i(r)v_j(r)\d r

Introducing radial basis $\phi_\mu(r)$ (here $i$ runs over all $l$):

.. math::

    u_i(r) = \sum_\nu C_{\nu i} \phi_\nu(r)

we get (here $i$ is again restricted for the subset corresponding to the given
$l$):

.. math::

    \sum_\nu \int_0^\infty \left( \half \phi_\mu'(r) \phi_\nu'(r) +
        \left({l(l+1)\over 2r^2} -{Z\over r} + V_H(r)\right)\phi_\mu(r)
            \phi_\nu(r)
            \right) \d r\,C_{\nu i}+

            -\sum_\nu \sum_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \sqrt{2l'+1\over 2l+1}c^k(l, 0, l', 0)
                \int_0^\infty
                \phi_\mu(r)
                P_{n'l'}(r)
                {Y^k(\phi_\nu(r) P_{n'l'}(r), r)\over r}
                \d r\,C_{\nu i}
        = \epsilon \sum_\nu \int_0^\infty \phi_\mu(r)\phi_\nu(r) \d r\,C_{\nu i}

This can be written as ($i$ is restricted to the subset corresponding to the
given $l$ and these equations are solved separately for all $l$ to obtain
orbitals $C_{\nu i}$ for all $i$):

.. math::

    \sum_\nu F_{\mu\nu} C_{\nu i} = \epsilon_i \sum_\nu S_{\mu\nu} C_{\nu i}

    F_{\mu\nu} = H_{\mu\nu}^{\mbox{core}} + G_{\mu\nu}
        = T_{\mu\nu} + V_{\mu\nu} + G_{\mu\nu}

where

.. math::

    T_{\mu\nu} = \int_0^\infty \half \phi_\mu'(r) \phi_\nu'(r)
        + \phi_\mu(r){l(l+1)\over 2r^2} \phi_\nu(r) \d r

    V_{\mu\nu} = \int_0^\infty \phi_\mu(r)\left(-{Z\over r}\right)
        \phi_\nu(r) \d r

    G_{\mu\nu} = \int_0^\infty \phi_\mu(r) V_H(r) \phi_\nu(r) \d r +

            -\sum_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \sqrt{2l'+1\over 2l+1}c^k(l, 0, l', 0)
                \int_0^\infty
                \phi_\mu(r)
                P_{n'l'}(r)
                {Y^k(\phi_\nu(r) P_{n'l'}(r), r)\over r}
                \d r

    S_{\mu\nu} = \int_0^\infty \phi_\mu(r)\phi_\nu(r) \d r

    V_H(r) = \sum_{n'l'} 2(2l'+1) {Y^0(P_{n'l'}^2(r), r) \over r}

The indices $n' l'$ go over all occupied orbitals $P_{n' l'}$.
Introducing density:

.. math::

    n({\bf x}) = 2 \sum_{k=1}^{N/2} | \psi_k({\bf x})|^2
        = 2 \sum_{nlm} | \psi_{nlm}({\bf x})|^2
        = 2 \sum_{nlm} {P_{nl}^2(r)\over r^2} |Y_{lm}(\Omega)|^2 =

        = 2 \sum_{nl} {P_{nl}^2(r)\over r^2} {2l+1\over 4\pi}
        = {1\over 4\pi} \sum_{nl} 2(2l+1) {P_{nl}^2(r)\over r^2}
        = n(r)

Using density matrix we can write $n(r)$ as ($k$ runs over all occupied
orbitals $nl$):

.. math::

    P_{\alpha\beta} = 2 \sum_{k=1}^{N/2} C_{\alpha k} C_{\beta k}^*
        = 2 \sum_{nlm} C_{\alpha nlm} C_{\beta nlm} =

        = \sum_{nl} 2(2l+1) C_{\alpha nl} C_{\beta nl}
        = \sum_{l} (2l+1) P^l_{\alpha \beta}

    P^l_{\alpha\beta} = \sum_n 2 C_{\alpha nl} C_{\beta nl}

    P_{nl}(r) = \sum_\alpha C_{\alpha nl} \phi_\alpha(r)

    n(r) = {1\over 4\pi} \sum_{nl} 2(2l+1) {P_{nl}^2(r)\over r^2}
        = {1\over 4\pi} \sum_{\alpha\beta}\sum_{nl} 2(2l+1)
            C_{\alpha nl}C_{\beta nl}{\phi_\alpha(r)\phi_\beta(r)\over r^2} =

        = {1\over 4\pi} \sum_{\alpha\beta}
            {\phi_\alpha(r) P_{\alpha\beta} \phi_\beta(r)\over r^2}

Finally we get:

.. math::

    V_H(r) = \sum_{nl} 2(2l+1) {Y^0(P_{nl}^2(r), r) \over r}
        = {Y^0(4\pi n(r) r^2, r) \over r}
        = \sum_{\alpha\beta} P_{\alpha\beta}
            {Y^0(\phi_\alpha(r) \phi_\beta(r), r) \over r}

    \int_0^\infty \phi_\mu(r) V_H(r) \phi_\nu(r) \d r
     = \sum_{\alpha\beta} P_{\alpha\beta}
        \int_0^\infty \phi_\mu(r) \phi_\nu(r)
            {Y^0(\phi_\alpha(r) \phi_\beta(r), r) \over r}\d r
     = \sum_{\alpha\beta} P_{\alpha\beta} R^0(\mu, \beta, \nu, \alpha)

and

.. math::

            -\sum_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                \sqrt{2l'+1\over 2l+1}c^k(l, 0, l', 0)
                \int_0^\infty
                \phi_\mu(r)
                P_{n'l'}(r)
                {Y^k(\phi_\nu(r) P_{n'l'}(r), r)\over r}
                \d r =

            = -\sum_{n'l'}
                \sum_{k=|l-l'|}^{k=l+l'}
                2(2l'+1)
                \half \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                \sum_{\alpha\beta}
                C_{\alpha n'l'}
                C_{\beta n'l'}
                \int_0^\infty
                \phi_\mu(r)
                \phi_\alpha(r)
                {Y^k(\phi_\nu(r) \phi_\beta(r), r)\over r}
                \d r =

            = -\half
                \sum_{\alpha\beta}
                \sum_{l'}
                (2l'+1)
                P^{l'}_{\alpha\beta}
                \sum_{k=|l-l'|}^{k=l+l'}
                 \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                R^k(\mu, \beta, \alpha, \nu)


So we get:

.. math::

    G_{\mu\nu}
     = \sum_{\alpha\beta} P_{\alpha\beta} R^0(\mu, \beta, \nu, \alpha)
        -\half \sum_{\alpha\beta}
                \sum_{l'}
                (2l'+1)
                P^{l'}_{\alpha\beta}
                \sum_{k=|l-l'|}^{k=l+l'}
                 \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                R^k(\mu, \beta, \alpha, \nu) =

     = \sum_{l'} (2l'+1) \sum_{\alpha\beta} P^{l'}_{\alpha\beta} \left(
            R^0(\mu, \beta, \nu, \alpha)
                -\half \sum_{k=|l-l'|}^{k=l+l'}
                 \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
                R^k(\mu, \beta, \alpha, \nu) \right)
