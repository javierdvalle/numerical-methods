from ..ode import euler
from ..ode import method_order


if __name__ == '__main__':
    order = method_order(euler)
    print(f"euler: {order}")
    assert order == 1
