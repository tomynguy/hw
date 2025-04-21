import copy

class Variable:
    def __init__(self, name, value, knot):
        self.name = name
        self.value = value
        self.knot = knot

def evaluate_clause(clause):
    for x in clause:
        if x.knot != x.value:
            return True
    return False

def evaluate_expression(expression):
    for clause in expression:
        if not evaluate_clause(clause):
            return False
    return True

def recurse(clauses, clause_index, x_values, x_index):
    # If end of expression
    if clause_index == len(clauses):
        return evaluate_expression(clauses)
    
    # Init Variables
    clauses_copy = copy.deepcopy(clauses)
    clause = clauses_copy[clause_index]
    x_values_copy = copy.deepcopy(x_values)

    # If end of clause
    if x_index == len(clause):
        if evaluate_clause(clause):
            return recurse(clauses_copy, clause_index + 1, x_values_copy, 0)
        return False
    
    # If already exists
    if clause[x_index].name in x_values_copy:
        clause[x_index].value = x_values_copy[clause[x_index].name]
        return recurse(clauses_copy, clause_index, x_values_copy, x_index + 1)

    # Try True First
    x_values_copy[clause[x_index].name] = True
    clause[x_index].value = True
    if recurse(clauses_copy, clause_index, x_values_copy, x_index + 1):
        return True
    
    # Try False
    x_values_copy[clause[x_index].name] = False
    clause[x_index].value = False
    return recurse(clauses_copy, clause_index, x_values_copy, x_index + 1)

print(recurse([
    [Variable(1, None, False), Variable(2, None, False), Variable(3, None, False)],
    [Variable(3, None, False)],
    [Variable(1, None, True), Variable(3, None, True)]
], 0, {}, 0))

