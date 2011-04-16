Ordinary Differential Equations
===============================

Finite Difference Formulas
--------------------------

We define the backward difference operator $\nabla_h$ by:

.. math::

    \nabla_h f(a) = f(a) - f(a-h)

Repeated application gives:

.. math::

    \nabla_h^2 f(a) = \nabla_h (f(a) - f(a-h))
        = f(a) - f(a-h) -f(a-h) + f(a-2h)
        = f(a) - 2f(a-h) + f(a-2h)

    \nabla_h^3 f(a) = f(a) - 3f(a-h) + 3f(a-2h)-f(a-3h)

    \nabla_h^n f(a) = \sum_{k=0}^n \binom{n}{k}(-1)^k f(a-kh)

We can also derive a formula for $f(a+t)$ where $t$ is any real number,
independent of $h$:

.. math::

    f(a-h) = (1-\nabla_h) f(a)

    (1-\nabla_h)^{-1} f(a-h) = f(a)

    (1-\nabla_h)^{-1} f(a) = f(a+h)

    (1-\nabla_h)^{-n} f(a) = f(a+nh)

    (1-\nabla_h)^{-{t\over h}} f(a) = f(a+t)

Now we can express the following general integral using the function value from
either left ($f(a)$) or right ($f(a+h)$) hand side of the interval $h$:

.. math::

    \int_a^{a+h} f(t) \,\d t
        = \int_0^h f(a+t) \,\d t
        = \int_0^h (1-\nabla_h)^{-{t\over h}} f(a) \,\d t
        =

        = - {h\nabla_h\over (1-\nabla_h) \log(1-\nabla_h)}f(a) =

        = h \left(1+\half\nabla_h + {5\over 12}\nabla_h^2+{3\over8}
            \nabla_h^3+\cdots\right) f(a) =

        = - {h\nabla_h\over \log(1-\nabla_h)} (1-\nabla_h)^{-1}f(a)
        = - {h\nabla_h\over \log(1-\nabla_h)} f(a+h) =

        = h \left(1-\half\nabla_h - {1\over 12}\nabla_h^2-{1\over24}
            \nabla_h^3+\cdots\right) f(a+h)
