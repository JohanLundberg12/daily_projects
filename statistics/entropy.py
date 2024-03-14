# entropy function
from math import log2


def entropy(p):
    """Given a probability, calculate the entropy of the distribution."""

    # If the probability is 0, the entropy is 0.
    # If the probability is 1, the entropy is 0.
    # Otherwise, the entropy is p * log2(p).
    #
    return p * log2(p) if p > 0 else 0


def entropy_of_a_system(probabilities):
    """Given a list of probabilities, calculate the entropy of the distribution."""
    # The entropy of a distribution is the sum of the entropy of each outcome.

    return -sum(entropy(p) for p in probabilities)


probabilities = [0.5, 0.5]

print(entropy_of_a_system(probabilities))  # 1

probabilities = [0.25, 0.25, 0.25, 0.25]

print(entropy_of_a_system(probabilities))  # 2

probabilities = [1]

print(entropy_of_a_system(probabilities))  # -0.0 (no surprise)


probabilities = [0.5, 0.25, 0.25]

print(entropy_of_a_system(probabilities))  # 1.5

probabilities = [0.75, 0.25]

print(entropy_of_a_system(probabilities))  # 0.81
