"""
8.1 Triple Step.

A child is running up a staircase with n steps and can hop either 1 step, 2
steps, or 3 steps at a time. Implement a method to count how many possible
ways the child can run up the stairs.
"""

mem = {}


def triple_step(n):
    """Method to count how many possible ways can run up the stairs."""
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in mem:
        return mem[n]
    mem[n] = triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)
    return mem[n]
