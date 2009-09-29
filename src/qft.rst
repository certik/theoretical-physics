.. index:: QFT, quantum field theory, QM, quantum mechanics

==========================================
Quantum Field Theory and Quantum Mechanics
==========================================


Introduction
============

The aim of these (work in progress) notes is to use the Standard Model of particle physics to derive all equations in quantum mechanics (and quantum field theory) that we need for our research.

We start by deriving the electroweak Standard Model from the $SU(2)\times U(1)$ symmetry and couple other (standard) assumptions in the quantum field theory. After that, we only want to derive things and make nonrelativistic limits or other approximations in order to derive everything else in quantum mechanics. In particular we show how to derive the Dirac and Schrödinger equations (as a low energy limit). We then show some particular ways to solve those equations, like perturbation theory, scattering theory, ...

The goal is to have a complete theory on about 30 or 40 pages and then lots of examples (arbitrarily long), that use the theory (but do not develop new ideas), so that one can learn how the theory works from the examples. For instance, one can ask "why is there the term $({\bf p}-e{\bf A})^2$ in the Schrödinger equation for electromagnetic field, why this and not something else?" or "why is there the $\boldsymbol\sigma\cdot{\bf B}$ term in the Pauli equation?", to find the answer, one just finds the Pauli equation in the theory and then looks at the derivation, so in this case one quickly finds that it follows from the minimal coupling in QED, e.g. it's the easiest way how electron-foton interaction can be coupled, e.g. the $U(1)$ symmetry. Nice thing about QFT is that one can find really nice geometrical reasons why things are that way and not some other way (just open any advance book on QFT), but the problem is that basically nowhere is some easy (but correct) translation of those results to regular QM, so that everything fits into just couple dozens pages, so that it can serve as a reference.

The advantage of this top-down approach is that it is easy to see where things come from and also to understand exactly what approximations one is using when dealing with any equation in QM. However, as is well-known in physics, to be a good physicist one has to understand all the approaches, e.g. both top-down and bottom-up and all other approaches to QM and QFT, because there are no two approaches that would be 100% equivalent, so one has to use the right approach for the particular problem. So these notes do not aspire to be the right way to teach QM, but rather to serve as a reference to get quickly oriented and to find the equations to start from.

.. index:: Standard Model

Standard Model
==============

.. index:: Electroweak Standard Model

Electroweak Standard Model
--------------------------

Lagrangian with a global $SU(2)\times U(1)$ symmetry:

.. math::

    \L=i\bar L^{(l)}\gamma_\mu\partial^\mu L^{(l)}+i\bar l_R \gamma_\mu\partial^\mu l_R +\half \partial_\mu\Phi^*\partial^\mu\Phi-m^2\Phi^*\Phi-{1\over4} \lambda(\Phi^*\Phi)^2 -h_e\bar L^{(l)} \Phi e_R - \hbox{h.c.}


where $l=e,\mu,\tau$ and $a=1,2$, $l_{L,R} = \half (1\mp\gamma_5)l$ and 

.. math::

    L^{(l)} = \left( \begin{array}{c} \nu_{(l)L} \\ l_L \end{array} \right)



Local $SU(2)\times U(1)$ symmetry:

This consists of two things. First changing the partial derivatives to covariant ones: 

.. math::

    \partial^\mu \to D^\mu =\partial^\mu-{i\over2}g\tau_k A_k^\mu - {i\over2}g'YB^\mu


and second adding the kinetic terms 

.. math::

    -{1\over4}F^a_{\mu\nu}F^{a\mu\nu}-{1\over4}B_{\mu\nu}B^{\mu\nu}


of the vector gauge particles to the lagrangian. 

.. math::

    F^a_{\mu\nu} = \partial_\mu A^a_\nu-\partial_\nu A^a_\mu+ g\epsilon^{abc}A^b_\mu A^c_\nu



.. math::

    B_{\mu\nu} = \partial_\mu B_\nu-\partial_\nu B_\mu




.. math::

    \Phi = e^{{i\over v}\pi^a(x)\tau^a} \left( \begin{array}{c} 0 \\ {1\over\sqrt{2}}(v+H(x)) \end{array} \right)


This breaks the gauge invariance. The $\partial^\mu\pi^a$ are going to be added to $A^a_\mu$ so we can set $\pi_a = 0$ now. 

.. index:: Higgs boson

Higgs Terms
~~~~~~~~~~~


.. math::

    \L_{Higgs}= \half \partial_\mu\Phi^*\partial^\mu\Phi-m^2\Phi^*\Phi-{1\over4} \lambda(\Phi^*\Phi)^2


Plugging in the covariant derivatives and $\Phi$ in U-gauge (symmetry breaking): 

.. math::

    \L_{Higgs} = {1\over2}\Phi^+(\overleftarrow\partial_\mu+igA^a_\mu {\tau^a\over 2} + ig'YB_\mu) (\overrightarrow\partial^\mu+igA^{a\mu} {\tau^a\over 2} + ig'YB^\mu)\Phi -\lambda(\Phi^+\Phi-{v^2\over2})^2=



.. math::

    = \Phi^+_U(\overleftarrow\partial_\mu+igA^a_\mu {\tau^a\over 2} + ig'YB_\mu) (\overrightarrow\partial^\mu+igA^{a\mu} {\tau^a\over 2} + ig'YB\mu)\Phi_U -\lambda(\Phi^+_U\Phi_U-{v^2\over2})^2 =



.. math::

    = {1\over2}\partial_\mu H\partial^\mu H - \lambda v^2 H^2 - \lambda v H^3 - {1\over 4}\lambda H^4 +



.. math::

    +{1\over 8}(v+H)^2 \left(2g^2{A^1_\mu+iA^2_\mu\over\sqrt2}{A^{1\mu}-iA^{2\mu}\over\sqrt2} + (g^2+4Y^2g'^2){gA^3_\mu-2Yg'B_\mu\over\sqrt{g^2+4Y^2g'^2}} {gA^{3\mu}-2Yg'B^\mu\over\sqrt{g^2+4Y^2g'^2}}\right) =



.. math::

    = {1\over2}\partial_\mu H\partial^\mu H - \lambda v^2 H^2 - \lambda v H^3 - {1\over 4}\lambda H^4 + {1\over 8}(v+H)^2 \left(2g^2W^-_\mu W^{+\mu} + {g^2\over\cos^2\theta_W}Z_\mu Z^\mu\right) =



.. math::

    = {1\over2}\partial_\mu H\partial^\mu H - \lambda v^2 H^2 +{1\over4}g^2v^2W^-_\mu W^{+\mu}+{g^2v^2\over8\cos^2\theta_W}Z_\mu Z^\mu - \lambda v H^3 - {1\over 4}\lambda H^4 +



.. math::

    +{1\over2}vg^2W_\mu^-W^{+\mu}H +{g^2\over4\cos\theta_W}vZ_\mu Z^\mu H +{1\over4}g^2W_\mu^-W^{+\mu}H^2 +{g^2\over8\cos\theta_W}Z_\mu Z^\mu H^2


Where we put 

.. math::

    W^{\pm}_\mu = {1\over\sqrt2}(A^1_\mu \mp iA^2_\mu)



.. math::

    Z_\mu = {g\over\sqrt{g^2+4Y^2g'^2}}A^3_\mu- {2Yg'\over\sqrt{g^2+4Y^2g'^2}}B_\mu


we defined $\theta_W$ by the relation 

.. math::

    \cos\theta_W = {g\over\sqrt{g^2+4Y^2g'^2}}


so that the expressions simplify a bit, e.g. we now get: 

.. math::

    \sin\theta_W = {2Yg'\over\sqrt{g^2+4Y^2g'^2}}



.. math::

    Z_\mu= \cos\theta_W A^3_\mu - \sin\theta_W B_\mu



.. math::

    g^2+4Y^2g'^2 = {g^2\over\cos^2\theta_W}


.. index:: Yukawa terms

Yukawa terms
~~~~~~~~~~~~


.. math::

    \L_{Yukawa} = -h_e \bar L \Phi e_R - \hbox{h.c.}= -h_e \bar L \Phi_U e_R - \hbox{h.c.}=



.. math::

    =-{1\over\sqrt2}h_e(v+H)(\bar e_L e_R + \bar e_R e_L)= -{1\over\sqrt2}h_e(v+H)\bar ee=



.. math::

    =-{1\over\sqrt2}h_ev\bar ee-{1\over\sqrt2}h_e\bar eeH


The term $\bar L \Phi e_R$ is $U(1)$ (hypercharge) invariant, so 

.. math::

    -Y_L+Y+Y_R=0


.. index:: leptons

Leptonic Terms
~~~~~~~~~~~~~~


.. math::

    \L=i\bar L\gamma^\mu\partial_\mu L+i\bar e_R \gamma^\mu\partial_\mu e_R \to



.. math::

    \to i\bar L\gamma^\mu(\partial_\mu-igA^a_\mu{\tau^a\over2}-ig'Y_LB_\mu) L +i\bar e_R \gamma^\mu(\partial_\mu-ig'Y_RB_\mu) e_R =



.. math::

    = i\bar L\gamma^\mu\partial_\mu L+i\bar e_R \gamma^\mu\partial_\mu e_R +g\bar L\gamma^\mu{\tau^a\over2}LA^a_\mu +g'Y_L\bar L\gamma^\mu LB_\mu +g'Y_R\bar e_R \gamma^\mu e_R B_\mu =



.. math::

    = i\bar L\gamma^\mu\partial_\mu L+i\bar e_R \gamma^\mu\partial_\mu e_R +{g\over\sqrt2}(\bar \nu_L\gamma^\mu e_L W^+_\mu + \hbox{h.c.}) +{1\over2}g\bar L\gamma^\mu\tau^3L A^3_\mu +g'Y_L\bar L\gamma^\mu LB_\mu +g'Y_R\bar e_R \gamma^\mu e_R B_\mu =



.. math::

    = i\bar \nu_L\gamma^\mu\partial_\mu \nu_L+i\bar e \gamma^\mu\partial_\mu e +{g\over\sqrt2}(\bar \nu_L\gamma^\mu e_L W^+_\mu + \hbox{h.c.}) +{1\over2}g\bar\nu_L\gamma^\mu\nu_LA^3_\mu -{1\over2}g\bar e_L\gamma^\mu e_LA^3_\mu



.. math::

    +g'Y_L\bar\nu_L\gamma^\mu\nu_LB_\mu +g'Y_L\bar e_L\gamma^\mu e_LB_\mu +g'Y_R\bar e_R \gamma^\mu e_R B_\mu =



.. math::

    = i\bar \nu_L\gamma^\mu\partial_\mu \nu_L+i\bar e \gamma^\mu\partial_\mu e +{g\over\sqrt2}(\bar \nu_L\gamma^\mu e_L W^+_\mu + \hbox{h.c.})



.. math::

    +\left[ (\half g\sin\theta_W+Y_Lg'\cos\theta_W)\bar\nu_L\gamma^\mu\nu_L +(-\half g\sin\theta_W +Y_Lg'\cos\theta_W)\bar e_L\gamma^\mu e_L +Y_Rg'\cos\theta_W\bar e_R\gamma^\mu e_R \right]A_\mu



.. math::

    +\left[ (\half g\cos\theta_W-Y_Lg'\sin\theta_W)\bar\nu_L\gamma^\mu\nu_L +(-\half g\cos\theta_W -Y_Lg'\sin\theta_W)\bar e_L\gamma^\mu e_L -2Y_Lg'\sin\theta_W\bar e_R\gamma^\mu e_R \right]Z_\mu


Where we substituted new fields $Z_\mu$ and $A_\mu$ for the old ones $A^3_\mu$ and $B_\mu$ using the relation: 

.. math::

    Z_\mu= \cos\theta_W A^3_\mu - \sin\theta_W B_\mu



.. math::

    A_\mu= \sin\theta_W A^3_\mu + \cos\theta_W B_\mu


The angle $\theta_W$ must be the same as in the Higgs sector, so that the field $Z_\mu$ is the same. We now need to make the following requirement in order to proceed further: 

.. math::

    Y = -Y_L


This follows for example by requiring that neutrinos have zero charge, i.e. setting $\half g\sin\theta_W+Y_Lg'\cos\theta_W = 0$ and substituting for $\theta_W$ from the definition (see the Higgs terms), from which one gets $Y=-Y_L$. From $-Y_L+Y+Y_R=0$ we now get 

.. math::

    Y_R = 2Y_L


it now follows: 

.. math::

    \half g\sin\theta_W+Y_Lg'\cos\theta_W = 0



.. math::

    -\half g\sin\theta_W +Y_Lg'\cos\theta_W = -g\sin\theta_W



.. math::

    Y_Rg'\cos\theta_W = -g\sin\theta_W



.. math::

    \tan\theta_W = -2Y_L {g'\over g}


and the Lagrangian can be further simplified: 

.. math::

    \L= i\bar\nu_L\gamma^\mu\partial_\mu\nu_L+i\bar e\gamma^\mu\partial_\mu e +{g\over\sqrt2}(\bar \nu_L\gamma^\mu e_L W^+_\mu + \hbox{h.c.})



.. math::

    -g\sin\theta_W(\bar e_L\gamma^\mu e_L+\bar e_R\gamma^\mu e_R) A_\mu



.. math::

    +{g\over\cos\theta_W}\left[ \half \bar\nu_L\gamma^\mu\nu_L +(-\half + \sin^2\theta_W)\bar e_L\gamma^\mu e_L +\sin^2\theta_W\bar e_R\gamma^\mu e_R \right]Z_\mu=



.. math::

    = i\bar\nu_L\gamma^\mu\partial_\mu\nu_L+i\bar e \gamma^\mu\partial_\mu e +{g\over2\sqrt2}(\bar \nu\gamma^\mu (1-\gamma_5) e W^+_\mu + \hbox{h.c.}) -g\sin\theta_W\bar e\gamma^\mu e A_\mu



.. math::

    +{g\over2\cos\theta_W}\left[ \bar\nu\gamma^\mu(1-\gamma_5)\nu +\bar e\gamma^\mu (-\half+2\sin^2\theta_W+\half\gamma_5) e \right]Z_\mu


Where we used the relations $\bar\nu_L\gamma^\mu e_L=\half\bar\nu\gamma^\mu (1-\gamma_5)e$ and $\bar\nu_R\gamma^\mu e_R=\half\bar\nu\gamma^\mu (1+\gamma_5)e$ .

.. index:: gauge

Gauge terms
~~~~~~~~~~~


.. math::

    \L_{Gauge} = -{1\over4}F^a_{\mu\nu}F^{a\mu\nu} -{1\over4}B_{\mu\nu}B^{\mu\nu}=



.. math::

    = -{1\over4}(\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+g\epsilon^{abc} A^b_\mu A^c_\nu)(\partial^\mu A^{a\nu}-\partial^\nu A^{a\mu}+g\epsilon^{ajk} A^{j\mu} A^{k\nu}) -{1\over4}B_{\mu\nu}B^{\mu\nu}=



.. math::

    = -{1\over4}\partial_\mu A^a_\nu\partial^\mu A^{a\nu} -{1\over4}B_{\mu\nu}B^{\mu\nu} -{1\over2}(\partial_\mu A^a_\nu-\partial_\nu A^a_\mu)g\epsilon^{abc} A^{b\mu} A^{c\nu} -{1\over4}g^2\epsilon^{abc}\epsilon^{ajk}A^b_\mu A^c_\nu A^{k\mu} A^{l\nu} =



.. math::

    = -{1\over2}W^-_{\mu\nu}W^{+\mu\nu} -{1\over4}A_{\mu\nu}A^{\mu\nu} -{1\over4}Z_{\mu\nu}Z^{\mu\nu} -g[(\partial_\mu A^1_\nu-\partial_\nu A^1_\mu)A^{2\mu}A^{3\nu}+ \hbox{cycl. perm. (123)}]



.. math::

    -{1\over4}g^2[(A^a_\mu A^{a\mu})(A^b_\nu A^{b\nu})- (A^a_\mu A^a_\nu)(A^{b\mu} A^{b\nu})]=



.. math::

    = -{1\over2}W^-_{\mu\nu}W^{+\mu\nu} -{1\over4}A_{\mu\nu}A^{\mu\nu} -{1\over4}Z_{\mu\nu}Z^{\mu\nu} -g[A^1_\mu A^2_\nu \overleftrightarrow\partial^\mu A^{3\nu}+ \hbox{cycl. perm. (123)}]



.. math::

    -{1\over4}g^2[(A^a_\mu A^{a\mu})(A^b_\nu A^{b\nu})- (A^a_\mu A^a_\nu)(A^{b\mu} A^{b\nu})] =



.. math::

    = -{1\over2}W^-_{\mu\nu}W^{+\mu\nu} -{1\over4}A_{\mu\nu}A^{\mu\nu} -{1\over4}Z_{\mu\nu}Z^{\mu\nu} -ig(W^0_\mu W^-_\nu\overleftrightarrow\partial^\mu W^{+\nu}+ \hbox{cycl. perm. (0-+)})



.. math::

    -g^2[ \half(W^+_\mu W^{-\mu})^2 -\half(W^+_\mu W^{+\mu})(W^-_\nu W^{-\nu}) +(W^0_\mu W^{0\mu})(W^+_\nu W^{-\nu}) -(W^-_\mu W^+_\nu)(W^{0\mu} W^{0\nu})=



.. math::

    = -{1\over2}W^-_{\mu\nu}W^{+\mu\nu} -{1\over4}A_{\mu\nu}A^{\mu\nu} -{1\over4}Z_{\mu\nu}Z^{\mu\nu} +\L_{WW\gamma}+L_{WWZ}+L_{WW\gamma\gamma}+L_{WWWW}+L_{WWZZ}+L_{WWZ\gamma}


Where $W^0_\mu = A^3_\mu=\cos\theta_W Z_\mu + \sin\theta_W A_\mu$ and: 

.. math::

    \L_{WW\gamma}=-ig\sin\theta_W(A_\mu W^-_\nu\overleftrightarrow\partial^\mu W^{+\nu} + \hbox{cycl. perm. ($A$ $W^-$ $W^+$)})



.. math::

    \L_{WWZ}=-ig\cos\theta_W(Z_\mu W^-_\nu\overleftrightarrow\partial^\mu W^{+\nu}+\hbox{cycl. perm. ($Z$ $W^-$ $W^+$)})



.. math::

    \L_{WW\gamma\gamma}=-g^2\sin^2\theta_W(W^-_\mu W^{+\mu}A_\nu A^\nu- W^-_\mu A^\mu W^+_\nu A^\nu)



.. math::

    \L_{WWWW}=\half g^2(W^-_\mu W^{-\mu}W^+_\nu W^{+\nu} -W^-_\mu W^{+\mu}W^-_\nu W^{+\nu} )



.. math::

    \L_{WWZZ}=-g^2\cos^2\theta_W(W^-_\mu W^{+\mu}Z_\nu Z^\nu -W^-_\mu Z^\mu W^+_\nu Z^\nu )



.. math::

    \L_{WWZ\gamma}=g^2\sin\theta_W\cos\theta_W(-2W^-_\mu W^{+\mu}A_\nu Z^\nu+W^-_\mu Z^\mu W^+_\nu A^\nu+W^-_\mu A^\mu W^+_\nu Z^\nu)


.. index::
    pair: GWS; Lagrangian

GWS Lagrangian
~~~~~~~~~~~~~~

Plugging everything together we get the GWS Lagrangian: 

.. math::

    \L = {1\over2}\partial_\mu H\partial^\mu H - \lambda v^2 H^2 +{1\over4}g^2v^2W^-_\mu W^{+\mu}+{g^2v^2\over8\cos^2\theta_W}Z_\mu Z^\mu - \lambda v H^3 - {1\over 4}\lambda H^4 +



.. math::

    +{1\over2}vg^2W_\mu^-W^{+\mu}H +{g^2\over4\cos\theta_W}vZ_\mu Z^\mu H +{1\over4}g^2W_\mu^-W^{+\mu}H^2 +{g^2\over8\cos\theta_W}Z_\mu Z^\mu H^2



.. math::

    -{1\over\sqrt2}h_ev\bar ee-{1\over\sqrt2}h_e\bar eeH



.. math::

    -{1\over2}W^-_{\mu\nu}W^{+\mu\nu} -{1\over4}A_{\mu\nu}A^{\mu\nu} -{1\over4}Z_{\mu\nu}Z^{\mu\nu} +\L_{WW\gamma}+L_{WWZ}+L_{WW\gamma\gamma}+L_{WWWW}+L_{WWZZ}+L_{WWZ\gamma}



.. math::

    +i\bar\nu_L\gamma^\mu\partial_\mu\nu_L+i\bar e \gamma^\mu\partial_\mu e +{g\over2\sqrt2}(\bar \nu\gamma^\mu (1-\gamma_5) e W^+_\mu + \hbox{h.c.}) -g\sin\theta_W\bar e\gamma^\mu e A_\mu



.. math::

    +{g\over2\cos\theta_W}\left[ \bar\nu\gamma^\mu(1-\gamma_5)\nu +\bar e\gamma^\mu (-\half+2\sin^2\theta_W+\half\gamma_5) e \right]Z_\mu



.. math::

    + (e, \nu_e, h_e \leftrightarrow \mu, \nu_\mu, h_\mu) + (e, \nu_e, h_e \leftrightarrow \tau, \nu_\tau, h_\tau)



The free parameters are $g$, $\theta_W$, $v$, $\lambda$, $h_e$, $h_\mu$, $h_\tau$.

.. index:: particle mass

Particle Masses
~~~~~~~~~~~~~~~

The particle masses are deduced from the terms 

.. math::

    \L = -{1\over2}m_H^2 H^2 +m_W^2 W^-_\mu W^{+\mu} +{1\over2}m_Z^2 Z_\mu Z^\mu -m_e\bar ee +\cdots


comparing to the above: 

.. math::

    \L = -\lambda v^2 H^2 +{1\over4}g^2v^2W^-_\mu W^{+\mu} +{g^2v^2\over8\cos^2\theta_W}Z_\mu Z^\mu -{1\over\sqrt2}h_ev\bar ee +\cdots


we get 

.. math::

    m_W = \half g v



.. math::

    m_Z = {gv\over2\cos\theta_W}={m_W\over\cos\theta_W}



.. math::

    m_H = v\sqrt{2\lambda}



.. math::

    m_e = {1\over\sqrt2}h_ev


.. index:: quarks

Quarks
~~~~~~



.. math::

    \L_{fermion}+\!\!= \sum_{q=d,s,b}i\bar L_0^{(q)}\gamma^\mu\partial_\mu L_0^{(q)} +\sum_{q=d,u,s,c,b,t}i\bar q_{0R}\gamma^\mu\partial_\mu q_{0R}



.. math::

    \L_{Yukawa}+\!\!= -\sum_{q=d,s,b\atop q'=d,s,b}h_{qq'}i\bar L_0^{(q)}\Phi q_{0R}'+\hbox{h.c.} -\sum_{q=d,s,b\atop q'=u,c,t}\tilde h_{qq'}i\bar L_0^{(q)}\tilde\Phi q_{0R}'+\hbox{h.c.}




QFT
---



Field Operators
~~~~~~~~~~~~~~~

The free (non-interacting) fields in the interaction picture are expressed
using the creation and anihilation operators below, also the corresponding
non-interacting Hamiltonian is shown.

The general idea behind the machinery is that the field operator
$\hat\psi({\bf x}) = \sum_k \psi_k({\bf x}) c_k$ is constructed as a sum (or
an integral, depending on if the index $k$ is discrete or continuous) of
single-particle wave functions (i.e. solutions of the noninteracting equation
of motion) multiplied by the creation/anihilation operators ($c_k$ or
$c_k^\dag$) that create/destroy
the particle in the given single-particle state. Note that the noninteracting
equation of motion usually means that we set all potentials (interactions) as
zero, but in principle it can be any equation that we can solve exactly.

The coefficients $\psi_k({\bf x})$ don't depend on time (so neither the field
operators in the Schrödinger picture), but we work in the interaction picture,
where the creation/anihilation operators depend on time, and the time
dependence is put into the exponentials below (but the integration is still
done over the spatial components of $p$ only).

Scalar bosons:

.. math::

    \phi_I(x) = \int {\d^3 p\over (2\pi)^3} {1\over\sqrt{2 E_{\bf p}}}
        \left(a_{\bf p} e^{-ip\cdot x} + a_{\bf p}^\dag e^{ip\cdot x}\right)

    \pi_I(x) = {\partial_t}\phi_I(x)
        = \int {\d^3 p\over (2\pi)^3}(-i) {\sqrt{E_{\bf p}\over2}}
        \left(a_{\bf p} e^{-ip\cdot x} - a_{\bf p}^\dag e^{ip\cdot x}\right)

where:

.. math::

    \left[a_{\bf p}, a_{\bf q}^{\dag}\right] =
        (2\pi)^3\delta^{(3)}({\bf p} - {\bf q})

(all other commutators are equal to zero).
The equal-time commutation relations for $\phi$ and $\pi$ are then:

.. math::

    \left[\phi({\bf x}), \pi({\bf y})\right] =
        i\delta^{(3)}({\bf x} - {\bf y})

(all other commutators are equal to zero).

The Hamiltonian is

.. math::

    H = \int{\d^3p\over(2\pi)^3} E_{\bf p}
        a_{\bf p}^\dag a_{\bf p}

Fermions:

.. math::

    \psi_I(x) = \int {\d^3 p\over (2\pi)^3} {1\over\sqrt{2 E_{\bf p}}}
        \sum_{s=1}^2
        \left(b_{\bf p}^s u^s({\bf p}) e^{-ip\cdot x}
        + d_{\bf p}^{s\dag} v^s({\bf p}) e^{ip\cdot x}\right)

    \bar\psi_I(x) = \psi_I^\dag(x)\gamma^0 =
    \int {\d^3 p\over (2\pi)^3} {1\over\sqrt{2 E_{\bf p}}}
        \sum_{s=1}^2
        \left(d_{\bf p}^s \bar v^s({\bf p}) e^{-ip\cdot x}
        + b_{\bf p}^{s\dag} \bar u^s({\bf p}) e^{ip\cdot x}\right)

where

.. math::

    u^s({\bf p}) = \mat{\sqrt{{\bf p}\cdot\sigma}\xi^s\cr
        \sqrt{{\bf p}\cdot\bar\sigma}\xi^s\cr}

    v^s({\bf p}) = \mat{\sqrt{{\bf p}\cdot\sigma}\eta^s\cr
        -\sqrt{{\bf p}\cdot\bar\sigma}\eta^s\cr}

    \sum_{s=1}^2 u^s({\bf p})\bar u^s({\bf p}) = \slashed{p} + m

    \sum_{s=1}^2 v^s({\bf p})\bar v^s({\bf p}) = \slashed{p} - m

    \left\{b_{\bf p}^r, b_{\bf q}^{s\dag}\right\} =
    \left\{d_{\bf p}^r, d_{\bf q}^{s\dag}\right\} =
        (2\pi)^3\delta^{(3)}({\bf p} - {\bf q}) \delta^{rs}

(all other anticommutators are equal to zero).
The equal-time anticommutation relations for $\psi$ and $\psi^\dag$ are then:

.. math::

    \left\{\psi_a({\bf x}), \psi_b^\dag({\bf y})\right\} =
        \delta^{(3)}({\bf x} - {\bf y}) \delta_{ab}

    \left\{\psi_a({\bf x}), \psi_b({\bf y})\right\} =
    \left\{\psi_a^\dag({\bf x}), \psi_b^\dag({\bf y})\right\} =
    0

The Hamiltonian is

.. math::

    H = \int{\d^3p\over(2\pi)^3}\sum_{s=1}^2 E_{\bf p}
        \left(b_{\bf p}^{s\dag}b_{\bf p}^{s}
        +d_{\bf p}^{s\dag}d_{\bf p}^{s}\right)

and the total charge:

.. math::

    Q = \int{\d^3p\over(2\pi)^3}\sum_{s=1}^2
        \left(b_{\bf p}^{s\dag}b_{\bf p}^{s}
        -d_{\bf p}^{s\dag}d_{\bf p}^{s}\right)

So the $b$-type particles and $d$-type particles are identical except the
charge. In QED, we identify the $b$-type particles as electrons and the
$d$-type particles as positrons.


Vector bosons:

.. math::

    A_\mu(x) = \int {\d^3 p\over (2\pi)^3} {1\over\sqrt{2 E_{\bf p}}}
        \sum_{r=0}^3
        \left(a_{\bf p}^r\epsilon_\mu^r({\bf p}) e^{-ip\cdot x}
        + a_{\bf p}^{r\dag}\epsilon_\mu^{r*}({\bf p}) e^{ip\cdot x}\right)

where

.. math::

    \left[a_{\bf p}^r, a_{\bf q}^{s\dag}\right] =
        (2\pi)^3\delta^{(3)}({\bf p} - {\bf q}) \delta^{rs}

The equal-time commutation relations for $A_\mu$ are then:

.. math::

    \left[A_\mu({\bf x}), A_\nu^\dag({\bf y})\right] =
        \delta^{(3)}({\bf x} - {\bf y}) \delta_{\mu\nu}

Calculating Scattering Amplitudes using Green Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We are interested in calculating the following scattering amplitudes:

.. math::

    \braket{f|i}

where the initial $\ket{i}$ and final $\ket{f}$ states are created by creation
operators of the fields from the previous section. For example

.. math::

    \ket{i} = b_1^\dag b_2^\dag\ket{\Omega}

    \ket{f} = b_{1'}^\dag b_{2'}^\dag\ket{\Omega}

Depending on the particular creation and anihilation operators, it can be shown
that they can be replaced by:

.. math::

    a^\dag_{\bf k}\,{}_\text{in} \to
        i\int\d^4 x e^{ikx}\left(-\partial^2+m^2\right)\phi(x)

    a_{\bf k}\,{}_\text{out} \to
        i\int\d^4 x e^{-ikx}\left(-\partial^2+m^2\right)\phi(x)

    b^{s\dag}_{\bf k}\,{}_\text{in} \to
        i\int\d^4 x\bar\psi(x) \left(i\overleftarrow{\fslash\partial}+m\right)u^s({\bf k})e^{ikx}

    b^s_{\bf k}\,{}_\text{out} \to
        i\int\d^4 x e^{-ikx}\bar u^s({\bf k})\left(-i\fslash\partial+m\right)\psi(x)

    d^{s\dag}_{\bf k}\,{}_\text{in} \to
        -i\int\d^4 x e^{ikx}\bar v^s({\bf k})\left(-i\fslash\partial+m\right)\psi(x)

    d^s_{\bf k}\,{}_\text{out} \to
        -i\int\d^4 x\bar\psi(x) \left(i\overleftarrow{\fslash\partial}+m\right)v^s({\bf k})e^{-ikx}

    a^{r\dag}_{\bf k}\,{}_\text{in} \to
        i\epsilon_\mu^{r*}({\bf k})
            \int\d^4 x e^{ikx}\left(-\partial^2\right) A^\mu(x)

    a^r_{\bf k}\,{}_\text{out} \to
        i\epsilon_\mu^r({\bf k})
            \int\d^4 x e^{-ikx}\left(-\partial^2\right) A^\mu(x)

where the "in" is the operator for $t\to -\infty$ and "out" for $t\to\infty$.
The fields $\phi(x)$, $\psi(x)$, $\bar\psi(x)$ and $A^\mu(x)$ have to be time
ordered. For our example we get:

.. math::

    \braket{f|i} = \braket{\Omega|
        b_{{\bf p}_{2'}}
        b_{{\bf p}_{1'}}
        b_{{\bf p}_{1}}^\dag
        b_{{\bf p}_{2}}^\dag
        |\Omega}
    = \braket{\Omega|T\,
        b_{{\bf p}_{2'}}
        b_{{\bf p}_{1'}}
        b_{{\bf p}_{1}}^\dag
        b_{{\bf p}_{2}}^\dag
        |\Omega}=

    = i^4 \int \d^4 x_1\d^4 x_2\d^4 x_{1'}\d^4 x_{2'}

    e^{-ip_{1'}x_{1'}}\left[\bar u^{s_{1'}}({\bf k}_{1'})
        \left(-i\fslash\partial_{1'} +m\right)\right]_{\alpha_{1'}}

    e^{-ip_{2'}x_{2'}}\left[\bar u^{s_{2'}}({\bf k}_{2'})
        \left(-i\fslash\partial_{2'} +m\right)\right]_{\alpha_{2'}}

    \braket{\Omega|T\,
        \psi_{\alpha_{2'}}(x_{2'})
        \psi_{\alpha_{1'}}(x_{1'})
        \bar\psi_{\alpha_1}(x_1)
        \bar\psi_{\alpha_2}(x_2)
        |\Omega}

    \left[\left(i\overleftarrow{\fslash\partial_1}+m\right)
        u^s({\bf p}_1)\right]_{\alpha_1} \,e^{ip_1x_1}

    \left[\left(i\overleftarrow{\fslash\partial_2}+m\right)
        u^s({\bf p}_2)\right]_{\alpha_2} \,e^{ip_2x_2}

where the $\alpha_1$, $\alpha_2$, $\alpha_{1'}$ and $\alpha_{2'}$ spinor
indices were introduced to show how the matrices should be multiplied.
The vacuum amplitude is called a 4 point interacting Green function in position
space:

.. math::

    G^{(4)}_{\alpha_{1'} \alpha_{2'} \alpha_1 \alpha_2}
        (x_{1'}, x_{2'}, x_1, x_2) =
    \braket{\Omega|T\,
        \psi_{\alpha_{2'}}(x_{2'})
        \psi_{\alpha_{1'}}(x_{1'})
        \bar\psi_{\alpha_1}(x_1)
        \bar\psi_{\alpha_2}(x_2)
        |\Omega}

we can also take a Fourier transform to get the Green function in momentum
space:

.. math::

    \tilde G^{(n)}(p_1,\dots, p_n) =
    \int\prod_{i=1}^n \d^4 x_i e^{-i p_i x_i}\,
    G^{(n)}(x_1, \dots, x_n)

then the scattering amplitude becomes (resuming the previous calculation):

.. math::

    \braket{f|i} = \cdots =
        i^4

    \left[\bar u^{s_{1'}}({\bf k}_{1'})
        \left(-i\fslash p_{1'} +m\right)\right]_{\alpha_{1'}}

    \left[\bar u^{s_{2'}}({\bf k}_{2'})
        \left(-i\fslash p_{2'} +m\right)\right]_{\alpha_{2'}}

    \tilde G^{(4)}_{\alpha_{1'} \alpha_{2'} \alpha_1 \alpha_2}
        (p_{1'}, p_{2'}, -p_1, -p_2)

    \left[\left(i{\fslash p_1}+m\right)
        u^s({\bf p}_1)\right]_{\alpha_1}

    \left[\left(i{\fslash p_2}+m\right)
        u^s({\bf p}_2)\right]_{\alpha_2}

This is called Lehmann-Symanzik-Zimmermann (LSZ) reduction formula.  One
obtains similar expressions for other fields as well (if there were different
creation operators been in the initial and final states). We now need to
calculate the interacting Green functions.

Evaluation of the Interacting Green Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The interacting Green functions can be evaluated using the formula:

.. math::

    G^{(n)}(x_1, \dots, x_n) =
        \braket{\Omega|T\, \phi_H(x_1) \dots \phi_H(x_n) |\Omega}
    =

    ={\braket{0|T\, \phi_I(x_1) \dots \phi_I(x_n) S|0}\over
    \braket{0|S|0}}

where

.. math::

    S=U_I(\infty, -\infty) =
    T\exp\left(-{i\over\hbar}\int_{-\infty}^{\infty}H_1(t)\d t \right) =
    T\exp\left(-{i\over\hbar}\int\d^4 x \H_1(x) \right)


$\phi_H$ is a field in the Heisenberg picture
($\phi({\bf x}, t)=e^{iHt}\phi({\bf x}, 0)e^{-iHt}$) and $\phi_I$ is a field in
the interaction picture ($\phi({\bf x}, t)=e^{iH_0t}\phi({\bf x},
0)e^{-iH_0t}$), where the Hamiltonian is $H=H_0 + H_1$ and the vacua (ground
states) are $H_0\ket{0} = 0$ and $H\ket{\Omega} = 0$.

This can be proven by evaluating the right hand side:

.. math::

    {\braket{0|T\, \phi_I(x_1) \dots \phi_I(x_n) S|0}\over
    \braket{0|S|0}}
    =
    {\braket{0|T\, \phi_I(x_1) \dots \phi_I(x_n) U_I(\infty, -\infty)|0}\over
    \braket{0|U_I(\infty, 0)U_I(0, -\infty)|0}}

    =
    {\braket{0|U_I(\infty, t_1) \phi_I(x_1) U_I(t_1, t_2) \dots
        U_I(t_{n-1}, t_n)\phi_I(x_n) U_I(t_n, -\infty)|0}\over
    \braket{0|U_I(\infty, 0)U_I(0, -\infty)|0}}

    =
    {\braket{0|U_I(\infty, 0) \phi_H(x_1) \dots \phi_H(x_n) U_I(0, -\infty)|0}\over
    \braket{0|U_I(\infty, 0)U_I(0, -\infty)|0}}=

    =
    {\braket{0|\Omega}\braket{\Omega|T \phi_H(x_1) \dots \phi_H(x_n)
        |\Omega}\braket{\Omega|0}\over
    \braket{0|\Omega}\braket{\Omega|\Omega}\braket{\Omega|0}}=

    =
    {\braket{\Omega|T \phi_H(x_1) \dots \phi_H(x_n) |\Omega}\over
    \braket{\Omega|\Omega}}=

    =
    \braket{\Omega|T \phi_H(x_1) \dots \phi_H(x_n) |\Omega}

where we used the following relations:

.. math::

    U_I(t_{k-1}, t_k) \phi_I(x_k) U_I(t_k, t_{k+1})=
    U_I(t_{k-1}, 0) U_I^\dag(t_k, 0) \phi_I(x_k) U_I(t_k, 0) U_I(0, t_{k+1})=
    U_I(t_{k-1}, 0) \phi_H(x_k) U_I(0, t_{k+1})

    U_I(0, -\infty)\ket{0}=
    U_I(0, -\infty)\left[\ket{\Omega}\bra{\Omega}+\sum_{n\neq0}\ket{n}\bra{n}
        \right]\ket{0} =
    \ket{\Omega}\braket{\Omega|0}+\lim_{t\to-\infty}
        \sum_{n\neq0}e^{i E_n t}\ket{n}\braket{n|0}
    =
    \ket{\Omega}\braket{\Omega|0}

    \braket{\Omega|\Omega}=1


.. index::
    single: S-matrix
    pair: evolution; operator

Evolution Operator, S-Matrix Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The evolution operator $U$ is defined by the equations:

.. math::

    \ket{\phi(t_2)}=U(t_2, t_1)\ket{\phi(t_1)}



.. math::

    i\hbar{\partial U(t, t_1)\over\partial t} = H(t)U(t, t_1)



.. math::

    U(t_1, t_1) = 1


We are interested in calculating the S matrix elements:

.. math::

    \braket{f|U(\infty, -\infty)|i}=\braket{f|S|i}=S_{fi}


so we first calculate $U(\infty, -\infty)$. Integrating the equation for the
evolution operator:

.. math::

    U(t_2, t_1)=U(t_1, t_1)-{i\over\hbar}\int_{t_1}^{t_2} H(t)U(t, t_1)\d t =1-{i\over\hbar}\int_{t_1}^{t_2} H(t)U(t, t_1)\d t


Now: 

.. math::

    S=U(\infty, -\infty) =1-{i\over\hbar} \int_{-\infty}^{\infty} H(t')U(t', -\infty)\d t'=



.. math::

    =1+\left(-{i\over\hbar}\right)\int_{-\infty}^{\infty} H(t')U(t', -\infty)\d t' +\left(-{i\over\hbar}\right)^2\int_{-\infty}^{\infty} \int_{-\infty}^{t'} H(t')H(t'')U(t'', -\infty)\d t'\d t''=



.. math::

    =\cdots= \sum_{n=0}^\infty \left(-{i\over\hbar}\right)^n {1\over n!} \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\cdots T\{H(t_1)H(t_2)\cdots\}\d t_1\d t_2\cdots=



.. math::

    = T\exp\left(-{i\over\hbar}\int_{-\infty}^{\infty}H(t)\d t \right) = T\exp\left(-{i\over\hbar}\int_{-\infty}^{\infty}\d^4 x \H(x) \right)


If $\L$ doesn't contain derivatives of the fields, then $\H = -\L$ so: 

.. math::

    U(\infty, -\infty) = T\exp\left({i\over\hbar}\int_{-\infty}^{\infty}\d^4 x \L(x) \right)



Let's write $S=1+iT$ and $\ket{i}=\ket{k_1\cdots k_m}$, $\ket{f}=\ket{p_1\cdots p_n}$. As a first step now, let's investigate a scalar field, e.g. $\L=-{\lambda\over4}\phi^4$ (e.g. a Higgs self interaction term above), we'll look at other fields later: 

.. math::

    \braket{f|S|i}= \braket{f|iT|i}= \braket{p_1\cdots p_n|iT|k_1\cdots k_m}= {1\over\tilde D(k_1)\cdots\tilde D(k_m)} {1\over\tilde D(p_1)\cdots\tilde D(p_n)}



.. math::

    \int\d^4 x_1\cdots \d^4 x_m e^{-i(k_1 x_1+\cdots + k_m x_m)} \int\d^4 y_1\cdots \d^4 y_n e^{+i(p_1 y_1+\cdots + p_n y_n)} G(x_1, \cdots, x_m, y_1, \cdots, y_m)


where 

.. math::

    G(x_1, \cdots, x_n)= \braket{\Omega|T\{\phi(x_1)\cdots\phi(x_n)\}|\Omega} =



.. math::

    {\braket{0|T\{\phi_I(x_1)\cdots\phi_I(x_n)\exp\left({i\over\hbar}\int_{-\infty}^{\infty}\d^4 x \L(x) \right)\}|0} \over \braket{0|T\exp\left({i\over\hbar}\int_{-\infty}^{\infty}\d^4 x \L(x) \right)|0} }


This is called the LSZ formula. Now we use the Wick contraction, get some terms like $D_{23}D_{34}$ integrate things out, this will give the delta function and $\tilde D(p)$'s and that's it.

Let's see how it goes for $\L=-{\lambda\over4}\phi^4$ for the process
$k_1+k_2\to p_1+p_2$:

.. math::

    \braket{p_1 p_2|S|k_1 k_2} = {\int\d^4 x_1\d^4 x_2 e^{-i(k_1x_1+k_2x_2)} \int\d^4 y_1\d^4 y_2 e^{i(p_1y_1+p_2y_2)} \over \tilde D(k_1)\tilde D(k_2) \tilde D(p_1)\tilde D(p_2)}



.. math::

    {\braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(y_1)\phi_I(y_2)\exp\left( -{i\lambda\over4\hbar} \int\d^4 x \phi_I^4(x) \right)\}|0} \over \braket{0|T\exp\left(-{i\lambda\over4\hbar}\int\d^4 x \phi_I^4(x) \right)|0} }=



.. math::

    = {\int\d^4 x_1\d^4 x_2 e^{-i(k_1x_1+k_2x_2)} \int\d^4 y_1\d^4 y_2 e^{i(p_1y_1+p_2y_2)} \over \tilde D(k_1)\tilde D(k_2) \tilde D(p_1)\tilde D(p_2)}



.. math::

    \left[ { \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(y_1)\phi_I(y_2)\}|0} \over \braket{0|T\exp\left(-{i\lambda\over4\hbar}\int\d^4 x \phi_I^4(x) \right)|0} }\right. +



.. math::

    +{ \left(-{i\lambda\over4\hbar}\right)\int\d^4 x \braket{0|T\{\phi_I(x_1)\phi_I(x_2) \phi_I(y_1)\phi_I(y_2) \phi_I^4(x)\}|0} \over \braket{0|T\exp\left(-{i\lambda\over4\hbar}\int\d^4 x \phi_I^4(x) \right)|0} } +



.. math::

    \left. +{ \left(-{i\lambda\over4\hbar}\right)^2\int\d^4 x\,\d^4 y \braket{0|T\{\phi_I(x_1)\phi_I(x_2) \phi_I(y_1)\phi_I(y_2) \phi_I^4(x)\phi_I^4(y)\}|0} \over \braket{0|T\exp\left(-{i\lambda\over4\hbar}\int\d^4 x \phi_I^4(x) \right)|0} } +\cdots\right]=



.. math::

    = { 1 \over \tilde D(k_1)\tilde D(k_2) \tilde D(p_1)\tilde D(p_2)}



.. math::

    \left[ (2\pi)^4 \delta^{(4)}(p_1+p_2)(2\pi)^4 \delta^{(4)}(k_1+k_2)\tilde D(p_1) \tilde D(k_1)+\right.



.. math::

    (-i\lambda)6(2\pi)^4\delta^{(4)}(p_1+p_2-k_1-k_2)\tilde D(k_1)\tilde D(k_2) \tilde D(p_1)\tilde D(p_2)+



.. math::

    \left. (-i\lambda)(\hbox{disconnected terms with not enough $\tilde D(\cdots)$s})+(-i\lambda)^2(\cdots)+\cdots\right]=



.. math::

    = (2\pi)^4\delta^{(4)}(p_1+p_2-k_1-k_2)\left[6(-i\lambda)+ 3(-i\lambda)^2\int{\d^4 k\over (2\pi)^4}\tilde D(k)\tilde D(p1+p2-k) +(-i\lambda)^3(\cdots)+\cdots\right]


The denominator cancels with the disconnected terms. We used the Wick contractions (see below for a thorough explanation+derivation): 

.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(y_1)\phi_I(y_2)\}|0}= D(x_1-x_2)D(y_1-y_2)+D(x_2-y_1)D(x_1-y_2)+D(x_2-y_2)D(x_1-y_1)



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2) \phi_I(y_1)\phi_I(y_2) \phi_I^4(x)\}|0}= D(x_1-x)D(x_2-x)D(y_1-x)D(y_2-x)+\hbox{disconnected}



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2) \phi_I(y_1)\phi_I(y_2) \phi_I^4(x)\phi_I^4(y)\}|0}= D(x_1-x)D(x_2-x)D(y_1-y)D(y_2-y)D(x-y)D(x-y)



.. math::

    +\hbox{disconnected}


Where the "disconnected" terms are $D(x_1-y_1)D(x_2-y_2)D(x-x)D(x-x)$ and similar. When they are integrated over, they do not generate enough $\tilde D(p_1)$ propagators to cancel the propagators from the LSZ formula, which will cause the terms to vanish.

For the $\L=\phi^3(x)$ theory, one also needs the following contractions: 

.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2) \phi_I(y_1)\phi_I(y_2) \phi_I^3(x)\}|0} = 0



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2) \phi_I(y_1)\phi_I(y_2) \phi_I^3(x)\phi_I^3(y)\}|0} = D(x_1-x)D(x_2-x)D(x-y)D(y_1-y)D(y_2-y)


Thus it is clear that the only difference from the above is the factor $D(x-y)$ which after integrating changes to $\tilde D(p_1+p_2)$ and this ends up in the final result.

One always gets the delta function in the result, so we define the matrix element $\M_{fi}$ by: 

.. math::

    S_{fi} = (2\pi)^4\delta^{(4)}(p_1+p_2+\cdots - k_1 - k_2 - \cdots) i \M_{fi}


.. index:: fermions, vector bosons

Propagators for Scalar Bosons, Fermions and Vector Bosons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The only nonzero contractions that can occur are the propagators below. All
other contractions are zero.

Propagator for a scalar boson is:

.. math::

    \braket{0|T\{\phi_I(x)\phi_I(y)\}|0}\equiv D(x-y)= \int {\d^4 p\over (2\pi)^4}\tilde D(p) e^{-ip(x-y)}


with

.. math::

    \tilde D(p) = {i\over p^2-m^2+i\epsilon}

For fermions (Feynman propagator):

.. math::

    \braket{0|T\{\psi_I(x)\bar\psi_I(y)\}|0}\equiv S(x-y)= \int {\d^4 p\over (2\pi)^4}\tilde S(p) e^{-ip(x-y)}


with

.. math::

    \tilde S(p) = {i\over \fslash{p} - m +i\epsilon}= {i(\fslash{p}+m)\over p^2-m^2+i\epsilon}


For vector bosons:

.. math::

    \braket{0|T\{A_\mu(x)A_\nu(y)\}|0}\equiv D_{\mu\nu}(x-y)= \int {\d^4 p\over (2\pi)^4}\tilde D_{\mu\nu}(p) e^{-ip(x-y)}


with

.. math::

    \tilde D_{\mu\nu}(p) = i{-g_{\mu\nu}+{p_\mu p_\nu\over m^2}\over p^2-m^2+i\epsilon}


For massless bosons:

.. math::

    \tilde D_{\mu\nu}(p) = i{-g_{\mu\nu}\over p^2+i\epsilon}



.. index:: Wick Theorem

Wick Theorem
~~~~~~~~~~~~

As seen above, we need to be able to calculate 

.. math::

    \braket{0|T\{\phi_I(x_1)\cdots\phi_I(x_n)\}|0}


The Wick theorem says, that this is equal to all possible contractions of fields (all fields need to be contracted), where a contraction is defined as: 

.. math::

    \braket{0|T\{\phi_I(x)\phi_I(y)\}|0}\equiv D(x-y)= \int {\d^4 p\over (2\pi)^4}\tilde D(p) e^{-ip(x-y)}


with 

.. math::

    \tilde D(p) = {i\over p^2-m^2+i\epsilon}


A few lowest possibilities: 

.. math::

    \braket{0|T\{\phi_I(x_1)\}|0}= 0



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\}|0}= D_{12}



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(x_3)\}|0}= 0



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(x_3)\phi_I(x_4)\}|0}= \hbox{disconnected}



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(x_3)\phi_I(x_4)\phi_I(x)\}|0}= 0



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(x_3)\phi_I(x_4)\phi_I^2(x)\}|0}= \hbox{disconnected}



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(x_3)\phi_I(x_4)\phi_I^3(x)\}|0}= 0



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(x_3)\phi_I(x_4)\phi_I^4(x)\}|0}= 4!\,D(x_1-x)D(x_2-x)D(x_3-x)D(x_4-x)+\hbox{disconnected}



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(x_3)\phi_I(x_4)\phi_I^3(x)\phi_I^3(y)\}|0}=



.. math::

    =D(x_1-x)D(x_2-x)D(x-y)D(x_3-y)D(x_4-y) + \hbox{disconnected}



.. math::

    \braket{0|T\{\phi_I(x_1)\phi_I(x_2)\phi_I(x_3)\phi_I(x_4)\phi_I^4(x)\phi_I^4(y)\}|0}=



.. math::

    =D(x_1-x)D(x_2-x)D(x-y)D(x-y)D(x_3-y)D(x_4-y) + \hbox{disconnected}


For the last two equations, not all possibilities of the connected graphs are listed (and also the combinatorial factor is omitted).

Nonrelativistic Field Operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One difference in nonrelativistic quantum mechanics is that the noninteracting
solutions to the equation of motion (Schrödinger equation in this case) can be
numbered using a discrete index, so for example the momentum $\bf q$ is not
continuous, thus the (anti)commutation relations for creation and anihilation
operators contain the Kronecker delta (instead of a delta function) and
integrals over the index are replaced by sums. The reason for that is that we
usually employ boundary conditions (like a lattice, or one particle potential
due to nuclei, etc.) that make the spectrum discrete.


For bosons the field operators are given by:

.. math::

    \hat\psi({\bf x}) = \sum_k \psi_k({\bf x}) c_k

    \hat\psi^\dag({\bf x}) = \sum_k \psi_k^*({\bf x}) c_k^\dag

where the coefficients are the single-particle wave functions.

..  math::

    [c_k, c_l^\dag] = \delta_{kl}

    [c_k, c_l] = [c_k^\dag, c_l^\dag] = 0

so the commutation relations for $\hat\psi$ and $\hat\psi^\dag$ are:

.. math::

    [\hat\psi({\bf x}), \hat\psi^\dag({\bf y})] = \delta^{(3)}({\bf x}-{\bf y})

    [\hat\psi({\bf x}), \hat\psi({\bf y})] =
    [\hat\psi^\dag({\bf x}), \hat\psi^\dag({\bf y})] = 0

For fermions:

.. math::

    \hat\psi({\bf x}) = \sum_k\sum_{s=1}^2 \psi_k^s({\bf x}) c_k

    \hat\psi^\dag({\bf x}) = \sum_k\sum_{s=1}^2 \psi_k^{s*}({\bf x}) c_k^\dag

where

..  math::

    \{c_k, c_l^\dag\} = \delta_{kl}

    \{c_k, c_l\} = \{c_k^\dag, c_l^\dag\} = 0

so the commutation relations for $\hat\psi$ and $\hat\psi^\dag$ are:

.. math::

    \{\hat\psi({\bf x}), \hat\psi^\dag({\bf y})\} =\delta^{(3)}({\bf x}-{\bf y})

    \{\hat\psi({\bf x}), \hat\psi({\bf y})\} =
    \{\hat\psi^\dag({\bf x}), \hat\psi^\dag({\bf y})\} = 0

The (interacting) Hamiltonian for both bosons and fermions is

.. math::

    i\hbar\partial_t\ket{\Psi(t)} = \hat H\ket{\Psi(t)}

    \hat H = \hat T + \hat V = \sum_{ij} c_i^\dag\braket{i|T|j}c_j +
        \half \sum_{ijkl} c_i^\dag c_j^\dag\braket{ij|V|kl}c_l c_k

Note the ordering of the final two destruction operators $c_l c_k$, which is
opposite that of the last two single-particle wave functions in the matrix
elements of the potential $\braket{ij|V|kl}$ (for bosons it doesn't matter, for
fermions it changes a sign).


Nonrelativistic Propagator
~~~~~~~~~~~~~~~~~~~~~~~~~~

Nonrelativistic limits of the propagators are obtained by assuming $|{\bf p}|/m
\ll 1$ (we substitute $\omega=p_0-m$):

.. math::

    \tilde D(p) = {i\over p^2-m^2+i\epsilon}
    = {i\over p_0^2-{\bf p}^2-m^2+i\epsilon}
    = {i\over \left(p_0-\sqrt{{\bf p}^2+m^2}\right)\left(p_0
        +\sqrt{{\bf p}^2+m^2}\right)+i\epsilon}
    \approx

    \approx
    {i\over \left(p_0-m-{{\bf p}^2\over 2m}\right)
        \left(p_0+m+{{\bf p}^2\over 2m}\right) + i\epsilon}
    =
    {i\over \left(\omega-{{\bf p}^2\over 2m}\right)
        \left(\omega+2m+{{\bf p}^2\over 2m}\right) + i\epsilon}

the behavior of the propagator in the vicinity of its positive frequency pole
$\omega\approx{{\bf p}^2\over 2m}$ is (remember $\omega \to 0$ in the
nonrelativistic limit):

.. math::

    \tilde D(p) \approx
    {i\over \left(\omega-{{\bf p}^2\over 2m}\right)
        \left(\omega+2m+{{\bf p}^2\over 2m}\right) + i\epsilon}
    \approx
    {i\over \left(\omega-{{\bf p}^2\over 2m}\right) 2m + i\epsilon}
    =
    {1\over2m}{i\over\omega-{{\bf p}^2\over 2m} + i\epsilon'}

Similarly for fermions:

.. math::

    \tilde S(p) = {i(\fslash{p}+m)\over p^2-m^2+i\epsilon}
    = {i(p^0\gamma_0 - p^j\gamma_j+m)\over p^2-m^2+i\epsilon}
    \approx
    {1\over2m}{i(p^0\gamma_0 - p^j\gamma_j+m)\over
        \omega-{{\bf p}^2\over 2m} + i\epsilon'}
    =

    = {1\over2m}{i((\omega+m)\gamma_0 - p^j\gamma_j+m)\over
        \omega-{{\bf p}^2\over 2m} + i\epsilon'}
    \approx
    {1\over2m}{i(m\gamma_0 - p^j\gamma_j+m)\over
        \omega-{{\bf p}^2\over 2m} + i\epsilon'}
    =

.. math::
    :label: fermion-propagator-approx

    =
    {i\left(\half(\gamma_0+1) - {p^j\gamma_j\over2m}\right)\over
        \omega-{{\bf p}^2\over 2m} + i\epsilon'}

The first term

.. math::

    \half(\gamma_0+1) = \mat{
        1 & 0 & 0 & 0\cr
        0 & 1 & 0 & 0\cr
        0 & 0 & 0 & 0\cr
        0 & 0 & 0 & 0\cr
        }

selects the two upper components of a given bispinor. The second term

.. math::

    - {p^j\gamma_j\over2m} = \mat{
        0 & -{p^j\sigma_j\over2m} \cr
        {p^j\sigma_j\over2m} & 0 \cr
        }

mixes the upper and lower components of the bispinor and the contribution of
this term is quadratic in ${\bf p}\over m$ so it can be neglected. The
numerator of :eq:`fermion-propagator-approx` reduces to a unit matrix (in spin
space):

.. math::

    \tilde S(p) \approx
    {i\left(\half(\gamma_0+1) - {p^j\gamma_j\over2m}\right)\over
        \omega-{{\bf p}^2\over 2m} + i\epsilon}
    \approx
    {i\one\over \omega-{{\bf p}^2\over 2m} + i\epsilon}
    =\one G_0^+({\bf p}, \omega)

where $G_0^+({\bf p}, \omega)$ is the nonrelativistic retarded propagator
defined by:

.. math::

    G_0^+(x-y) =
    i \int {\d^3 p\over (2\pi)^3}
    \int {\d \omega\over 2\pi}
    G_0^+({\bf p}, \omega)
        e^{i{\bf p}\cdot({\bf x-y})}
        e^{-i\omega(t_x - t_y)}

(For the other pole $p_0 = -\sqrt{{\bf p}^2+m^2}$, we define $\omega=-p_0-m$ and
we would see that the antiparticles' propagator reduces to the advanced
Green's function in the nonrelativistic limit.)

As shown above, the nonrelativistic free propagator is defined by:

.. math::

    G_0^+(x-y) =
    i \int {\d^3 p\over (2\pi)^3}
    \int {\d \omega\over 2\pi}
    G_0^+({\bf p}, \omega)
        e^{i{\bf p}\cdot({\bf x-y})}
        e^{-i\omega(t_x - t_y)}


with:

.. math::

    G_0^+({\bf p}, \omega)=
    {i\over \omega-{{\bf p}^2\over 2m} + i\epsilon}

If we use the energies of the nonineracting particles
$E_k \equiv \epsilon_k = {\hbar^2k^2\over 2m} = {k^2\over 2m}$, we can write it
as:

.. math::

    G_0^+({\bf p}, \omega)=
    {i\over \omega-{{\bf p}^2\over 2m} + i\epsilon}
    =
    {i\over \omega-E_k + i\epsilon}

so

.. math::

    G_0^+(k, \omega) = {i\over \omega-E_k + i\epsilon}

using $E = \hbar\omega$ we can also write:

.. math::

    G_0^+(k, E) = {i\over E-E_k + i\epsilon}

Other equivalent ways of representing the propagator:

.. math::

    G_0^+(x-y)
    =
    G_0^+({\bf x}, t_x, {\bf y}, t_y)
    =
    i \int {\d^3 p\d E\over (2\pi\hbar)^4}
    G_0^+({\bf p}, E)
        e^{{i\over\hbar}{\bf p}\cdot({\bf x-y})}
        e^{-{i\over\hbar}E(t_x - t_y)}
    =

    =
    i \int {\d^3 k\d \omega\over (2\pi)^4}
    G_0^+(k, \omega)
        e^{i {\bf k}\cdot({\bf x-y})}
        e^{-i\omega(t_x - t_y)}

Sometimes it's useful to calculate the mixed representation $G_0^+(k, t)$:

.. math::

    G_0^+(k, t) = \int {\d\omega\over2\pi}e^{-i\omega t}G_0^+(k, \omega)
    = \int {\d\omega\over2\pi}e^{-i\omega t}
    {i\over \omega-E_k + i\epsilon}
    =
    \cdots
    =\theta_t e^{-i (E_k-i\epsilon)t}

(The "$\cdots$" means to use the Residue Theorem and distinguish two cases $t <
0$ and $t > 0$, thus getting the Heaviside step function $\theta_t$ in the
result.)

Very often, in practice, one just needs to work with $G_0^+(k, t)$ and
$G_0^+(k, \omega)$, here is how to convert between those:

.. math::

    G_0^+(k, t) = \int_{-\infty}^\infty
        {\d\omega\over2\pi}e^{-i\omega t}G_0^+(k, \omega)

    G_0^+(k, \omega) = \int_{-\infty}^\infty \d t\, e^{i\omega t}G_0^+(k, t)

The relation to the contraction of operators is:

.. math::

    G_0^+({\bf k}, t_2 - t_1) = -i \theta_{t_2-t_1} \braket{\Psi_0|
        c_{\bf k}(t_2) c_{\bf k}^\dag(t_1)|\Psi_0}

where $\ket{\Psi_0}$ is the ground state wavefunction and:

.. math::

    c_{\bf k}(t) = e^{i H_0 t} c_{\bf k} e^{-i H_0 t}

so to understand the meaning of $G_0^+({\bf k}, t_2 - t_1)$, we write it as:

.. math::

    G_0^+({\bf k}, t_2 - t_1) = -i \theta_{t_2-t_1} \braket{\Psi_0|
        c_{\bf k}(t_2) c_{\bf k}^\dag(t_1)|\Psi_0}
    = -i \theta_{t_2-t_1} \braket{\Psi_0|e^{i H_0 t_2}
        c_{\bf k}e^{-i H_0 (t_2-t_1)}c_{\bf k}^\dag e^{-i H_0 t_1}|\Psi_0}
    =

    = -i \theta_{t_2-t_1} \left(e^{-i H_0 t_2}\ket{\Psi_0}\right)^\dag
        \left(
        c_{\bf k}e^{-i H_0 (t_2-t_1)}c_{\bf k}^\dag e^{-i H_0 t_1}\ket{\Psi_0}
        \right)

which describes the probability amplitude of adding a bare particle at time
$t_1$, removing at time $t_2$ and regaining the original many-body system (that
in the meantime evolved into $e^{-i H_0 t_2}\ket{\Psi_0}$).

.. index:: Feynman rules

Feynman Rules
~~~~~~~~~~~~~

We can deduce a set of rules, so that one doesn't have to repeat the whole calculation each time. For a scalar field we derived the rules above, for fermion and vector boson fields it's more difficult.


ZZH interaction
~~~~~~~~~~~~~~~

Let's calculate the $\L_{ZZH}=\lambda Z_\mu Z^\mu H$ interaction in the SM, where $\lambda={g^2\over4\cos\theta_W}$. Consider $H(p)\to Z(k)+Z(l)$: 

.. math::

    \braket{f|S|i}= \braket{f|iT|i}= \braket{k l|iT|p}= {\varepsilon_\alpha(k)\varepsilon^\alpha(l)\over\tilde D_{\mu\nu}(k)\tilde D^{\mu\nu}(l)} {1\over\tilde D(p)}



.. math::

    \int\d^4 x_1 e^{-i p x_1} \int\d^4 y_1 \d^4 y_2 e^{+i(k y_1+l y_2)} \braket{0|T\{Z_\mu(y_1) Z^\mu(y_2) H(x_1)
    \exp\left({i\over\hbar}\int\d^4 x \L_{ZZH}(x) \right)\}|0} =



.. math::

    = {\varepsilon_\alpha(k)\varepsilon^\alpha(l)\over\tilde D_{\mu\nu}(k)\tilde D^{\mu\nu}(l)} {1\over\tilde D(p)}



.. math::

    \int\d^4 x_1 e^{-i p x_1} \int\d^4 y_1 \d^4 y_2 e^{+i(k y_1+l y_2)}\int\d^4 x i\lambda D_{\alpha\mu}(y_1-x)D^{\alpha\mu}(y_2-x)D(x_1-x) =



.. math::

    =i\lambda(2\pi)^4\delta^{(4)}(p-k-l)\varepsilon_\alpha(k)\varepsilon^\alpha(l)


where we used the fact, that the only nonzero element of the Green function is 

.. math::

    \int\d^4 x \braket{0|T\{Z_\alpha(y_1) Z^\alpha(y_2) H(x_1)Z_\mu(x)Z^\mu(x) H(x)\}|0}




eeH interaction
~~~~~~~~~~~~~~~

Let's calculate the $\L_{eeH}=-\lambda \bar ee H$ interaction in the SM, where $\lambda={h_e\over\sqrt2}$. Consider $H(p)\to e^-(k)+e^+(l)$: 

.. math::

    \braket{f|S|i}= \braket{f|iT|i}= \braket{k l|iT|p}= {\bar u(k) v(l)\over\tilde S(k)\tilde S(l)} {1\over\tilde D(p)}



.. math::

    \int\d^4 x_1 e^{-i p x_1} \int\d^4 y_1 \d^4 y_2 e^{+i(k y_1+l y_2)} \braket{0|T\{\bar e(y_1) e(y_2) H(x_1)\}|0} =



.. math::

    = {\bar u(k) v(l)\over\tilde S(k)\tilde S(l)} {1\over\tilde D(p)}



.. math::

    \int\d^4 x_1 e^{-i p x_1} \int\d^4 y_1 \d^4 y_2 e^{+i(k y_1+l y_2)}\int\d^4 x (-i\lambda) S(y_1-x)S(y_2-x)D(x_1-x) =



.. math::

    =(-i\lambda)(2\pi)^4\delta^{(4)}(p-k-l)\bar u(k) v(l)


where we used the fact, that the only nonzero element of the Green function is 

.. math::

    \int\d^4 x \braket{0|T\{\bar e(y_1) e(y_2) H(x_1)\bar e(x)e(x) H(x)\}|0}




ee gamma interaction
~~~~~~~~~~~~~~~~~~~~

Let's calculate the $\L_{ee\gamma}=-\lambda \bar e\gamma^\mu e A_\mu$ interaction in the SM, where $\lambda=g\sin\theta_W$. Consider $\gamma(p)\to e^-(k)+e^+(l)$: 

.. math::

    \braket{f|S|i}= \braket{f|iT|i}= \braket{k l|iT|p}= {\bar u(k) v(l)\over\tilde S(k)\tilde S(l)} {\varepsilon_\mu(p)\over\tilde D_{\alpha\beta}(p)}



.. math::

    \int\d^4 x_1 e^{-i p x_1} \int\d^4 y_1 \d^4 y_2 e^{+i(k y_1+l y_2)} \braket{0|T\{\bar e(y_1) e(y_2) A^\mu(x_1)\}|0} =



.. math::

    = {\bar u(k) v(l)\over\tilde S(k)\tilde S(l)} {\varepsilon_\mu(p)\over\tilde D_{\alpha\beta}(p)}



.. math::

    \int\d^4 x_1 e^{-i p x_1} \int\d^4 y_1 \d^4 y_2 e^{+i(k y_1+l y_2)}\int\d^4 x (-i\lambda) S(y_2-x) \gamma^\mu S(y_1-x) D^\alpha_\mu(x_1-x) =



.. math::

    =(2\pi)^4\delta^{(4)}(p-k-l)\bar u(k)(-i\lambda)\gamma^\mu v(l)\varepsilon_\mu(p)


where we used the fact, that the only nonzero element of the Green function is 

.. math::

    \int\d^4 x \braket{0|T\{\bar e(y_1) e(y_2) A^\alpha(x_1)\bar e(x)\gamma^\mu e(x) A_\mu(x)\}|0} =



.. math::

    =\pm S(y_2-x) \gamma^\mu S(y_1-x) D^\alpha_\mu(x_1-x)




eeee interaction
~~~~~~~~~~~~~~~~

Let's calculate the $\L_{ee\gamma}=-\lambda \bar e\gamma^\mu e A_\mu$ interaction in the SM, where $\lambda=g\sin\theta_W$. Consider $e^-(p_1)+e^+(p_2)\to\gamma(q)\to e^-(k_1)+e^+(k_2)$: 

.. math::

    \braket{f|S|i}= \braket{f|iT|i}= \braket{k_1 k_2|iT|p_1p_2}= {\bar u(k_1) v(k_2)\over\tilde S(k_1)\tilde S(k_2)} {\bar v(p_2) u(p_1)\over\tilde S(p_2)\tilde S(p_1)}



.. math::

    \int\d^4 x_1\d^4 x_2 e^{-i (p_1x_1 + p_2x_2)} \int\d^4 y_1\d^4 y_2 e^{+i (k_1y_1 + k_2y_2)} \braket{0|T\{\bar e(y_1) e(y_2) \bar e(x_1) e(x_2)\}|0} =



.. math::

    = {\bar u(k_1) v(k_2)\over\tilde S(k_1)\tilde S(k_2)} {\bar v(p_2) u(p_1)\over\tilde S(p_2)\tilde S(p_1)}



.. math::

    \int\d^4 x_1\d^4 x_2 e^{-i (p_1x_1 + p_2x_2)} \int\d^4 y_1\d^4 y_2 e^{+i (k_1y_1 + k_2y_2)} \int\d^4 x \int\d^4 y



.. math::

    (-i\lambda)^2 S(x_1-x)\gamma^\mu S(x_2-x) D_{\mu\nu}(x-y)S(y_1-y)\gamma^\nu S(y_2-y) =



.. math::

    =(2\pi)^4\delta^{(4)}(p_1+p_2-k_1-k_2)\bar v(p_2)(-i\lambda)\gamma^\mu u(p_1)\tilde D_{\mu\nu}(q=p_1+p_2=k_1+k_2) \bar u(k_1)(-i\lambda)\gamma^\nu v(k_2)


where we used the fact, that the only nonzero element of the Green function is 

.. math::

    \int\d^4 x \int\d^4 y \braket{0|T\{\bar e(y_1) e(y_2) \bar e(x_1) e(x_2) \bar e(x)\gamma^\mu e(x) A_\mu(x) \bar e(y)\gamma^\nu e(y) A_\nu(y) \}|0} =



.. math::

    =\pm S(x_1-x) \gamma^\mu S(x_2-x)D_{\mu\nu}(x-y)S(y_1-y)\gamma^\nu S(y_2-y)


.. index:: low energy theories

Low energy theories
-------------------


Fermi-type theory
~~~~~~~~~~~~~~~~~

This is a low energy ($m_W^2 \gg m_\mu m_e$) model for the EW interactions, that can be derived for example from the muon decay: 

.. math::

    \mu^- \to e^- +\nu_\mu + \bar \nu_e


From the SM the relevant Lagrangian is 

.. math::

    \L = {g\over2\sqrt2}(\bar e \gamma^\mu (1-\gamma_5) \nu_e W^-_\mu) + {g\over2\sqrt2}(\bar \mu \gamma^\mu (1-\gamma_5) \nu_\mu W^-_\mu)


and one gets the diagram $\mu^- +\bar\nu_\mu+ \to e^- + \bar \nu_e$ and the corresponding matrix element: 

.. math::

    iM = -i{g^2\over8}[\bar u\gamma_\mu (1-\gamma_5) u] {-g^{\mu\nu}+{q^\mu q^\nu\over m_W^2}\over q^2 - m_W^2} [\bar u\gamma_\nu (1-\gamma_5) v]


which when the momentum transfer $q$ is much less than $m_w$ becomes 

.. math::

    iM = -i{g^2\over8m_W^2}[\bar u\gamma^\mu (1-\gamma_5) u] [\bar u\gamma_\mu (1-\gamma_5) v]


but this element can be derived directly from the Lagrangian: 

.. math::

    \L = -{G_\mu\over\sqrt2} [\bar \psi_{\nu_\mu}\gamma^\mu (1-\gamma_5) \psi_\mu] [\bar \psi_e\gamma^\mu (1-\gamma_5) \psi_{\nu_e}]


with 

.. math::

    {G_\mu\over\sqrt2} = {g^2\over8m_W^2}


This is the universal V-A theory Lagrangian (after adding the h.c. term).

.. index:: quantum mechanics

Quantum Mechanics
=================

.. index:: QED, quantum electrodynamics

From QED to Quantum Mechanics
-----------------------------

The QED Lagrangian density is 

.. math::

    \L=\bar\psi(i\hbar c\gamma^\mu D_\mu-mc^2)\psi-{1\over4}F_{\mu\nu}F^{\mu\nu}


where 

.. math::

    \psi=\left( \begin{array}{c} \psi_1 \\ \psi_2 \\ \psi_3 \\ \psi_4 \\ \end{array}\right)


and 

.. math::

    D_\mu=\partial_\mu+{i\over \hbar}eA_\mu


is the gauge covariant derivative and ($e$ is the elementary charge, which is $1$ in atomic units, i.e. the electron has a charge $-e$) 

.. math::

    F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu


is the electromagnetic field tensor. It's astonishing, that this simple Lagrangian can account for all phenomena from macroscopic scales down to something like $10^{-13}\rm\,cm$. So it's not a surprise that Feynman, Schwinger and Tomonaga received the 1965 Nobel Prize in Physics for such a fantastic achievement.

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



.. math::

    =\int\d^3k' {\braket{{\bf r}|{\bf k'}}\braket{\bf{k'}|\bf{r'}}\over E_k-E_{k'}+i\epsilon} =\int\d^3k' {e^{i{\bf k'}\cdot({\bf r}-{\bf r'})}\over E_k-E_{k'}+i\epsilon} ={2m\over\hbar^2}\int\d^3k' {e^{i{\bf k'}\cdot({\bf r}-{\bf r'})}\over k^2-{k'}^2+i\epsilon}=



.. math::

    ={4\pi m\over\hbar^2i|{\bf r}-{\bf r'}|} \int_{-\infty}^\infty\d^3k' k'{e^{i k'|{\bf r}-{\bf r'}|}\over k^2-{k'}^2+i\epsilon} ={4\pi m\over\hbar^2i|{\bf r}-{\bf r'}|} (2\pi i)k{e^{i k|{\bf r}-{\bf r'}|}\over 2k}=



.. math::

    ={4\pi^2 me^{i k|{\bf r}-{\bf r'}|}\over\hbar^2|{\bf r}-{\bf r'}|}



.. math::

    G_-({\bf r}, {\bf r'}) = \braket{{\bf r}|G_-|{\bf r'}}=\bra{{\bf r}}{1\over E_k-H_0-i\epsilon}\ket{{\bf r'}} =\cdots ={4\pi^2 me^{-i k|{\bf r}-{\bf r'}|}\over\hbar^2|{\bf r}-{\bf r'}|}


Assuming $|{\bf r'}|\ll|{\bf r}|$, we can taylor expand $|{\bf r}-{\bf r'}|$: 

.. math::

    |{\bf r}-{\bf r'}| =e^{-{\bf r'}\cdot\nabla}|{\bf r}| =\left(1-{\bf r'}\cdot\nabla+\left(-{\bf r'}\cdot\nabla\right)^2 +O\left(r'^3\right) \right)|{\bf r}| =|{\bf r}|-{\bf r'}\cdot\nabla|{\bf r}|+O\left(r'^2\right) =



.. math::

    =r-{\bf r'}\cdot{\bf \hat r}+O\left(r'^2\right)


and simplify the result even further: 

.. math::

    G_+({\bf r}, {\bf r'}) ={4\pi^2 m\over\hbar^2}{e^{ikr}\over r} e^{-i k{\bf r'}\cdot{\bf\hat r}}



.. math::

    G_-({\bf r}, {\bf r'}) ={4\pi^2 m\over\hbar^2}{e^{-ikr}\over r} e^{i k{\bf r'}\cdot{\bf\hat r}}


Note: both functions may be divided by the factor $(2\pi)^3$ due to the momentum integration.

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


Plugging the representation of the Green function for $|{\bf r'}|\ll|{\bf r}|$ in: 

.. math::

    \psi({\bf r}) =e^{i{\bf k}\cdot{\bf r}} + {4\pi^2 m\over\hbar^2}{e^{ikr}\over r} \int\d^3 r'\d^3k' e^{-i k{\bf r'}\cdot{\bf\hat r}} e^{i{\bf k'}\cdot{\bf r'}} \braket{{\bf k'}|T|{\bf k}}=



.. math::

    =e^{i{\bf k}\cdot{\bf r}} + {4\pi^2 m\over\hbar^2}{e^{ikr}\over r} \int\d^3 r'\d^3k' e^{i {\bf r'}\cdot({\bf k'}-k{\bf\hat r})} \braket{{\bf k'}|T|{\bf k}}=



.. math::

    =e^{i{\bf k}\cdot{\bf r}} + {4\pi^2 m\over\hbar^2}{e^{ikr}\over r} \int\d^3k' \delta({\bf k'}-k{\bf\hat r}) \braket{{\bf k'}|T|{\bf k}}=



.. math::

    =e^{i{\bf k}\cdot{\bf r}} + {4\pi^2 m\over\hbar^2}{e^{ikr}\over r} \braket{k{\bf\hat r}|T|{\bf k}}=



.. math::

    =e^{i{\bf k}\cdot{\bf r}} + f(\theta,\phi)\, {e^{ikr}\over r}


where the scattering amplitude $f(\theta,\phi)$ is: 

.. math::

    f(\theta,\phi)= {4\pi^2 m\over\hbar^2} \braket{k{\bf\hat r}|T|{\bf k}} = {4\pi^2 m\over\hbar^2} \braket{{\bf k'}|T|{\bf k}}


Where ${\bf k'}=k{\bf\hat r}$ is the final momentum.

The differential cross section ${\d\sigma\over\d\Omega}$ is defined as the probability to observe the scattered particle in a given state per solid angle, e.g. the scattered flux per unit of solid angle per incident flux: 

.. math::

    {\d\sigma\over\d\Omega}= {1\over|{\bf j}_i|}{\d n\over\d\Omega} = {r^2\over|{\bf j}_i|}{\d n\over r^2\d\Omega} = {r^2\over|{\bf j}_i|}{\d n\over \d S} = {r^2\over|{\bf j}_i|}\,{\bf j}_o\cdot {\bf n} = {r^2\over|{\bf j}_i|}\,{\bf j}_o\cdot {\bf \hat r} =



.. math::

    = {r^2\over{\hbar k\over m}}\,{\hbar k\over m}\left({1\over r^2} +{i\over k r^3}\right)|f(\theta, \phi)|^2 = \left(1 +{i\over k r}\right)|f(\theta, \phi)|^2 \to |f(\theta, \phi)|^2


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

    =\int\d^3r e^{i({\bf k}-{\bf k'})\cdot{\bf r}}V({\bf r}) +\int\d^3r\d^3r'e^{-i{\bf k'}\cdot{\bf r}} V({\bf r}) {e^{i k|{\bf r}-{\bf r'}|}\over|{\bf r}-{\bf r'}|} V({\bf r'})e^{i{\bf k}\cdot{\bf r'}}+\cdots=


The Born approximation is just the first term: 

.. math::

    \braket{{\bf k'}|T|{\bf k}} \approx\int\d^3r e^{i({\bf k}-{\bf k'})\cdot{\bf r}}V({\bf r}) =\int \d r\, \d\theta\,\d\phi\, e^{iqr\cos\theta}V(r) r^2\sin\theta =



.. math::

    =4\pi\int_0^\infty rV(r)\sin(qr)\,\d r


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



.. math::

    [A_\mu]={[\phi]\over [c]}=\rm{V\,s\over m} = {kg\, m\over A\,s^2}=M



.. math::

    [c]=\rm {m\over s} = 1



.. math::

    [e]=\rm C = A\, s=1



.. math::

    [\hbar]=\rm J\,s = {m^2\,kg\over s}=1



.. math::

    [\partial_\mu]=\rm {1\over m}=M



.. math::

    [F_{\mu\nu}]=[\partial_\mu A_\nu]=\rm {kg\over A\,s^2}=M^2



.. math::

    [\L]=[F_{\mu\nu}]^2=\rm {kg^2\over A^2\,s^4}=M^4



.. math::

    [\psi]=\rm {kg^{1\over2}\over A\,m\,s}=M^{3\over2}


The SI units are useful for checking that the $c$, $e$ and $\hbar$ constants are at correct places in the expression.

.. index::
    pair: tensors; QFT

Tensors in QFT
--------------

In general, the covariant and contravariant vectors and tensors work just like in general relativity. We use the metric $g_{\mu\nu}={\rm diag}(1, -1, -1, -1)$ (e.g. signature -2, but it's possible to also use the metric with signature +2). The four potential $A^\mu$ is given by: 

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

Gradient is defined as:

.. math::

    \partial_\mu = (\partial_0, \partial_1, \partial_2, \partial_3)= \left({1\over c}{\partial\over\partial t},{\partial\over\partial x},{\partial\over\partial y},{\partial\over\partial z}\right)


the upper indices depend on the signature, e.g. for -2: 

.. math::

    \partial^\mu = (\partial^0, \partial^1, \partial^2, \partial^3)= \left({1\over c}{\partial\over\partial t},-{\partial\over\partial x},-{\partial\over\partial y},-{\partial\over\partial z}\right)


and +2: 

.. math::

    \partial^\mu = (\partial^0, \partial^1, \partial^2, \partial^3)= \left(-{1\over c}{\partial\over\partial t},{\partial\over\partial x},{\partial\over\partial y},{\partial\over\partial z}\right)



Momentum (${\bf p}=-i\hbar\nabla$) and energy ($E=i\hbar{\partial\over\partial t}$) is combined into 4-momentum as 

.. math::

    p^\mu = \left({E\over c},{\bf p}\right) = i\hbar\left({1\over c}{\partial\over\partial t},-\nabla\right) = i\hbar\left(\partial_0,-\partial_j\right) = i\hbar\left(\partial^0,\partial^j\right) = i\hbar\partial^\mu



.. math::

    p_\mu = g_{\mu\nu}p^\nu = i\hbar\left(\partial^0,-\partial^j\right) = i\hbar\left(\partial_0,\partial_j\right) = i\hbar\partial_\mu

For $p^2$ we get:

.. math::

    p^2 = p_\mu p^\mu = (p^0)^2 - {\bf p}^2 = (p_0)^2 - {\bf p}^2
    = {E^2\over c^2} - {\bf p}^2

the following relations are also useful:

.. math::

    p^2 = p_\mu p^\mu = -\hbar^2\partial_\mu \partial^\mu \equiv
    -\hbar^2\partial^2
    = -\hbar^2\left(\partial_0\partial^0 + \partial_i\partial^i\right)
    = -\hbar^2\left(\partial_0\partial_0 - \partial_i\partial_i\right)
    =

    = -\hbar^2\left({1\over c^2}{\partial^2\over\partial t^2} - \nabla^2\right)
    = -{\hbar^2\over c^2}{\partial^2\over\partial t^2} + \hbar^2\nabla^2

Now if the particle is not moving (${\bf p} = 0$), then it's energy $E=mc^2$,
where $m$ is the rest mass, so $|p| = {E\over c}= mc$, from which:

.. math::

    E^2 = p^2c^2 + {\bf p}^2c^2 = m^2c^4 + {\bf p}^2c^2

    E = \sqrt{m^2c^4 + {\bf p}^2c^2}
    = mc^2\sqrt{1 + {{\bf p}^2\over m^2c^2}}
    = mc^2\left(1 + {{\bf p}^2\over 2m^2c^2} + O\left({p^4\over m^4c^4}\right)
        \right)
    =

    = mc^2 + {{\bf p}^2\over 2m} + O\left(p^4\over m^3c^2\right)

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



.. math::

    {1\over |{\bf r}-{\bf r'}|} ={1\over \sqrt{({\bf r}-{\bf r'})^2}} ={1\over \sqrt{r^2-2{\bf r}\cdot {\bf r'} + r'^2}} ={1\over r\sqrt{1-2\left(r'\over r\right){\bf\hat r}\cdot {\bf\hat r'} + \left(r'\over r\right)^2}} =



.. math::

    ={1\over r}\sum_{l=0}^\infty\left(r'\over r\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =



.. math::

    ={1\over r}\left( P_0({\bf\hat r}\cdot {\bf\hat r'}) + P_1({\bf\hat r}\cdot {\bf\hat r'}){r'\over r} + P_2({\bf\hat r}\cdot {\bf\hat r'})\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =



.. math::

    ={1\over r}\left( 1 + {\bf\hat r}\cdot {\bf\hat r'} {r'\over r} + \half\left(3({\bf\hat r}\cdot {\bf\hat r'})^2-1\right)\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =



.. math::

    ={1\over r} +{{\bf r}\cdot {\bf r'}\over r^3} +{3({\bf r}\cdot {\bf r'})^2-r^2r'^2\over 2r^5} + O\left(r'^3\over r^4\right)


We can also use the formula: 

.. math::

    \sum_m \braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r}'}={4\pi\over 2l+1} \braket{{\bf\hat r}\cdot{\bf\hat r'}|P_l}


and rewrite the expansion using spherical harmonics: 

.. math::

    {1\over |{\bf r}-{\bf r'}|} ={1\over r}\sum_{l=0}^\infty\left(r'\over r\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'}) =



.. math::

    ={1\over r}\sum_{l,m}\left(r'\over r\right)^l {2l+1\over4\pi}\braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r}'} ={1\over r}\sum_{l,m}\left(r'\over r\right)^l {2l+1\over4\pi}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')
