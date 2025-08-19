# Car Price Prediction

A Machine Learning project to predict car selling prices based on key features.  
Built with **Python**, **scikit-learn**, and  **Streamlit** for a simple web app.

---

## Repository Structure 
```
car-price-prediction/
├─ 01-data_cleaning/           # notebooks or scripts for cleaning
├─ 02-eda_car/                 # EDA notebooks/plots
├─ 03-implementation/          # modeling and evaluation
├─ car_price_app/              # Streamlit app (if applicable)
├─ data/                       # raw data (or link in README if not shareable)
├─ cleaned_car_data/           # processed data (optional)
├─ car_price_model.pkl         # saved trained model
├─ requirements.txt
└─ README.md
```



## Model
- Pipeline: preprocessing → feature engineering → **Random Forest Regressor** 


---

## Setup

1) **Clone** this repo
```bash
git clone https://github.com/<your-username>/car-price-prediction.git
cd car-price-prediction
```

2) **Create venv** 
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3) **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Run the Streamlit App
If you have the Streamlit app in `car_price_app`
```bash

streamlit run car_price_app.py
```

---



## Dataset
-The cleaned dataset used in this project is included in the repository:  
`cleaned_car_data.xlsx`

It contains 8 features (independent variables) and 1 target variable (selling price).  
---


## Author
**Sakshi Parit**  
LinkedIn: <https://www.linkedin.com/in/sakshi-parit>  
Email: <sakshiparit1920@gmail.com>


