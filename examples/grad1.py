import mygrad
from mygrad import pm
from mygrad import fwd


def f(x):
    y = pm.sin(x) * 2.0
    z = -y + x
    return z


x, xdot = 3.0, 1.0
y, ydot = fwd.jvp(f, (x,), (xdot,))
print(y)
print(ydot)
