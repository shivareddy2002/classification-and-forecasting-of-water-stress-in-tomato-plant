<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:56ab2f,100:a8e063&height=220&section=header&text=Classification%20and%20Forecasting%20of%20Water%20Stress&desc=in%20Tomato%20Plant&fontSize=32&descSize=20&fontColor=ffffff&animation=fadeIn&fontAlignY=30"/>
</p>

This project predicts and forecasts water stress in tomato plants using Bioristor sensor data. 🌿It combines Decision Tree, Random Forest, LSTM, and CNN for accurate classification and forecasting. 🤖 An interactive Streamlit web app provides visual insights for farmers and researchers. 👩‍🌾

## 🔗 Live Demo  
<p align="center">🚀 Visit <strong>Water Stress Prediction WebApp</strong></p>
<p align="center">
  <a href="https://classification-and-forecasting-of-water-stress-in-tomato-plant.streamlit.app/">
    <img src="https://img.shields.io/badge/-Project%20DEMO-success?logo=streamlit&logoColor=white&color=ff4b4b&style=for-the-badge" alt="Streamlit App" height="50">
  </a>
</p>

---

## ✨ Key Highlights  
✔️ Forecasts drought stress in tomato plants using 🌿 **Bioristor sensor data**  
✔️ Implements **Decision Tree, Random Forest, LSTM, and CNN**  
✔️ Provides **visual insights for farmers & researchers** 👩‍🌾  
✔️ Interactive **Streamlit web app** for real-time prediction  

---

## 📌 Project Workflow  

### 🔵 Step 1: Importing Libraries  
📥 **Importing necessary libraries**  
`TensorFlow` • `Keras` • `Scikit-learn` • `Pandas` • `NumPy` • `Matplotlib`  

### 🟢 Step 2: Data Preparation  
🧹 **Loading & Preprocessing Dataset**  
- Scaling features  
- Splitting into training & testing sets

### 🟣 Step 3: Model Training & Evaluation  
🏋️ **Training & Evaluating Models**  
- ML: 🌳 Decision Tree, 🌲 Random Forest  
- DL: 🔄 LSTM, 🖼️ CNN  
- Metrics: ✅ Accuracy • 📉 Confusion Matrix • 🎯 F1-score  

### 🟠 Step 4: Predictions  
🔮 **Making Predictions**  
- Forecast drought conditions 🌦️  
- Recommend irrigation schedules 💧  

### 🔺 Step 5: Visualization  
📊 **Visualization of Results**  
- Charts 📈  
- Plots 📉  
- Performance comparison ⚖️  

### 🟡 Step 6: Insights & Recommendations  
💡 **Feature Insights**  
- Actionable recommendations for farmers 👨‍🌾👩‍🌾  
- Research support 🌱  
- Decision support for irrigation and water management 🚜💧  


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
✨ Interactive **performance metrics** and **visualizations** 📊 (Bar Charts & Tables).
✨ Predict drought status for **new sensor data** in real-time.

---
## 📈 Machine Learning & Deep Learning Models
| 🌟 Model                     | ⚡ Description                                   |
|-------------------------------|-------------------------------------------------|
| 🌳 Decision Tree  | Simple classifier based on tree splitting rules. |
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
- ✅ High accuracy achieved across ML/DL models  
- ✅ LSTM 🔄 & CNN 🖼️ improved performance on time-series forecasting  
- ✅ Visualization shows clear stress patterns in tomato plants 🌱  
- ✅ Helps farmers & researchers optimize irrigation 💧  

## 🖼️ Web App Screenshots
🏠 Home Page – Upload New Data & Preprocessing   
![Home Page](galary/Screenshot%202025-09-21%20164036.png)

🔮 Predictions – Drought status for New data  
![Prediction Output](galary/Screenshot%202025-09-21%20164132.png)

---

## 🔮 Future Improvements
- 🚀 Integrate real-time IoT sensor feeds for live predictions.  
- 📈 Enhance time-series forecasting with hybrid **CNN-LSTM models**.  
- 📊 Add **Power BI/Excel dashboards** for farmer-friendly analytics.  
- 🔥 Integrate **more advanced deep learning models** like GRU or Transformer for better forecasting.

---


## 🗂️ Project Workflow Diagram

```mermaid
flowchart TD
    %% Dataset & Preprocessing
    A[📥 Load Bioristor Data] --> B[🧹 Data Preprocessing]
    B --> C{🔀 Split Data: Train/Test}

    %% ML & DL Models
    C -->|🏋️ Train| D1[🌳 Decision Tree]
    C -->|🏋️ Train| D2[🌲 Random Forest]
    C -->|🏋️ Train| D3[🔄 LSTM -Time-Series]
    C -->|🏋️ Train| D4[🖼️ CNN -Feature Extraction]

    %% Model Evaluation
    D1 --> E1[🧪 Evaluate Accuracy & Metrics]
    D2 --> E2[🧪 Evaluate Accuracy & Metrics]
    D3 --> E3[🧪 Evaluate Accuracy & Metrics]
    D4 --> E4[🧪 Evaluate Accuracy & Metrics]

    %% Predictions
    F[🔮 Make Predictions 💧]
    E1 -->|Testing| F
    E2 -->|Testing| F
    E3 -->|Testing| F
    E4 -->|Testing| F

    %% Results Visualization & Insights
    F --> G[📊 Visualize Results & Metrics]
    G --> H[💡 Insights for Farmers & Researchers 🌱]

    %% Styling
    style A fill:#42A5F5,stroke:#0D47A1,stroke-width:2px,color:#fff
    style B fill:#66BB6A,stroke:#1B5E20,stroke-width:2px,color:#fff
    style C fill:#AB47BC,stroke:#4A148C,stroke-width:2px,color:#fff
    
    %% Models
    style D1 fill:#FFEB3B,stroke:#000,stroke-width:1px
    style D2 fill:#4CAF50,stroke:#000,stroke-width:1px
    style D3 fill:#2196F3,stroke:#000,stroke-width:1px
    style D4 fill:#FF5722,stroke:#000,stroke-width:1px

    %% Evaluation
    style E1 fill:#26C6DA,stroke:#006064,stroke-width:2px,color:#fff
    style E2 fill:#26C6DA,stroke:#006064,stroke-width:2px,color:#fff
    style E3 fill:#26C6DA,stroke:#006064,stroke-width:2px,color:#fff
    style E4 fill:#26C6DA,stroke:#006064,stroke-width:2px,color:#fff

    %% Predictions & Results
    style F fill:#9C27B0,stroke:#4A148C,stroke-width:2px,color:#fff
    style G fill:#F44336,stroke:#B71C1C,stroke-width:2px,color:#fff
    style H fill:#FFD54F,stroke:#F57F17,stroke-width:2px,color:#000
```
## 👨‍💻 Author  

**Lomada Siva Gangi Reddy**  
- 🎓 B.Tech CSE (Data Science), RGMCET (2021–2025)  
- 💡 Interests: Python | Machine Learning | Deep Learning | Data Science  
- 📍 Open to **Internships & Job Offers**

 **Contact Me**:  

- 📧 **Email**: lomadasivagangireddy3@gmail.com  
- 📞 **Phone**: 9346493592  
- 💼 [LinkedIn](https://www.linkedin.com/in/lomada-siva-gangi-reddy-a64197280/)  🌐 [GitHub](https://github.com/shivareddy2002)  🚀 [Portfolio](https://lsgr-portfolio-pulse.lovable.app/)

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:56ab2f,100:ff4b4b&height=120&section=footer"/>
</p>
