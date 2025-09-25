
# 🌱 Classification and Forecasting of Water Stress in Tomato Plant  
### 🔬 Predicting Water Stress Using Bioristor Data and Deep Learning Model (Streamlit Web App)

[![🚀 Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-success?logo=streamlit&logoColor=white&color=ff4b4b)](https://classification-and-forecasting-of-water-stress-in-tomato-plant.streamlit.app/)

This project is a **Streamlit web application** that predicts **drought stress in tomato plants** using 🌿 **Bioristor sensor data** and 🤖 **ML & DL models**. It classifies plant status and forecasts water stress conditions to help farmers 👩‍🌾 and researchers monitor tomato plant health efficiently.

---

## 📌 Project Workflow

1. **Importing necessary libraries**  
   Libraries such as `TensorFlow`, `Keras`, `Scikit-learn`, `Pandas`, `NumPy`, and `Matplotlib` are used for data processing, modeling, and visualization.

2. **Loading Tomato Plant Dataset**  
   The dataset containing sensor measurements is loaded for preprocessing and model training.

3. **Preprocessing**  
   - Scaling the features  
   - Splitting the dataset into training and testing sets  

4. **Training & Evaluating the Model**  
   - Building a deep learning model with Keras/TensorFlow  
   - Training on the preprocessed dataset  
   - Evaluating using metrics such as accuracy, confusion matrix, and classification report

5. **Making Predictions**  
   - Using the trained model to predict water stress conditions  
   - Insights can be used for irrigation scheduling and monitoring crop health

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
   - 🔄 **LSTM (Recurrent Neural Network)**  
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

### 🔮 Future Improvements
- 🚀 Integrate real-time IoT sensor feeds for live predictions.  
- 📈 Enhance time-series forecasting with hybrid **CNN-LSTM models**.  
- 📊 Add **Power BI/Excel dashboards** for farmer-friendly analytics.  
- 🔥 Integrate **more advanced deep learning models** like GRU or Transformer for better forecasting.

### 🏆 Results
- ✅ **LSTM** provided reliable water-stress forecasting for sequential sensor data. 
- ✅ **CNN** improved feature extraction from high-dimensional signals.
- 
## 🖼️ App Screenshots
🏠 Home Page – Upload Dataset & Preprocessing   
![Home Page](galary/Screenshot%202025-09-21%20164036.png)

🔮 Predictions – Drought status for test data  
![Prediction Output](galary/Screenshot%202025-09-21%20164132.png)

### 👨‍💻 Author
**LOMADA SIVA GANGI REDDY**  
💡 B.Tech CSE (Data Science), RGMCET (2021–2025)  
📍 Available for internships & Job offer
💌 Contact Me : 9346493592
📍 [LinkedIn](https://www.linkedin.com/in/lomada-siva-gangi-reddy-a64197280/) | [GitHub](https://github.com/shivareddy2002)

---
## 🗂️ Project Workflow Diagram

```mermaid
flowchart TD
    %% Dataset & Preprocessing
    A[📥 Load Dataset CSV] --> B[🧹 Data Preprocessing]
    B --> C{🔀 Split Data: Train/Test}

    %% ML & DL Models
    C -->|🏋️ Train| D1[🌳 Decision Tree]
    C -->|🏋️ Train| D2[🌲 Random Forest]
    C -->|🏋️ Train| D3[🔄 LSTM (Time-Series)]
    C -->|🏋️ Train| D4[🖼️ CNN (Feature Extraction)]

    %% Model Evaluation
    D1 --> E1[🧪 Evaluate Accuracy & Metrics]
    D2 --> E2[🧪 Evaluate Accuracy & Metrics]
    D3 --> E3[🧪 Evaluate Accuracy & Metrics]
    D4 --> E4[🧪 Evaluate Accuracy & Metrics]

    %% Predictions
    E1 --> F[🔮 Make Predictions 💧]
    E2 --> F
    E3 --> F
    E4 --> F

    %% Results Visualization & Insights
    F --> G[📊 Visualize Results & Metrics]
    G --> H[💡 Insights for Farmers & Researchers 🌱]

    %% Styling (optional for color differentiation)
    style D1 fill:#FFEB3B,stroke:#000,stroke-width:1px
    style D2 fill:#4CAF50,stroke:#000,stroke-width:1px
    style D3 fill:#2196F3,stroke:#000,stroke-width:1px
    style D4 fill:#FF5722,stroke:#000,stroke-width:1px
    style F fill:#9C27B0,stroke:#000,stroke-width:1px
