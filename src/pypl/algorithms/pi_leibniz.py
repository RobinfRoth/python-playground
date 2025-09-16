#!/usr/bin/env python3

def calculate_pi(n_terms: int) -> float:
    """Calculate Pi using the Leibnitz formula with ``n_terms``."""
    numerator = 4.0
    denominator = 1.0

    pi_approximation: float = 0.0

    for i in range(n_terms):
        term: float = numerator / denominator
        pi_approximation += term if i & 1 == 0 else -term
        denominator += 2

    return pi_approximation


if __name__ == "__main__":
    import sys

    default_n_terms: int = 10
    res: float

    if len(sys.argv) > 1:
        try:
            custom_n_terms: int = int(sys.argv[1])
        except ValueError as e:
            print("Cannot parse custom number of terms: ", e)
            sys.exit(1)
            
        res = calculate_pi(custom_n_terms)
    else:
        print(f"Using default number of terms:", default_n_terms)
        res = calculate_pi(default_n_terms)

    print(res)