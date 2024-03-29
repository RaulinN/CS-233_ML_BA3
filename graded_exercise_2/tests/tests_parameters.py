""" Parameters for generating unit tests data.
"""

test_params = {
    'lda_mat_data_mean': dict(),
    'lda_mat_clswise_mean': dict(),
    'lda_mat': dict(),
    'count_support_vectors': dict(),
    'compute_primal_coef': dict(),
    'simulate_cover': dict(trials=30, D=50, min_N=2, max_N=200, num_of_N=25),
    'find_probabilities': dict(N=200, D=4, K=8),
    'top_k': dict(N=175, K=15, k=4),
    'kernel_matrix': dict(N=123, D=21),
    'compute_eigvecs': dict()
}
