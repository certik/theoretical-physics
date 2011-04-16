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

Keeping terms only to third-order, we obtain:

.. math::

    \int_a^{a+h} f(t) \,\d t
        = - {h\nabla_h\over (1-\nabla_h) \log(1-\nabla_h)}f(a)
        \approx h \left(1+\half\nabla_h + {5\over 12}\nabla_h^2+{3\over8}
            \nabla_h^3\right) f(a)
        =

        = h f(a) + h\half\left(f(a)-f(a-h)\right)
            +h{5\over 12}\left(f(a)-2f(a-h)+f(a-2h)\right)+

            +h{3\over8}\left(f(a)-3f(a-h)+3f(a-2h)-f(a-3h)\right)
        =

        = h\left(1+\half+{5\over12}+{3\over8}\right)f(a)
          -h\left(\half+{2\cdot5\over12}+{3\cdot3\over8}\right)f(a-h) +

          +h\left({5\over12}+{3\cdot3\over8}\right)f(a-2h)
          -h\left({3\over8}\right)f(a-3h)
        =

        = h{55\over24}f(a) -h{59\over24}f(a-h) +
          h{37\over24}f(a-2h) -h{3\over8}f(a-3h)
        =

        = {h\over24}\left(55f(a) -59f(a-h) + 37f(a-2h) -9f(a-3h)\right)

Similarly:

.. math::

    \int_a^{a+h} f(t) \,\d t
        = - {h\nabla_h\over\log(1-\nabla_h)}f(a+h)
        \approx h \left(1-\half\nabla_h - {1\over 12}\nabla_h^2-{1\over24}
            \nabla_h^3\right) f(a)
        =

        = {h\over24}\left(9f(a+h) +19f(a) -5f(a-h) +f(a-2h)\right)
