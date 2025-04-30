# notebooks/01_ab_test_simulation.ipynb (exported as script for clarity)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Set random seed for reproducibility
np.random.seed(42)

# --- 1. SIMULATE CONTROL & TREATMENT DATA ---
n = 10000  # users per group
p_control = 0.10  # 10% conversion in control
p_treatment = 0.11  # 11% conversion in treatment

control = np.random.binomial(1, p_control, n)
treatment = np.random.binomial(1, p_treatment, n)

data = pd.DataFrame({
    'group': ['control'] * n + ['treatment'] * n,
    'converted': np.concatenate([control, treatment])
})

# Save data
os.makedirs("../data", exist_ok=True)
data.to_csv('../data/synthetic_ab_test.csv', index=False)

# --- 2. MANUAL HYPOTHESIS TEST ---
mean_control = control.mean()
mean_treatment = treatment.mean()
delta = mean_treatment - mean_control

p_pooled = (control.sum() + treatment.sum()) / (2 * n)
se_pooled = np.sqrt(p_pooled * (1 - p_pooled) * 2 / n)
z_score = delta / se_pooled
p_value_manual = 2 * (1 - stats.norm.cdf(np.abs(z_score)))

print(f"Observed lift: {delta:.4f}")
print(f"Z-score: {z_score:.4f}, p-value (manual): {p_value_manual:.4f}")

# --- 3. SCIPY VALIDATION ---
_, p_value_scipy = stats.ttest_ind(treatment, control)
print(f"p-value (scipy t-test): {p_value_scipy:.4f}")

# --- 4. CONFIDENCE INTERVAL ---
ci_low = delta - 1.96 * se_pooled
ci_high = delta + 1.96 * se_pooled
print(f"95% CI for lift: ({ci_low:.4f}, {ci_high:.4f})")

# --- 5. VISUALIZATION ---
plt.bar(['Control', 'Treatment'], [mean_control, mean_treatment],
        yerr=[1.96 * np.sqrt(mean_control * (1 - mean_control) / n),
              1.96 * np.sqrt(mean_treatment * (1 - mean_treatment) / n)],
        capsize=5, color=['skyblue', 'salmon'])
plt.ylabel('Conversion Rate')
plt.title('Conversion Rates with 95% CI')
plt.savefig('../images/conversion_bar_ci.png')
plt.show()

# --- 6. SIMULATE FALSE POSITIVE RATE ---
def simulate_fpr(null_p=0.10, sims=1000, n=10000, alpha=0.05):
    false_positives = 0
    for _ in range(sims):
        ctrl = np.random.binomial(1, null_p, n)
        trt = np.random.binomial(1, null_p, n)
        _, pval = stats.ttest_ind(trt, ctrl)
        if pval < alpha:
            false_positives += 1
    return false_positives / sims

fpr = simulate_fpr()
print(f"Simulated False Positive Rate (alpha=0.05): {fpr:.3f}")
