# Alex Thayn
# Lab 9: NP Reductions

from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable, LpBinary

# Implement and test the reduction from SAT to ILP using PULP


# Example input: ilp_sat(['a,b,c', '-a,b,-c', '-d,-b', '-a,c', '-b,a'])
def ilp_sat(sat_formula):
    # create the constraints list
    constraints = []
    # Create an LpVariable for every variable in the SAT formula and its negation
    varLabels = getVarLabels(sat_formula)
    lpVariables = {}
    for label in varLabels:
        lpVariables[label] = (LpVariable(label, 0, 1, cat=LpBinary))
        # add negated variable
        negLabel = '-'+label
        lpVariables[negLabel] = LpVariable(negLabel, 0, 1, cat=LpBinary)
        # add constraint for not gate
        constraints.append(lpVariables[negLabel] == 1 - lpVariables[label])

    # OR the variables in each clause
    clauses = []
    finalClauses = []
    for clause in sat_formula:
        clauseVars = []
        for v in clause.split(','):
            clauseVars.append(lpVariables[v])
        clauses.append(clauseVars)

    for clause in clauses:
        constraint, ORClauseVar = getORConstraints(clause)
        constraints.extend(constraint)
        finalClauses.append(ORClauseVar)

    # AND the final clauses with each other
    constraints.extend(getAndConstraints(finalClauses))

    p, s, a = lp('max', 1, constraints)
    answer = getAnswer(a)
    if checkAnswer(sat_formula, answer):
        return answer
    return None


def getORConstraints(clause):
    if len(clause) < 1:
        return None

    clauseLpVariable = None

    ORconstraints = []
    while(len(clause) > 1):
        lhs = clause.pop()
        rhs = clause.pop()

        g = LpVariable(f'{lhs}\u25BC{rhs}', 0, 1, cat=LpBinary)
        # add constraints for OR
        ORconstraints.append(g >= lhs)
        ORconstraints.append(g >= lhs)
        ORconstraints.append(g <= lhs + rhs)

        clause.append(g)
        if(len(clause) == 1):
            clauseLpVariable = g

    return ORconstraints, clauseLpVariable


def getAndConstraints(clauses):
    if len(clauses) < 1:
        return None

    ANDconstraints = []
    finalConstraint = None
    while(len(clauses) > 1):
        lhs = clauses.pop()
        rhs = clauses.pop()

        g = LpVariable(f'{lhs}^{rhs}', 0, 1, cat=LpBinary)

        ANDconstraints.append(g <= lhs)
        ANDconstraints.append(g <= rhs)
        ANDconstraints.append(g >= lhs + rhs - 1)

        clauses.append(g)
        if(len(clauses) == 1):
            finalConstraint = g

    ANDconstraints.append(finalConstraint == 1)
    return ANDconstraints


def getVarLabels(sat_formula):  # Returns a list of unique variables contained in a SAT problem
    variables = []
    for clause in sat_formula:
        result = [v.strip() for v in clause.split(',')]
        for v in result:
            if v[0] == '-':
                v = v[1:]
            if not v in variables:
                variables.append(v)
    return variables


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


def getAnswer(answer):
    a = {}
    for key in answer.keys():
        if len(key) == 1:
            a[key] = answer[key]
    return a


def checkAnswer(sat_formula, answer):
    for clause in sat_formula:
        orClause = False
        c = [v.strip() for v in clause.split(',')]
        for var in c:
            if len(var) > 1:
                orClause = orClause or not(answer[var[1]])
            else:
                orClause = orClause or answer[var]
        if orClause == False:
            return False
    return True


if __name__ == "__main__":
    answer = ilp_sat(
        ['a,b,c', '-a,b,-c', '-d,-b', '-a,c', '-b,a'])
    print(answer)

# Test getVarLabels


def test_getVarLabels():
    answer = getVarLabels(['a,c,b', '-r,-j,-e,-y,-i'])
    assert answer == ['a', 'c', 'b', 'r', 'j', 'e', 'y', 'i']

    answer = getVarLabels(['-a,-c,-b', 'r,-j,-e,-y,-i'])
    assert answer == ['a', 'c', 'b', 'r', 'j', 'e', 'y', 'i']


def test_ilp_sat():
    answer = ilp_sat(
        ['a,b,c', '-a,b,-c', '-d,-b', '-a,c', '-b,a'])
    assert answer['a'] == 1
    assert answer['b'] == 1
    assert answer['c'] == 1
    assert answer['d'] == 0


def test_ilp_sat1():
    answer = ilp_sat(
        ['a,-b,-c'])

    assert answer['a'] == 1
    assert answer['b'] == 0
    assert answer['c'] == 1


def test_ilp_sat2():
    answer = ilp_sat(['a,b,c', '-a,-b,-c'])
    assert answer['a'] == 1
    assert answer['b'] == 1
    assert answer['c'] == 0
