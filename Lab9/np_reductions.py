# Alex Thayn
# Lab 9: NP Reductions

from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable

# Implement and test the reduction from SAT to ILP using PULP


# Example input: ilp_sat(['a,b,c', '-a,b,-c', '-d,-b', '-a,c', '-b,a'])
def ilp_sat(sat_formula):
    varLabels = getVarLabels(sat_formula)
    # Create an LpVariable for every variable in the SAT formula
    lpVariables = {}
    for label in varLabels:
        lpVariables[label] = (LpVariable(label, 0, 1, cat='LpBinary'))

    # create the constraints list
    constraints = []
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
    # Returns a list of constraints from and OR on the clause variables
    print(f'constraints: {constraints}')


def getORConstraints(clause):
    if len(clause) < 1:
        return None

    clauseLpVariable = None

    ORconstraints = []
    while(len(clause) > 1):
        lhs = clause.pop()
        rhs = clause.pop()

        g = LpVariable(f'{lhs}\u25BC{rhs}', 0, 1, cat='LpBinary')
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
    while(len(clauses) > 1):
        lhs = clauses.pop()
        rhs = clauses.pop()

        g = LpVariable(f'{lhs}^{rhs}', 0, 1, cat="LpBinary")

        ANDconstraints.append(g <= lhs)
        ANDconstraints.append(g <= rhs)
        ANDconstraints.append(g >= lhs + rhs - 1)

        clauses.append(g)

    return ANDconstraints


def getVarLabels(sat_formula):  # Returns a list of unique variables contained in a SAT problem
    variables = []
    for clause in sat_formula:
        result = [v.strip() for v in clause.split(',')]
        for v in result:
            if not v in variables:
                variables.append(v)
    return variables


if __name__ == "__main__":
    ilp_sat(['a,b,c', '-a,b,-c', '-d,-b', '-a,c', '-b,a'])


# Test getVarLabels
