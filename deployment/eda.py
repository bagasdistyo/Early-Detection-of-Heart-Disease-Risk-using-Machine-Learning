import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

# Membaca data
df = pd.read_csv('https://raw.githubusercontent.com/bagasdistyo/datapenyakit/refs/heads/main/heart_disease.csv')

# Fungsi untuk histogram semua kolom numerik
def plot_numerical_histograms():
    numerical_cols = df.select_dtypes(include='number').columns
    st.subheader("Distribusi Kolom Numerik")
    
    for col in numerical_cols:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color='steelblue')
        ax.set_title(f'Distribusi: {col}')
        st.pyplot(fig)

# Fungsi-fungsi visualisasi lainnya tetap seperti sebelumnya
def plot_lifestyle_impact():
    fig, axes = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle('Pengaruh Gaya Hidup terhadap Penyakit Jantung', fontsize=16)

    sns.countplot(x='Exercise Habits', hue='Heart Disease Status', data=df, ax=axes[0, 0])
    axes[0, 0].set_title('Exercise Habits vs Heart Disease')

    sns.countplot(x='Smoking', hue='Heart Disease Status', data=df, ax=axes[0, 1])
    axes[0, 1].set_title('Smoking vs Heart Disease')

    sns.countplot(x='Alcohol Consumption', hue='Heart Disease Status', data=df, ax=axes[1, 0])
    axes[1, 0].set_title('Alcohol Consumption vs Heart Disease')

    sns.countplot(x='Sugar Consumption', hue='Heart Disease Status', data=df, ax=axes[1, 1])
    axes[1, 1].set_title('Sugar Consumption vs Heart Disease')

    sns.countplot(x='Stress Level', hue='Heart Disease Status', data=df, ax=axes[2, 0])
    axes[2, 0].set_title('Stress Level vs Heart Disease')

    axes[2, 1].axis('off')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    st.pyplot(fig)

def plot_health_variables_impact():
    variables = ['Blood Pressure', 'Cholesterol Level', 'Triglyceride Level', 
                 'Fasting Blood Sugar', 'CRP Level', 'Homocysteine Level']
    fig, axes = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle('Pengaruh Variabel Kesehatan terhadap Penyakit Jantung', fontsize=16)

    for i, var in enumerate(variables):
        ax = axes[i // 2, i % 2]
        sns.boxplot(x='Heart Disease Status', y=var, data=df, ax=ax)
        ax.set_title(f'{var} vs Heart Disease')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    st.pyplot(fig)

def plot_age_bmi_impact():
    variables = ['Age', 'BMI']
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    fig.suptitle('Pengaruh Usia dan BMI terhadap Penyakit Jantung', fontsize=16)

    for i, var in enumerate(variables):
        ax = axes[i]
        sns.boxplot(x='Heart Disease Status', y=var, data=df, ax=ax)
        ax.set_title(f'{var} vs Heart Disease')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    st.pyplot(fig)

def plot_family_heart_disease():
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.countplot(x='Family Heart Disease', hue='Heart Disease Status', data=df, ax=ax)
    ax.set_title('Family Heart Disease vs Heart Disease')
    plt.tight_layout()
    st.pyplot(fig)

def plot_heart_disease_distribution():
    counts = df['Heart Disease Status'].value_counts()
    labels = ['No Heart Disease', 'Heart Disease']
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'salmon'])
    plt.title('Distribusi Penyakit Jantung')
    plt.axis('equal')
    st.pyplot(plt)

def plot_heart_disease_by_gender():
    df_gender = df[['Gender', 'Heart Disease Status']].dropna()
    prop_gender = pd.crosstab(df_gender['Gender'], df_gender['Heart Disease Status'], normalize='index') * 100
    heart_disease_by_gender = prop_gender['Yes']
    plt.figure(figsize=(6, 6))
    colors = ['lightblue', 'salmon']
    heart_disease_by_gender.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Proporsi Penderita Penyakit Jantung berdasarkan Gender')
    plt.ylabel('')
    st.pyplot(plt)

def plot_sleep_hours_impact():
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Heart Disease Status', y='Sleep Hours', data=df)
    plt.title('Distribusi Jam Tidur Berdasarkan Status Penyakit Jantung')
    st.pyplot(plt)

# Fungsi untuk histogram kolom numerik terpilih
def plot_selected_histogram(selected_columns):
    for col in selected_columns:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color='steelblue')
        ax.set_title(f'Distribusi: {col}')
        st.pyplot(fig)

# Fungsi utama aplikasi
def run():
    st.title('Aplikasi Prediksi Penyakit Jantung Rumah Sakit XYZ')
    st.subheader("Halaman ini menyajikan Exploratory Data Analysis (EDA) dari dataset Heart Disease")

    image = Image.open('gambar.jpg')
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption='EDA Heart Disease', use_container_width=True)

    st.write("""
    ### Deskripsi Dataset
    Dataset ini berisi berbagai indikator kesehatan dan faktor risiko yang berkaitan dengan penyakit jantung. Data dikumpulkan dari berbagai pasien untuk menganalisis risiko dan pola penyakit jantung.

    **Kolom-kolom dalam dataset ini meliputi:**
    - **Age**: Usia individu.
    - **Gender**: Jenis kelamin (Male atau Female).
    - **Blood Pressure**: Tekanan darah sistolik.
    - **Cholesterol Level**: Total kadar kolesterol.
    - **Exercise Habits**: Kebiasaan olahraga (Low, Medium, High).
    - **Smoking**: Status merokok (Yes atau No).
    - **Family Heart Disease**: Riwayat keluarga dengan penyakit jantung.
    - **Diabetes**: Status diabetes (Yes atau No).
    - **BMI**: Indeks massa tubuh.
    - **High Blood Pressure**: Memiliki tekanan darah tinggi atau tidak.
    - **Low HDL Cholesterol**: HDL rendah atau tidak.
    - **High LDL Cholesterol**: LDL tinggi atau tidak.
    - **Alcohol Consumption**: Konsumsi alkohol (None, Low, Medium, High).
    - **Stress Level**: Tingkat stres (Low, Medium, High).
    - **Sleep Hours**: Jumlah jam tidur.
    - **Sugar Consumption**: Konsumsi gula (Low, Medium, High).
    - **Triglyceride Level**: Kadar trigliserida.
    - **Fasting Blood Sugar**: Gula darah saat puasa.
    - **CRP Level**: C-reactive protein (indikator peradangan).
    - **Homocysteine Level**: Kadar homosistein.
    - **Heart Disease Status**: Apakah individu memiliki penyakit jantung (Yes atau No).
    """)

    st.dataframe(df)

    st.subheader("EDA")
    option = st.selectbox("Pilih EDA untuk ditampilkan:", 
                          ["Pengaruh Gaya Hidup", "Pengaruh Variabel Kesehatan", "Pengaruh Usia dan BMI", 
                           "Dampak Riwayat Keluarga", "Distribusi Penyakit Jantung", 
                           "Proporsi Penyakit Jantung Berdasarkan Gender", "Pengaruh Jam Tidur"])

    if option == "Pengaruh Gaya Hidup":
        plot_lifestyle_impact()
    elif option == "Pengaruh Variabel Kesehatan":
        plot_health_variables_impact()
    elif option == "Pengaruh Usia dan BMI":
        plot_age_bmi_impact()
    elif option == "Dampak Riwayat Keluarga":
        plot_family_heart_disease()
    elif option == "Distribusi Penyakit Jantung":
        plot_heart_disease_distribution()
    elif option == "Proporsi Penyakit Jantung Berdasarkan Gender":
        plot_heart_disease_by_gender()
    elif option == "Pengaruh Jam Tidur":
        plot_sleep_hours_impact()
    
    st.subheader("Histogram Kolom Numerik")

    numerical_cols = df.select_dtypes(include='number').columns.tolist()
    selected_columns = st.multiselect("Pilih kolom numerik untuk ditampilkan histogramnya:", numerical_cols)

    if selected_columns:
        plot_selected_histogram(selected_columns)
    else:
        st.info("Silakan pilih satu atau lebih kolom numerik di atas untuk melihat histogramnya.")

if __name__ == '__main__':
    run()
