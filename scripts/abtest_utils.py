# scripts/abtest_utils.py

import numpy as np
import pandas as pd
from scipy import stats


def simulate_ab_test(n=10000, p_control=0.10, p_treatment=0.11, seed=None):
    if seed is not None:
        np.random.seed(seed)
    control = np.random.binomial(1, p_control, n)
    treatment = np.random.binomial(1, p_treatment, n)
    return control, treatment


def compute_z_score(control, treatment):
    mean_c = control.mean()
    mean_t = treatment.mean()
    delta = mean_t - mean_c

    p_pooled = (control.sum() + treatment.sum()) / (len(control) + len(treatment))
    se_pooled = np.sqrt(p_pooled * (1 - p_pooled) * (1 / len(control) + 1 / len(treatment)))
    z = delta / se_pooled
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p_value, delta, se_pooled


def bootstrap_ci(data1, data2, n_bootstrap=1000, ci=95):
    diffs = []
    for _ in range(n_bootstrap):
        sample1 = np.random.choice(data1, len(data1), replace=True)
        sample2 = np.random.choice(data2, len(data2), replace=True)
        diffs.append(sample2.mean() - sample1.mean())
    lower = np.percentile(diffs, (100 - ci) / 2)
    upper = np.percentile(diffs, 100 - (100 - ci) / 2)
    return lower, upper


def simulate_false_positives(null_p=0.10, sims=1000, n=10000, alpha=0.05):
    false_positives = 0
    for _ in range(sims):
        ctrl = np.random.binomial(1, null_p, n)
        trt = np.random.binomial(1, null_p, n)
        _, pval = stats.ttest_ind(trt, ctrl)
        if pval < alpha:
            false_positives += 1
    return false_positives / sims
