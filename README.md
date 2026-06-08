# 🐼 Pandas 30 Days Practice Challenge

Welcome to my **Pandas 30 Days Practice Challenge** repository! This project documents my structured, daily journey to mastering data manipulation, exploration, and engineering using Python and the **Pandas** library. 

As an aspiring Data Engineer, this challenge focuses on building muscle memory for handling real-world datasets, optimizing data workflows, and preparing data pipelines for downstream analytical environments.

## 🚀 Project Overview

The objective of this challenge is to move from basic DataFrame operations to advanced data transformation techniques, addressing common data engineering challenges such as handling missing values, encoding categorical variables, structural reshaping, and aggregating large datasets.

### 🛠️ Tech Stack & Tools
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy
- **Environment:** Jupyter Notebooks (`.ipynb`)
- **Version Control:** Git & GitHub

---

## 📅 Challenge Roadmap & Progress Tracker

Below is the structured breakdown of the concepts covered throughout the 30-day challenge:

| Day | Topic / Core Concept | Notebook Link / Key Focus | Status |
| :---: | :--- | :--- | :---: |
| **01** | Introduction to Pandas Series & DataFrames | Creating structures from lists, dicts, and arrays | ✔️ |
| **02** | Advanced DataFrame Filtering | Boolean indexing, `.loc[]`, `.iloc[]`, and multi-conditional queries | ✔️ |
| **03** | Data Inspection & Summary Statistics | `.info()`, `.describe()`, `.value_counts()`, and memory usage | ✔️ |
| **04** | Handling Missing Data (Part 1) | Identifying nulls, dropping rows/columns (`.dropna()`) | ✔️ |
| **05** | Handling Missing Data (Part 2) | Basic imputation strategies (`.fillna()`, mean/median/mode) | ✔️ |
| **06** | String Data Manipulations | `.str` accessor, string cleaning, splitting, and replacing |✔️  |
| **07** | Renaming & Reordering Columns | Axis mapping, cleaning column whitespace, and case formatting | ✔️ |
| **08** | Dropping and Adding Columns | Dynamic feature engineering and memory cleanup | ✔️ |
| **09** | Sorting & Ranking Data | Multi-column sorting and assigning rank methodologies | ✔️ |
| **10** | Categorical Encoding & Imputation | Ordinal encoding, `get_dummies()`, and forward/backward filling |✔️  |
| **11** | GroupBy Mechanics (Basic) | Split-apply-combine paradigm and basic aggregations |✔️  |
| **12** | Advanced GroupBy & `.agg()` | Named aggregations and custom aggregation functions | ✔️ |
| **13** | Transforming Data with `.transform()` | Broadcasted group statistics and group-level data scaling | ✔️ |
| **14** | Filtering Groups with `.filter()` | Excluding groups based on aggregate conditions | ✔️ |
| **15** | Merging Datasets (Joins) | Inner, Left, Right, and Outer joins using `.merge()` | ✔️ |
| **16** | Concatenating & Appending Data | Axis-wise concatenation with `.concat()` |  |
| **17** | Reshaping Data: Melt | Pivoting data from wide format to long format |  |
| **18** | Reshaping Data: Pivot Tables | Aggregating long format data into wide summaries |  |
| **19** | Working with DateTime Data (Part 1) | Parsing dates, extracting components (year, month, day) |  |
| **20** | Working with DateTime Data (Part 2) | Time-series slicing, rolling windows, and resampling |  |
| **21** | Mapping & Replacing Values | Utilizing `.map()`, `.replace()`, and dictionary mappings |  |
| **22** | Element-wise Operations | Custom transformations using `.apply()` and `.applymap()` |  |
| **23** | Vectorized Operations with NumPy | Optimizing execution speed with `np.where()` and vector math |  |
| **24** | Handling Duplicates | Identifying, flagging, and removing duplicate records |  |
| **25** | Working with Outliers | Detection via IQR/Z-score and capping techniques |  |
| **26** | Reading & Writing Diverse Formats | Optimizing I/O performance (CSV, Excel, JSON, Parquet) |  |
| **27** | Multi-Indexing (Hierarchical) | Creating, slicing, and unstacking MultiIndex DataFrames |  |
| **28** | Memory Optimization Strategies | Downcasting data types and utilizing `category` types |  |
| **29** | Method Chaining Techniques | Writing clean, readable, pipeline-style Pandas code |  |
| **30** | Capstone Mini-Project | Building an end-to-end ET(L) pipeline on a dirty dataset |  |

---

## 💡 Key Takeaways & Highlights

* **Jupyter Notebook Tip:** To maintain clean version control history and prevent large JSON merge conflicts, always clear cell outputs (`Cell` -> `All Output` -> `Clear`) before staging files to Git.
* **Data Engineering Focus:** Special emphasis is placed on preparing data for database integration (PostgreSQL) and downstream data modeling workflows.

## 🛠️ Local Setup Instructions

To run these notebooks locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/HoseaMutwiri/Pandas_30_Days_Practice_Challenge.git](https://github.com/HoseaMutwiri/Pandas_30_Days_Practice_Challenge.git)
   cd Pandas_30_Days_Practice_Challenge
