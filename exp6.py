import random

def generate_uniform():
    return random.random()

def f(x):
    return x ** 2

samples = [generate_uniform() for _ in range(10)]
function_values = [f(x) for x in samples]

print("Generated Samples:")
for i, x in enumerate(samples):
    print(f"x[{i+1}] = {x:.4f}, f(x) = {function_values[i]:.4f}")

monte_carlo_estimate = sum(function_values) / len(samples)
print(f"\nEstimated Integral (Monte Carlo): {monte_carlo_estimate:.4f}")
