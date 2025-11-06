 # --- Verification Script for Example 5.6.1 ---

# 1. Definition of the semigroup S from Example~\ref{ex:s_regular_n4}
S = [
    [0, 0, 2, 2],
    [0, 0, 2, 2],
    [2, 2, 0, 0],
    [2, 2, 0, 0]
]

# 2. Helper function to precompute N_S(k)
def precompute_NS(semigroup):
    """Counts the total number of factorizations for each element s_k."""
    n = len(semigroup)
    N_S_list = [0] * n 
    for p in range(n):
        for q in range(n):
            k = semigroup[p][q]
            N_S_list[k] += 1
    return N_S_list

# 3. Main function to verify regularity based on Theorem 2
def verify_regularity(semigroup):
    """Computes Q(i,j) for all vertices and checks for regularity."""
    n = len(semigroup)
    
    # Precompute N_S values
    N_S_lookup = precompute_NS(semigroup)
    print(f"Precomputed N_S values (for k=0..{n-1}): {N_S_lookup}")
    
    Q_values = []     
    base_degree = 2 * n - 3
    
    # Iterate over all n^2 vertices v = (s_i, s_j, s_k)
    for i in range(n):
        for j in range(n):
            k = semigroup[i][j]
            NS = N_S_lookup[k]
            
            # Compute N_R(s_i, s_k)
            NR = 0
            for q_prime in range(n):
                if q_prime != j and semigroup[i][q_prime] == k:
                    NR += 1
            
            # Compute N_C(s_j, s_k)
            NC = 0
            for p_prime in range(n):
                if p_prime != i and semigroup[p_prime][j] == k:
                    NC += 1
            
            # Compute Q(i,j) as per Theorem 2
            Q = NS - 2 * NR - 2 * NC
            Q_values.append(Q)
            
    # Final check for regularity
    is_Q_constant = all(q == Q_values[0] for q in Q_values)
    
    if is_Q_constant:
        print(f"\nResult: Q(i,j) = {Q_values[0]} (constant for all {n*n} vertices).")
        degree = base_degree + Q_values[0]
        print(f"Result: Degree = {degree} (constant for all {n*n} vertices).")
        print("Conclusion: Γ(S) is REGULAR.")
    else:
        print(f"\nResult: Q(i,j) is NOT constant. Found values: {set(Q_values)}")
        print("Conclusion: Γ(S) is NOT REGULAR.")
    
    return is_Q_constant

# 4. Execute the verification
print("--- Verifying the semigroup from Example 5.6.1 ---")
verify_regularity(S)
