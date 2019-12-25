import random

n = 5

# Generate numbers D
memo_D = {}
def D(e, n):
    global memo_D
    # Base case
    if e == 0:
        return 0
    if n == 0:
        return 1
    # Recurse
    if (e, n) in memo_D:
        return memo_D[(e, n)]
    memo_D[(e, n)] = D(e-1, n) + D(e, n-1) + D(e+1, n-1)
    return memo_D[(e, n)]

# Generate distribution L
memo_L = {}
def L(e, n):
    global memo_L
    if (e, n) in memo_L:
        return memo_L[(e, n)]
    dist = []
    for k in range(e):
        dist.append(D(e-k, n-1) / D(e, n))
    for k in range(e):
        dist.append(D(e-k+1, n-1) / D(e, n))
    memo_L[(e, n)] = dist
    return memo_L[(e, n)]

def sample_ka(e, n):
    choices = [(k, 1) for k in range(e)] + [(k, 2) for k in range(e)]
    distribution = L(e, n)
    return random.choice(choices, weight=distribution)


def generate_expression(operators, n, num_expr):
    """Generates a number of expressions given size of expression and operators.

    Args:
        operators (dict): dictionary holding operatos as keys and probability of
            it showing up as values.
        n (int): size of expression.
        num_expr (int): number of expressions to be generated.

    Returns:
        list: a list of generated expressions.
    """
    raise NotImplementedError