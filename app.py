# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Attrition Prediction </h1>", unsafe_allow_html=True)
st.markdown('---'*10)

# Load model
my_model = pickle.load(open('model_klasifikasi_terbaik.pkl', 'rb'))

# Pilihan utama

pilihan = st.selectbox('Apa yang ingin Anda lakukan?',['Prediksi dari file csv','Input Manual'])

if pilihan == 'Prediksi dari file csv':
    # Mengupload file
    upload_file = st.file_uploader('Pilih file csv', type='csv')
    if upload_file is not None:
        dataku = pd.read_csv(upload_file)
        st.write(dataku)
        st.success('File berhasil diupload')
        hasil = my_model.predict(dataku)
        #st.write('Prediksi',hasil)
        # Keputusan
        for i in range(len(hasil)):
            if hasil[i] == 1:
                st.write('Attrition',dataku['Attrition'][i],'= diprediksi akan KELUAR PERUSAHAAN')
            else:
                st.write('Attrition',dataku['Attrition'][i],'= diprediksi akan STAY DI PERUSAHAAN')
    else:
        st.error('File yang diupload kosong, silakan pilih file yang valid')
        #st.markdown('File yang diupload kosong, silakan pilih file yang valid')
else:
   # Baris Pertama
    with st.container():
        col1, col2 = st.columns(2)
    with col1:
        Age = st.number_input('Age', value=25)
    with col2:
        BusinessTravel = st.selectbox('BusinessTravel', ['Non_Travel', 'Travel_Rarely', 'Travel_Frequently'])     
   # Baris Kedua
    with st.container():
        col1, col2 = st.columns(2)
    with col1:
        DistanceFromHome = st.number_input('DistanceFromHome', value=5)
    with col2:
        Education = st.selectbox('Education', [1, 2, 3, 4, 5])

   # Baris Ketiga
    with st.container():
       col1, col2, col3 = st.columns(3)
    with col1:
       JobSatisfaction = st.selectbox('JobSatisfaction', [1, 2, 3,4])
    with col2:
       JobInvolvement = st.selectbox('JobInvolvement', [1, 2, 3,4])        
    with col3:
       JobLevel = st.selectbox('Level',[1, 2, 3,4,5])        
   # Baris Keempat
    with st.container():
        col1, col2, col3 = st.columns(3)
    with col1:
        MaritalStatus = st.selectbox('MaritalStatus',['Divorced', 'Married', 'Single'])    
    with col2:
        MonthlyIncome = st.number_input('MonthlyIncome', value=10000.0)
    with col3:
        EducationField = st.selectbox('EducationField',['Life Sciences', 'Medical', 'Human Resources', 'Marketing','Other', 'Technical Degree'])
       
   # Baris Kelima
    with st.container():
        col1, col2, col3 = st.columns(3)
    with col1:
        TotalWorkingYears = st.number_input('TotalWorkingYears', value=5)
    with col2:
        YearsAtCompany = st.number_input('YearsAtCompany', value=5) 
    with col3:
        OverTime = st.selectbox('OverTime',[1, 0])

    # Baris Keenam
    with st.container():
        col1, col2, col3 = st.columns(3)
    with col1:
        DailyRate = st.number_input('DailyRate', value=500)
    with col2:
        EmployeeCount = st.number_input('EmployeeCount', value=1) 
    with col3:
        EnvironmentSatisfaction = st.selectbox('EnvironmentSatisfaction',[1, 2, 3, 4])

    # Baris Ketujuh
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
    with col1:
        HourlyRate = st.number_input('HourlyRate', value=50)
    with col2:
        MonthlyRate = st.number_input('MonthlyRate', value=5000) 
    with col3:
        NumCompaniesWorked = st.selectbox('NumCompaniesWorked',[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    with col4:
        PercentSalaryHike = st.number_input('PercentSalaryHike', value=20)

    # Baris Kedelapan
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        PerformanceRating = st.selectbox('PerformanceRating',[3, 4])
    with col2:
        RelationshipSatisfaction = st.selectbox('RelationshipSatisfaction',[1, 2, 3, 4]) 
    with col3:
        StandardHours = st.selectbox('StandardHours',[80])
    with col4:
        StockOptionLevel = st.selectbox('StockOptionLevel',[0, 1, 2, 3])
    with col5:
        TrainingTimesLastYear = st.selectbox('TrainingTimesLastYear',[0, 1, 2, 3])


    # Baris Kesembilan
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
    with col1:
        WorkLifeBalance = st.selectbox('WorkLifeBalance',[1, 2, 3, 4])
    with col2:
        YearsInCurrentRole = st.number_input('YearsInCurrentRole', value=5) 
    with col3:
        YearsSinceLastPromotion = st.number_input('YearsSinceLastPromotion', value=5)
    with col4:
        YearsWithCurrManager = st.number_input('YearsWithCurrManager', value=3)

    # Baris Kesepuluh
    with st.container():
        col1, col2, col3, col4 = st.columns(4)
    with col1:
        Department = st.selectbox('Department',['Human Resources', 'Sales','Research & Development'])
    with col2:
        Gender = st.selectbox('Gender',['Female', 'Male']) 
    with col3:
        JobRole = st.selectbox('JobRole',['Healthcare Representative', 'Human Resources', 'Laboratory Technician', 'Manager'], '')
    with col4:
        Over18 = st.selectbox('Over18',['Y'])

   # Inference
    data = {
           'Age': Age,
           'BusinessTravel': BusinessTravel,
           'DistanceFromHome': DistanceFromHome,
           'Education': Education,
           'JobSatisfaction': JobSatisfaction,
           'JobInvolvement': JobInvolvement,
           'JobLevel': JobLevel,
           'MaritalStatus': MaritalStatus, 
           'MonthlyIncome': MonthlyIncome,
           'EducationField': EducationField,
           'TotalWorkingYears': TotalWorkingYears,
           'YearsAtCompany': YearsAtCompany,
           'OverTime': OverTime,
           'DailyRate': DailyRate,
           'EmployeeCount': EmployeeCount,
           'EnvironmentSatisfaction': EnvironmentSatisfaction,
           'HourlyRate': HourlyRate,
           'MonthlyRate': MonthlyRate,
           'NumCompaniesWorked': NumCompaniesWorked,
           'PercentSalaryHike': PercentSalaryHike,
           'PerformanceRating': PerformanceRating,
           'RelationshipSatisfaction': RelationshipSatisfaction, 
           'StandardHours': StandardHours,
           'StockOptionLevel': StockOptionLevel,
           'TrainingTimesLastYear': TrainingTimesLastYear,
           'WorkLifeBalance': WorkLifeBalance,
           'YearsInCurrentRole': YearsInCurrentRole, 
           'YearsSinceLastPromotion': YearsSinceLastPromotion,
           'Department': Department,
           'Gender': Gender,
           'JobRole': JobRole,
           'Over18': Over18
           }

   # Tabel data
    kolom = list(data.keys())
    df = pd.DataFrame([data.values()], columns=kolom)
   
   # Melakukan prediksi
    hasil = my_model.predict(df)
    hasil_proba = my_model.predict_proba(df)
    keputusan1 = round(float(hasil_proba[:,0])*100,2)
    keputusan2 = round(float(hasil_proba[:,1])*100,2)


   # Memunculkan hasil di Web 
    st.write('***'*10)
    st.write('<center><b><h4>Probabilitas Keluar = ', str(keputusan1),'%</b></h4>', unsafe_allow_html=True)
    st.write('<center><b><h4>Probabilitas Stay di Perusahaan = ', str(keputusan2),'%</b></h4>', unsafe_allow_html=True)
