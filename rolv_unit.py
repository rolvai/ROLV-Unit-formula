import math

def calculate_rolv(S, D, E, epsilon=1e-6):
    """
    Calculate the ROLV Unit.
    - S: Speedup factor (>1)
    - D: Sparsity density (0 < D < 1)
    - E: Energy savings percentage (0 ≤ E ≤ 100)
    - epsilon: Small constant for stability (default 1e-6)
    Returns: ROLV value (float)
    """
    if S > 1 and 0 < D < 1:
        denominator = abs(math.log10(1 - D + epsilon))
        if denominator == 0:
            denominator = epsilon  # Avoid division by zero
        term1 = S * math.log10(S) / denominator
        term2 = (E * S) / 100
        return term1 + term2
    return 0

# Example usage
S = 500.82  # Example speedup vs. cuSPARSE at 20% sparsity
D = 0.2     # 20% density (80% sparsity)
E = 100     # 100% energy savings
rolv_value = calculate_rolv(S, D, E)
print(f"ROLV Unit: {rolv_value:.2f}")  # Outputs ~14452.55
