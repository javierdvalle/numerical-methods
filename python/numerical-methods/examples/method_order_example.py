from ..ode import euler, rungekutta
from ..ode import method_order
from ..ode.methods.rungekutta_tables import EMP, Heun3, RKclassic 
from ..ode.methods.rungekutta_tables import regla3octavos, dop5, Fehlberg7

if __name__ == '__main__':
    order = method_order(euler)
    print(f"euler is order={order}")
    print()
    assert order == 1, print(order)

    order = method_order(rungekutta, show_info=True, table=EMP())
    print(f"EMP is order={order}")
    print()
    assert order == 2, print(order)

    order = method_order(rungekutta, show_info=True, table=Heun3())
    print(f"Heun3 is order={order}")
    print()
    assert order == 3, print(order)

    order = method_order(rungekutta, show_info=True, table=RKclassic())
    print(f"RKclassic is order={order}")
    print()
    assert order == 4, print(order)

    order = method_order(rungekutta, show_info=True, table=regla3octavos())
    print(f"regla3octavos is order={order}")
    print()
    assert order == 4, print(order)

    order = method_order(rungekutta, show_info=True, table=dop5())
    print(f"dop5 is order={order}")
    print()
    assert order == 5, print(order)

    order = method_order(rungekutta, show_info=True, table=Fehlberg7())
    print(f"Fehlberg7 is order={order}   <---?????")
    print()
    assert order == 8, print(order)
