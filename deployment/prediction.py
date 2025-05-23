import streamlit as st
import pandas as pd
import pickle

# Load model dari file pickle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def run():
    # Title aplikasi
    st.title("Prediksi Risiko Penyakit Jantung")
    st.write("Masukkan data pasien untuk memprediksi risiko penyakit jantung.")

    # Input dari user sesuai dengan data yang diberikan
    age = st.number_input('Usia', min_value=1, max_value=120, value=30)
    gender = st.selectbox('Jenis Kelamin', ['Male', 'Female'])
    blood_pressure = st.number_input('Tekanan Darah', min_value=80, max_value=250, value=120)
    cholesterol = st.number_input('Kadar Kolesterol', min_value=100, max_value=400, value=200)
    exercise = st.selectbox('Kebiasaan Olahraga', ['Low', 'Medium', 'High'])
    smoking = st.selectbox('Merokok?', ['Yes', 'No'])
    family_history = st.selectbox('Riwayat Keluarga?', ['Yes', 'No'])
    diabetes = st.selectbox('Diabetes?', ['Yes', 'No'])
    bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, step=0.1, value=22.0)
    high_blood_pressure = st.selectbox('Tekanan Darah Tinggi?', ['Yes', 'No'])
    low_hdl_cholesterol = st.selectbox('Low HDL Cholesterol?', ['Yes', 'No'])
    high_ldl_cholesterol = st.selectbox('High LDL Cholesterol?', ['Yes', 'No'])
    alcohol = st.selectbox('Konsumsi Alkohol', ['Low', 'Medium', 'High'])
    stress = st.selectbox('Tingkat Stres', ['Low', 'Medium', 'High'])
    sleep = st.slider('Jam Tidur', min_value=1.0, max_value=12.0, step=0.5, value=7.0)
    sugar = st.selectbox('Konsumsi Gula', ['Low', 'Medium', 'High'])
    triglyceride = st.number_input('Triglyceride Level', min_value=50, max_value=500, value=150)
    fbs = st.number_input('Fasting Blood Sugar', min_value=50, max_value=250, value=90)
    crp = st.number_input('CRP Level', min_value=0.1, max_value=10.0, step=0.1, value=1.0)
    homocysteine = st.number_input('Homocysteine Level', min_value=5.0, max_value=50.0, value=15.0)

    # Susun ke DataFrame
    data_inf = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Blood Pressure': [blood_pressure],
        'Cholesterol Level': [cholesterol],
        'Exercise Habits': [exercise],
        'Smoking': [smoking],
        'Family Heart Disease': [family_history],
        'Diabetes': [diabetes],
        'BMI': [bmi],
        'High Blood Pressure': [high_blood_pressure],
        'Low HDL Cholesterol': [low_hdl_cholesterol],
        'High LDL Cholesterol': [high_ldl_cholesterol],
        'Alcohol Consumption': [alcohol],
        'Stress Level': [stress],
        'Sleep Hours': [sleep],
        'Sugar Consumption': [sugar],
        'Triglyceride Level': [triglyceride],
        'Fasting Blood Sugar': [fbs],
        'CRP Level': [crp],
        'Homocysteine Level': [homocysteine]
    })

    # Tombol Prediksi
    if st.button('Prediksi'):
        predict = model.predict(data_inf)
        
        # If prediction is 1, user has heart disease risk
        if predict == 1:
            st.write("## Prediksi Risiko Penyakit Jantung: Ya")
            st.write("Berdasarkan data yang Anda masukkan, model memprediksi bahwa Anda memiliki risiko penyakit jantung. Harap berkonsultasi dengan dokter untuk tindakan lebih lanjut.")
        # If prediction is 0, user is not at risk
        else:
            st.write("## Prediksi Risiko Penyakit Jantung: Tidak")
            st.write("Berdasarkan data yang Anda masukkan, model memprediksi bahwa Anda tidak memiliki risiko penyakit jantung. Tetap menjaga gaya hidup sehat.")

if __name__ == '__main__':
    run()