📁 Folder: `data/`

This folder is intended for **input/output datasets**, typically:

- Simulated control/treatment groups
- Real-world A/B test logs (in later projects)
- CSVs students or users can upload or analyze

---

## 📄 File: `synthetic_ab_test.csv`

### ✅ Expected Structure

This file contains the **simulated binary outcome data** from a simple A/B test.

| group     | converted |
| --------- | --------- |
| control   | 0         |
| control   | 1         |
| ...       | ...       |
| treatment | 0         |
| treatment | 1         |

### 🔍 Schema

| Column Name   | Type    | Description                               |
| ------------- | ------- | ----------------------------------------- |
| `group`     | string  | `'control'` or `'treatment'`          |
| `converted` | integer | `0` or `1` (simulated binary outcome) |

- Each row = one user
- `converted = 1` means the user converted (e.g., clicked, purchased, etc.)
- Equal sample size per group (e.g., 10,000 control + 10,000 treatment)

---

## 🧪 Example: First 10 Rows

```csv
group,converted
control,0
control,1
control,0
control,0
control,1
control,0
control,0
control,1
control,0
control,0
```

Once the treatment rows follow, you’ll see:

```csv
treatment,0
treatment,1
treatment,0
...
```

---

## 🛠 How It's Generated

It’s produced by this line in your notebook or `abtest_utils.py`:

```python
control, treatment = simulate_ab_test(n=10000, p_control=0.10, p_treatment=0.11)
```

Then written to CSV:

```python
data = pd.DataFrame({
    'group': ['control'] * n + ['treatment'] * n,
    'converted': np.concatenate([control, treatment])
})
data.to_csv('data/synthetic_ab_test.csv', index=False)
```

---

## 🧑‍🏫 Teaching Tip

Let students experiment with:

- Changing `n` (sample size)
- Adjusting `p_control`, `p_treatment`
- Introducing a **third group** (e.g., variant B)

Encourage them to visualize this data before running tests!

---

Would you like me to:

- Generate a ready-to-use version of `synthetic_ab_test.csv` now?
- Move on to review the `notebooks/` folder in this same level of detail?
