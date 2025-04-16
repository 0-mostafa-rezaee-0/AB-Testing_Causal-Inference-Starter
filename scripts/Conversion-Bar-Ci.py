# images/conversion_bar_ci.png generator

import matplotlib.pyplot as plt
import numpy as np

# Simulated means
mean_control = 0.10
mean_treatment = 0.11
n = 10000

# Compute 95% CI error bars
ci_control = 1.96 * np.sqrt(mean_control * (1 - mean_control) / n)
ci_treatment = 1.96 * np.sqrt(mean_treatment * (1 - mean_treatment) / n)

# Plot
plt.figure(figsize=(6, 4))
plt.bar(['Control', 'Treatment'],
        [mean_control, mean_treatment],
        yerr=[ci_control, ci_treatment],
        capsize=6,
        color=['#6baed6', '#fc9272'])

plt.title('Conversion Rates with 95% Confidence Intervals')
plt.ylabel('Conversion Rate')
plt.ylim(0, 0.14)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('../images/conversion_bar_ci.png', dpi=150)
plt.show()
