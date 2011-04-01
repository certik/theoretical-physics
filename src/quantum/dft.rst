Density Functional Theory (DFT)
===============================

Many Body Schrödinger Equation
------------------------------

We use the Born-Oppenheimer approximation, which says that the nuclei of the
treated atoms are seen as fixed. A stationary electronic state (for $N$
electrons) is then described by a wave function
$\Psi({\bf r_1},{\bf r_2},\cdots,{\bf r}_N)$
fulfilling the many-body Schrödinger equation

.. math::

  \hat H\ket\Psi=(\hat T+\hat U+\hat V)\ket\Psi=E\ket\Psi

where

.. math::

  \hat T = \sum_i^N -{1\over2}\nabla_i^2

is the kinetic term,

.. math::

  \hat U = \sum_{i<j}U({\bf r_i},{\bf r_j})= {1\over2}\sum_{i,j}U({\bf r_i},{\bf r_j})

  U({\bf r_i},{\bf r_j})=U({\bf r_j},{\bf r_i})={1\over|{\bf r_i}-{\bf r_j}|}

is the electron-electron interaction term and

.. math::

  \hat V = \sum_i^N v({\bf r_i})

  v({\bf r_i})=\sum_k -{Z_k\over|{\bf r_i}-{\bf R_k}|}

is the interaction term between electrons and nuclei, where $R_k$ are positions
of nuclei and $Z_k$ the number of nucleons in each nucleus (we are using atomic
units). So for one atomic calculation with the atom nucleus in the origin, we
have just $v({\bf r_i})=-{Z\over|{\bf r_i}|}$.

$|\Psi|^2=\Psi^*\Psi$ gives the probability density of measuring the first
electron at the position $\bf r_1$, the second at $\bf r_2$, \dots and the Nth
electron at the position ${\bf r}_N$. The normalization is such that
$\int|\Phi|^2\d^3 r_1\d^3 r_2\dots\d^3 r_N=1$. The $\Psi$ is antisymmetric,
i.e.  $\Psi({\bf r_1},{\bf r_2},\cdots,{\bf r}_N)= -\Psi({\bf r_2},{\bf
r_1},\cdots,{\bf r}_N)= -\Psi({\bf r_1},{\bf r}_N,\cdots,{\bf r_2})$ etc.

Integrating $|\Psi|^2$ over the first $N-1$ electrons is the probability
density that the $N$-th electron is at the position ${\bf r}_N$. Thus the
probability density $n({\bf r})$ that any of the N electrons (i.e the first, or
the second, or the third, \dots, or the $N$-th) is at the position $\bf r$ is
called the particle (or charge or electron) density and is therefore given by:

.. math::
  n({\bf r})= \int \Psi^*({\bf r},{\bf r}_2,\cdots,{\bf r}_N) \Psi ({\bf r},{\bf r}_2,\cdots,{\bf r}_N) \,\d^3 r_2\,\d^3 r_3\cdots\d^3 r_N+

  +\int \Psi^*({\bf r}_1,{\bf r},\cdots,{\bf r}_N) \Psi ({\bf r}_1,{\bf r},\cdots,{\bf r}_N) \,\d^3 r_1\,\d^3 r_3\cdots\d^3 r_N+\cdots

  +\int \Psi^*({\bf r}_1,{\bf r}_2,\cdots,{\bf r}) \Psi ({\bf r}_1,{\bf r}_2,\cdots,{\bf r}) \,\d^3 r_1\,\d^3 r_2\,\d^3 r_3\cdots\d^3 r_{N-1}=

  =\int(\delta({\bf r}-{\bf r}_1)+\delta({\bf r}-{\bf r}_2)+\cdots+\delta({\bf r}-{\bf r}_N))

  \Psi^*({\bf r}_1,{\bf r}_2,\cdots,{\bf r}_N) \Psi ({\bf r}_1,{\bf r}_2,\cdots,{\bf r}_N) \,\d^3 r_1\,\d^3 r_2\,\d^3 r_3\cdots\d^3 r_{N}=

  =\sum_{i=1}^N\int \braket{\Psi|{\bf r}_1,{\bf r}_2,\cdots,{\bf r}_N}\delta({\bf r}-{\bf r}_i) \braket{{\bf r}_1,{\bf r}_2,\cdots,{\bf r}_N|\Psi} \,\d^3 r_1\,\d^3 r_2\,\d^3 r_3\cdots\d^3 r_{N}=

  =N\int \braket{\Psi|{\bf r}_1,{\bf r}_2,\cdots,{\bf r}_N}\delta({\bf r}-{\bf r}_1) \braket{{\bf r}_1,{\bf r}_2,\cdots,{\bf r}_N|\Psi} \,\d^3 r_1\,\d^3 r_2\,\d^3 r_3\cdots\d^3 r_{N}=

.. math::
    :label: chargedensity

    =N\int \Psi^*({\bf r},{\bf r}_2,\cdots,{\bf r}_N) \Psi ({\bf r},{\bf r}_2,\cdots,{\bf r}_N) \,\d^3 r_2\,\d^3 r_3\cdots\d^3 r_N

Thus $\int_\Omega n({\bf r})\,\d^3r$ gives the number of particles (and also
the amount of charge) in the region of integration $\Omega$. Obviously $\int
n({\bf r})\,\d^3r=N$.

The energy of the system is given by

.. math::
    :label: Emanybody

    E=\braket{\Psi|\hat H|\Psi}= \braket{\Psi|\hat T|\Psi}+\braket{\Psi|\hat U|\Psi}+\braket{\Psi|\hat V|\Psi}= T+U+V

where

.. math::
  T=\braket{\Psi|\hat T|\Psi}=\sum_i^N\int \Psi^*({\bf r_1},{\bf r_2},\cdots,{\bf r_N})(-\half\nabla_i^2) \Psi({\bf r_1},{\bf r_2},\cdots,{\bf r_N})\,\d^3 r_1\,\d^3 r_2\cdots\d^3 r_N

  U=\braket{\Psi|\hat U|\Psi}

  V=\braket{\Psi|\hat V|\Psi}=\sum_i^N\int \Psi^*({\bf r_1},{\bf r_2},\cdots,{\bf r_N})v({\bf r_i}) \Psi({\bf r_1},{\bf r_2},\cdots,{\bf r_N})\,\d^3 r_1\,\d^3 r_2\cdots\d^3 r_N=

  =\sum_i^N\int \Psi^*({\bf r_1},{\bf r_2},\cdots,{\bf r_N})v({\bf r_1}) \Psi({\bf r_1},{\bf r_2},\cdots,{\bf r_N})\,\d^3 r_1\,\d^3 r_2\cdots\d^3 r_N=

  =N\int \Psi^*({\bf r_1},{\bf r_2},\cdots,{\bf r_N})v({\bf r_1}) \Psi({\bf r_1},{\bf r_2},\cdots,{\bf r_N})\,\d^3 r_1\,\d^3 r_2\cdots\d^3 r_N=

.. math::
    :label: V[n]

    =\int v({\bf r}) n({\bf r})\d^3 r=V[n]

It needs to be stressed, that $E$ generally is *not* a functional of $n$
alone, only the $V[n]$ is. In the next section we show however, that if the
$\ket{\Psi}$ is a ground state (of any system), then $E$ becomes a functional
of $n$.

The Hohenberg-Kohn Theorem
--------------------------

The Schrödinger equation gives the map

.. math::
  C: V \to \Psi

where $\Psi$ is the ground state. C is bijective (one-to-one correspondence),
because to every $V$ we can compute the corresponding $\Psi$ from Schrödinger
equation and two different $V$ and $V'$ (differing by more than a constant)
give two different $\Psi$, because if $V$ and $V'$ gave the same $\Psi$, then
by substracting

.. math::

  \hat H\ket{\Psi}=E_{gs}\ket{\Psi}

from

.. math::

  \hat H'\ket{\Psi}=(\hat H-\hat V+\hat V')\ket{\Psi}=E_{gs}'\ket{\Psi}

we would get $V-V'=E-E'$, which is a contradiction with the assumption that $V$ and $V'$ differ by more than a constant.

Similarly, from the ground state wavefunction $\Psi$ we can compute the charge
density $n$ giving rise to the map

.. math::
  D: \Psi \to n

which is also bijective, because to every $\Psi$ we can compute $n$ from
:eq:`chargedensity` and two different $\Psi$ and $\Psi'$ give two different
$n$ and $n'$, because different $\Psi$ and $\Psi'$ give

.. math::

  E_{gs}=\braket{\Psi|\hat H|\Psi}<\braket{\Psi'|\hat H|\Psi'}= \braket{\Psi'|\hat H'+\hat V-\hat V'|\Psi'}=E_{gs}'+\int n'({\bf r}) (v({\bf r})-v'({\bf r}))\,\d^3 r

  E_{gs}'=\braket{\Psi'|\hat H'|\Psi'}<\braket{\Psi|\hat H'|\Psi}= \braket{\Psi|\hat H+\hat V'-\hat V|\Psi}=E_{gs}+\int n({\bf r}) (v'({\bf r})-v({\bf r}))\,\d^3 r

adding these two inequalities together gives

.. math::

  0<\int n'({\bf r}) (v({\bf r})-v'({\bf r}))\,\d^3 r + \int n({\bf r}) (v'({\bf r})-v({\bf r}))\,\d^3 r= \int (n({\bf r})-n'({\bf r}))(v'({\bf r})-v({\bf r}))\,\d^3 r

which for $n=n'$ gives $0<0$, which is nonsense, so $n\neq n'$.

So we have proved that for a given ground state density $n_0({\bf r})$
(generated by a potential $\hat V_0$) it is possible to calculate the
corresponding ground state wavefunction $\Psi_0({\bf r_1},{\bf r_2},\cdots,{\bf
r_N})$, in other words, $\Psi_0$ is a unique functional of $n_0$:

.. math::
  \Psi_0=\Psi_0[n_0]

so the ground state energy $E_0$ is also a functional of $n_0$

.. math::
  E_0=\braket{\Psi_0[n_0]|\hat T+\hat U+\hat V_0|\Psi_0[n_0]}=E[n_0]

We define an energy functional

.. math::
    :label: Efunct

    E_{v_0}[n]=\braket{\Psi[n]|\hat T+\hat U+\hat V_0|\Psi[n]}= \braket{\Psi[n]|\hat T+\hat U|\Psi[n]}+\int v_0({\bf r})n({\bf r})\d^3r

where $\ket{\Psi[n]}$ is any ground state wavefunction (generated by an
arbitrary potential), that is, $n$ is a ground state density belonging to an
arbitrary system. $E_0$ which is generated by the potential $V_0$ can then be
expressed as

.. math::
    E_0=E_{v_0}[n_0]

and for $n\neq n_0$ we have (from the Ritz principle)

.. math::
  E_0<E_{v_0}[n]

and one has to minimize the functional $E_{v_0}[n]$:

.. math::
    :label: Emin

    E_0=\min_n E_{v_0}[n]

The term

.. math::

  \braket{\Psi[n]|\hat T+\hat U|\Psi[n]}\equiv F[n]

in :eq:`Efunct` is universal in the sense that it doesn't depend on $\hat
V_0$. It can be proven \cite{DFT}, that $F[n]$ is a functional of $n$ for
degenerated ground states too, so :eq:`Emin` stays true as well.

The ground state densities in :eq:`Efunct` and :eq:`Emin` are called
*pure-state v-representable* because they are the densities of (possible
degenerate) ground state of the Hamiltonian with some local potential $v({\bf
r})$. One may ask a question if all possible functions are v-representable
(this is called the v-representability problem). The question is relevant,
because we need to know which functions to take into account in the
minimization process :eq:`Emin`. Even though not every function is
v-representable \cite{DFT}, every density defined on a grid (finite of
infinite) which is strictly positive, normalized and consistent with the Pauli
principle is ensemble v-representable. Ensemble v-representation is just a
simple generalization of the above, for details see \cite{DFT}.

The functional $E_{v_0}[n]$ in :eq:`Emin` depends on the particle number $N$,
so in order to get $n$, we need to solve the variational formulation

.. math::

  {\delta\over\delta n}\left(E_v[n]-\mu(N)\int n(\bf r)\d^3r\right)=0

so

.. math::
    :label: euler

    {\delta E_v[n]\over\delta n}=\mu(N)

Let the $n_N(\bf r)$ be the solution of :eq:`euler` with a particle number
$N$ and the energy $E_N$:

.. math::

  E_N=E_v[n_N]

The Lagrangian multiplier $\mu$ is the exact chemical potential of the system

.. math::

  \mu(N)={\partial E_N\over\partial N}

becuase

.. math::

  E_{N+\epsilon}-E_N=E_v[n_{N+\epsilon}]-E_v[n_N] =\int {\delta E_v\over\delta n} (n_{N+\epsilon}-n_N)\d^3r=

  =\int \mu(N) (n_{N+\epsilon}-n_N)\d^3r =\mu(N)(N+\epsilon-N)=\mu(N)\epsilon

so

.. math::

  \mu(N)={E_{N+\epsilon}-E_N\over\epsilon} \ \longrightarrow \ {\partial E_N\over\partial N}

The Kohn-Sham Equations
-----------------------

Consider an auxiliary system of $N$ noninteracting electrons (noninteracting
gas):

.. math::

  \hat H_s=\hat T+\hat V_s

Then the many-body ground state wavefunction can be decomposed into single
particle orbitals

.. math::

  \ket{\Psi ({\bf r_1},{\bf r_2},\cdots,{\bf r_N})}= \ket{\psi_1({\bf r})}\ket{\psi_2({\bf r})}\cdots\ket{\psi_N({\bf r})}

and

.. math::

  E_s[n]=T_s[\{\psi_i[n]\}]+V_s[n]

where

.. math::

  T_s[n]=\braket{\Psi[n]|\hat T|\Psi[n]}= \sum_i\braket{\psi_i|-\half\nabla^2|\psi_i}

  V_s[n]=\braket{\Psi[n]|\hat V|\Psi[n]}=\int v_s({\bf r})n({\bf r})\d^3r

From :eq:`euler` we get

.. math::
    :label: noninteract

    \mu={\delta E_s[n]\over\delta n({\bf r})}= {\delta T_s[n]\over\delta n({\bf r})}+{\delta V_s[n]\over\delta n({\bf r})}= {\delta T_s[n]\over\delta n({\bf r})}+v_s({\bf r})

Solution to this equation gives the density $n_s$.

Now we want to express the energy in :eq:`Emanybody` using $T_s$ and $E_H$
for convenience, where $E_H$ is the classical electrostatic interaction energy
of the charge distribution $n({\bf r})$:

.. math::

  \nabla^2 V_H=n({\bf r})

or equivalently

.. math::

  E_H[n]=\half\int\int {n({\bf r})n({\bf r'})\over|{\bf r}-{\bf r'}|} \d^3r\d^3r'

.. math::
    :label: V_H

  V_H({\bf r})={\delta E_H\over\delta n({\bf r})}=\half\int {n({\bf r'})\over|{\bf r}-{\bf r'}|} \d^3r'

So from :eq:`Efunct` we get

.. math::
    :label: Efunctxc

    E[n]=(T+U)[n]+V[n]=T_s[n]+E_H[n]+(T-T_s+U-E_H)[n]+V[n]=

    =T_s[n]+E_H[n]+E_{xc}[n]+V[n]

The rest of the energy is denoted by $E_{xc}=U-E_H+T-T_s$ and it is called is
the exchange and correlation energy functional. From :eq:`euler`

.. math::

  \mu={\delta E[n]\over\delta n({\bf r})}= {\delta T_s[n]\over\delta n({\bf r})}+ {\delta E_H[n]\over\delta n({\bf r})}+ {\delta E_{xc}[n]\over\delta n({\bf r})}+ {\delta V[n]\over\delta n({\bf r})}

From :eq:`V_H` we have

.. math::

  {\delta E_H\over\delta n({\bf r})}=V_H({\bf r})

from :eq:`V[n]` we get

.. math::

  {\delta V[n]\over\delta n({\bf r})}=v({\bf r})

we define

.. math::
    :label: Vxcpot

    {\delta E_{xc}[n]\over\delta n({\bf r})}=V_{xc}({\bf r})

so we arrive at

.. math::
    :label: interact

    \mu={\delta E[n]\over\delta n({\bf r})}= {\delta T_s[n]\over\delta n({\bf r})}+V_H({\bf r})+V_{xc}({\bf r})+v({\bf r})

Solution to this equation gives the density $n$. Comparing :eq:`interact` to
:eq`noninteract` we see that if we choose

.. math::

  v_s\equiv V_H+V_{xc}+v

then $n_s({\bf r})\equiv n({\bf r})$. So we solve the Kohn-Sham equations of
this auxiliary non-interacting system

.. math::

    (-\half\nabla^2+v_s({\bf r}))\psi_i({\bf r}) \equiv(-\half\nabla^2+V_H({\bf r})+V_{xc}({\bf r})+v({\bf r}))\psi_i({\bf r}) =\epsilon_i\psi({\bf r})  \label{KSeq}

which yield the orbitals $\psi_i$ that reproduce the density $n({\bf r})$ of the original interacting system

.. math::

  n({\bf r})\equiv n_s({\bf r})=\sum_i^N|\psi_i({\bf r})|^2  \label{KSdensity}

The sum is taken over the lowest $N$ energies. Some of the $\psi_i$ can be
degenerated, but it doesn't matter - the index $i$ counts every eigenfunction
including all the degenerated. In plain words, the trick is in realizing, that
the ground state energy can be found by minimizing the energy functional
:eq:`Efunct` and in rewriting this functional into the form :eq:`Efunctxc`,
which shows that the interacting system can be treated as a noninteracting one
with a special potential.

The XC Term
-----------

The exchange and correlation functional

.. math::

  E_{xc}[n]=(T+U)[n]-E_H[n]-T_S[n]

can always be written in the form

.. math::

  E_{xc}[n]=\int n({\bf r}')\epsilon_{xc}({\bf r}';n)\d^3r'

where the $\epsilon_{xc}({\bf r}';n)$ is called the xc energy density.

Unfortunately, no one knows $\epsilon_{xc}({\bf r}';n)$ exactly (yet). The most
simple approximation is the *local density approximation* (LDA), for which the
xc energy density $\epsilon_{xc}$ at $\bf r$ is taken as that of a homogeneous
electron gas (the nuclei are replaced by a uniform positively charged
background, density $n=\rm const$) with the same local density:

.. math::
  \epsilon_{xc}({\bf r};n)\approx\epsilon_{xc}^{LD}(n({\bf r}))

The xc potential $V_{xc}$ defined by :eq:`Vxcpot` is then

.. math::
  V_{xc}({\bf r};n)={\delta E_{xc}[n]\over\delta n({\bf r})}= \epsilon_{xc}({\bf r}';n)+ \int n({\bf r}'){\delta \epsilon_{xc}({\bf r}';n)\over\delta n({\bf r})}\d^3r'

which in the LDA becomes

.. math::
    :label: Vxcld

    V_{xc}({\bf r};n) =\epsilon_{xc}^{LD}(n)+n{\d \epsilon_{xc}^{LD}(n)\over \d n}= {\d \over \d n}\left(n\epsilon_{xc}^{LD}(n)\right)= V_{xc}^{LD}(n)

The xc energy density $\epsilon_{xc}^{LD}$ of the homogeneous gas can be
computed exactly:

.. math::
  \epsilon_{xc}^{LD}(n)=\epsilon_x^{LD}(n)+\epsilon_c^{LD}(n)

where the $\epsilon_x^{LD}$ is the electron gas exchange term given
by

.. math::
  \epsilon_x^{LD}(n)=-{3\over4\pi}(3\pi^2 n)^{1\over3}

the rest of $\epsilon_{xc}^{LD}$ is hidden in $\epsilon_c^{LD}(n)$ for which
there doesn't exist an analytic formula, but the correlation energies are known
exactly from quantum Monte Carlo (QMC) calculations by Ceperley and
Alder\cite{pickett}. The energies were fitted by Vosko, Wilkes and Nussair
(VWN) with $\epsilon_c^{LD}(n)$ and they got accurate results with errors less
than $0.05\rm\,mRy$ in $\epsilon_c^{LD}$, which means that $\epsilon_c^{LD}(n)$
is virtually known exactly. VWN result:

.. math::
  \epsilon_c^{LD}(n)\approx {A\over2}\left\{ \ln\left(y^2\over Y(y)\right)+{2b\over Q}\arctan\left(Q\over 2y+b\right)+ \right.

  \left. -{by_0\over Y(y_0)}\left[\ln\left((y-y_0)^2\over Y(y)\right) +{2(b+2y_0)\over Q}\arctan\left(Q\over 2y+b\right) \right] \right\}

where $y=\sqrt{r_s}$, $Y(y)=y^2+by+c$, $Q=\sqrt{4c-b^2}$, $y_0=-0.10498$,
$b=3.72744$, $c=12.93532$, $A=0.0621814$ and $r_s$ is the electron gas
parameter, which gives the mean distance between electrons (in atomic units):

.. math::
  r_s=\left(3\over4\pi n\right)^{1\over3}

The xc potential is then computed from :eq:`Vxcld`:

.. math::

  V_{xc}^{LD}=V_x^{LD}+V_c^{LD}

  V_x^{LD}=-{1\over\pi}(3\pi^2 n)^{1\over3}

  V_c^{LD}={A\over2}\left\{ \ln\left(y^2\over Y(y)\right)+{2b\over Q}\arctan\left(Q\over 2y+b\right)+ \right.

  \left. -{by_0\over Y(y_0)}\left[\ln\left((y-y_0)^2\over Y(y)\right) +{2(b+2y_0)\over Q}\arctan\left(Q\over 2y+b\right) \right] \right\}+

  -{A\over6}{c(y-y_0)-by_0y\over (y-y_0)Y(y)}

Some people also use Perdew and Zunger formulas, but they give essentially the
same results. The LDA, although very simple, is surprisingly successful. More
sophisticated approximations exist, for example the generalized gradient
approximation (GGA), which sometimes gives better results than the LDA, but is
not perfect either. Other options include orbital-dependent (implicit) density
functionals or a linear response type functionals, but this topic is still
evolving. The conclusion is, that the LDA is a good approximation to start
with, and only when we are not satisfied, we will have to try some more
accurate and modern approximation.

RLDA: Relativistic corrections to the energy-density functional were proposed
by MacDonald and Vosko and basically are just a change in
$\epsilon_x^{LD}(n)\rightarrow\epsilon_x^{LD}(n)R$:

.. math::

  R = \left[1-{3\over2}\left(\beta\mu-\ln(\beta+\mu)\over\beta^2\right)^2\right]

where

.. math::

  \mu=\sqrt{1+\beta^2}

and

.. math::

  \beta={(3\pi^2n)^{1\over3}\over c}

We also need to calculate these derivatives:

.. math::

  {\d R\over\d \beta}= -6{\beta\mu-\ln(\beta+\mu)\over\beta^2}\left({1\over\mu}- {\beta\mu-\ln(\beta+\mu)\over\beta^3}\right)

  {\d \beta\over\d n}={\beta\over 3n}

  {\d \epsilon_x^{LD}\over\d n}={\epsilon_x^{LD}\over 3n}

So

.. math::
    :label: RLDA

    V_x^{RLD}=\epsilon_x^{LD}R+n{\d \epsilon_x^{LD}R\over\d n}=
    {4\over3}\epsilon_x^{LD}R+{1\over3}\epsilon_x^{LD}{\d R\over\d\beta}\beta
    \label{RLDA}

For $c\to\infty$ we get $\beta\to0$, $R\to1$ and $V_x^{RLD}\to
{4\over3}\epsilon_x^{LD}=V_x^{LD}$ as expected, because

.. math::

  \lim_{\beta\to0}{\beta\sqrt{1+\beta^2}-\ln(\beta+\sqrt{1+\beta^2})\over \beta^2} = 0

Code::

    >>> from sympy import limit, var, sqrt, log
    >>> var("beta")
    beta
    >>> limit((beta*sqrt(1+beta**2) - log(beta+sqrt(1+beta**2)))/beta**2, beta, 0)
    0