
# 🌱 Classification and Forecasting of Water Stress in Tomato Plant  
### 🔬 Predicting Water Stress Using Bioristor Data and Deep Learning Model (Streamlit Web App)

[![🚀 Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-success?logo=streamlit&logoColor=white&color=ff4b4b)](https://classification-and-forecasting-of-water-stress-in-tomato-plant.streamlit.app/)

## ✨ Highlights  
✔️ Forecasts drought stress in tomato plants using 🌿 **Bioristor sensor data**  
✔️ Implements **Decision Tree, Random Forest, LSTM, and CNN**  
✔️ Provides **visual insights for farmers & researchers** 👩‍🌾  
✔️ Interactive **Streamlit web app** for real-time prediction  

---

## Project Workflow

🔹 📥 Importing libraries & dataset
🔹 🧹 Data Preprocessing (scaling, cleaning, splitting)
🔹 🏋️ Model Training (Decision Tree 🌳, Random Forest 🌲, LSTM 🔄, CNN 🖼️)
🔹 🧪 Evaluation Metrics (accuracy,precision,recall,f1-score)
🔹 🔮 Prediction (forecast water stress levels 💧)
🔹 📊 Visualization (charts, plots, comparison)
🔹 💡 Insights (recommendations for farmers & researchers 🌱)

---

## 🛠️ Requirements

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-orange?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24%2B-blue?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.2%2B-blue?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20%2B-blue?logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4%2B-orange?logo=matplotlib&logoColor=white)](https://matplotlib.org/)

---
## 📊 Dataset
The application works with **Bioristor sensor data** collected from tomato plants.  
Example CSV format:
| feature1 | feature2 | ... | status | y |
|----------|----------|-----|-------|---|
| 0.12     | 0.85     | ... | Healthy | 0 |
| 0.09     | 0.70     | ... | Stressed| 1 |

- **`status`** → Plant health status (**Healthy, Uncertainty, Recovery, Stress**).  
- **`y`** → Drought condition (**0 = No Drought**, **1 = Drought**).  

---

## 🌟 Features
✨ Upload CSV datasets for training and testing.  
✨ Automatic **data preprocessing** (missing value handling & normalization).  
✨ Train and evaluate multiple ML algorithms:
   - 🌳 **Decision Tree**
   - 🌲 **Random Forest**
   - 🔄 **LSTM (Long Short Term Memory)**  
   - 🖼️ **CNN (Convolutional Neural Network)**
   - ✨ Interactive **performance metrics** and **visualizations** 📊 (Bar Charts & Tables).
   - ✨ Predict drought status for **new sensor data** in real-time.

---
## 📈 Machine Learning & Deep Learning Models
| 🌟 Model                     | ⚡ Description                                   |
|-------------------------------|-------------------------------------------------|
| 🌳 Decision Tree (Gini/Entropy) | Simple classifier based on tree splitting rules. |
| 🌲 Random Forest             | Ensemble of decision trees for higher accuracy. |
| 🔄 LSTM                      | Recurrent neural network for sequential/time-series sensor data. |
| 🖼️ CNN                       | Convolutional neural network for feature extraction from sensor patterns. |

---

## 🛠️ Tech Stack
- 🐍 **Programming Language:** Python 
- 🎯 **Frontend:** Streamlit  
- 🤖 **ML & DL :** DecisionTree, RandomForest, LSTM, CNN
- 📚 **Libraries:** Pandas, NumPy, Matplotlib ,Scikit-learn,Tensorflow   


## 🏆 Results
✅ High accuracy achieved across ML/DL models
✅ LSTM 🔄 & CNN 🖼️ improved performance on time-series forecasting
✅ Visualization shows clear stress patterns in tomato plants 🌱
✅ Helps farmers & researchers optimize irrigation 💧

## 🖼️ App Screenshots
🏠 Home Page – Upload Dataset & Preprocessing   
![Home Page](galary/Screenshot%202025-09-21%20164036.png)

🔮 Predictions – Drought status for test data  
![Prediction Output](galary/Screenshot%202025-09-21%20164132.png)

---

## 🔮 Future Improvements
- 🚀 Integrate real-time IoT sensor feeds for live predictions.  
- 📈 Enhance time-series forecasting with hybrid **CNN-LSTM models**.  
- 📊 Add **Power BI/Excel dashboards** for farmer-friendly analytics.  
- 🔥 Integrate **more advanced deep learning models** like GRU or Transformer for better forecasting.

---

## 👨‍💻 Author
**LOMADA SIVA GANGI REDDY**  
💡 B.Tech CSE (Data Science), RGMCET (2021–2025)  
📍 Available for internships & Job offer
💌 Contact Me : 9346493592
📍 [LinkedIn](https://www.linkedin.com/in/lomada-siva-gangi-reddy-a64197280/) | [GitHub](https://github.com/shivareddy2002)

---

## 🗂️ Project Workflow Diagram

```mermaid
flowchart TD
    %% Step 1: Importing Libraries
    A[🔵 Step 1: 📥 Import Libraries] --> B[🟢 Step 2: 🧹 Data Preparation]

    %% Step 2: Data Preparation
    B --> C[🟣 Step 3: 🏋️ Model Training & Evaluation]

    %% Step 3: Models
    C --> C1[🌳 Decision Tree]
    C --> C2[🌲 Random Forest]
    C --> C3[🔄 LSTM]
    C --> C4[🖼️ CNN]

    %% Step 4: Predictions
    C1 --> D[🟠 Step 4: 🔮 Predictions]
    C2 --> D
    C3 --> D
    C4 --> D

    %% Step 5: Visualization
    D --> E[🔺 Step 5: 📊 Visualization]

    %% Step 6: Insights
    E --> F[🟡 Step 6: 💡 Insights & Recommendations 🌱]

    %% Styling for Color-Coding
    style A fill:#42A5F5,stroke:#0D47A1,stroke-width:2px,color:#fff
    style B fill:#66BB6A,stroke:#1B5E20,stroke-width:2px,color:#fff
    style C fill:#AB47BC,stroke:#4A148C,stroke-width:2px,color:#fff
    style C1 fill:#FFEB3B,stroke:#000,stroke-width:1px
    style C2 fill:#4CAF50,stroke:#000,stroke-width:1px
    style C3 fill:#2196F3,stroke:#000,stroke-width:1px
    style C4 fill:#FF5722,stroke:#000,stroke-width:1px
    style D fill:#FF7043,stroke:#BF360C,stroke-width:2px,color:#fff
    style E fill:#F44336,stroke:#B71C1C,stroke-width:2px,color:#fff
    style F fill:#FFD54F,stroke:#F57F17,stroke-width:2px,color:#000

