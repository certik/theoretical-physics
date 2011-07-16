Wigner D Function
-----------------

The Wigner $D$ function gives the matrix elements of the rotation operator $R$
in the $jm$-representation. For the Euler angles $\alpha$, $\beta$, $\gamma$,
the $D$ function is defined as:

.. math::

    \braket{j,m| R(\alpha, \beta, \gamma) |j',m'} =
        \delta_{jj'} D(j, m, m', \alpha, \beta, \gamma)

Where the rotation operator $R(\alpha, \beta, \gamma)$ is defined using the
$z$-$y$-$z$ convention:

.. math::

    R(\alpha, \beta, \gamma) =
        e^{-i\alpha J_z}
        e^{-i\beta J_y}
        e^{-i\gamma J_z}

Here $J_i$ is the projection of the total angular momentum on an
$i$-axis. The $\ket{jm}$ is the eigenstate of the operators $J^2$ and $J_z$.
Using the fact that $e^{-i\gamma J_z}\ket{jm}=e^{-im\gamma}\ket{jm}$, we can
see that the Wigner $D$ function can always be written using the Wigner
small-$d$ function as:

.. math::

    D(j, m, m', \alpha, \beta, \gamma)
        = \braket{j,m| R(\alpha, \beta, \gamma) |j,m'}
        = \braket{j,m| e^{-i\alpha J_z} e^{-i\beta J_y} e^{-i\gamma J_z} |j,m'}
        =

        = e^{-i m \alpha}\braket{j,m| e^{-i\beta J_y} |j,m'} e^{-i m' \gamma}
        = e^{-i m \alpha} d(j, m, m', \beta) e^{-i m' \gamma}

where

.. math::

    d(j, m, m', \beta) = \braket{j,m| e^{-i\beta J_y} |j,m'}

We can use the following relations to evaluate $d(j, m, m', \beta)$:

.. math::

    d(j, m, m', \beta) = i^{2j-m-m'} (-1)^{2m}\sum_{m''=-j}^j
        d(j, m, m'', {\pi\over2})
        e^{-i m'' \beta}
        d(j, m'', -m', {\pi\over2})

    d(j, m, m', {\pi\over2}) = (-1)^{m-m'} {1\over 2^j}
        \sqrt{(j+m)! (j-m)! \over (j+m')! (j-m')!} \sum_k
        (-1)^k \binom{j+m'}{k} \binom{j-m'}{k+m-m'}
