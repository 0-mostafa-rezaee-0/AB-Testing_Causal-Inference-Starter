# 📂 scripts/

This folder contains modular Python scripts for simulation, statistical analysis, and visualization used throughout the A/B testing project.

These scripts help keep the notebook clean and allow for easier reuse, testing, and automation.

---

## 📜 File Overview

### ✅ `abtest_utils.py`
Core utility functions for statistical testing and simulation:

- `simulate_ab_test()` — Generate binary outcome data for control and treatment
- `compute_z_score()` — Calculate pooled SE, z-statistic, and p-value manually
- `bootstrap_ci()` — Estimate confidence intervals for lift using bootstrapping
- `simulate_false_positives()` — Run multiple null experiments and report FPR

### 📊 `Conversion-Bar-Ci.py`
Generates a bar plot with 95% confidence intervals for control vs. treatment conversion rates.
- Used for visual storytelling in notebook and README
- Output: `images/conversion_bar_ci.png`

### 📉 `p-value-distribution.py`
Simulates 1000 null experiments (no treatment effect) and visualizes the p-value distribution.
- Illustrates the base rate of false positives
- Output: `images/pvalue_distribution.png`

---

## 🧪 Usage
These scripts are not meant to be executed directly like a CLI tool but are instead intended to be:
- Imported into Jupyter notebooks
- Used in automated pipelines or tests
- Extended for future projects

---

## 📦 Coming Soon
Future scripts may include:
- Sequential testing logic
- Multi-metric analysis
- Integration with CLI or API endpoints

---

## 🧑‍💻 Tip for Contributors
If you add a new script, include:
1. A docstring at the top
2. Function docstrings with input/output
3. A line in this README for discoverability

Stay modular. Keep your experiments reproducible. 🧪