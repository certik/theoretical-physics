Groups
======

These are notes of Karel Výborný and Ondřej Čertík on the group theory as a
result of the first VDNK (Výprava do neznámých krajů) held between October 30
and November 2, 2006 in Prague.  So that the next time we look at it we should
be able to quickly recover our forgotten ideas.

Theory
------

Definition of a group:

    * I1: $x,y \in G  \Rightarrow  xy \in G$
    * I2: there exist $e$ such that $ex=xe=x$ for each $x\in G$
    * I3: there exist $x^{-1}$ such that $xx^{-1}=x^{-1}x=e$ for each $x\in G$
    * I4: $(xy)z=x(yz)$ for each $x,y,z\in G$

Every finite group is isomorphic to a subgroup of $S_n$ (permutations).

Representation
~~~~~~~~~~~~~~

Set of linear operators $T(x)$ (for each $x\in G$ there is one $T(x)$)

.. math::

    T(x)T(y)=T(xy),\quad T(e)={\hbox{\dsrom 1}}\,.

$T(x)$ fulfills all the group axioms I1, I2, I3, I4. The requirement $T(e)=1$ is
non-trivial, consider for example the following 4 matrices

.. math::

    T(\bsigma)=\begin{pmatrix}
        \bsigma & 0 \\
        0       & 0 \\
                \end{pmatrix}, \quad T(e)=\begin{pmatrix}
                    \hbox{\dsrom 1} & 0 \\
                    0               & 0 \\
                                \end{pmatrix}\,,

that fulfill $T(x)T(y)=T(xy)$ but not $T(e)={\hbox{\dsrom 1}}$.

The representation $T(x)$ is said to be *faithful* if there is a one-to-one
relationship between $T(x)$ and $x$ (an isomorphism).

Equivalent representations $T_1$ and $T_2$: there exist $S$ such that
$T_2=ST_1(x)S^{-1}$ for each $x\in G$.

Reducible representation $T(x)$: there exist an equivalent representation that
is diagonal:

.. math::
    :label: eq-1-1

    T'(x)=ST(x)S^{-1}=\begin{pmatrix}
        T_1' & 0 \\
        0    & T_2' \\
        \end{pmatrix}\,, \qquad \forall x\in G\,.

We say that $T'$ is a direct sum of $T_1'$ and $T_2'$: $T'=T_1'\oplus T_2'$.

Irreducible representation: is not reducible.

Conjugate element: $x$ is conjugate to $y$ ($x\sim y$) if there exist $c$ such that:

.. math::

    x=cyc^{-1}

if $x\sim y$ and $y\sim z$ then $x\sim z$.

Conjugate class: elements which are all conjugate to each other

No element may belong to more than one class $\Rightarrow$ every group may be
broken up into separate classes.

Character $\chi$ of the representation $T(x)$: set of numbers $\chi(x)=\Tr
T(x)$ as the group element $x$ runs through the group.

Equivalent representations have the same character:

.. math::

    \chi'(x)=\Tr T'(x)=\Tr ST(x)S^{-1}=\Tr T(x)=\chi(x)

Representations having the same character are equivalent.

Proof: Characters can be thought of as elements of a q-dimensional vector space
where q is the number of conjugacy classes. Using the orthogonality relations
derived above, we find that the q characters for the q inequivalent irreducible
representations forms a basis set. Also, according to Maschke's theorem, both
representations can be expressed as the direct sum of irreducible
representations. Since the character of the direct sum of representations is
the sum of their characters, from linear algebra, we see they are equivalent.

All the elements in the same class have the same character.

Maschke's theorem: for finite groups, every class of equivalent representations
contains unitary representations. The theorem is also true for most infinite
groups of interest in physics.

Let $T$ be a reducible representation, then:

.. math::

    T=m_1T^{(1)} \oplus m_2T^{(2)} \oplus m_3T^{(3)}\oplus \cdots

where $T^{(1)}$, $T^{(2)}$, $T^{(3)}$ \dots are all the inequivalent
irreducible representations and $m_\alpha$ ($\alpha=1,2,3,\dots$) gives the
number of times that the irreducible representation $T^{(\alpha)}$ occurs in
the reduction.

Similar relation holds for group characters:

.. math::

    \chi=m_1\chi^{(1)} + m_2\chi^{(2)} + m_3\chi^{(3)} + \cdots

and it can be shown [Elliott]_ (eq. 4.28, page 63):

.. math::

    m_\alpha={1\over g}\sum_{x\in G} \chi^{(\alpha)*}(x)\chi^{(\alpha)}(x)=

    = {1\over g}\sum_{p} c_p\chi^{(\alpha)*}_p\chi^{(\alpha)}_p

where $c_p$ is the number of elements in the class $p$, $g$ is the number of
elements in $G$ (the order of the group).


Other facts
~~~~~~~~~~~

Number of irreducible representations $=$ the number of classes.

Regular representation of $G$:
    Take $R^n$ with $n=\# G$ and assign a canonical basis to the elements $g_i$
    of $G$. A matrix $A_a$ assigned to $a\in G$ now describes the mapping
    $(g_1,g_2,\ldots)\mapsto (ag_1,ag_2,\ldots)$, i.e. in if $ag_1=g_5$, then
    the fifth element of the first row is one and others of that row are zero
    in $A_a$. Each IR of the reg. rep. occurs in its decomposition with the
    multiplicity equal to its dimension. Thus (p. 65, [Sternberg]_)

        .. math::

            \# G = \sum p_i^2\,.

Schur's lemma
    (a) Be $r$ an IR of $G$. If $[r(a),T]=0$, $\forall a\in G$, then
    $T=cI$.

    (b) Be $r_1$, $r_2$ two inequivalent IRs of $G$. Then
    $r_1(a)T=Tr_2(a)$ valid $\forall a\in G$ implies $T=0$. See p. 55 in
    [Sternberg]_. This can be used to derive the orthogonality relations for
    characters.

Complete reducibility
    Every rep can be decomposed into IRs: true for finite
    (p. 52) and compact (p. 179 in [Sternberg]_) groups. Counterexample for
    larger groups, p. 53.

Sum of reps.
    Opposite process to reduction, $\rho\oplus\sigma$, it
    lives on the direct sum of the two vector spaces of $\rho$ and $\sigma$.

Take an IR $\rho$ of $G$. Then $\rho$ will also be a rep. of any subgroup
$H\subset G$, but it need not be an IR, because the condition for
reducibility, Eq. :eq:`eq-1-1`, is less strict: it suffices if the matrices
$T(g)$ are simultaneously block diagonal only for $g\in H$, not for all $g\in
G$. This is called *restriction* and it is denoted by $\downarrow$.

*Induced representation*, denoted by $\uparrow$, is an opposite of the
restriction. It works as follows: if $F=G\otimes H$, then
$\rho(f)=\rho(g)$, when $f=g\otimes h$.

*Product of representations*, $\rho\otimes\sigma$ lives on the direct product
of the two vector spaces. Product of IRs need not be an IR. Most prominent
example: adding of angular momenta.





Interesting examples
~~~~~~~~~~~~~~~~~~~~

$O$ and $T_d$ (see :ref:`point_groups`) are isomorphic to $S_4$ (p. 35
in [Sternberg]_). Written as matrices in 3D,
they are 3D representations. Since $O$ has only $\det A=1$ matrices unlike
$T_d$, they are inequivalent.

Homeomorphism of $SL(2,C)$ into the Lorentz group [or $SU(2)$ into $SO(3)$],
p. 7 [Sternberg]_}. Start with the following $1-1$ correspondence between
$\vec{x}$ and $x$:

.. math::

  \vec{x}=(x_0,x_1,x_2,x_3)^T\,,\qquad
  x=\begin{pmatrix}
    x_0+x_3  & x_1-ix_2 \\
    x_1+ix_2 & x_0-x_3
    \end{pmatrix}\,.

For any matrix of $A\in SL(2,C)$ take $AxA^*=x'$. Decode $x'$ into $\vec{x}'$
and the relation between $\vec{x}$ and $\vec{x}'$ defines uniquely a Lorentz
transformation; thus $A$ was mapped into some Lorentz group element. If
$x_0=0$ this gives a mapping from $SU(2)$ into $SO(3)$. The mapping is $2-1$
because $A$ and $-A$ give the same $x'$.

$SO(3)$ is not simply connected. Consider matrices
$U_{\theta}=diag(e^{-i\theta}, e^{i\theta})\in SU(2)$, $\theta\in[0,\pi]$.
These map into $SO(3)$ rotations by $2\theta$ around the $z$--axis. These
matrices $A_\theta=R_{z,2\theta}$ in $SO(3)$ form a closed loop,
$R_{z,0}=R_{z,2\pi}$. If $SO(3)$ were simply connected it would be possible to
contract this loop into a point while keeping $A_0$ and $A_\pi$ unchanged. But
then the same would have to happen with the original curve of matrices
$U_\theta$ while keeping $U_0$ and $U_\pi$ at their place. Since
$U_{\pi}=-I\not= U_0=I$, this curve is not closed and such a contraction is
not possible.

All IRs of $S_3$ are in [Sternberg]_, p. 57.

.. _point_groups:

Crystallographic Point Groups
-----------------------------

Point group is a subgroup of O(3).

Crystallographic point groups are all subgroups of $O(3)$, which leave a
monoatomic crystal lattice invariant. Those can be symmetries of an infinite
crystal (e.g. $C_5$ is excluded since pentagons cannot cover the plane).

There are only 7 crystallographic point groups: $S_2$ (triclinic),
$C_{2h}$ (monoclinic), $D_{2h}$ (orthorhombic), $D_{3d}$ (rhombohedral),
$D_{4h}$ (tetragonal), $D_{6h}$ (hexagonal) and $O_{h}$ (cubic).

For simple monoatomic crystals with one atom per unit cell these seven are the
only possible crystallographic point groups. For more complicated crystals
with a molecule or an arrangement of atoms in the unit cell, the symmetry will
be reduced to the subgroup which leaves not only the lattice but also the unit
cell invariant.

The complete list of all possible crystallographic point groups will therefore
be given by the above seven together with all their subgroups
(Tab. 3 in [Birss]_ or Tab. 4 in [Sternberg]_):

.. math::

    \begin{array}{cc}
    S_2    & C_{1h}, S_2 \\
    C_{2h} & C_2, C_{1h}, C_{2h} \\
    D_{2h} & D_2, C_{2v}, D_{2h} \\
    D_{3d} & C_3, S_6, D_3, C_{3v}, D_{3d} \\
    D_{4h} & C_4, S_4, C_{4h}, D_4, C_{4v}, D_{2d}, D_{4h} \\
    D_{6h} & C_3, S_6, D_3, C_{3v}, D_{3d}, C_6, C_{3h}, C_{6h}, D_6, C_{6v},
        D_{3h}, D_{6h} \\
    O_h    & T, T_h, O, T_d, O_h \\
    \end{array}

There are 37 subgroups together. $D_{3d}$ is a subgroup of $D_{6h}$ (so all
5 subgroups of $D_{3d}$ are also subgroups of $D_{6h}$).
Together we get 37-5 = 32
distinct subgroups. Groups, which might at first sight appear to be missing
from the list are $C_{1v}$, $D_1$, $D_{1h}$, $S_1$, and $S_3$, but these are
the same as $C_{1h}$, $C_2$, $C_{2v}$, $C_{1h}$ and $C_{3h}$ respectively.

The following groups are isomorphic:

$C_{1h}$, $S_2$, $C_2$

$S_4$, $C_4$

$S_6$, $C_{3h}$, $C_6$

$C_{2h}$, $C_{2v}$, $D_2$

$C_{3v}$, $D_3$

$D_{2d}$, $C_{4v}$, $D_4$

$D_{3d}$, $D_{3h}$, $C_{6v}$, $D_6$

$T_d, O$




The way to derive the above lists is the following.

Procedure:

#. Find all finite crystallographic subgroups of $SO(3)$ called
   *rotation subgroups*
#. Take each subgroup from 1) and add $-I$ and
   close the subgroup ('non-rot containing $-I$')
#. for each subgroup $G^\wedge$ in 1), find whether it has some normal
   subgroups $G^+$ of index 2 (half a size of $G^\wedge$) and construct
   $G^+\cup (-I)aG^+$, where $a\notin G^+$ and $a\in G^\wedge$; this will be a
   'non-rot not containing $-I$' (for each $G^\wedge$ there can be zero, one or
   more such $G^+$).

The sum of 1.,2.,3. are all finite crystallographic groups
of $O(3)$.  The procedure is described in [Sternberg]_, p. 28-40.

An example: $O$ (all rot. symm. of a cube, i.e. no mirroring) is 1), $O^h$
(all symm. of a cube) is 2) made of $O$ and $T_d$ (all symm. of a tetrahedron)
is 3) made of 1).



Zoology
~~~~~~~

Schönflies notation: $C_n$ is an $n$--fold rotation ($2_z$, $3_z$ ...)
group (planar polygon), $D_n$ is a diedric group, i.e. $C_n$ plus
turn-the-page two-fold rotations (e.g. $2_x$, $2_\perp$), $T$, $O$ and $I$
(= $Y$) are the rotational symmetries of a tetrahedron, octahedron (identical
to those of a cube) and icosahedron (identical to those of a dodecahedron),
respectively. Additional indexes mean reflection planes, horizontal, vertical,
diagonal (h,v,d) or $-I$ (i). Some atypical notation: $S_2=C_i$,
$S_6=C_{3i}$, $S_4=C_{2i}$, $C_s=C_{1h}$.

Hermann--Mauguin (HM, international) notation: 2,3,4 means $C_n$, $\bar{4}$
means rotation-inversion axis (rotation followed by $-I$), $m$ is a vertical
mirror plane, $/m$ is a horizontal mirror plane.


Symmetry operations (in Table 3 of [Birss]_): like HM, $2_x$ means a
two-fold rotation around $x$--axis, $2_\perp$ means some other axis in the
$xy$ plane than $x,y$ or $xy$ (diagonal), $\bar{3}_z$ is a rotation followed
by $-I$. $3(2_\perp)$ means three different two-fold axes $2_\perp$.




Construction and usage of the character table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For simpler groups the character tables can be constructed using the following
four rules:

#. The sum of the squares of the dimensions $n_i$ of the irreducible
   representations is equal to the order $g$ of the point group:

        .. math::

            \sum_{\mu=1}^k n_\mu^2 = g

   The dimension $n_\mu$ is given by the character of the identity matrix
   (first column) $n_\mu = \chi^\mu(E)$, so the sum of squares of the first
   column is $g$. It is customary to put the characters of the one dimensional
   representation ($\chi^1(C_i)=1$) into the first row, so , so the first row
   is filled with 1s.
#. The number of irreducible representations $r$ (rows) is equal to the number
   of classes $k$ (columns)
#. The rows must satisfy

        .. math::

            \sum_{i=1}^k g_i \chi^\mu(C_i) \chi^\nu(C_i)^* = g \delta_{\mu\nu}

#. The columns must satisfy

        .. math::

            \sum_{\nu=1}^k \chi^\nu(C_i) \chi^\nu(C_j)^* = {g\over g_i}
                \delta_{ij}

There exists a systematic approach that works for any group, but it is
complicated (see for example [Dixon67]_, [Blokker72]_ and [Cannon69]_).

The notation for irreducible representation:
One-dimensional irreducible representations are labeled either $A$ or $B$
according to whether the character of a $2\pi\over n$ (proper or improper)
rotation about the symmetry axis of highest order $n$ is $+1$ or $-1$. If there
is no symmetry axis, all one-dimensional representations are labeled $A$.

For general information, see [Elliott]_ (sec. 4.15, page 67) and [Bishop]_, page
128.

Example
^^^^^^^

Let's take the group $C_{3v}$, which has three classes $E$, $2C_3$ and
$3\sigma_v$.

So $g_1=1$, $g_2=2$ and $g_3=3$ and the order is
$g=g_1+g_2+g_3=6$. Therefore it has three irreducible representations, whose
dimensions must satisfy:

.. math::

    n_1^2 + n_2^2 + n_3^2 = 6

The only integer solution (up to a permutation) is $n_1=n_2=1$ and $n_3=2$. So
we immediately have:

.. math::

    \begin{array}{c|ccc}
    C_{3v} & E & 2 C_3 & 3 \sigma_v \\
    \hline
           & 1 &   1   & 1 \\
           & 1 &   a   & b \\
           & 2 &   c   & d \\
    \end{array}

The rule 3. generates the following equations for all $\mu$ and $\nu$:

.. math::

    \begin{array}{cc|c}
    \mu & \nu & \sum_{i=1}^k g_i \chi^\mu(C_i) \chi^\nu(C_i)^* = g \delta_{\mu\nu} \\
    \hline
    1 & 1 &     6 = 6 \\
    1 & 2 &     1 + 2a + 3b = 0 \\
    1 & 3 &     2 + 2c + 3d = 0 \\
    2 & 2 &     1 + 2a^2 + 3b^2 = 6 \\
    2 & 3 &     2 + 2ac + 3bd = 0 \\
    3 & 3 &     4 + 2c^2 + 3d^2 = 6
    \end{array}

Solving all these equations simultaneously, we
get two independent solutions. One is:

.. math::

    a &= 1 \\
    b &= -1 \\
    c &= -1 \\
    d &= 0

and the other is:

.. math::

    a &= -{7\over 5} \\
    b &= {3\over 5} \\
    c &= {1\over 5} \\
    d &= -{4\over 5}

The rule 4. generates the following equations for all $i$ and $j$:

.. math::

    \begin{array}{cc|c}
    i & j & \sum_{\nu=1}^k \chi^\nu(C_i) \chi^\nu(C_j)^* = {g\over g_i} \delta_{ij} \\
    \hline
    1 & 1 &     6 = 6 \\
    1 & 2 &     1 + a + 2c = 0 \\
    1 & 3 &     1 + b + 2d = 0 \\
    2 & 2 &     1 + a^2 + c^2 = 3 \\
    2 & 3 &     1 + ab + cd = 0 \\
    3 & 3 &     1 + b^2 + d^2 = 2
    \end{array}

Both of the above solutions for $(a, b, c, d)$ satisfy all of these equations,
so the column equations are redundant.

The final character table is:

.. math::

    \begin{array}{c|ccc}
    C_{3v} & E & 2 C_3 & 3 \sigma_v \\
    \hline
     A_1   & 1 &   1   &  1 \\
     A_2   & 1 &   1   & -1 \\
      E    & 2 &  -1   &  0 \\
    \end{array}


Code::

    from sympy import var, solve, Matrix
    var("a, b, c, d")
    g = [1, 2, 3]
    M = Matrix([
        [1, 1, 1],
        [1, a, b],
        [2, c, d]])

    def rows(mu, nu, M, g):
        eq = 0
        for i in range(len(g)):
            eq += g[i] * M[mu, i] * M[nu, i]
        if mu == nu:
            eq -= sum(g)
        return eq

    def cols(i, j, M, g):
        eq = 0
        for nu in range(len(g)):
            eq += M[nu, i] * M[nu, j]
        if i == j:
            eq -= sum(g) / g[i]
        return eq

    print "Character table:"
    print M
    print "Rows conditions:"
    eqs = []
    for mu in range(3):
        for nu in range(mu, 3):
            eq = rows(mu, nu, M, g)
            eqs.append(eq)
            print mu+1, nu+1, ":    ", eq
    print "-"*40
    print "Columns conditions:"
    eqs2 = []
    for i in range(3):
        for j in range(i, 3):
            eq = cols(i, j, M, g)
            eqs2.append(eq)
            print i+1, j+1, ":    ", eq
    print "-"*40
    print "Solving the 1, 2, 4, 5 equations out of 0..5 from the rows conditions"
    s = solve(eqs[1:3]+eqs[4:], [a, b, c, d])
    print s
    print "Test that all the solutions satisfy the rest of the equations:"
    for a, b, c, d in s:
        print
        print "Solution:", a, b, c, d
        r = eqs[3].subs({
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            })
        print "Equation 3 from rows conditions, result: ", r
        assert r == 0
        print "Columns conditions:"
        for i, eq in enumerate(eqs2):
            r = eq.subs({
                    "a": a,
                    "b": b,
                    "c": c,
                    "d": d,
                    })
            print "Equation %i from columns conditions, result: %r" % (i, r)
            assert r == 0

This prints::

    Character table:
    [1, 1, 1]
    [1, a, b]
    [2, c, d]
    Rows conditions:
    1 1 :     0
    1 2 :     2*a + 3*b + 1
    1 3 :     2*c + 3*d + 2
    2 2 :     2*a**2 + 3*b**2 - 5
    2 3 :     2*a*c + 3*b*d + 2
    3 3 :     2*c**2 + 3*d**2 - 2
    ----------------------------------------
    Columns conditions:
    1 1 :     0
    1 2 :     a + 2*c + 1
    1 3 :     b + 2*d + 1
    2 2 :     a**2 + c**2 - 2
    2 3 :     a*b + c*d + 1
    3 3 :     b**2 + d**2 - 1
    ----------------------------------------
    Solving the 1, 2, 4, 5 equations out of 0..5 from the rows conditions
    [(-7/5, 3/5, 1/5, -4/5), (1, -1, -1, 0)]
    Test that all the solutions satisfy the rest of the equations:

    Solution: -7/5 3/5 1/5 -4/5
    Equation 3 from rows conditions, result:  0
    Columns conditions:
    Equation 0 from columns conditions, result: 0
    Equation 1 from columns conditions, result: 0
    Equation 2 from columns conditions, result: 0
    Equation 3 from columns conditions, result: 0
    Equation 4 from columns conditions, result: 0
    Equation 5 from columns conditions, result: 0

    Solution: 1 -1 -1 0
    Equation 3 from rows conditions, result:  0
    Columns conditions:
    Equation 0 from columns conditions, result: 0
    Equation 1 from columns conditions, result: 0
    Equation 2 from columns conditions, result: 0
    Equation 3 from columns conditions, result: 0
    Equation 4 from columns conditions, result: 0
    Equation 5 from columns conditions, result: 0


Applications of finite groups
-----------------------------


Distinct energy levels ('vibrations')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assume that we know number of atoms in a molecule and measure the number of
its distinct vibrational modes (frequencies) in a multiplet. We want to know
its symmetry.

We go through the list of all possible (point) symmetries $S$ of such a
molecule and look at what all reps. $S$ has. If an $n$--tuplet was observed
among the vibrational modes and there is no $n$-dimensional IR of $S$, then
can be excluded.

This procedure assumes that (a) the original symmetry $S$ is slightly disturbed
because of something and (b) two multiplets ($m$ and $n$ dimensional) do not
accidentally happen to have the same frequencies ('accidental degeneracy').



Selection rules ('transitions')
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

According to [Pilar]_, p. 572.

Probability of an optical transition is proportional to

.. math::
    :label: eq-1-2

    \braket{i| H_1 |f}\,,

where $\ket{i}$, $\ket{f}$ are the initial and final states and $H_1$ is
the operator of the interaction causing the transition. This is the
Fermi golden rule (first order time dep. perturbation theory).

The integral (:eq:`eq-1-2`) may vanish because of the symmetry. A simple 1D
example is that $\ket{f}$ is an even function $f(x)$, $\ket{i}$ is an odd
function $i(x)$ and $H_1$ is an even function $h_1(x)$. Then
$i^*(x)h_1(x)f(x)$ is odd and thus the integral over $(-\infty,\infty)$
vanishes. The group theory only generalizes this observation.

The procedure is: find the IRs $\rho_i$, $\rho_f$ to which $\ket{i}$,
$\ket{f}$ belong and also $\rho$, the regular rep of $H_1$ in order to catch
all IRs of $H_1$ (is this procedure correct?). Then construct
$\rho_i\otimes\rho\otimes\rho_f$, decompose it into IRs and see if the trivial
rep is present. If not, the integral (:eq:`eq-1-2`) vanishes. This procedure
is claimed to be equivalent to checking whether $\rho_i\otimes \rho_f$ and
$\rho$ contain at least one common IR.

The infrared absorption (IRa) is described by $H_1\propto x$ (or $y$, $z$,
depending probably on the polarization of light), the Raman scattering has
$H_1\propto x^2$ (it comes from the second order perturbation theory?).


Zoology
~~~~~~~


Todo:

* Describe the representations $A_1$, $A_2$, $B_1$, $E$ etc.

* Reps are specified
  by the generating functions $f(x,y,z)$ and the symmetry operations $T$ acting
  on these functions $f(x,y,z)\mapsto f(x',y',z')$  then transform the
  arguments, $(x,y,z)\mapsto (x',y',z')=T(x,y,z)$. Explain what functions are
  commonly used ($x$, $R_x,\ldots$) and give maybe some examples.

* Further reading: Davydov, p. 318, 195. Joe Penrose: Symmetry in Science.




Continuous Groups
-----------------

Lie groups+algebras
~~~~~~~~~~~~~~~~~~~

A continuous group with metrics is a Lie group (more exactly a differentiable
manifold and $a\mapsto ag$ and $a\mapsto a^{-1}$ are differentiable $\forall
g$, p. 172 in [Sternberg]_) usually a subgroup of $GL(n)$ is meant, a
linear Lie group (i.e. matrices). Peter--Weyl theorem (p. 179
in [Sternberg]_) looks like that compact Lie groups are practically as
nice as finite groups.

Consider $G=O(n)$, p. 234 in [Sternberg]_. If $A\in G$ then
$\exp(-tA)\subset G$ where $t\in R$. At least in $O(3)$ and probably in any
$O(n)$, any element of $G$ can be written as $\exp(-tA)$ where $A$ is a
$\pi/2$ rotation around some axis. These $A$'s are the generators of $G$.

Typical example: for
$G=SO(3)$ there are three generators, $iA_x$, $iA_y$, $iA_z$, where $A_x$ is
the rotation by $\pi/2$ around $x$--axis in $R^3$. The generators form a
vector space (here the linear span of $iA_x$, $iA_y$, $iA_z$) with an
additional operation of commutation. This structure is closed and it is called
the Lie algebra of the group $G$. The commutation relations between the
generators fully specify the Lie algebra. E.g. $[iA_x,iA_y]=iA_z$
and the two other ones.

This is a great simplification because a continuous (infinite) group was thus
mapped on a vector space, the algebra, where it suffices to look at the basis
elements, the generator. The net effect is that we have to watch only three
objects instead of infinitely many in the example above.

Todo: weights, roots and Dynkin diagrams. Octets and decuplets. Classification
of IRs of $SU(n)$. From [Georgi]_.


IRs of SU(2)
^^^^^^^^^^^^

p. 181 in [Sternberg]_; alternative somewhere in [Georgi]_.

The Peter-Weyl theorem concerns also the orthogonality of characters and that
in turn strongly restricts any possible characters of $SU(2)$. The conjugacy
classes of $SU(2)$ are exemplified by matrices
$U_\theta=\diag(e^{i\theta},e^{-i\theta})$ and their possible characters can
only be

.. math::

    \chi(\theta)=\sum_{k=-s}^{s} \exp(-i2k\theta)

with $2s$ integer.

All the corresponding reps exist, they are defined on the space
$z_1^{2s},z_1^{2s-1}z_2,\ldots, z_2^{2s}$ by
$U_{-\theta}z_1^{2s-k}z_2^k\mapsto [\exp i(2s-2k)\theta]z_1^{2s-k}z_2^k$.

For an IR of $SU(2)$ the complex conjugate is just the original. For other
$SU(n)$ it is not necessarily the case, p. 182 in [Sternberg]_.

IRs of $SO(3)$ are just those of $SU(2)$ but $s$ must be an integer.




Young diagrams
~~~~~~~~~~~~~~

YD is a systematic method to find all IRs of any symmetric group $S_n$
(permutations of an $n$-element set). The idea:

* find all conjugacy classes of $S_n$

* assign an IR to each of them

Char'n of the conjugacy classes: each permutation can be decomposed into
cycles. This cycle structure (i.e. how many cycles of length 1, how many of
length 2, etc. $=[\nu_1,\nu_2\,\ldots,\nu_n]$) is a unique mark of each
conjugation class. The Young diagram is written by rows, each row has
$\lambda_i$ empty boxes and $\lambda_i-\lambda_{i+i}=\nu_i\ge 0$. Each
conjugacy class has one YD. An YD of $S_n$ has $n$ boxes.

A Young tabloid (YTd) is obtained by filling an YD with numbers $1,\ldots,n$ where
ordering in each row does not matter. A Young tableau is an YTd where all
orderings (thus also in rows) matter.

The IRs of $S_n$. Take an YD $\lambda$. On the space of all corresponding
YTd's ($M_\lambda$) a rep. of the $S_n$ is created. It is decomposed into IRs
and shown to have some 'new' IR compared to $\mu>\lambda$.


Details are explained in [Sternberg]_, p. 76 or in the lecture notes of
J. Niederle.


Comments from p. 82 of [Sternberg]_:
Basis of $M_\lambda$ is defined ($e_t$; $\delta_{\{t\}}$ means probably a function on
$M_\lambda$ which is zero for all $\{y\}$ unless $\{y\}=\{t\}$). The action of
$a\in S_n$ on this basis functions is described.




Literature
----------

Books:

.. [Birss] Birss, R.R. (1961). Symmetry and Magnetism. Volume III.  North-Holland Publishing Company.

.. [Bishop] Bishop D.M. (1993). Group theory and chemistry. Courier Dover Publications.

.. [Elliott] Elliott, J.P. and Dawber, P.G. (1979). Symmetry in Physics. The Macmillan Press Ltd.

.. [Georgi] Georgi, H. (1990). Lie Algebras in Particle Physics. Addison-Wesley.

.. [Pilar] Pilar, F.L. (1990). Elementary Quantum Chemistry, McGraw--Hill.

.. [Sternberg] Sternberg, S. (1994). Group theory and physics. Cambridge University Press

Articles:

.. [Blokker72] Blokker, E. International journal of quantum chemistry VI, 925, (1972)

.. [Cannon69] Cannon, J.J. Communications of the association for computing machinery, **12**, 3 (1969)

.. [Dixon67] Dixon, J.D. Numerische Mathematik **10**, 446 (1967)
