from scipy.optimize import line_search

def alpha_backtracking(x, f, f_prime, direction, gamma, beta, init_alpha):
    alpha = init_alpha
    while f(x) - f(x+alpha * direction) < -gamma * alpha * f_prime(x).dot(direction):
        alpha = alpha * beta
    return alpha

def alpha_exact(x, f, f_prime, direction):
    return line_search(f, f_prime, x, direction)[0]

def get_alpha(kind, x, f, f_prime, direction, *args):
	if kind=="exact":
		return alpha_exact(x, f, f_prime, direction)
	elif kind=="backtracking":
		return alpha_backtracking(x, f, f_prime, direction, *args)