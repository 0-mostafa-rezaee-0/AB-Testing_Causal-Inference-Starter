## 📁 Folder: `notebooks/`

This is the **main interface for learners**, students, and recruiters. It’s where you:
- Walk through your thinking
- Show working code
- Teach and explore experimentation interactively

---

## 📄 File: `01_ab_test_simulation.ipynb`

This is your **flagship notebook** for Project 1:  
📘 **Simulate & Analyze Your First A/B Test**

It walks users through designing, running, and analyzing a simple binary-outcome A/B test using **simulation + inference**.

---

### 🧠 Notebook Outline (Section by Section)

| Section | Purpose |
|--------|---------|
| **1. Introduction to A/B Testing** | Teach basic A/B concepts, causality, and hypotheses |
| **2. Simulate Control vs Treatment** | Generate synthetic binary outcomes for 2 groups |
| **3. Manual Z-Test (First Principles)** | Compute pooled SE, Z-statistic, and p-value manually |
| **4. Scipy Validation** | Use `scipy.stats.ttest_ind` to confirm manual results |
| **5. Confidence Intervals** | Compute 95% CI for delta; visualize with error bars |
| **6. P-Value Distribution (FPR Demo)** | Run 1,000 null simulations; plot histogram of p-values |
| **7. What-If Scenarios** | Show how power, sample size, and effect size affect results |
| **8. Wrap-up** | Summarize decisions, tradeoffs, and caveats in experiment interpretation |

---

### 📌 Best Practices for the Notebook

✅ **Teaching Comments**
- Start each section with a markdown cell explaining what’s happening and why

✅ **Modular Code**
- Keep code readable and logical
- Use `scripts/abtest_utils.py` for function logic to keep notebook clean

✅ **Beautiful Plots**
- Use `matplotlib`/`seaborn` to visualize conversion rates, p-value histograms, CI bands

✅ **Interpretation Cells**
- After key output, add a markdown cell with takeaways:
  - “The p-value was 0.032, so we reject the null hypothesis at alpha = 0.05.”
  - “CI does not include 0 → statistically significant difference.”

✅ **Bonus (optional)**
- Add interactive widgets (e.g., sliders for MDE, sample size)
- Add citations or links to industry sources (Expedia, Microsoft, Airbnb)

---

### 👀 Where Recruiters Will Look

When a recruiter or senior DS opens this:
- They'll scroll quickly looking for **clarity**, **insight**, and **completeness**
- Clear cell markdowns and professional plots make a big difference
- Bonus points if you include:
  - Tradeoff discussion (false positives vs false negatives)
  - Real-world analogies (e.g., “a 1% lift at 1M users = 10K extra sales”)
