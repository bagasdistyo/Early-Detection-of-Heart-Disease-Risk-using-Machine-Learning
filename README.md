# 🫀 Prediksi Risiko Penyakit Jantung


## Repository Outline
1. README.md - Penjelasan gambaran umum project
2. P1M2_bagas_distyo.ipynb - Notebook yang berisi pengolahan data dan pembuatan model dengan Python
3. P1M2_bagas_distyo_inf.ipynb - Notebook yang berisi pengujian data baru pada model yang sudah dibuat
4. Url.txt - Berisi URL dataset dan URL deployment
5. app.py - Model deployment untuk menjalankan EDA dan prediksi
6. eda.py - Model deployment untuk menampilkan EDA
7. predict.py - Model deployment untuk memprediksi data
8. model.pkl - Berisi model yang sudah dibuat dari P1M2_bagas_distyo.ipynb

## 📌 Problem Background
Penyakit jantung merupakan penyebab utama kematian di dunia. Salah satu tantangan di dunia medis adalah kurangnya deteksi dini terhadap pasien yang berisiko tinggi, yang bisa berakibat fatal karena keterlambatan penanganan. Project ini bertujuan untuk membangun sistem prediksi berbasis machine learning menggunakan data indikator kesehatan pasien di Rumah Sakit XYZ. Sistem ini diharapkan mampu membantu tenaga medis dalam pengambilan keputusan klinis secara cepat dan akurat, sekaligus meminimalkan kasus false negative dalam waktu 3 bulan ke depan.

## 🎯 Project Output
Sistem prediksi berbasis web menggunakan model machine learning (SVM) yang mampu mengidentifikasi risiko penyakit jantung berdasarkan input data kesehatan pasien. Aplikasi ini memberikan hasil klasifikasi serta rekomendasi kepada pasien dan dapat digunakan sebagai alat bantu diagnosis oleh tenaga medis.

## 📊 Data
Data diambil dari kaggle yang terdiri dari 10.000 data pasien dengan berbagai indikator kesehatan seperti:
- Age, Gender, Blood Pressure, Cholesterol Level
- Exercise Habits, Smoking, Family Heart Disease
- Diabetes, BMI, High Blood Pressure
- Low HDL Cholesterol, High LDL Cholesterol
- Alcohol Consumption, Stress Level, Sleep Hours
- Sugar Consumption, Triglyceride Level
- Fasting Blood Sugar, CRP Level, Homocysteine Level
- Heart Disease Status (label target)

## 🧠 Method
Project ini menggunakan pendekatan supervised classification dengan lima algoritma:
1. K-Nearest Neighbors (KNN)
2. Support Vector Machine (SVM)
3. Decision Tree
4. Random Forest
5. XGBoost
Model dievaluasi berdasarkan recall score untuk meminimalkan false negative (kasus pasien sakit yang tidak terdeteksi). Hasil evaluasi menunjukkan bahwa SVM memberikan performa paling stabil, bahkan dengan parameter default. Model ini kemudian dioptimasi melalui:
- Hyperparameter tuning
- Class imbalance handling menggunakan SMOTENC
- Validasi akhir menggunakan Cross-validation dan recall

## 🛠️ Stacks
- Bahasa Pemrograman: Python
- Libraries: scikit-learn, xgboost, pandas, numpy, matplotlib, seaborn, imbalanced-learn
- Tools: VSCode
- Deployment: Streamlit
