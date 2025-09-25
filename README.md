
# 🌱 Classification and Forecasting of Water Stress in Tomato Plant  
### 🔬 Using Bioristor Data and Machine Learning (Streamlit Web App)

[![🚀 Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-success?logo=streamlit&logoColor=white&color=ff4b4b)](https://classification-and-forecasting-of-water-stress-in-tomato-plant.streamlit.app/)

This project is a **Streamlit web application** that predicts **drought stress in tomato plants** using 🌿 **Bioristor sensor data** and 🤖 **machine learning models**.  
It classifies plant status and forecasts water stress conditions to help farmers 👩‍🌾 and researchers monitor tomato plant health efficiently.

---

## 🚀 Project Overview
Tomato 🍅 plants are highly sensitive to drought stress, which can significantly impact yield and quality.  
This app uses **Decision Tree**, **Random Forest**, and **MLPClassifier (Neural Network)** models to:
- ✅ Classify drought conditions (**No Drought / Drought**).
- ✅ Compare model performance using metrics like **Accuracy**, **Precision**, **Recall**, and **F1-score**.
- ✅ Predict water stress on **new, unseen test data**.

---

## 📊 Dataset
The application works with **Bioristor sensor data** collected from tomato plants.  
Example CSV format:
| feature1 | feature2 | ... | status | y |
|----------|----------|-----|-------|---|
| 0.12     | 0.85     | ... | Healthy | 0 |
| 0.09     | 0.70     | ... | Stressed| 1 |

- **`status`** → Plant health status (label for classification).  
- **`y`** → Drought condition (**0 = No Drought**, **1 = Drought**).  

---

## 🌟 Features
✨ Upload CSV datasets for training and testing.  
✨ Automatic **data preprocessing** (missing value handling & normalization).  
✨ Train and evaluate multiple ML algorithms:
   - 🌳 **Decision Tree (Gini & Entropy)**
   - 🌲 **Random Forest**
   - 🧠 **MLPClassifier (Neural Network)**  
✨ Interactive **performance metrics** and **visualizations** 📊 (Bar Charts & Tables).  
✨ Predict drought status for **new sensor data** in real-time.

---

## 🛠️ Tech Stack
- 🐍 **Programming Language:** Python 3.x  
- 🎯 **Frontend:** [Streamlit](https://streamlit.io/)  
- 🤖 **Machine Learning:** Scikit-learn  
- 📚 **Libraries:** Pandas, NumPy, Pickle, Matplotlib  

