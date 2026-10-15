# Sleep Debt Assessment

A machine-learning web application that estimates a user's sleep debt category from selected sleep metrics, bedtime screen habits, and lifestyle information. The project includes a Streamlit interface, exploratory data analysis (EDA), model development and evaluation notebooks, and a saved scikit-learn pipeline.

> **Educational-use notice:** This application provides a machine-learning estimate based on the project's dataset. It is not a medical device, medical diagnosis, or substitute for professional healthcare advice.

## Project features

- Collects sleep, screen-use, and lifestyle inputs through a Streamlit form.
- Predicts one of four sleep debt categories:
  - `Optimal Recovery`
  - `Mild Deficit`
  - `Moderate Debt`
  - `Severe Sleep Debt`
- Displays the predicted category and class probability information when supported by the loaded model.
- Includes EDA covering data quality, descriptive statistics, distributions, feature-target relationships, categorical associations, and outlier investigation.
- Compares Logistic Regression, Random Forest, and Decision Tree classifiers using cross-validation and hyperparameter search.
- Saves the selected preprocessing-and-model pipeline for use by the application.

## Technologies used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web application |
| pandas | Tabular data handling and prediction input |
| NumPy | Numerical operations in EDA |
| scikit-learn | Preprocessing, pipelines, classification, cross-validation, hyperparameter search, and evaluation |
| joblib | Saving and loading the fitted model pipeline |
| Matplotlib | Plot creation |
| Seaborn | Statistical data visualizations |
| SciPy | Statistical tests used in EDA |
| Jupyter Notebook / IPython kernel | Running the EDA and model-development notebooks |

## Project structure

This layout reflects the files currently included in the project archive:

```text
Halo_Sleep-Debt-Predictor/
├── .streamlit/
│   └── config.toml
├── app.py
├── data/
│   └── bedtime_screentime_sleep_debt.csv
├── models/
│   └── sleep_debt_model.pkl
├── notebooks/
│   ├── EDA.ipynb
│   └── Preprocessing,_Training,_and_Evaluation.ipynb
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.11 is recommended because the notebooks were created with Python 3.11.9.
- `pip`
- The project files shown in the structure above.

**Model compatibility:** The supplied `models/sleep_debt_model.pkl` was serialized with scikit-learn 1.9.1. The requirements file pins scikit-learn to that version because scikit-learn does not guarantee that serialized estimators are compatible across versions. Use the same version to load the supplied model, or retrain and resave the model in your intended deployment environment.

## Installation

### 1. Open the project directory

Open a terminal in the `ML Proj` directory, where `app.py`, `data/`, `models/`, and `notebooks/` are located.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell does not allow activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

**macOS/Linux:**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the Streamlit app

From the project root, run:

```bash
python -m streamlit run app.py
```

Streamlit prints a local address, normally `http://localhost:8501`. Open that address in your browser.

The app loads the saved pipeline from `models/sleep_debt_model.pkl`. Run the command from the project root because the current `app.py` uses a relative model path.

## Run the notebooks

With the virtual environment activated, launch Jupyter:

```bash
python -m jupyter lab
```

Or:

```bash
python -m jupyter notebook
```

Open and run:

- `notebooks/EDA.ipynb` for exploratory data analysis.
- `notebooks/Preprocessing,_Training,_and_Evaluation.ipynb` for preprocessing, model comparison, tuning, evaluation, and saving the selected model.

### Retraining the model

The training notebook saves the selected Random Forest pipeline to:

```text
models/sleep_debt_model.pkl
```

When the notebook runs from the `notebooks/` directory, its current save path is `../models/sleep_debt_model.pkl`. Retraining overwrites the model artifact, so keep a backup if you need to preserve the existing version.

## Model and prediction workflow

1. The user enters the required sleep metrics, screen-use values, and lifestyle categories.
2. The Streamlit app assembles the values into a pandas DataFrame using the feature names expected by the model.
3. The saved scikit-learn pipeline applies the fitted numerical scaling and categorical encoding, then generates the classification.
4. The app displays the predicted sleep debt category and class probabilities when the loaded estimator supports `predict_proba`.

Because preprocessing is already part of the saved pipeline, do not manually scale or one-hot encode app inputs before calling `model.predict()`.

The training notebook compares Logistic Regression, Random Forest, and Decision Tree classifiers using stratified cross-validation and GridSearchCV. Macro-F1 is used as the refit metric, with accuracy, macro precision, and macro recall also recorded.
