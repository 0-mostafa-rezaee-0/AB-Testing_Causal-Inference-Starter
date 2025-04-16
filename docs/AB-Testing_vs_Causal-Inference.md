# 🧪 A/B Testing vs. Causal Inference

Understanding how these two powerful concepts relate helps frame the purpose of this project—and where to go next.

---

## 🔁 Overview

| | **A/B Testing** | **Causal Inference** |
|---|----------------|---------------------|
| **What** | Controlled randomized experiments | Frameworks for estimating causal effects |
| **Data** | Experimental (randomized) | Often observational (non-randomized) |
| **Goal** | Measure treatment impact in a clean, unbiased way | Estimate causal effects even with confounding |
| **Toolset** | Random assignment, hypothesis testing | Potential outcomes, DAGs, IV, matching, DiD, etc. |
| **Assumptions** | Randomization → exchangeability | Assumptions vary: ignorability, exclusion, SUTVA |
| **Usage** | Online experiments, product changes | Health, economics, policy, fairness, experimentation |

---

## ✅ A/B Testing = Cleanest Form of Causal Inference

- You randomly assign users to Control or Treatment.
- No need for covariate adjustment.
- Provides **unbiased estimates** of treatment effects.
- Often used in product development, UX, pricing tests.

> It is **causal inference by design**—minimal assumptions, maximum internal validity.

---

## 🧠 Causal Inference = Broader Framework

Causal inference tackles questions **where randomization is not possible**.

Includes methods like:
- Potential Outcomes / Rubin Causal Model
- DAGs and structural causal models
- Instrumental Variables
- Propensity Score Matching
- Regression Discontinuity
- Difference-in-Differences (DiD)

> All A/B testing is causal inference—but not all causal inference is A/B testing.

---

## 🎯 When to Use What?

| Use Case | Tool |
|----------|------|
| You can randomly assign users | **A/B Testing** |
| You can’t randomize (e.g. gender, platform) | **Causal Inference** |
| Product or UX experiments | A/B Testing |
| Observational data (e.g. historical logs) | Causal Inference methods |
| Estimating long-term impact across subgroups | Causal Inference |

---

## 💡 Example: Signup Flow Change

**You test a new onboarding flow:**
- Use A/B test to estimate impact on conversion.
- But some users skip onboarding → **non-compliance** → causal inference needed.
- Want to estimate effect **by geography or over time**? → Causal tools like DiD or stratified analysis.

---

## 📌 Summary

> A/B testing is a method within causal inference when randomization is available.
> Causal inference is the science of figuring out cause and effect—especially when you *can’t* randomize.

Both are essential. Together, they make you unstoppable. 🚀

