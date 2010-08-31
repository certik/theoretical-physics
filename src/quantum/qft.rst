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



The free parameters are $g$, $\theta_W$, $v$, $\lambda$, $h_e$, $h_\mu$,
$h_\tau$.

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

    m_Z = {gv\over2\cos\theta_W}={m_W\over\cos\theta_W}

    m_H = v\sqrt{2\lambda}

    m_e = {1\over\sqrt2}h_ev

    m_\mu = {1\over\sqrt2}h_\mu v

    m_\tau = {1\over\sqrt2}h_\tau v

Note that those are the bare masses (e.g. in order to obtain the real mesaured
masses of the particles, one has to renormalize them by calculating the higher
order corrections given by the loop diagrams).


.. index:: quarks

Parameters of the Standard Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The free parameters are $g$, $\theta_W$, $v$, $\lambda$, then three masses of
the charged leptons $h_e$, $h_\mu$, $h_\tau$, six quark masses and four
parameters of the CKM mixing matrix, which gives 4 + 3 + 6 + 4 = 17 free
parameters (if one allows for three neutrino masses and the corresponding four
mixings parameters, one gets 17 + 3 + 4 = 24 free parameters).

They can be traded for other physical parameters (see below), but
their numerical values are not predicted by the theory, so they have to be
measured and their experimental values are approximately:

.. math::

    g = 0.631

    \theta_W = 28.67^\circ

    v = 246.218 {\rm\,GeV}

    0.2 < \lambda < 4.0

    h_e = 2.929\cdot 10^{-6} {\rm\,eV}

    h_\mu = 6.065\cdot 10^{-4} {\rm\,eV}

    h_\tau = 1.021\cdot 10^{-2} {\rm\,eV}

All the parameters have been measured quite exactly, except $\lambda$.

Other physical constants can then be calculated using the formulas:

.. math::

    m_W = \half g v = 77.7 {\rm\, GeV}

    m_Z = {m_W\over\cos\theta_W} = 88.6 {\rm\, GeV}

    m_H = v\sqrt{2\lambda} = \mbox{from }150 {\rm\,GeV}\mbox{ to }700 {\rm\,GeV}

    m_e = {1\over\sqrt2}h_ev = 511{\rm\,KeV}

    m_\mu= {1\over\sqrt2}h_\mu v = 105.6{\rm\,MeV}

    m_\tau= {1\over\sqrt2}h_\tau v = 1.777{\rm\,GeV}

    G_F = {1\over\sqrt{2} v^2} = (1.16639 \pm 0.00001) \times 10^{-5}
        {\rm\, GeV^{-2}}

    e = g \sin\theta_W = 0.3

    \alpha = {1\over 4\pi} g^2 \sin^2 \theta_W \doteq {1\over 137}

Code::

    >>> from math import pi, sin, cos, sqrt
    >>> eV = 1
    >>> KeV = 1e3
    >>> MeV = 1e6
    >>> GeV = 1e9
    >>> g = 0.631
    >>> theta_W = 28.67 * pi / 180
    >>> v = 246.218 * GeV
    >>> h_e = 2.935 * 1e-6 * eV
    >>> h_mu = 6.065 * 1e-4 * eV
    >>> h_tau = 1.021 * 1e-2 * eV
    >>> g*v/2 / GeV
    77.681779
    >>> g*v/2/cos(theta_W) / GeV
    88.5365869768
    >>> h_e * v / sqrt(2) / KeV
    510.99059521630568
    >>> h_mu * v / sqrt(2) / MeV
    105.59311618353983
    >>> h_tau * v / sqrt(2) / GeV
    1.7775856821664329
    >>> 1./sqrt(2)/v**2 / (1e-5 * GeV**-2)
    1.1663943402665491
    >>> g*sin(theta_W)
    0.30273118431564783
    >>> 1. / (g**2*sin(theta_W)**2/(4*pi))
    137.11833915409719


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
        i\int\d^4 x e^{ikx}\left(\partial^2+m^2\right)\phi(x)
        ={k^2-m^2\over i}\tilde\phi(-k)
        ={1\over\tilde D(k)}\tilde\phi(-k)

    a_{\bf k}\,{}_\text{out} \to
        i\int\d^4 x e^{-ikx}\left(\partial^2+m^2\right)\phi(x)
        ={k^2-m^2\over i}\tilde\phi(k)
        ={1\over\tilde D(k)}\tilde\phi(k)

    b^{s\dag}_{\bf k}\,{}_\text{in} \to
        i\int\d^4 x\bar\psi(x) \left(i\overleftarrow{\fslash\partial}+m\right)u^s({\bf k})e^{ikx}
        =\tilde{\bar\psi}(-k){-\fslash k - m\over i}u^s({\bf k})
        =\tilde{\bar\psi}(-k){1\over\tilde S(-k)}u^s({\bf k})

    b^s_{\bf k}\,{}_\text{out} \to
        i\int\d^4 x e^{-ikx}\bar u^s({\bf k})\left(-i\fslash\partial+m\right)\psi(x)
        =\bar u^s({\bf k}){\fslash k - m\over i}\psi(k)
        =\bar u^s({\bf k}){1\over\tilde S(k)}\psi(k)

    d^{s\dag}_{\bf k}\,{}_\text{in} \to
        -i\int\d^4 x e^{ikx}\bar v^s({\bf k})\left(-i\fslash\partial+m\right)\psi(x)
        =-\bar v^s({\bf k}){\fslash k - m\over i}\psi(-k)
        =-\bar v^s({\bf k}){1\over\tilde S(k)}\psi(-k)

    d^s_{\bf k}\,{}_\text{out} \to
        -i\int\d^4 x\bar\psi(x) \left(i\overleftarrow{\fslash\partial}+m\right)v^s({\bf k})e^{-ikx}
        =-\tilde{\bar\psi}(k){-\fslash k - m\over i}v^s({\bf k})
        =-\tilde{\bar\psi}(k){1\over\tilde S(-k)}v^s({\bf k})

    a^{r\dag}_{\bf k}\,{}_\text{in} \to
        i\epsilon_\mu^{r*}({\bf k})
            \int\d^4 x e^{ikx} \partial^2 A^\mu(x)
        =
        \epsilon_\mu^{r*}({\bf k}){k^2\over i}
            \tilde A^\mu(-k)

    a^r_{\bf k}\,{}_\text{out} \to
        i\epsilon_\mu^r({\bf k})
            \int\d^4 x e^{-ikx} \partial^2 A^\mu(x)
        =
        \epsilon_\mu^r({\bf k}){k^2\over i}
            \tilde A^\mu(k)

where the "in" is the operator for $t\to -\infty$ and "out" for $t\to\infty$.
The fields $\phi(x)$, $\psi(x)$, $\bar\psi(x)$ and $A^\mu(x)$ have to be time
ordered. On the left hand side is a position space representation, the two
expressions on the right hand side are the momentum representation (the last
expression is written using the propagators), e.g. a Fourier transform, which
is essentially just the following substitutions:

.. math::

    \partial^2\to -k^2

    i\fslash\partial\to\fslash k

    e^{\pm ikx}\phi(x) \to \tilde\phi(\mp k)

    {k^2 - m^2\over i} \to {1\over\tilde D(k)}

    {\pm\fslash k - m\over i} \to {1\over\tilde S(\pm k)}

both representations are of course equivalent (but the momentum one is easier
to use, since the formulas are shorter).

For our example we get in the position space:

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
        u^{s_1}({\bf p}_1)\right]_{\alpha_1} \,e^{ip_1x_1}

    \left[\left(i\overleftarrow{\fslash\partial_2}+m\right)
        u^{s_2}({\bf p}_2)\right]_{\alpha_2} \,e^{ip_2x_2}

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
        \left(-\fslash p_{1'} +m\right)\right]_{\alpha_{1'}}

    \left[\bar u^{s_{2'}}({\bf k}_{2'})
        \left(-\fslash p_{2'} +m\right)\right]_{\alpha_{2'}}

    \tilde G^{(4)}_{\alpha_{1'} \alpha_{2'} \alpha_1 \alpha_2}
        (p_{1'}, p_{2'}, -p_1, -p_2)

    \left[\left({\fslash p_1}+m\right)
        u^{s_1}({\bf p}_1)\right]_{\alpha_1}

    \left[\left({\fslash p_2}+m\right)
        u^{s_2}({\bf p}_2)\right]_{\alpha_2}

We can get the same result much faster if we use the momentum space from the
beginning:

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

    = \braket{\Omega|T\,
        \bar u^{s_{2'}}({\bf p}_{2'}){1\over\tilde S({\bf p}_{2'})}
                \tilde\psi({\bf p}_{2'})
        \bar u^{s_{1'}}({\bf p}_{1'}){1\over\tilde S({\bf p}_{1'})}
                \tilde\psi({\bf p}_{1'})
        \tilde{\bar\psi}(-{\bf p}_1){1\over\tilde S(-{\bf p}_1)}
                u^{s_1}({\bf p}_1)
        \tilde{\bar\psi}(-{\bf p}_2){1\over\tilde S(-{\bf p}_2)}
                u^{s_2}({\bf p}_2)
        |\Omega}=

        =
        \left[\bar u^{s_{2'}}({\bf p}_{2'}){1\over\tilde S({\bf p}_{2'})}
            \right]_{\alpha_{2'}}
        \left[\bar u^{s_{1'}}({\bf p}_{1'}){1\over\tilde S({\bf p}_{1'})}
            \right]_{\alpha_{1'}}

        \braket{\Omega|T\,
            \tilde\psi_{\alpha_{2'}}({\bf p}_{2'})
            \tilde\psi_{\alpha_{1'}}({\bf p}_{1'})
            \tilde{\bar\psi}_{\alpha_1}(-{\bf p}_1)
            \tilde{\bar\psi}_{\alpha_2}(-{\bf p}_2)
        |\Omega}

        \left[{1\over\tilde S(-{\bf p}_1)} u^{s_1}({\bf p}_1)
            \right]_{\alpha_1}
        \left[{1\over\tilde S(-{\bf p}_2)} u^{s_2}({\bf p}_2)
            \right]_{\alpha_1}

This is called Lehmann-Symanzik-Zimmermann (LSZ) reduction formula.  One
obtains similar expressions for other fields as well (if there were different
creation operators between the initial and final states). All that remains is
to calculate the interacting Green functions (for which we need to know the
interaction Lagrangian). But first couple more examples:

Example 1
^^^^^^^^^

$\nu_e$ - $e$ elastic scattering:

.. math::

    \nu_e(k) + e(p) \to \nu_e(k') + e(p')

So the initial and final states are:

.. math::

    \ket{i} = b_{\bf k}^\dag b_{\bf p}^\dag\ket{\Omega}

    \ket{f} = b_{\bf k'}^\dag b_{\bf p'}^\dag\ket{\Omega}

and we get:

.. math::

    \braket{f|i} = \braket{\Omega|
        b_{{\bf p'}}
        b_{{\bf k'}}
        b_{{\bf k}}^\dag
        b_{{\bf p}}^\dag
        |\Omega}
    =\braket{\Omega|T\,
        b_{\bf p'}
        b_{\bf k'}
        b_{\bf k}^\dag
        b_{\bf p}^\dag
        |\Omega}=

    =
    \left[\bar u({\bf p'}){1\over\tilde S({\bf p'})}
        \right]
    \left[\bar u({\bf k'}){1\over\tilde S({\bf k'})}
        \right]

    \braket{\Omega|T\,
        \tilde\psi({\bf p'})
        \tilde\psi({\bf k'})
        \tilde{\bar\psi}(-{\bf k})
        \tilde{\bar\psi}(-{\bf p})
    |\Omega}

    \left[{1\over\tilde S(-{\bf k})} u({\bf k})
        \right]
    \left[{1\over\tilde S(-{\bf p})} u({\bf p})
        \right]

We only multiply the matrices with the same momentum, i.e.
$\left[\bar u^s({\bf p'}){1\over\tilde S({\bf p'})}\right]$ with
$\tilde\psi({\bf p'})$,
$\left[\bar u^s({\bf k'}){1\over\tilde S({\bf k'})}\right]$ with
$\tilde\psi({\bf k'})$ and so on. Also we don't write the spin anymore, e.g.
$u({\bf k})$ should in fact be $u^{s_k}({\bf k})$ and so on.

Example 2
^^^^^^^^^

Muon decay:

.. math::

    \mu(P) \to e(p) + \bar\nu_e(k') + \nu_\mu(k)

So the initial and final states are:

.. math::

    \ket{i} = b_{\bf P}^\dag\ket{\Omega}

    \ket{f} = b_{\bf p}^\dag d_{\bf k'}^\dag b_{\bf k}^\dag\ket{\Omega}

and we get:

.. math::

    \braket{f|i} = \braket{\Omega|
        b_{{\bf k}}
        d_{{\bf k'}}
        b_{{\bf p}}
        b_{{\bf P}}^\dag
        |\Omega}

    =
    \left[\bar u({\bf k}){1\over\tilde S({\bf k})} \right]
    \left[\bar u({\bf p}){1\over\tilde S({\bf p})} \right]

    \braket{\Omega|T\,
        \tilde\psi({\bf k})
        \tilde\psi({\bf p})
        \tilde{\bar\psi}({\bf k'})
        \tilde{\bar\psi}(-{\bf P})
    |\Omega}

    \left[-{1\over\tilde S(-{\bf k'})} v({\bf k'}) \right]
    \left[{1\over\tilde S(-{\bf P})} u({\bf P}) \right]

Example 3
^^^^^^^^^

$e^+ + e^-$ scattering:

.. math::

    e^-(p_1)+e^+(p_2) \to e^-(k_1)+e^+(k_2)

Initial and final states:

.. math::

    \ket{i} = b_{{\bf p}_1}^{t\dag} d_{{\bf p}_2}^{u\dag}\ket{\Omega}

    \ket{f} = b_{{\bf k}_1}^{r\dag} d_{{\bf k}_2}^{s\dag}\ket{\Omega}


And we get:

.. math::

    \braket{f|i}=
    \braket{\Omega|
        b^r_{{\bf k}_1}
        d^s_{{\bf k}_2}
        b^{t\dag}_{{\bf p}_1}
        d^{u\dag}_{{\bf p}_2}
        |\Omega} =

    =\braket{\Omega|T
        b^r_{{\bf k}_1}
        d^s_{{\bf k}_2}
        b^{t\dag}_{{\bf p}_1}
        d^{u\dag}_{{\bf p}_2}
        |\Omega} =

    =\braket{\Omega|T
        \left[\bar u^r({\bf k}_1){1\over\tilde S(k_1)}\tilde \psi(k_1)\right]
        \left[-\tilde{\bar\psi}(k_2){1\over\tilde S(-k_2)}v^s({\bf k}_2)\right]
        \left[\tilde{\bar\psi}(-p_1){1\over\tilde S(-p_1)}u^t({\bf p}_1)\right]
        \left[-\bar v^u({\bf p}_2){1\over\tilde S(p_2)}\tilde \psi(-p_2)\right]
        |\Omega} =

    =
    \left[\bar u^r({\bf k}_1){1\over\tilde S(k_1)}\right]
    \left[\bar v^u({\bf p}_2){1\over\tilde S(p_2)}\right]

    \braket{\Omega|T
        \tilde \psi(k_1)
        \tilde{\bar\psi}(k_2)
        \tilde{\bar\psi}(-p_1)
        \tilde \psi(-p_2)
        |\Omega}

    \left[{1\over\tilde S(-k_2)}v^s({\bf k}_2)\right]
    \left[{1\over\tilde S(-p_1)}u^t({\bf p}_1)\right]


Example 4
^^^^^^^^^

$H(p)\to Z(k)+Z(l)$ decay. Initial and final states:

.. math::

    \ket{i} = a^\dag_{\bf p}\ket{\Omega}

    \ket{f} = a^{r\dag}_{\bf k}a^{s\dag}_{\bf l}\ket{\Omega}

and we get:

.. math::

    \braket{f|i}=
    \braket{\Omega|a^r_{\bf k} a^s_{\bf l} a^\dag_{\bf p}|\Omega} =
    \braket{\Omega|T a^r_{\bf k} a^s_{\bf l} a^\dag_{\bf p}|\Omega} =

    =
    \braket{\Omega|T
        \epsilon^{r*}_\mu({\bf k}){k^2\over i} \tilde A^\mu(k)
        \epsilon^{s*}_\nu({\bf l}){l^2\over i} \tilde A^\nu(l)
        {1\over\tilde D(p)}\tilde\phi(-p)
        |\Omega} =

    = {\epsilon^{r*}_\mu({\bf k})\epsilon^{s*}_\nu({\bf l})
    \over {i\over k^2}{i\over l^2}\tilde D(p)}
    \braket{\Omega|T \tilde A^\mu(k)\tilde A^\nu(l)\tilde \phi(-p)|\Omega}

Example 5
^^^^^^^^^

$e^+ e^- \to W^+ W^-$ scattering:

.. math::

    e^-(k) + e^+(-l) \to W^-(p) + W^+(r)

So the initial and final states are:

.. math::

    \ket{i} = b_{\bf k}^\dag d_{-{\bf l}}^\dag\ket{\Omega}

    \ket{f} = a_{\bf p}^{\lambda \dag} a_{\bf r}^{\mu \dag}\ket{\Omega}

and we get:

.. math::

    \braket{f|i} = \braket{\Omega|
        a_{\bf r}^\mu
        a_{\bf p}^\lambda
        b_{\bf k}^\dag d_{-{\bf l}}^\dag
        |\Omega}

    =
    \epsilon^\mu_\alpha({\bf r}) {r^2\over i}
    \epsilon^\lambda_\beta({\bf p}) {p^2\over i}
    \left[-\bar v(-{\bf l}){1\over\tilde S(-{\bf l})} \right]

    \braket{\Omega|T\,
        \tilde A^\alpha({\bf r})
        \tilde A^\beta({\bf p})
        \tilde{\bar\psi}(-{\bf k})
        \tilde\psi({\bf l})
    |\Omega}

    \left[{1\over\tilde S(-{\bf k})} u({\bf k}) \right]

Example 6
^^^^^^^^^

$W^+ W^- \to W^+ W^-$ scattering:

.. math::

    W^-(k) + W^+(p) \to W^-(r) + W^+(l)

So the initial and final states are:

.. math::

    \ket{i} = a_{\bf k}^{\mu \dag} a_{\bf p}^{\nu \dag}\ket{\Omega}

    \ket{f} = a_{\bf r}^{\alpha \dag} a_{\bf l}^{\beta \dag}\ket{\Omega}

and we get:

.. math::

    \braket{f|i} = \braket{\Omega|
        a_{\bf l}^\beta
        a_{\bf r}^\alpha
        a_{\bf k}^{\mu \dag} a_{\bf p}^{\nu \dag}
        |\Omega}

    =
    \epsilon^{\mu*}_\rho({\bf k}) {k^2\over i}
    \epsilon^{\nu*}_\sigma({\bf p}) {p^2\over i}
    \braket{\Omega|T\,
        \tilde A^\kappa({\bf r})
        \tilde A^\lambda({\bf l})
        \tilde A^\sigma(-{\bf p})
        \tilde A^\rho(-{\bf k})
    |\Omega}
    \epsilon^\alpha_\kappa({\bf r}) {r^2\over i}
    \epsilon^\beta_\lambda({\bf l}) {l^2\over i}



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

Evaluating the Interacting Green Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Green functions below can either be evaluated using the Wick theorem, or
using Feynman diagrams and the corresponding Feynman rules.


Example 1
^^^^^^^^^

$\L_{ZZH} = \lambda Z_\mu Z^\mu H$, in the first order:

.. math::

    \braket{\Omega|T \tilde A^\mu(k)\tilde A^\nu(l)\tilde \phi(-p)|\Omega}
    =i\lambda (2\pi)^4 \delta(k+l-p) \tilde D^\mu{}_\alpha(k)
        \tilde D^{\nu\alpha}(l)\tilde D(p)

Example 2
^^^^^^^^^

$\L_{ee\gamma}=-\lambda \bar e\gamma^\mu e A_\mu$, in the second order:

.. math::

    \braket{\Omega|T\tilde\psi(k_1)\tilde{\bar\psi}(k_2)\tilde{\bar\psi}(-p_1)
        \tilde\psi(-p_2) |\Omega}
    =

    =(-i\lambda)^2(2\pi)^4\delta(k_1+k_2-p_1-p_2)\left[
        \tilde S(k_1)\gamma^\mu\tilde S(-k_2)
        D_{\mu\nu}(k_1+k_2)
        \tilde S(p_2)\gamma^\nu\tilde S(-p_1)
        +\right.

        \left. +
        \tilde S(k_1)\gamma^\mu\tilde S(-p_1)
        D_{\mu\nu}(k_1-p_1)
        \tilde S(p_2)\gamma^\nu\tilde S(-k_2)\right]

Example 3
^^^^^^^^^

$\L_{\rm int}={g\over 2 \sqrt 2} \bar\nu_e \gamma^\mu (1-\gamma_5) e
W_\mu^+ + \hbox{h.c.}$, in the second order:

.. math::

    \braket{\Omega|T\tilde A^\alpha(r) \tilde A^\beta(p)
        \tilde{\bar\psi}(-k)\tilde{\psi}(-l)
        |\Omega}
        =

    =\int \d^4x\,\d^4 y
    \bra{0}T\tilde A^\alpha(r) \tilde A^\beta(p)
        \tilde{\bar\psi}(-k)\tilde{\psi}(-l)

        i{g\over 2 \sqrt 2}\bar\nu_e(x) \gamma^\mu (1-\gamma_5) e(x) W_\mu^+(x)

        i{g\over 2 \sqrt 2}\bar\nu_e(y) \gamma^\nu (1-\gamma_5) e(y) W_\nu^+(y)

        \ket{0}
        =

    =\left(i{g\over 2 \sqrt 2}\right)^2
    \int \d^4x\,\d^4 y \,\d\hat r\,\d\hat p\,\d\hat k\,\d\hat l\,
    e^{i(\hat rr + \hat pp - \hat kk - \hat ll)}

    \bra{0}T A^\alpha(\hat r) A^\beta(\hat p)
        {\bar\psi}(\hat k){\psi}(\hat l)

        \bar\nu_e(x) \gamma^\mu (1-\gamma_5) e(x) W_\mu^+(x)

        \bar\nu_e(y) \gamma^\nu (1-\gamma_5) e(y) W_\nu^+(y)

        \ket{0}
        =

    =\left(i{g\over 2 \sqrt 2}\right)^2
    \int \d^4x\,\d^4 y \,\d\hat r\,\d\hat p\,\d\hat k\,\d\hat l\,
    e^{i(\hat rr + \hat pp - \hat kk - \hat ll)}

    D^\alpha{}_\mu(\hat r - x) D^\mu{}_\nu(\hat p - y)
    S(\hat l - x) \gamma^\mu (1-\gamma_5)S(x-y)\gamma^\nu(1-\gamma_5)
    S(\hat k - y)
        =

    =\left(i{g\over 2 \sqrt 2}\right)^2
    \int \d^4x\,\d^4 y \,\d\hat r\,\d\hat p\,\d\hat k\,\d\hat l\,
    e^{i((\hat r+x)r + (\hat p+y)p - (\hat k+y)k - (\hat l+x)l)}

    D^\alpha{}_\mu(\hat r) D^\mu{}_\nu(\hat p)
    S(\hat l) \gamma^\mu (1-\gamma_5)S(x-y)\gamma^\nu(1-\gamma_5)
    S(\hat k)
        =

    =\left(i{g\over 2 \sqrt 2}\right)^2
    \int \d^4x\,\d^4 y \,
    e^{i(xr + yp - yk - xl)}

    \tilde D^\alpha{}_\mu(r) \tilde D^\mu{}_\nu(p)
    \tilde S(l) \gamma^\mu (1-\gamma_5)S(x-y)\gamma^\nu(1-\gamma_5)
    \tilde S(k)
        =

    =\left(i{g\over 2 \sqrt 2}\right)^2
    \int \d^4x\,\d^4 y \,
    e^{i((x+y)r + yp - yk - (x+y)l)}

    \tilde D^\alpha{}_\mu(r) \tilde D^\mu{}_\nu(p)
    \tilde S(l) \gamma^\mu (1-\gamma_5)S(x)\gamma^\nu(1-\gamma_5)
    \tilde S(k)
        =

    =\left(i{g\over 2 \sqrt 2}\right)^2
    \int \d^4 y \,
    e^{i(yr + yp - yk - yl)}

    \tilde D^\alpha{}_\mu(r) \tilde D^\mu{}_\nu(p)
    \tilde S(l) \gamma^\mu (1-\gamma_5)\tilde S(r-l)\gamma^\nu(1-\gamma_5)
    \tilde S(k)
        =

    = \left(i{g\over 2 \sqrt 2}\right)^2
        (2\pi)^4\delta(r+p-k-l)
        \tilde D^\alpha{}_\mu(r) \tilde D^\beta{}_\nu(p)\tilde S(l)
        \gamma^\mu(1-\gamma_5) \tilde S(r-l) \gamma^\nu(1-\gamma_5)\tilde S(k)

ZZH interaction
~~~~~~~~~~~~~~~

Let's calculate the $\L_{ZZH}=\lambda Z_\mu Z^\mu H$ interaction in the SM,
where $\lambda={g^2\over4\cos\theta_W}$. Consider $H(p)\to Z(k)+Z(l)$:

.. math::

    \braket{f|S|i}= \braket{f|iT|i}= \braket{k l|iT|p}=
    \braket{\Omega|a^r_{\bf k} a^s_{\bf l} a^\dag_{\bf p}|\Omega} =
    \braket{\Omega|T a^r_{\bf k} a^s_{\bf l} a^\dag_{\bf p}|\Omega} =

    =
    \braket{\Omega|T
        \epsilon^{r*}_\mu({\bf k}){k^2\over i} \tilde A^\mu(k)
        \epsilon^{s*}_\nu({\bf l}){l^2\over i} \tilde A^\nu(l)
        {1\over\tilde D(p)}\tilde\phi(-p)
        |\Omega} =

    = {\epsilon^{r*}_\mu({\bf k})\epsilon^{s*}_\nu({\bf l})
    \over {i\over k^2}{i\over l^2}\tilde D(p)}
    \braket{\Omega|T \tilde A^\mu(k)\tilde A^\nu(l)\tilde \phi(-p)|\Omega}

    = {\epsilon^{r*}_\mu({\bf k})\epsilon^{s*}_\nu({\bf l})
    \over {i\over k^2}{i\over l^2}\tilde D(p)}
    i\lambda (2\pi)^4 \delta(k+l-p) \tilde D^\mu{}_\alpha(k)
        \tilde D^{\nu\alpha}(l)\tilde D(p)

    = {\epsilon^{r*}_\mu({\bf k})\epsilon^{s*}_\nu({\bf l})
    \over {i\over k^2}{i\over l^2}\tilde D(p)}
    i\lambda (2\pi)^4 \delta(k+l-p)
        {-ig^\mu{}_\alpha\over k^2}
        {-ig^{\nu\alpha}\over l^2}
        \tilde D(p)

    = \epsilon^{r*}_\mu({\bf k})\epsilon^{s*}_\nu({\bf l})
    i\lambda (2\pi)^4 \delta(k+l-p)
        g^\mu{}_\alpha
        g^{\nu\alpha}

    = \epsilon^{r*}_\mu({\bf k})\epsilon^{s*}_\nu({\bf l})
    i\lambda (2\pi)^4 \delta(k+l-p) g^{\mu\nu}

    = i\lambda (2\pi)^4 \delta(k+l-p)
        \epsilon^{r*}_\mu({\bf k})\epsilon^{s\mu*}({\bf l})

where we used the fact, that the first order contribution of the $\lambda Z_\mu
Z^\mu H$ interaction to the interacting Green function is:

.. math::

    \braket{\Omega|T \tilde A^\mu(k)\tilde A^\nu(l)\tilde \phi(-p)|\Omega}
    =i\lambda (2\pi)^4 \delta(k+l-p) \tilde D^\mu{}_\alpha(k)
        \tilde D^{\nu\alpha}(l)\tilde D(p)


eeH interaction
~~~~~~~~~~~~~~~

This is only approximate, it will be fixed soon.

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

This is only approximate, it will be fixed soon.

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

Let's calculate the $\L_{ee\gamma}=-\lambda \bar e\gamma^\mu e A_\mu$
interaction in the SM, where $\lambda=g\sin\theta_W$. Consider
$e^-(p_1)+e^+(p_2)\to\gamma(q)\to e^-(k_1)+e^+(k_2)$:

.. math::

    \braket{f|S|i}= \braket{f|iT|i}= \braket{k_1 k_2|iT|p_1p_2}=
    \braket{\Omega|
        b^r_{{\bf k}_1}
        d^s_{{\bf k}_2}
        b^{t\dag}_{{\bf p}_1}
        d^{u\dag}_{{\bf p}_2}
        |\Omega} =

    =\braket{\Omega|T
        b^r_{{\bf k}_1}
        d^s_{{\bf k}_2}
        b^{t\dag}_{{\bf p}_1}
        d^{u\dag}_{{\bf p}_2}
        |\Omega} =

    =\braket{\Omega|T
        \left[\bar u^r({\bf k}_1){1\over\tilde S(k_1)}\tilde \psi(k_1)\right]
        \left[-\tilde{\bar\psi}(k_2){1\over\tilde S(-k_2)}v^s({\bf k}_2)\right]
        \left[\tilde{\bar\psi}(-p_1){1\over\tilde S(-p_1)}u^t({\bf p}_1)\right]
        \left[-\bar v^u({\bf p}_2){1\over\tilde S(p_2)}\tilde \psi(-p_2)\right]
        |\Omega} =

    =
    \left[\bar u^r({\bf k}_1){1\over\tilde S(k_1)}\right]
    \left[\bar v^u({\bf p}_2){1\over\tilde S(p_2)}\right]

    \braket{\Omega|T
        \tilde \psi(k_1)
        \tilde{\bar\psi}(k_2)
        \tilde{\bar\psi}(-p_1)
        \tilde \psi(-p_2)
        |\Omega}

    \left[{1\over\tilde S(-k_2)}v^s({\bf k}_2)\right]
    \left[{1\over\tilde S(-p_1)}u^t({\bf p}_1)\right]
    =

    =
    \left[\bar u^r({\bf k}_1){1\over\tilde S(k_1)}\right]
    \left[\bar v^u({\bf p}_2){1\over\tilde S(p_2)}\right]

    (-i\lambda)^2(2\pi)^4\delta(k_1+k_2-p_1-p_2)\left[
        \tilde S(k_1)\gamma^\mu\tilde S(-k_2)
        D_{\mu\nu}(k_1+k_2)
        \tilde S(p_2)\gamma^\nu\tilde S(-p_1)
        +\right.

        \left. +
        \tilde S(k_1)\gamma^\mu\tilde S(-p_1)
        D_{\mu\nu}(k_1-p_1)
        \tilde S(p_2)\gamma^\nu\tilde S(-k_2)\right]

    \left[{1\over\tilde S(-k_2)}v^s({\bf k}_2)\right]
    \left[{1\over\tilde S(-p_1)}u^t({\bf p}_1)\right]
    =

    =
    -\lambda^2(2\pi)^4\delta(k_1+k_2-p_1-p_2)\left[
        \bar u^r({\bf k}_1)\gamma^\mu v^s({\bf k}_2)
        {1\over (k_1+k_2)^2}
        \bar v^u({\bf p}_2)\gamma_\mu u^t({\bf p}_1)
        +\right.

        \left. +
        \bar u^r({\bf k}_1)\gamma^\mu u^t({\bf p}_1)
        {1\over (k_1-p_1)^2}
        \bar v^u({\bf p}_2)\gamma_\mu v^s({\bf k}_2)
        \right]


where we used the fact, that the interacting Green function is in the lowest
nonzero order equal to:

.. math::

    \braket{\Omega|T\tilde\psi(k_1)\tilde{\bar\psi}(k_2)\tilde{\bar\psi}(-p_1)
        \tilde\psi(-p_2) |\Omega}
    =

    =(-i\lambda)^2(2\pi)^4\delta(k_1+k_2-p_1-p_2)\left[
        \tilde S(k_1)\gamma^\mu\tilde S(-k_2)
        D_{\mu\nu}(k_1+k_2)
        \tilde S(p_2)\gamma^\nu\tilde S(-p_1)
        +\right.

        \left. +
        \tilde S(k_1)\gamma^\mu\tilde S(-p_1)
        D_{\mu\nu}(k_1-p_1)
        \tilde S(p_2)\gamma^\nu\tilde S(-k_2)\right]



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


but this matrix element can be derived directly from the Lagrangian:

.. math::

    \L = -{G_\mu\over\sqrt2} [\bar \psi_{\nu_\mu}\gamma^\mu (1-\gamma_5) \psi_\mu] [\bar \psi_e\gamma^\mu (1-\gamma_5) \psi_{\nu_e}]


with

.. math::

    {G_\mu\over\sqrt2} = {g^2\over8m_W^2}


This is the universal V-A theory Lagrangian (after adding the h.c. term). Note
that the Fermi constant $G_F$ is equal to $G_\mu$.

For the beta decay we get:

.. math::

    \L = -{G_\beta\over\sqrt2} [\bar \psi_p\gamma^\mu (1-f\gamma_5) \psi_n] [\bar \psi_e\gamma^\mu (1-\gamma_5) \psi_{\nu_e}]

where $G_\beta = G_F \cos\theta_C$, $\theta_C=13^\circ$ is the Cabibbo
angle and $f\doteq 1.26$.
