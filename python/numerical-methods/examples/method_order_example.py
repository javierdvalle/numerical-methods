from ..ode import euler, rungekutta
from ..ode import method_order
from ..ode.methods.rungekutta_tables import EMP, Heun3, RKclassic 
from ..ode.methods.rungekutta_tables import regla3octavos, dop5, Fehlberg7

if __name__ == '__main__':
    order = method_order(euler)
    print(f"euler is order={order}")
    assert order == 1

    order = method_order(rungekutta, table=EMP())
    print(f"EMP is order={order}")
    assert order == 2

    order = method_order(rungekutta, table=Heun3())
    print(f"Heun3 is order={order}")
    assert order == 3

    order = method_order(rungekutta, table=RKclassic())
    print(f"RKclassic is order={order}")
    assert order == 4

    order = method_order(rungekutta, table=regla3octavos())
    print(f"regla3octavos is order={order}")
    assert order == 4

    order = method_order(rungekutta, table=dop5())
    print(f"dop5 is order={order}")
    assert order == 5

    order = method_order(rungekutta, table=Fehlberg7())
    print(f"Fehlberg7 is order={order}   <---?????")
    assert order == 8
