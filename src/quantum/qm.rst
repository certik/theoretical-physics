.. index:: quantum mechanics

Quantum Mechanics
=================

.. index:: QED, quantum electrodynamics

From QED to Quantum Mechanics
-----------------------------

The QED Lagrangian density is

.. math::

    \L=\bar\psi(i\hbar c\gamma^\mu D_\mu-mc^2)\psi-{1\over4}F_{\mu\nu}F^{\mu\nu}


Plugging this Lagrangian into the Euler-Lagrange equation of motion for a field, we get:

.. math::

    (i\hbar c\gamma^\mu D_\mu-mc^2)\psi=0



.. math::

    \partial_\nu F^{\nu\mu}=-ec\bar\psi\gamma^\mu\psi


The first equation is the Dirac equation in the electromagnetic field and the second equation is a set of Maxwell equations ($\partial_\nu F^{\nu\mu}=-ej^\mu$) with a source $j^\mu=c\bar\psi\gamma^\mu\psi$, which is a 4-current comming from the Dirac equation.

The fields $\psi$ and $A^\mu$ are quantized. The first approximation is that we take $\psi$ as a wavefunction, that is, it is a classical 4-component field. It can be shown that this corresponds to taking the tree diagrams in the perturbation theory.

We multiply the Dirac equation by $\gamma^0$ from left to get:

.. math::

    0=\gamma^0(i\hbar c\gamma^\mu D_\mu-mc^2)\psi= \gamma^0(i\hbar c\gamma^0(\partial_0+{i\over\hbar}eA_0)+ic\gamma^i (\partial_i+{i\over\hbar}eA_i)-mc^2)\psi=



.. math::

    = (i\hbar c\partial_0+i\hbar c\gamma^0\gamma^i\partial_i-\gamma^0mc^2-ceA_0 -ce\gamma^0\gamma^iA_i)\psi


and we make the following substitutions (it's just a formalism, nothing more): $\beta=\gamma^0$, $\alpha^i=\gamma^0\gamma^i$, $p_j=i\hbar\partial_j$, $\partial_0={1\over c}{\partial\over\partial t}$ to get

.. math::

    (i\hbar{\partial\over\partial t}+c\alpha^i p_i-\beta mc^2-ceA_0-ce\alpha^iA_i)\psi=0\,.


or:

.. math::

    i\hbar{\partial\psi\over\partial t}=(c\alpha^i(-p_i+eA_i) +\beta mc^2+ceA_0)\psi\,.


This can be written as:

.. math::

    i{\partial\psi\over\partial t}=H\psi\,,


where the Hamiltonian is given by:

.. math::

    H=c\alpha^i(-p_i+eA_i)+\beta mc^2+ceA_0\,,


or introducing the electrostatic potential $\phi=cA_0$ and writing the momentum as a vector (see the appendix for all the details regarding signs):

.. math::

    H=c{\boldsymbol\alpha}\cdot({\bf p}-e{\bf A})+\beta mc^2+e\phi\,.



The right hand side of the Maxwell equations is the 4-current, so it's given by:

.. math::

    j^\mu=c\bar\psi\gamma^\mu\psi


Now we make the substitution $\psi=e^{-imc^2t}\varphi$, which states, that we separate the largest oscillations of the wavefunction and we get

.. math::

    j^0=c\bar\psi\gamma^0\psi=c\psi^\dagger\psi=c\varphi^\dagger\varphi



.. math::

    j^i=c\bar\psi\gamma^i\psi=c\psi^\dagger\alpha^i\psi=c\varphi^\dagger\alpha^i\varphi


Derivation of the Pauli Equation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We start from the Dirac equation:

.. math::

    H\psi = W\psi

where:

.. math::

    H=c{\boldsymbol\alpha}\cdot({\bf p}-e{\bf A})+\beta mc^2+e\phi\,.

    W = E + mc^2

$W$ is the relativistic energy, $E$ is the nonrelativistic energy,
$e\phi=V$ is the potential. The matrices
${\boldsymbol\alpha}$ and $\beta$ are given by:

.. math::

    \alpha^i = \gamma^0\gamma^i

    \beta = \gamma^0

so written explicitly:

.. math::

    \alpha = \begin{pmatrix}
        0 & {\boldsymbol\sigma} \\
        {\boldsymbol\sigma} & 0 \\
        \end{pmatrix}

    \beta = \begin{pmatrix}
        \one & 0 \\
        0 & -\one \\
        \end{pmatrix}

And the Dirac equation is:

.. math::

    \begin{pmatrix}
        V+mc^2 & c{\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) \\
        c{\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) & V-mc^2 \\
        \end{pmatrix}
    \begin{pmatrix}
        \psi^L \\
        \psi^S \\
    \end{pmatrix}
    =
    W
    \begin{pmatrix}
        \psi^L \\
        \psi^S \\
    \end{pmatrix}

After introducing $E$ we get:

.. math::

    \begin{pmatrix}
        V & c{\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) \\
        c{\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) & V-2mc^2 \\
        \end{pmatrix}
    \begin{pmatrix}
        \psi^L \\
        \psi^S \\
    \end{pmatrix}
    =
    E
    \begin{pmatrix}
        \psi^L \\
        \psi^S \\
    \end{pmatrix}

We put everything on the left hand side:

.. math::

    \begin{pmatrix}
        V -E & c{\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) \\
        c{\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) & V-E-2mc^2 \\
        \end{pmatrix}
    \begin{pmatrix}
        \psi^L \\
        \psi^S \\
    \end{pmatrix}
    = 0

We put $c$ next to $\psi^S$:

.. math::

    \begin{pmatrix}
        V -E & {\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) \\
        c{\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) & {V-E\over c}-2mc \\
        \end{pmatrix}
    \begin{pmatrix}
        \psi^L \\
        c\psi^S \\
    \end{pmatrix}
    = 0

And we divide the second equation by $c$:

.. math::

    \begin{pmatrix}
        V -E & {\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) \\
        {\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) & {V-E\over c^2}-2m \\
        \end{pmatrix}
    \begin{pmatrix}
        \psi^L \\
        c\psi^S \\
    \end{pmatrix}
    = 0

Now we express $c\psi^S$ from the second equation:

.. math::

    c\psi^S ={ {\boldsymbol\sigma}\cdot({\bf p}-e{\bf A}) \psi^L \over
        2m - {V-E\over c^2}}

And substitute into the first equation:

.. math::

    \left(
    V - E +
    {\boldsymbol\sigma}\cdot({\bf p}-e{\bf A})
        {1 \over 2m - {V-E\over c^2}}
        {\boldsymbol\sigma}\cdot({\bf p}-e{\bf A})
    \right) \psi^L = 0

So we get the following equation (so far this is an exact equation for the
first two components of the Dirac equation, no approximation has been made):

.. math::

    \left(
    {\boldsymbol\sigma}\cdot({\bf p}-e{\bf A})
        {1 \over 2m - {V-E\over c^2}}
        {\boldsymbol\sigma}\cdot({\bf p}-e{\bf A})
    + V
    \right) \psi^L = E \psi^L

Note that the first operator ${\bf p}$ (on the left hand side) acts among other
things on the $V$ in the denominator.
By doing the nonrelativistic approximation ${V-E\over c^2} \ll 2m$ we obtain
the Pauli equation:

.. math::

    \left(
    {\left({\boldsymbol\sigma}\cdot({\bf p}-e{\bf A})\right)^2 \over
        2m} + V
    \right) \psi^L = E \psi^L

We can see, that the quantity

.. math::

    M = m - {V-E\over 2c^2}

can be interpreted as relativistic mass.

Using the relations between the Pauli matrices, we can further simplify:

.. math::

    \left({\boldsymbol\sigma}\cdot({\bf p}-e{\bf A})\right)^2
        = \left({\bf p}-e{\bf A}\right)^2+i{\boldsymbol\sigma}
            \cdot{({\bf p}-e{\bf A})\times({\bf p}-e{\bf A})} =

        = \left({\bf p}-e{\bf A}\right)^2+i{\boldsymbol\sigma}
            \cdot\left({\bf p}\times{\bf p}-e{\bf A}\times{\bf p}
                -e{\bf p}\times{\bf A}+e^2{\bf A}\times{\bf A}\right) =

        = \left({\bf p}-e{\bf A}\right)^2-ie{\boldsymbol\sigma}
            \cdot\left({\bf A}\times{\bf p} +{\bf p}\times{\bf A}\right) =

        = \left({\bf p}-e{\bf A}\right)^2-ie{\boldsymbol\sigma}
            \cdot\left({\bf A}\times{\bf p}-{\bf A}\times{\bf p}
            -i\hbar(\nabla\times{\bf A})\right) =

        = \left({\bf p}-e{\bf A}\right)^2-{e\hbar}{\boldsymbol\sigma}
            \cdot(\nabla\times{\bf A}) =

        = \left({\bf p}-e{\bf A}\right)^2-{e\hbar}{\boldsymbol\sigma}
            \cdot{\bf B}

At the end, we have introduced the magnetic field ${\bf B} = {\nabla\times{\bf A}}$.
In the above, one has to be careful, because ${\bf p}$ and ${\bf A}$ don't
commute and also the operator ${\bf p}$ acts on everything on the right. We
used the formula
${\bf p}\times{\bf A}=-{\bf A}\times{\bf p}-i\hbar(\nabla\times{\bf A})$,
that can be proven by:

.. math::

    ({\bf p}\times{\bf A} \psi)_i =
        \epsilon_{ijk}p_j A_k \psi =

        = -i\hbar\epsilon_{ijk}\partial_j (A_k \psi) =

        = -i\hbar\epsilon_{ijk}((\partial_j A_k)\psi + A_k\partial_j \psi) =

        = -i\hbar\epsilon_{ijk}((\partial_j A_k)\psi - A_j\partial_k \psi) =

        = \epsilon_{ijk}(-i\hbar(\partial_j A_k)\psi - A_j p_k \psi) =

        = -i\hbar((\nabla\times{\bf A})\psi)_i - ({\bf A}\times{\bf p} \psi)_i

Putting this into the Pauli equation, we get:

.. math::

    \left(
    {\left({\bf p}-e{\bf A}\right)^2 \over 2m} + V
    -{e\hbar\over 2m}{\boldsymbol\sigma}\cdot{\bf B}
    \right) \psi^L = E \psi^L

Nonrelativistic Limit in the Lagrangian
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We use the identity ${\partial\over\partial t}\left(e^{-imc^2t}f(t)\right)= e^{-imc^2t}(-imc^2+{\partial\over\partial t})f(t)$ to get:



.. math::

    L=c^2\partial^\mu\psi^*\partial_\mu\psi-m^2c^4\psi^*\psi= {\partial\over\partial t}\psi^*{\partial\over\partial t}\psi -c^2\partial^i\psi^*\partial_i\psi-m^2c^4\psi^*\psi=



.. math::

    =(imc^2+{\partial\over\partial t})\varphi^* (-imc^2+{\partial\over\partial t})\varphi -c^2\partial^i\varphi^*\partial_i\varphi-m^2c^4\varphi^*\varphi=



.. math::

    =2mc^2\left[{1\over2}i(\varphi^*{\partial\varphi\over\partial t}- \varphi{\partial\varphi^*\over\partial t})- {1\over2m}\partial^i\varphi^*\partial_i\varphi +{1\over2mc^2}{\partial\varphi^*\over\partial t} {\partial\varphi\over\partial t}\right]


The constant factor $2mc^2$ in front of the Lagrangian is of course irrelevant, so we drop it and then we take the limit $c\to\infty$ (neglecting the last term) and we get

.. math::

    L={1\over2}i(\varphi^*{\partial\varphi\over\partial t}- \varphi{\partial\varphi^*\over\partial t})- {1\over2m}\partial^i\varphi^*\partial_i\varphi


After integration by parts we arrive at the Lagrangian for the Schrödinger equation:

.. math::

    L=i\varphi^*{\partial\varphi\over\partial t} -{1\over 2m}\partial^i\varphi^*\partial_i \varphi


.. index::
    pair: Klein-Gordon; equation

Klein-Gordon Equation
~~~~~~~~~~~~~~~~~~~~~

The Dirac equation implies the Klein-Gordon equation:

.. math::

    0=(-i\hbar c\gamma^\mu D_\mu-mc^2)(i\hbar c\gamma^\nu D_\nu-mc^2)\psi= (\hbar^2c^2\gamma^\mu\gamma^\nu D_\mu D_\nu+m^2c^4)\psi=



.. math::

    =(\hbar^2c^2g^{\mu\nu}D_\mu D_\nu+m^2c^4)\psi =(\hbar^2c^2D^\mu D_\mu+m^2c^4)\psi


Note however, the $\psi$ in the true Klein-Gordon equation is just a scalar, but here we get a 4-component spinor. Now:

.. math::

    D_\mu D_\nu = (\partial_\mu+ieA_\mu)(\partial_\nu+ieA_\nu)= \partial_\mu\partial_\nu+ie(A_\mu\partial_\nu+A_\nu\partial_\mu+ (\partial_\mu A_\nu))-e^2A_\mu A_\nu



.. math::

    [D_\mu, D_\nu] = D_\mu D_\nu-D_\nu D_\mu=ie(\partial_\mu A_\nu)- ie(\partial_\nu A_\mu)


We rewrite $D^\mu D_\mu$:

.. math::

    D^\mu D_\mu=g^{\mu\nu}D_\mu D_\nu= \partial^\mu\partial_\mu+ie((\partial^\mu A_\mu)+2A^\mu\partial_\mu) -e^2A^\mu A_\mu=



.. math::

    =\partial^\mu\partial_\mu+ ie((\partial^0 A_0)+2A^0\partial_0+(\partial^i A_i)+2A^i\partial_i) -e^2(A^0A_0+A^i A_i)=



.. math::

    =\partial^\mu\partial_\mu +i{1\over c^2}{\partial V\over\partial t}+ 2i{V\over c^2}{\partial\over\partial t} +ie(\partial^i A_i)+2ieA^i\partial_i -{V^2\over c^2}-e^2A^iA_i



The nonrelativistic limit can also be applied directly to the Klein-Gordon equation:

.. math::

    0=(\hbar^2c^2D^\mu D_\mu+m^2c^4)\psi=



.. math::

    =\left( \hbar^2c^2\partial^\mu\partial_\mu +i{\partial V\over\partial t} +2iV{\partial\over\partial t} +i\hbar ec^2(\partial^i A_i) +2i\hbar ec^2A^i\partial_i -V^2 -e^2c^2A^iA_i +m^2c^4 \right)e^{-{i\over\hbar}mc^2t}\varphi=



.. math::

    =\left( \hbar^2{\partial^2\over\partial t^2} -c^2\hbar^2\nabla^2 +2iV{\partial\over\partial t} +i{\partial V\over\partial t} +i\hbar ec^2(\partial^i A_i) +2i\hbar ec^2A^i\partial_i -V^2 -e^2c^2A^iA_i +m^2c^4 \right)e^{-{i\over\hbar}mc^2t}\varphi=



.. math::

    =e^{-{i\over\hbar}mc^2t}\left( \hbar^2(-{i\over\hbar}mc^2+{\partial\over\partial t})^2 -\hbar^2c^2\nabla^2 +2iV(-{i\over\hbar}mc^2+{\partial\over\partial t}) +i{\partial V\over\partial t} +i\hbar ec^2(\partial^i A_i) +2i\hbar ec^2A^i\partial_i -V^2+ \right.



.. math::

    \left. -e^2c^2A^iA_i +m^2c^4 \right)\varphi=



.. math::

    =e^{-{i\over\hbar}mc^2t}\left( -2i\hbar mc^2{\partial\over\partial t}+\hbar^2{\partial^2\over\partial t^2} -c^2\hbar^2\nabla^2 +2Vm{c^2\over\hbar} +2iV{\partial\over\partial t} +i{\partial V\over\partial t} +i\hbar ec^2(\partial^i A_i) +2i\hbar ec^2A^i\partial_i -V^2+ \right.



.. math::

    \left. -e^2c^2A^iA_i \right)\varphi=



.. math::

    = -2mc^2 e^{-{i\over\hbar}mc^2 t} \left(i\hbar{\partial\over\partial t}+\hbar^2{\nabla^2\over2m}-V -{1\over2mc^2}{\partial^2\over\partial t^2}-{i\over2mc^2}{\partial V\over\partial t}+{V^2\over2mc^2}-{iV\over mc^2}{\partial\over\partial t}+\right.



.. math::

    \left.-{i\hbar e\over2m}\partial^i A_i-{i\hbar e\over m}A^i\partial_i+{e^2\over2m}A^iA_i\right)\varphi


Taking the limit $c\to\infty$ we again recover the Schrödinger equation:

.. math::

    i\hbar{\partial\over\partial t}\varphi=\left(-\hbar^2{\nabla^2\over2 m}+V +{i\hbar e\over2m}\partial^i A_i +{i\hbar e\over m}A^i\partial_i -{e^2\over2m}A^iA_i \right)\varphi\,,


we rewrite the right hand side a little bit:

.. math::

    i\hbar{\partial\over\partial t}\varphi=\left({\hbar^2\over2 m} (\partial^i\partial_i +{i\over\hbar}e\partial^i A_i +2{i\over\hbar}eA^i\partial_i -{e^2\over\hbar^2}A^iA_i ) +V \right)\varphi\,,



.. math::

    i\hbar{\partial\over\partial t}\varphi=\left({\hbar^2\over2 m} (\partial^i+{i\over\hbar}eA^i)(\partial_i+{i\over\hbar}eA_i) +V \right)\varphi\,,



.. math::

    i\hbar{\partial\over\partial t}\varphi=\left({1\over2 m} \hbar^2D^iD_i +V \right)\varphi\,,


Using (see the appendix for details):

.. math::

    \hbar^2D^iD_i=-\hbar^2\delta_{ij}D^iD^j =-\hbar^2\left({i\over\hbar}({\bf p}-e{\bf A})\right)^2 =({\bf p}-e{\bf A})^2


we get the usual form of the Schrödinger equation for the vector potential:

.. math::

    i\hbar{\partial\over\partial t}\varphi=\left({({\bf p}-e{\bf A})^2\over2 m} +V \right)\varphi\,.



A little easier derivation:

.. math::

    0=(\hbar^2c^2 D^\mu D_\nu+m^2c^4)\psi=



.. math::

    =(\hbar^2c^2 D^0 D_0+\hbar^2c^2D^i D_i+m^2c^4)\psi=



.. math::

    =2mc^2\left({\hbar^2\over2m} D^0 D_0+{\hbar^2\over2m}D^i D_i+\half mc^2\right)\psi=



.. math::

    =2mc^2\left({\hbar^2\over2m} \left(\partial^0+{i\over\hbar}eA^0\right) \left(\partial_0+{i\over\hbar}eA_0\right)+\half mc^2+{\hbar^2\over2m}D^i D_i \right) e^{-{i\over\hbar}mc^2 t} \varphi=



.. math::

    =2mc^2\left({\hbar^2\over2m} \left(\partial^0+{i\over\hbar}eA^0\right) e^{-{i\over\hbar}mc^2 t} \left(\partial_0-{i\over\hbar}mc+{i\over\hbar}eA_0\right)+\half mc^2+{\hbar^2\over2m}D^i D_i \right) \varphi=



.. math::

    =2mc^2 e^{-{i\over\hbar}mc^2 t} \left({\hbar^2\over2m} \left(\partial^0-{i\over\hbar}mc+{i\over\hbar}eA^0\right) \left(\partial_0-{i\over\hbar}mc+{i\over\hbar}eA_0\right)+\half mc^2+{\hbar^2\over2m}D^i D_i \right) \varphi=



.. math::

    =2mc^2 e^{-{i\over\hbar}mc^2 t} \left( {\hbar^2\over2m}\partial^0\partial_0 -\half mc^2 -{e^2A^0A_0\over 2m} +ceA^0 +{\hbar^2\over m}{i\over\hbar}e(\partial^0 A^0+A^0\partial^0) -i\hbar c\partial_0 +\half mc^2+{\hbar^2\over2m}D^i D_i \right) \varphi=



.. math::

    =2mc^2 e^{-{i\over\hbar}mc^2 t} \left( -i\hbar {\partial\over\partial t} +{\hbar^2\over2m}D^i D_i +ceA^0 +{\hbar^2\over2mc^2}{\partial^2\over\partial t^2} -{e^2\phi^2\over 2mc^2} +{ie\hbar\over mc^2}({\partial\over\partial t} \phi + \phi{\partial\over\partial t}) \right) \varphi=



.. math::

    =2mc^2 e^{-{i\over\hbar}mc^2 t} \left( -i\hbar {\partial\over\partial t} +{({\bf p}-e{\bf A})^2\over2m} +e\phi +{\hbar^2\over2mc^2}{\partial^2\over\partial t^2} -{e^2\phi^2\over 2mc^2} +{ie\hbar\over mc^2}({\partial\over\partial t} \phi + \phi{\partial\over\partial t}) \right) \varphi


and letting $c\to\infty$ we get the Schrödinger equation:

.. math::

    i\hbar {\partial\over\partial t}\varphi= \left( {({\bf p}-e{\bf A})^2\over2m} +e\phi \right)\varphi


.. index:: perturbation theory

Perturbation Theory
-------------------

We want to solve the equation:

.. math::
    :label: schroed

    i\hbar{\d \over\d t}\ket{\psi(t)}=H(t)\ket{\psi(t)}


with $H(t) = H^0 + H^1(t)$, where $H^0$ is time-independent part whose eigenvalue problem has been solved:

.. math::

    H^0\ket{n^0}=E^0_n\ket{n^0}


and $H^1(t)$ is a small time-dependent perturbation. $\ket{n^0}$ form a complete basis, so we can express $\ket{\psi(t)}$ in this basis:

.. math::
    :label: psi

    \ket{\psi(t)} = \sum_n d_n(t)e^{-{i\over\hbar}E^0_n t}\ket{n^0}


Substituting this into :eq:`schroed`, we get:

.. math::

    \sum_n\left( i\hbar{\d\over\d t} d_n(t)+E^0_n d_n(t) \right)e^{-{i\over\hbar}E^0_n t}\ket{n^0} =\sum_n\left( E^0_n d_n(t) +H^1 d_n(t) \right)e^{-{i\over\hbar}E^0_n t}\ket{n^0}


so:

.. math::

    \sum_n i\hbar{\d\over\d t}\left( d_n(t)\right) e^{-{i\over\hbar}E^0_n t}\ket{n^0} =\sum_n d_n(t) e^{-{i\over\hbar}E^0_n t}H^1\ket{n^0}


Choosing some particular state $\ket{f^0}$ of the $H^0$ Hamiltonian, we multiply the equation from the left by $\bra{f^0}e^{{i\over\hbar}E^0_f t}$:

.. math::

    \sum_n i\hbar{\d\over\d t}\left( d_n(t)\right)e^{i w_{fn} t} \braket{f^0|n^0} =\sum_n d_n(t) e^{i w_{fn} t}\braket{f^0|H^1|n^0}


where $w_{fn}={E^0_f - E^0_n\over \hbar}$. Using $\braket{f^0|n^0}=\delta_{fn}$:

.. math::

    i\hbar{\d\over\d t}d_f(t) =\sum_n d_n(t) e^{i w_{fn} t}\braket{f^0|H^1|n^0}


we integrate from $t_1$ to $t$:

.. math::

    i\hbar\left((d_f(t)-d_f(t_1)\right) =\sum_n\int_{t_1}^t d_n(t') e^{i w_{fn} t'}\braket{f^0|H^1(t')|n^0} \d t'


Let the initial wavefunction at time $t_1$ be some particular state $\ket{\psi(t_1)}=\ket{i^0}$ of the unperturbed Hamiltonian, then $d_n(t_1)=\delta_{ni}$ and we get:

.. math::
    :label: perturb0

    d_f(t) =\delta_{fi}-{i\over\hbar}\sum_n\int_{t_1}^t d_n(t') e^{i w_{fn} t'}\braket{f^0|H^1(t')|n^0} \d t'


This is the equation that we will use for the perturbation theory.

In the zeroth order of the perturbation theory, we set $H^1(t)=0$ and we get:

.. math::

    d_f(t)=\delta_{fi}



In the first order of the perturbation theory, we take the solution $d_n(t)=\delta_{ni}$ obtained in the zeroth order and substitute into the right hand side of :eq:`perturb0`:

.. math::

    d_f(t) = \delta_{fi} -{i\over\hbar}\int_{t_1}^{t} e^{i w_{fi} t'}\braket{f^0|H^1(t')|i^0}\d t'



In the second order, we take the last solution, substitute into the right hand side of :eq:`perturb0` again:

.. math::

    d_f(t) = \delta_{fi}+ \left(-{i\over\hbar}\right)\int_{t_1}^{t} e^{i w_{fi} t'}\braket{f^0|H^1(t')|i^0}\d t' +



.. math::

    + \left(-{i\over\hbar}\right)^2\sum_n \int_{t_1}^t\d t''\int_{t_1}^{t''}\d t' e^{iw_{fn}t''}\braket{f^0|H^1(t'')|n^0} e^{i w_{ni} t'}\braket{n^0|H^1(t')|i^0}


And so on for higher orders of the perturbation theory --- more terms will arise on the right hand side of the last formula, so this is our main formula for calculating the $d_n(t)$ coefficients.

Time Independent Perturbation Theory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a special case, if $H^1$ doesn't depend on time, the coefficients $d_n(t)$ simplify, so we calculate them in this section explicitly. Let's take

.. math::

    H(t) = H^0 + e^{t/\tau} H^1


so at the time $t_1=-\infty$ the Hamiltonian $H(t)=H^0$ is unperturbed and we are interested in the time $t=0$, when the Hamiltonian becomes $H(t) = H^0 + H^1$ (the coefficients $d_n(t)$ will still depend on the $\tau$ variable) and we do the limit $\tau\to\infty$ (this corresponds to smoothly applying the perturbation $H^1$ at the time negative infinity).

Let's calculate $d_f(0)$:

.. math::

    d_f(0) = \delta_{fi}+ \left(-{i\over\hbar}\right)\int_{-\infty}^0 e^{i w_{fi} t'}e^{t\over\tau}\d t'\braket{f^0|H^1|i^0} +



.. math::

    + \left(-{i\over\hbar}\right)^2\sum_n \int_{-\infty}^0\d t''\int_{-\infty}^{t''}\d t' e^{iw_{fn}t''} e^{i w_{ni} t'} e^{t''\over\tau} e^{t'\over\tau} \braket{f^0|H^1|n^0} \braket{n^0|H^1|i^0} =



.. math::

    = \delta_{fi}+ \left(-{i\over\hbar}\right) {1\over{1\over\tau}+i\omega_{fi}} \braket{f^0|H^1|i^0} +



.. math::

    + \left(-{i\over\hbar}\right)^2\sum_n {1\over{1\over\tau}+i\omega_{ni}} {1\over{2\over\tau}+i\omega_{fn}+i\omega_{ni}} \braket{f^0|H^1|n^0} \braket{n^0|H^1|i^0}


Taking the limit $\tau\to\infty$:

.. math::

    d_f(0) = \delta_{fi}+ \left(-{1\over\hbar}\right) {1\over\omega_{fi}} \braket{f^0|H^1|i^0} +



.. math::

    + \left(-{1\over\hbar}\right)^2\sum_n {1\over\omega_{ni}} {1\over\omega_{fn}+\omega_{ni}} \braket{f^0|H^1|n^0} \braket{n^0|H^1|i^0} =



.. math::

    = \delta_{fi}- {\braket{f^0|H^1|i^0}\over E_f^0-E_i^0} +



.. math::

    + \sum_n { \braket{f^0|H^1|n^0} \braket{n^0|H^1|i^0} \over (E_n^0-E_i^0)(E_f^0-E_i^0) }


Substituting this into :eq:`psi` evaluated for $t=0$:

.. math::

    \ket{\psi(0)}=\sum_n d_n(0) \ket{n^0}=



.. math::

    = \ket{i^0}- \sum_n {\ket{n^0}\braket{n^0|H^1|i^0}\over E_n^0-E_i^0} +



.. math::

    + \sum_{n,m} {\ket{n^0} \braket{n^0|H^1|m^0} \braket{m^0|H^1|i^0} \over (E_m^0-E_i^0)(E_n^0-E_i^0) }


The sum $\sum_n$ is over all $n\neq i$, similarly for the other sum. Let's also calculate the energy:

.. math::

    E =\braket{\psi(0)|H|\psi(0)} =\braket{\psi(0)|H^0+H^1|\psi(0)} =



.. math::

    \left(\cdots- \sum_{n'\neq i} {\braket{i^0|H^1|n'^0}\bra{n'^0}\over E_{n'}^0-E_i^0} +\bra{i^0}\right) (H^0+H^1) \left(\ket{i^0}- \sum_{n\neq i} {\ket{n^0}\braket{n^0|H^1|i^0}\over E_n^0-E_i^0} +\cdots\right)


To evaluate this, we use the fact that $\braket{i^0|H^0|i^0}=E_i^0$ and $\braket{i^0|H^0|n^0}=E_i^0\delta_{ni}$:

.. math::

    E = E_i^0 + \braket{i^0|H^1|i^0} - \sum_{n\neq i} {\braket{i^0|H^1|n^0}\braket{n^0|H^1|i^0}\over E_n^0-E_i^0}+\cdots =



.. math::

    = E_i^0 + \braket{i^0|H^1|i^0} - \sum_{n\neq i} {|\braket{n^0|H^1|i^0}|^2\over E_n^0-E_i^0}+\cdots


Where we have neglected the higher order terms, so we can identify the corrections to the energy $E$ coming from the particular orders of the perturbation theory:

.. math::

    E_i^0 = \braket{i^0|H^0|i^0}



.. math::

    E_i^1 = \braket{i^0|H^1|i^0}



.. math::

    E_i^2 = - \sum_{n\neq i} {|\braket{n^0|H^1|i^0}|^2\over E_n^0-E_i^0}


.. index:: scattering theory

Scattering Theory
-----------------

The incoming plane wave state is a solution of

.. math::

    H_0\ket{{\bf k}}=E_k\ket{{\bf k}}


with $H_0={p^2\over 2m}$. E.g.

.. math::

    \braket{{\bf r}|{\bf k}}=e^{i{\bf r}\cdot{\bf k}}



.. math::

    E_k = {\hbar^2 k^2\over 2 m}


We want to solve:

.. math::

    (H_0+V)\ket{\psi}=E_k\ket{\psi}


The solution of this is:

.. math::

    \ket{\psi}=\ket{{\bf k}}+{1\over E_k-H_0}V\ket{\psi} =\ket{\bf{k}}+GV\ket{\psi}


where

.. math::

    G={1\over E_k-H_0}


is the Green function for the Schrödinger equation. $G$ is not unique, it contains both outgoing and ingoing waves. As shown below, one can distinguish between these two by adding a small $i\epsilon$ into the denominator, that moves the poles of the Green functions above and below the $x$-axis:

.. math::

    G_+={1\over E_k-H_0+i\epsilon}



.. math::

    G_-={1\over E_k-H_0-i\epsilon}


Both $G_+$ and $G_-$ are well-defined and unique. One can calculate both Green functions explicitly:

.. math::

    G_+({\bf r}, {\bf r'}) = \braket{{\bf r}|G_+|{\bf r'}}=\bra{{\bf r}}{1\over E_k-H_0+i\epsilon}\ket{{\bf r'}}=

    =\int{\d^3k'\over(2\pi)^3} {\braket{{\bf r}|{\bf k'}}\braket{\bf{k'}|\bf{r'}}\over E_k-E_{k'}+i\epsilon}
    =\int{\d^3k'\over(2\pi)^3} {e^{i{\bf k'}\cdot({\bf r}-{\bf r'})}\over E_k-E_{k'}+i\epsilon}
    ={2m\over\hbar^2}\int{\d^3k'\over(2\pi)^3} {e^{i{\bf k'}\cdot({\bf r}-{\bf r'})}\over k^2-{k'}^2+i\epsilon}=

    ={4\pi m\over(2\pi)^3\hbar^2i|{\bf r}-{\bf r'}|} \int_{-\infty}^\infty\d^3k' k'{e^{i k'|{\bf r}-{\bf r'}|}\over k^2-{k'}^2+i\epsilon}
    ={4\pi m\over(2\pi)^3\hbar^2i|{\bf r}-{\bf r'}|} (2\pi i)k{e^{i k|{\bf r}-{\bf r'}|}\over 2k}=


    ={me^{i k|{\bf r}-{\bf r'}|}\over2\pi\hbar^2|{\bf r}-{\bf r'}|}

Similarly:

.. math::

    G_-({\bf r}, {\bf r'})
    = \braket{{\bf r}|G_-|{\bf r'}}
    =\bra{{\bf r}}{1\over E_k-H_0-i\epsilon}\ket{{\bf r'}} =\cdots
    ={me^{-i k|{\bf r}-{\bf r'}|}\over2\pi\hbar^2|{\bf r}-{\bf r'}|}


Assuming $|{\bf r'}|\ll|{\bf r}|$, we can taylor expand $|{\bf r}-{\bf r'}|$:

.. math::

    |{\bf r}-{\bf r'}| =e^{-{\bf r'}\cdot\nabla}|{\bf r}| =\left(1-{\bf r'}\cdot\nabla+\left(-{\bf r'}\cdot\nabla\right)^2 +O\left(r'^3\right) \right)|{\bf r}| =|{\bf r}|-{\bf r'}\cdot\nabla|{\bf r}|+O\left(r'^2\right) =

    =r-{\bf r'}\cdot{\bf \hat r}+O\left(r'^2\right)

so:

.. math::

    e^{i k|{\bf r}-{\bf r'}|} \approx e^{ikr} e^{-i k{\bf r'}\cdot{\bf\hat r}}

    |{\bf r}-{\bf r'}| \approx r

and simplify the result even further:

.. math::

    G_+({\bf r}, {\bf r'}) ={m\over2\pi\hbar^2}{e^{ikr}\over r} e^{-i k{\bf r'}\cdot{\bf\hat r}}

    G_-({\bf r}, {\bf r'}) ={m\over2\pi\hbar^2}{e^{-ikr}\over r} e^{i k{\bf r'}\cdot{\bf\hat r}}

Let's get back to the solution of the Schrödinger equation:

.. math::

    \ket{\psi}=\ket{\bf{k}}+G_+V\ket{\psi}


It contains the solution $\ket{\psi}$ on both sides of the equation, so we express it explicitly:

.. math::

    \ket{\psi}-G_+V\ket{\psi}=\ket{\bf{k}}



.. math::

    \ket{\psi}={1\over 1-G_+V}\ket{\bf{k}}


and multiply by $V$:

.. math::

    V\ket{\psi}={V\over 1-G_+V}\ket{\bf{k}}=T\ket{\bf{k}}


where $T$ is the transition matrix:

.. math::

    T={V\over 1-G_+V}=V(1+G_+V + (G_+V)^2 + \cdots)=



.. math::

    =V+VG_+V + VG_+VG_+V + \cdots=



.. math::

    =V+V{1\over E_k-H_0+i\epsilon}V + V{1\over E_k-H_0+i\epsilon}V{1\over E_k-H_0+i\epsilon}V + \cdots


Then the final solution is:

.. math::

    \ket{\psi}=\ket{\bf{k}}+G_+V\ket{\psi}=\ket{\bf{k}}+G_+T\ket{{\bf k}}


and in a coordinate representation:

.. math::

    \psi({\bf r})=\braket{{\bf r}|\psi} =\braket{{\bf r}|\bf{k}}+\braket{{\bf r}|G_+T|{\bf k}} =\braket{{\bf r}|\bf{k}}+\int\d^3 r'\braket{{\bf r}|G_+|{\bf r'}} \braket{{\bf r'}|T|{\bf k}}=



.. math::

    =\braket{{\bf r}|\bf{k}}+\int\d^3 r'\d^3k'\braket{{\bf r}|G_+|{\bf r'}} \braket{{\bf r'}|{\bf k'}}\braket{{\bf k'}|T|{\bf k}}=



.. math::

    =e^{i{\bf k}\cdot{\bf r}} +\int\d^3 r'\d^3k' G_+({\bf r}, {\bf r'}) e^{i{\bf k'}\cdot{\bf r'}} \braket{{\bf k'}|T|{\bf k}}


Plugging the representation of the Green function for $|{\bf r'}|\ll|{\bf r}|$
in:

.. math::

    \psi({\bf r}) =e^{i{\bf k}\cdot{\bf r}} + {m\over2\pi\hbar^2}{e^{ikr}\over r} \int\d^3 r'\d^3k' e^{-i k{\bf r'}\cdot{\bf\hat r}} e^{i{\bf k'}\cdot{\bf r'}} \braket{{\bf k'}|T|{\bf k}}=

    =e^{i{\bf k}\cdot{\bf r}} + {m\over2\pi\hbar^2}{e^{ikr}\over r} \int\d^3 r'\d^3k' e^{i {\bf r'}\cdot({\bf k'}-k{\bf\hat r})} \braket{{\bf k'}|T|{\bf k}}=

    =e^{i{\bf k}\cdot{\bf r}} + {m\over2\pi\hbar^2}{e^{ikr}\over r} \int\d^3k' \delta({\bf k'}-k{\bf\hat r}) \braket{{\bf k'}|T|{\bf k}}=

    =e^{i{\bf k}\cdot{\bf r}} + {m\over2\pi\hbar^2}{e^{ikr}\over r} \braket{k{\bf\hat r}|T|{\bf k}}=

    =e^{i{\bf k}\cdot{\bf r}} + f(\theta,\phi)\, {e^{ikr}\over r}


where the scattering amplitude $f(\theta,\phi)$ is:

.. math::

    f(\theta,\phi)= {m\over2\pi\hbar^2} \braket{k{\bf\hat r}|T|{\bf k}}
        = {m\over2\pi\hbar^2} \braket{{\bf k'}|T|{\bf k}}


Where ${\bf k'}=k{\bf\hat r}$ is the final momentum.

The differential cross section ${\d\sigma\over\d\Omega}$ is defined as the probability to observe the scattered particle in a given state per solid angle, e.g. the scattered flux per unit of solid angle per incident flux:

.. math::

    {\d\sigma\over\d\Omega}
        = {1\over|{\bf j}_i|}{\d n\over\d\Omega}
        = {r^2\over|{\bf j}_i|}{\d n\over r^2\d\Omega}
        = {r^2\over|{\bf j}_i|}{\d n\over \d S}
        = {r^2\over|{\bf j}_i|}\,{\bf j}_o\cdot {\bf n}
        = {r^2\over|{\bf j}_i|}\,{\bf j}_o\cdot {\bf \hat r} =

    = {r^2\over{\hbar k\over m}}\,{\hbar k\over m}\left({1\over r^2}
            +{i\over k r^3}\right)|f(\theta, \phi)|^2
    = \left(1 +{i\over k r}\right)|f(\theta, \phi)|^2
    \to |f(\theta, \phi)|^2


where we used $|{\bf j}_i|={\hbar k\over m}$ and

.. math::

    {\bf j}_o\cdot {\bf \hat r} ={\hbar\over2 m i}\left( \psi^*\nabla\psi- \psi\nabla\psi^* \right)\cdot{\bf \hat r} ={\hbar\over2 m i}\left( \psi^*{\partial\over\partial r}\psi- \psi{\partial\over\partial r}\psi^* \right) =



.. math::

    ={\hbar\over2 m i}\left( f^*(\theta, \phi){e^{-ikr}\over r}{\partial\over\partial r} \left(f(\theta, \phi){e^{ikr}\over r}\right)- f(\theta, \phi){e^{ikr}\over r}{\partial\over\partial r}\left(f^*(\theta, \phi){e^{-ikr}\over r}\right) \right)=



.. math::

    ={\hbar k\over m}\left({1\over r^2}+{i\over k r^3} \right)|f(\theta, \phi)|^2


Let's write the explicit formula for the transition matrix:

.. math::

    \braket{{\bf k'}|T|{\bf k}} =\int\d^3r\braket{{\bf k'}|{\bf r}}\braket{{\bf r}|V|{\bf k}} +\int\d^3r\d^3r'\braket{{\bf k'}|{\bf r}}\braket{{\bf r}|VG_+|{\bf r'}} \braket{{\bf r'}|V|{\bf k}}+\cdots=



.. math::

    =\int\d^3r e^{i({\bf k}-{\bf k'})\cdot{\bf r}}V({\bf r})
    +\int\d^3r\d^3r'e^{-i{\bf k'}\cdot{\bf r}} V({\bf r}) {e^{i k|{\bf r}-{\bf
    r'}|}\over|{\bf r}-{\bf r'}|} V({\bf r'})e^{i{\bf k}\cdot{\bf r'}}+\cdots


Born Approximation
~~~~~~~~~~~~~~~~~~

The Born approximation is just the first term:

.. math::

    \braket{{\bf k'}|T|{\bf k}}
        \approx\int\d^3r e^{i({\bf k}-{\bf k'})\cdot{\bf r}}V({\bf r})
        = \int \d r\, \d\theta\,\d\phi\, e^{iqr\cos\theta}V(r) r^2\sin\theta =

    = 4\pi\int_0^\infty rV(r)\sin(qr)\,\d r

We can also write it as:

.. math::

    \braket{{\bf k'}|T|{\bf k}}
        \approx\int\d^3r e^{-i{\bf q}\cdot{\bf r}}V({\bf r})
        = \tilde V({\bf q})

where $\bf q=k'-k$. Note that for $\bf |k'|\approx |k|$ we can write
$|{\bf q}|$ using the angle $\theta$ between the vectors $\bf k'$ and $\bf k$:

.. math::

    |{\bf q}| = |{\bf k}' - {\bf k}|
        = \sqrt{k'^2 + k^2 - 2k'k\cos\theta}
        \approx \sqrt{k^2 + k^2 - 2k^2\cos\theta}
        =

        = \sqrt{2k^2 (1 -\cos\theta)}
        = \sqrt{4k^2 \sin^2 {\theta\over 2}}
        = 2k\sin\left(\theta\over2\right)



Given the $\tilde V({\bf q})$ we can then calculate the
scattering potential $V({\bf r})$ by the Fourier transform:

.. math::

    V({\bf r}) = \int {\d^3 q\over (2\pi)^3} \tilde V({\bf q})
        e^{i{\bf q}\cdot {\bf r}}

Example 1:

.. math::

    \tilde V({\bf q}) = - {g^2\over |{\bf q}|^2 + m_{\phi}^2}

    V({\bf r}) = \int {\d^3 q\over (2\pi)^3} {-g^2\over |{\bf q}|^2 +
        m_{\phi}^2} e^{i{\bf q}\cdot {\bf r}} = \cdots =
        - {g^2\over 4\pi} {1\over r} e^{-m_\phi r}

Example 2:

.. math::

    \tilde V({\bf q}) = {e^2\over |{\bf q}|^2}

    V({\bf r}) = \int {\d^3 q\over (2\pi)^3} {e^2\over |{\bf q}|^2}
        e^{i{\bf q}\cdot {\bf r}} = \cdots = {e^2\over 4\pi r}

Example 3 --- Yukawa potential in Born approximation:

.. math::

    V(r) = -V_0 {e^{-\alpha r}\over r}

    \tilde V({\bf q}) = -{4\pi V_0\over |{\bf q}|^2 + \alpha^2}

    f(\theta,\phi) = {m\over2\pi\hbar^2} \braket{{\bf k'}|T|{\bf k}}
        = {m\over2\pi\hbar^2} \tilde V({\bf q})
        = -{m\over2\pi\hbar^2} {4\pi V_0\over |{\bf q}|^2 + \alpha^2}
        = -{2m\over\hbar^2} {V_0\over |{\bf q}|^2 + \alpha^2}

    {\d\sigma\over\d\Omega} = |f(\theta, \phi)|^2
        = \left(2mV_0\over \hbar^2\right)^2
            {1\over\left(|{\bf q}|^2 + \alpha^2\right)^2}
        = \left(2mV_0\over \hbar^2\right)^2
            {1\over\left(4k^2\sin^2\left(\theta\over2\right)
            + \alpha^2\right)^2}

    \sigma
        = \int {\d\sigma\over\d\Omega} \d\Omega
        = \int {\d\sigma\over\d\Omega} \sin\theta \d \theta\d\phi
        =

        = \left(2mV_0\over \hbar^2\right)^2\int
        {1\over\left(4k^2\sin^2\left(\theta\over2\right) + \alpha^2\right)^2}
        \sin\theta \d \theta\d\phi =

        = \left(2mV_0\over \hbar^2\right)^2 2\pi\int_0^\pi
        {\sin\theta\d\theta\over
            \left(4k^2\sin^2\left(\theta\over2\right) + \alpha^2\right)^2} =

        = \left(2mV_0\over \hbar^2\right)^2 2\pi\int_0^\pi
        {\sin\theta\d\theta\over
            \left(2k^2(1-\cos\theta) + \alpha^2\right)^2} =

        = \left(2mV_0\over \hbar^2\right)^2 2\pi\int_{-1}^1
        {\d y\over \left(2k^2(1+y) + \alpha^2\right)^2} =

        = \left(2mV_0\over \hbar^2\right)^2 2\pi
            \int_{\alpha^2}^{4k^2+\alpha^2} {2k^2\d z\over z^2} =

        = \left(2mV_0\over \hbar^2\right)^2 2\pi 2k^2
            \left({1\over\alpha^2} - {1\over 4k^2 + \alpha^2}\right)


Example 4 --- Coulomb potential in Born approximation:

.. math::

    \alpha \to 0

    {\d\sigma\over\d\Omega}
        = \left(2mV_0\over \hbar^2\right)^2
            {1\over\left(4k^2\sin^2\left(\theta\over2\right)\right)^2}
        = \left(2mV_0\over 4\hbar^2k^2\right)^2
            {1\over\sin^4{\theta\over2}}

    E = {p^2\over 2m} = {\hbar^2k^2\over 2m}

    {\d\sigma\over\d\Omega}
        = \left(V_0\over 4 E\right)^2 {1\over\sin^4{\theta\over2}}

    V_0 \to {Z Z' e^2 \over 4\pi \epsilon_0}
        = Z Z' \alpha \hbar c

    {\d\sigma\over\d\Omega}
        = \left(ZZ'\alpha\hbar c\over 4 E\right)^2
            {1\over\sin^4{\theta\over2}}

By setting $E=\half m v_0^2$ we obtain the classical Rutherford cross-section
formula.


Systematic Perturbation Theory in QM
====================================

We have

.. math::

    H = H_0 + e^{-\epsilon |t|} H_1

where the ground state of the noninteracting Hamiltonian $H_0$ is:

.. math::

    H_0\ket{0} = E_0\ket{0}

and the ground state of the interacting Hamiltonian $H$ is:

.. math::

    H\ket{\Omega} = E\ket{\Omega}

Then:

.. math::

    H\ket{\Omega} = (H_0 + H_1)\ket{\Omega} = E\ket{\Omega}

    \braket{0|H_0 + H_1|\Omega} = E\braket{0 | \Omega}

    E_0\braket{0|\Omega} + \braket{0|H_1|\Omega} = E\braket{0 | \Omega}

    E = E_0 + {\braket{0|H_1|\Omega}\over\braket{0 | \Omega}}

We can also write

.. math::

    \ket{\Omega} = \lim_{\epsilon\to0+} U_\epsilon(0, -\infty)\ket{0}

where

.. math::

    U_\epsilon(t, t_0) = T \exp\left(-{i\over\hbar}\int_{t_0}^t \d t'
        e^{-\epsilon|t'|} H_1(t')\right)

Let's write several common expressions for the ground state energy:

.. math::

    \Delta E = E - E_0 = {\braket{0|H_1|\Omega}\over\braket{0 | \Omega}}
    = {\braket{0|H_1 U(0, -\infty)|0}\over\braket{0 |U(0, -\infty)|0}}
    =

    = \lim_{t\to0} {\braket{0|H_1 U(t, -\infty)|0}\over
        \braket{0 |U(t, -\infty)|0}}
    = \lim_{t\to0} {\braket{0|i\partial_t U(t, -\infty)|0}\over
        \braket{0 |U(t, -\infty)|0}}
    = \lim_{t\to0} {i\partial_t\braket{0| U(t, -\infty)|0}\over
        \braket{0 |U(t, -\infty)|0}}
    =

    = \lim_{t\to0} i\partial_t\log\braket{0| U(t, -\infty)|0}
    \equiv \lim_{t\to\infty(1-i\epsilon)} i{\d\over\d t}\log
        \braket{0| U(t, -\infty)|0}

The last expression incorporates the $\epsilon$ dependence of $U_\epsilon$
explicitly. The vacuum amplitude is sometimes denoted by $R(t)$:

.. math::

    R(t) = \braket{0| U(t, -\infty)|0}

The two point (interacting) Green (or correlation) function is:

.. math::

    G(x, y) = \braket{\Omega|T\phi(x)\phi(y)|\Omega} =
        {\braket{0|T\phi(x)\phi(y)U(\infty, -\infty)|0}\over
            \braket{0|U(\infty, -\infty)|0}}

The $\epsilon\to0$ limit of $U_\epsilon$ is tacitly assumed to make this
formula well defined (sometimes the other way $t\to\infty(1-i\epsilon)$ of writing the same limit is used). Another way of writing the formula above for the Green
function in QM is:

.. math::

    G({\bf k}_1, {\bf k}_2, t_2-t_1) = i
        \braket{\Omega|T c_{{\bf k}_2}(t_2)c_{{\bf k}_1}^\dag(t_1)|\Omega} =
        i {\braket{0|T c_{{\bf k}_2}(t_2)c_{{\bf k}_1}^\dag(t_1)
            U(\infty, -\infty)|0}\over
            \braket{0|U(\infty, -\infty)|0}}

Last type of similar expressions to consider is the scattering amplitude:

.. math::

    \braket{f|U(\infty, -\infty)|i}

where the initial state is let's say a boson+fermion and the final state a
boson+antifermion:

.. math::

    \ket{i} = a_{\bf k}^\dag b_{\bf l}^{s\dag} \ket{0}

    \ket{f} = a_{\bf p}^\dag a_{\bf q}^{r\dag} \ket{0}

This is just an example, the $\ket{i}$ and $\ket{f}$ states can contain any
number of (arbitrary) particles.

Appendix
========

.. index:: dimensional analysis

Units and Dimensional Analysis
------------------------------

The evolution operator is dimensionless:

.. math::

    U(-\infty,\infty) = T\exp\left({i\over\hbar}\int_{-\infty}^{\infty}\d^4 x \L(x) \right)


So:

.. math::

    \left[\int_{-\infty}^{\infty}\d^4 x \L(x) \right] = [\hbar] = M^0


where $M$ is an arbitrary mass scale. Length unit is $M^{-1}$, so then

.. math::

    [\L(x)] = M^4


For the particular forms of the Lagrangians above we get:

.. math::

    [m\bar ee] = [m^2 Z_\mu Z^\mu] = [m^2 H^2] = [i\bar e\gamma^\mu\partial_\mu e] = [\L] = M^4


so $[\bar ee] = M^3$, $[Z_\mu Z^\mu]=[H^2] = M^2$ and we get

.. math::

    [e] = [\bar e] = M^{3\over2}



.. math::

    [Z_\mu] = [Z^\mu] = [H] = [\partial_\mu] = [\partial^\mu] = M^1



Example: what is the dimension of $G_\mu$ in $\L = -{G_\mu\over\sqrt2} [\bar \psi_{\nu_\mu}\gamma^\mu (1-\gamma_5) \psi_\mu] [\bar \psi_e\gamma^\mu (1-\gamma_5) \psi_{\nu_e}]$? Answer:

.. math::

    [\L] = [G_\mu \bar\psi\psi\bar\psi\psi]



.. math::

    M^4 = [G_\mu] M^{3\over2}M^{3\over2}M^{3\over2}M^{3\over2}



.. math::

    [G_\mu] = M^{-2}



In order to get the above units from the SI units, one has to do the following identification:

.. math::

    kg\to M^1



.. math::

    m\to M^{-1}



.. math::

    s\to M^{-1}



.. math::

    A\to M^1


The SI units of the above quantities are:

.. math::

    [\phi] = \rm V={kg\,m^2\over A\,s^3}=M

    [A_\mu]={[\phi]\over [c]}=\rm{V\,s\over m} = {kg\, m\over A\,s^2}=M

    [c]=\rm {m\over s} = 1

    [e]=\rm C = A\, s=1

    [\hbar]=\rm J\,s = {m^2\,kg\over s}=1

    [\partial_\mu]=\rm {1\over m}=M

    [F_{\mu\nu}]=[\partial_\mu A_\nu]=\rm {kg\over A\,s^2}=M^2

    [\L]=[F_{\mu\nu}]^2=\rm {kg^2\over A^2\,s^4}=M^4

    [\psi]=\rm {kg^{1\over2}\over A\,m\,s}=M^{3\over2}

The SI units are useful for checking that the $c$, $e$ and $\hbar$ constants are at correct places in the expression.

.. index::
    pair: tensors; QFT

Atomic Units
------------

Hartree atomic units are defined using the relations:

.. math::

    \hbar = m = e = 4\pi\epsilon_0 = 1

so for example for the Bohr radius we get:

.. math::

    a_0 = {4\pi\epsilon_0 \hbar^2 \over m e^2} = 1

for fine structure constant ($\alpha=1/137.036...$) we get:

.. math::

    \alpha = {e^2\over 4\pi\epsilon_0 \hbar c} = {1\over c}

from which we calculate the speed of light $c$ in atomic units as:

.. math::

    c = {1\over\alpha}

Energy is measured in Hartrees, one Hartree being

.. math::

    1{\rm\,Ha} = {\hbar^2\over m a_0^2} = 1{\rm\,(a.u.)} = 27.211\rm\,eV

Hamiltonian and the corresponding spectrum of the Hydrogen atom:

.. math::

    H = -{\hbar^2\over 2m} \nabla^2 - {1\over 4\pi\epsilon_0} {e^2\over r}

    E_n = -{\hbar^2\over m a_0^2} {1\over 2n^2}

become in atomic units:

.. math::

    H = -{1\over 2} \nabla^2 - {1\over r}

    E_n = -{1\over 2n^2}

Poisson equation (Gauss's law)

.. math::

    \nabla^2\phi = -{\rho\over\epsilon_0}

becomes:

.. math::

    \nabla^2\phi = -{4\pi\rho}

Tensors in Special Relativity and QFT
-------------------------------------

In general, the covariant and contravariant vectors and tensors work just like
in special (and general) relativity. We use the metric $g_{\mu\nu}={\rm
diag}(1, -1, -1, -1)$ (e.g. signature -2, but it's possible to also use the
metric with signature +2). The four potential $A^\mu$ is given by:

.. math::

    A^\mu=\left({\phi\over c}, {\bf A}\right) = (A^0, A^1, A^2, A^3)


where $\phi$ is the electrostatic potential. Whenever we write $\bf A$, the
components of it are given by the upper indices, e.g. ${\bf A}=(A^1, A^2,
A^3)$. The components with lower indices can be calculated using the metric
tensor, so it depends on the signature convention:

.. math::

    A_\mu=g_{\mu\nu}A^\nu=(A^0, -{\bf A}) = (A^0, -A^1, -A^2, -A^3)


In our case we got $A_0=A^0$ and $A_i = -A^i$ (if we used the other signature
convention, then the sign of $A_0$ would differ and $A_i$ would stay the same).
The length (squared) of the vector is:

.. math::

    A^2 = A_\mu A^\mu = \left(A^0\right)^2 - \left| {\bf A} \right|^2
    = \left(A^0\right)^2 - {\bf A}^2

where ${\bf A}^2 \equiv |{\bf A}|^2 = (A^1)^2+(A^2)^2+(A^3)^2$.

The position 4-vector is (in any metric):

.. math::

    x^\mu = (ct, {\bf x})

Gradient is defined as (in any metric):

.. math::

    \partial_\mu = (\partial_0, \partial_1, \partial_2, \partial_3) =
    {\partial\over\partial x^\mu}=
    \left({1\over c}{\partial\over\partial t},{\partial\over\partial x},{\partial\over\partial y},{\partial\over\partial z}\right)


the upper indices depend on the signature, e.g. for -2:

.. math::

    \partial^\mu = (\partial^0, \partial^1, \partial^2, \partial^3)= \left({1\over c}{\partial\over\partial t},-{\partial\over\partial x},-{\partial\over\partial y},-{\partial\over\partial z}\right)


and +2:

.. math::

    \partial^\mu = (\partial^0, \partial^1, \partial^2, \partial^3)= \left(-{1\over c}{\partial\over\partial t},{\partial\over\partial x},{\partial\over\partial y},{\partial\over\partial z}\right)

The d'Alembert operator is:

.. math::

    \partial^2 \equiv \partial_\mu \partial^\mu


the 4-velocity is (in any metric):

.. math::

    v^\mu = {\d x^\mu\over\d\tau} =
    {\d t\over\d\tau}{\d x^\mu\over\d t} = \gamma(c, {\bf v})

where $\tau$ is the proper time,
$\gamma={\d t\over\d\tau}={1\over\sqrt{1 - {{\bf v}^2\over c^2}}}$
and ${\bf v}={\d {\bf x}\over\d t}$
is the velocity in the coordinate time $t$. In the metric
with signature +2:

.. math::

    v^2 = v_\mu v^\mu = g_{\mu\nu}v^\mu v^\nu =
        -\gamma^2 c^2 + \gamma^2{\bf v}^2
    = {-c^2 + {\bf v}^2 \over 1 - {{\bf v}^2\over c^2}} = -c^2

With signature -2 we get $v^2 = c^2$. The 4-momentum is (in any metric)

.. math::

    p^\mu = m v^\mu = m\gamma(c, {\bf v})

where $m$ is the rest mass. The fluid-density 4-current is (in any metric):

.. math::

    j^\mu = \rho v^\mu = \rho\gamma(c, {\bf v})

where $\rho$ is the fluid density at rest. For example the vanishing
4-divergence (the continuity equation) is written as (in any metric):

.. math::

    0 = \partial_\mu j^\mu = {1\over c}{\partial\over\partial t} (\rho\gamma c)
        + \nabla \cdot (\rho\gamma {\bf v})
    = {\partial\over\partial t} (\rho\gamma) + \nabla \cdot (\rho{\bf v}\gamma)
    = {\partial\over\partial t}\left(\rho\over
        \sqrt{1-{{\bf v}^2\over c^2}}\right)
      + \nabla \cdot\left(\rho{\bf v}\over
        \sqrt{1-{{\bf v}^2\over c^2}}\right)

Momentum (${\bf p}=-i\hbar\nabla$) and energy ($E=i\hbar{\partial\over\partial
t}$) is combined into 4-momentum as

.. math::

    p^\mu = \left({E\over c},{\bf p}\right) = i\hbar\left({1\over c}{\partial\over\partial t},-\nabla\right) = i\hbar\left(\partial_0,-\partial_j\right) = i\hbar\left(\partial^0,\partial^j\right) = i\hbar\partial^\mu

    p_\mu = g_{\mu\nu}p^\nu = i\hbar g_{\mu\nu}\partial^\nu = i\hbar\partial_\mu

For the signature $+2$ we get $p^\mu = -i\hbar\partial^\mu$ and $p_\mu =
-i\hbar\partial_\mu$.

For $p^2$ we get (signature -2):

.. math::

    p^2 = p_\mu p^\mu = (p^0)^2 - {\bf p}^2 = (p_0)^2 - {\bf p}^2
    = {E^2\over c^2} - {\bf p}^2

    p^2 = p_\mu p^\mu = m^2 v_\mu v^\mu = m^2 c^2

comparing those two we get the following useful relations (valid in any metric):

.. math::

    {E^2\over c^2} - {\bf p}^2 = m^2 c^2

    E^2 = m^2 c^4 + {\bf p}^2 c^2

    E = \sqrt{m^2c^4 + {\bf p}^2c^2}
    = mc^2\sqrt{1 + {{\bf p}^2\over m^2c^2}}
    = mc^2\left(1 + {{\bf p}^2\over 2m^2c^2} + O\left({p^4\over m^4c^4}\right)
        \right)
    =

    = mc^2 + {{\bf p}^2\over 2m} + O\left(p^4\over m^3c^2\right)


the following relations are also useful:

.. math::

    p^2 = p_\mu p^\mu = -\hbar^2\partial_\mu \partial^\mu \equiv
    -\hbar^2\partial^2
    = -\hbar^2\left(\partial_0\partial^0 + \partial_i\partial^i\right)
    = -\hbar^2\left(\partial_0\partial_0 - \partial_i\partial_i\right)
    =

    = -\hbar^2\left({1\over c^2}{\partial^2\over\partial t^2} - \nabla^2\right)
    = -{\hbar^2\over c^2}{\partial^2\over\partial t^2} + \hbar^2\nabla^2

For the signature $+2$ we get:

.. math::

    p^2 = p_\mu p^\mu = -\hbar^2\partial_\mu \partial^\mu \equiv
    -\hbar^2\partial^2
    = -\hbar^2\left(\partial_0\partial^0 + \partial_i\partial^i\right)
    = -\hbar^2\left(-\partial_0\partial_0 + \partial_i\partial_i\right)
    =

    = -\hbar^2\left(-{1\over c^2}{\partial^2\over\partial t^2} + \nabla^2\right)
    = {\hbar^2\over c^2}{\partial^2\over\partial t^2} - \hbar^2\nabla^2

So for example the Klein-Gordon equation:

.. math::

    \left({\hbar^2\over c^2}{\partial^2\over\partial t^2} - \hbar^2\nabla^2
    +m^2c^2\right)\psi = 0

can be for signature $-2$ written as:

.. math::

    (+\hbar^2\partial^2 + m^2 c^2)\psi = (-p^2 + m^2c^2)\psi = 0

and for $+2$ as:

.. math::

    (-\hbar^2\partial^2 + m^2 c^2)\psi = (p^2 + m^2c^2)\psi = 0

Note: for the signature +2, we would get $p^\mu=-i\hbar\partial^\mu$ and $p_\mu=-i\hbar\partial_\mu$.

For the minimal coupling $D_\mu = \partial_\mu + {i\over\hbar}e A_\mu$ we get:

.. math::

    D^0 = \partial^0 + {i\over\hbar}e A^0



.. math::

    D^j = \partial^j + {i\over\hbar}e A^j=-{i\over\hbar}(i\hbar\partial^j-eA^j) =-{i\over\hbar}({\bf p}-e{\bf A})


and for the lower indices:

.. math::

    D_0 = \partial_0 + {i\over\hbar}e A_0



.. math::

    D_j = \partial_j + {i\over\hbar}e A_j=-{i\over\hbar}(i\hbar\partial_j-eA_j) ={i\over\hbar}(i\hbar\partial^j-eA^j) ={i\over\hbar}({\bf p}-e{\bf A})


.. index:: multipole expansion

Multipole expansion
-------------------

Assuming $r' \ll r$:


.. math::

    {1\over |{\bf r}-{\bf r'}|} ={1\over \sqrt{({\bf r}-{\bf r'})^2}} ={1\over \sqrt{r^2-2{\bf r}\cdot {\bf r'} + r'^2}} ={1\over r\sqrt{1-2\left(r'\over r\right){\bf\hat r}\cdot {\bf\hat r'} + \left(r'\over r\right)^2}} =

    ={1\over r}\sum_{l=0}^\infty\left(r'\over r\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =

    ={1\over r}\left( P_0({\bf\hat r}\cdot {\bf\hat r'}) + P_1({\bf\hat r}\cdot {\bf\hat r'}){r'\over r} + P_2({\bf\hat r}\cdot {\bf\hat r'})\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =

    ={1\over r}\left( 1 + {\bf\hat r}\cdot {\bf\hat r'} {r'\over r} + \half\left(3({\bf\hat r}\cdot {\bf\hat r'})^2-1\right)\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =

    ={1\over r} +{{\bf r}\cdot {\bf r'}\over r^3} +{3({\bf r}\cdot {\bf r'})^2-r^2r'^2\over 2r^5} + O\left(r'^3\over r^4\right)

We can also use the formula:

.. math::

    \sum_m \braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r}'}
        ={2l+1 \over 4\pi} \braket{{\bf\hat r}\cdot{\bf\hat r'}|P_l}

and rewrite the expansion using spherical harmonics:

.. math::

    {1\over |{\bf r}-{\bf r'}|} ={1\over r}\sum_{l=0}^\infty\left(r'\over r\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =

    ={1\over r}\sum_{l,m}\left(r'\over r\right)^l {4\pi\over 2l+1}\braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r}'}
    ={1\over r}\sum_{l,m}\left(r'\over r\right)^l {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')

Assuming $r' \gg r$ we get:

.. math::

    {1\over |{\bf r}-{\bf r'}|} ={1\over r'}\sum_{l=0}^\infty\left(r\over r'\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =

    = {1\over r'}\sum_{l,m}\left(r\over r'\right)^l
    {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')

We can combine the two formulas by introducing $r_{>} = \max(r, r')$ and
$r_{<} = \min(r, r')$ and then for any $r$ and $r'$ we get:

.. math::

    {1\over |{\bf r}-{\bf r'}|}
        ={1\over r_{>}}\sum_{l=0}^\infty\left(r_{<}\over r_{>}\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =

        = {1\over r_{>}}\sum_{l,m}\left(r_{<}\over r_{>}\right)^l
            {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')
