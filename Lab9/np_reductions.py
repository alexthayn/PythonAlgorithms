# Alex Thayn
# Lab 9: NP Reductions

from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable

# Implement and test the reduction from SAT to ILP using PULP

# Example input: ilp_sat(['a,b,c', '-a,b,-c', '-d,-b', '-a,c', '-b,a'])


def ilp_sat(sat_formula):
    varLabels = getVarLabels(sat_formula)
    # Create an LpVariable for every variable in the SAT
    lpVariables = []
    for label in varLabels:
        lpVariables.append(LpVariable(label, 0, 1, cat='LpBinary'))
        lpVariables.append(LpVariable('~{label}', 0, 1, cat='LpBinary'))


# Returns a list of unique variable contained in a SAT problem
def getVarLabels(sat_formula):
    variables = []
    for clause in sat_formula:
        result = [v.strip() for v in clause.split(',')]
        for v in result:
            if not v in variables:
                variables.append(v)
    print(variables)

    return variables


if __name__ == "__main__":
    ilp_sat(['a,b,c', '-a,b,-c', '-d,-b', '-a,c', '-b,a'])
