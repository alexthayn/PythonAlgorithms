from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable


def vars(s, low=None, high=None):
    """example creates three variables bounded from 0 to 10:
    a, b, c = vars('a,b,c', 0, 10)
    """
    return tuple(LpVariable(v.strip(), low, high) for v in s.split(','))


def lp(mode, objective, constraints):
    """see lp1 below for an example"""
    if mode.lower() == 'max':
        mode = LpMaximize
    elif mode.lower() == 'min':
        mode = LpMinimize
    prob = LpProblem("", mode)
    prob += objective
    for c in constraints:
        prob += c
    prob.solve()
    return prob, prob.objective.value(), dict((v.name, v.value()) for v in prob.variables())


def lp1():
    x_1, x_2 = vars('x_1, x_2')
    return lp('max', x_1 + 6*x_2, [
            x_1 >= 0,
            x_2 >= 0,
            x_1 <= 200,
            x_2 <= 300,
            x_1 + x_2 <= 400])


def main():
    pass

