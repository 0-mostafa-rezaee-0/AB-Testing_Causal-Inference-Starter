# images/pvalue_distribution.png generator

import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Simulate 1000 p-values under the null
np.random.seed(42)
n = 10000
pvals = []
for _ in range(1000):
    a = np.random.binomial(1, 0.1, n)
    b = np.random.binomial(1, 0.1, n)
    _, pval = stats.ttest_ind(a, b)
    pvals.append(pval)

# Plot p-value distribution
plt.figure(figsize=(8, 5))
plt.hist(pvals, bins=50, color='skyblue', edgecolor='black')
plt.axvline(0.05, color='red', linestyle='--', label='alpha = 0.05')
plt.title('P-Value Distribution under Null Hypothesis')
plt.xlabel('p-value')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.savefig('../images/pvalue_distribution.png')
plt.show()
