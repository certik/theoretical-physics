.. index:: QED, quantum electrodynamics

Quantum Electrodynamics (QED)
=============================

QED Lagrangian
--------------

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


The first equation is the Dirac equation in the electromagnetic field and the
second equation is a set of Maxwell equations ($\partial_\nu
F^{\nu\mu}=-ej^\mu$) with a source $j^\mu=c\bar\psi\gamma^\mu\psi$, which is a
4-current comming from the Dirac equation.
