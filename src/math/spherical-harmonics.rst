.. index:: spherical harmonics

Spherical Harmonics
-------------------


Are defined by

.. math::

       Y_{lm}(\theta,\phi)=\sqrt{{2l+1\over4\pi}{(l-m)!\over(l+m)!}}\,P_l^m(\cos\theta)\,e^{im\phi}

where $P_l^m$ are associated Legendre polynomials defined by

.. math::

       P_l^m(x)=(-1)^m (1-x^2)^{m/2}{\d^m\over\d x^m} P_l(x)

and $P_l$ are Legendre polynomials defined by the formula

.. math::

       P_l(x)={1\over2^l l!}{\d^l\over\d x^l}[(x^2-1)^l]

they also obey the completeness relation

.. math::
    :label: Lorto

       \sum_{l=0}^\infty {2l+1\over2}P_l(x')P_l(x)=\delta(x-x')

The spherical harmonics are ortonormal:

.. math::
    :label: Yorto

       \int Y_{lm}\,Y^*_{l'm'}\,\d\Omega = \int_0^{2\pi}\int_0^{\pi} Y_{lm}(\theta,\phi)\,Y^*_{l'm'}(\theta,\phi)\sin\theta\,\d\theta\,\d\phi = \delta_{mm'}\delta_{ll'}

and complete (both in the $l$-subspace and the whole space):

.. math::
    :label: lcomplete

       \sum_{m=-l}^l|Y_{lm}(\theta,\phi)|^2={2l+1\over4\pi}


.. math::
    :label: Ycomplete

       \sum_{l=0}^\infty\sum_{m=-l}^lY_{lm}(\theta,\phi)Y_{lm}^*(\theta',\phi') ={1\over\sin\theta}\delta(\theta-\theta')\delta(\phi-\phi')= \delta({\bf\hat r}-{\bf\hat r'})

The relation :eq:`lcomplete` is a special case of an addition theorem for spherical harmonics

.. math::
    :label: lsum

       \sum_{m=-l}^lY_{lm}(\theta,\phi)Y_{lm}^*(\theta',\phi')= {2l+1\over 4\pi}P_l(\cos\gamma)

where $\gamma$ is the angle between the unit vectors given by ${\bf\hat r}=(\theta,\phi)$ and ${\bf\hat r'}=(\theta',\phi')$:

.. math::

       \cos\gamma=\cos\theta\cos\theta'+\sin\theta\sin\theta'\cos(\phi-\phi') ={\bf\hat r}\cdot{\bf\hat r'}
