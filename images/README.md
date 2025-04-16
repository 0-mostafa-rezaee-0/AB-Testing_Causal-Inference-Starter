📁 Folder: `images/`

This folder is used to store **visual outputs** of your analysis. These help:

- Enrich your `README.md` and Jupyter notebooks
- Communicate results visually (critical in experimentation)
- Provide polished visuals for portfolios or slide decks

---

## 📄 Suggested Image Files

### ✅ 1. `conversion_bar_ci.png`

> 📊 **Bar chart of conversion rates with 95% confidence intervals**

- X-axis: group (`Control`, `Treatment`)
- Y-axis: observed conversion rate
- Error bars: ±1.96 * standard error
- Optional: include delta or lift value as title/subtitle

This image comes from code like:

```python
plt.bar(['Control', 'Treatment'], [...], yerr=[...])
plt.savefig('images/conversion_bar_ci.png')
```

---

### ✅ 2. `pvalue_distribution.png`

> 📉 **Histogram of p-values under the null hypothesis**

- X-axis: p-values from 1,000 simulations where p_control == p_treatment
- Y-axis: frequency count
- Dashed line at `alpha = 0.05`

Purpose: visually demonstrate the **false positive rate**

---

### 🔁 Optional Future Images

You might add later:

| Filename                        | Description                                 |
| ------------------------------- | ------------------------------------------- |
| `bootstrap_lift_dist.png`     | Histogram of bootstrapped treatment effects |
| `ci_width_vs_sample_size.png` | Line plot of CI width vs sample size        |
| `fpr_vs_alpha.png`            | False positive rate as a function of alpha  |

These would be great for teaching statistical intuition and sharing deeper insights in your GitHub repo or talks.

---

## 📸 Best Practices for Image Files

- Use **transparent, descriptive filenames**
- Always call `plt.tight_layout()` before saving
- Save at **high resolution** (e.g., `dpi=150`) if you plan to embed them on LinkedIn or Notion
- Keep versions used in README in sync with code—not stale


