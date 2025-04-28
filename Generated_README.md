# Bank-Customer-Churn-End-To-End-Project

---
## ✉️ Project overview
> This comprehensive project, "Bank-customer-churn-end-to-end-project," tackles the critical business problem of customer churn prediction. It leverages a robust data science pipeline, encompassing data ingestion, transformation, and model training using both machine learning (CatBoost, XGBoost, LightGBM) and deep learning approaches. The project meticulously documents the entire process, from exploratory data analysis (EDA) in Jupyter notebooks to model evaluation and deployment.  Furthermore, it incorporates a dedicated dashboard for insightful visualization, along with model serving applications. The project is well-structured, utilizing DVC for version control and including all necessary components to provide a complete and deployable solution.


---

## 🍵 Features

<code>❯ REPLACE-ME</code>

---

## 🗂️ Project Structure
```
Bank-customer-churn-end-to-end-project/
├── 📄 .dvcignore
├── 📄 app.py
├── 📄 Bank_Churn.csv
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 setup.py
├── 📄 template.py
├── 📄 test.py
├── 📁 .devcontainer
│   └── 📄 devcontainer.json
├── 📁 .dvc
│   └── 📄 config
├── 📁 artifacts
│   ├── 📄 deep_model.h5
│   ├── 📄 deep_model.json
│   ├── 📄 deep_model_history.txt
│   ├── 📄 deep_model_summary.txt
│   ├── 📄 deep_model_weights.weights.h5
│   ├── 📄 model.pkl
│   ├── 📄 preprocessor.pkl
│   ├── 📄 raw.csv.dvc
│   ├── 📄 test.csv
│   └── 📄 train.csv
├── 📁 catboost_info
│   ├── 📄 catboost_training.json
│   ├── 📄 learn_error.tsv
│   ├── 📄 time_left.tsv
│   └── 📁 learn
│       └── 📄 events.out.tfevents
├── 📁 Dashboard
│   └── 📁 Power Bi
│       └── 📄 Bank_customers_churn_dashboard.pbix
├── 📁 datascienceproject
│   ├── 📄 exception.py
│   ├── 📄 logger.py
│   ├── 📄 utils.py
│   ├── 📄 __init__.py
│   ├── 📁 components
│   │   ├── 📄 data_ingestion.py
│   │   ├── 📄 data_transformation.py
│   │   ├── 📄 deep_trainer.py
│   │   ├── 📄 model_evaluation.py
│   │   ├── 📄 model_trainer.py
│   │   └── 📄 __init__.py
│   └── 📁 piplines
│       ├── 📄 prediction_pipeline.py
│       ├── 📄 training_pipeline.py
│       └── 📄 __init__.py
├── 📁 deployment
│   ├── 📄 Deep_learning_app.py
│   ├── 📄 Machine_learning_app.py
│   ├── 📄 model.pkl
│   ├── 📄 preprocessor.pkl
│   └── 📄 requirements.txt
├── 📁 notebook
│   ├── 📄 1 . EDA.ipynb
│   ├── 📄 2 . MODEL TRAINING.ipynb
│   ├── 📁 catboost_info
│   │   ├── 📄 catboost_training.json
│   │   ├── 📄 learn_error.tsv
│   │   ├── 📄 time_left.tsv
│   │   └── 📁 learn
│   │       └── 📄 events.out.tfevents
│   └── 📁 data
│       └── 📄 raw.csv
└── 📁 Previews
    ├── 📄 churned_preview_machine_learning_model.png
    ├── 📄 not_churned_preview_machine_learning_model.png
    └── 📄 Power_bi_dashboard.png

```
---

## 🛠️ Technologies Used
This project uses:
- dvc
- h5
- json
- jupyter notebook
- pbix
- pkl
- png
- python
- tfevents
- tsv

---


## 📥 Installation

Install dependencies:

```bash
pip install -r requirements.txt
```



---