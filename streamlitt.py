import numpy as np
import pandas as pd
import streamlit as st 
import pickle
from sklearn import preprocessing

model = pickle.load(open('model1.pkl', 'rb'))
cols=['Suhu, Detak Jantung, Saturasi Oksigen']    
  
def main(): 
    st.title("Predictor")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Pendeteksi Kondisi Kambing </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    Suhu = st.text_input("Suhu","0") 
    Detak_Jantung = st.text_input("Detak Jantung","0") 
    Saturasi_Oksigen = st.text_input("Saturasi Oksigen","0") 

    if st.button("Predict"): 
        features = [[Suhu,Saturasi_Oksigen,Detak_Jantung]]
        data = {'Suhu': float(Suhu), 'Detak Jantung': float(Saturasi_Oksigen), 'Saturasi_Oksigen': float(Detak_Jantung)}
        print(data)
        df=pd.DataFrame([list(data.values())], columns=['Suhu','Saturasi Osksigen','Detak_Jantung'])
                
        cols_list = df.values.tolist()
        prediction = model.predict(cols_list)
    
        output = int(prediction[0])

        if (38.5 <= float(Suhu) <= 40) and (70 <= float(Detak_Jantung) <= 90) and (95 <= float(Saturasi_Oksigen) <= 100):
          text = "Sehat"
        elif (38.5 >= float(Suhu) or float(Suhu) >= 40) and (70 >= float(Detak_Jantung) or float(Detak_Jantung) >= 90) and (95 >= float(Saturasi_Oksigen) or float(Saturasi_Oksigen) >= 100):
            text =  "Suhu,detak jantung, dan saturasi oksigen tidak normal. Segera bawa ke Dokter Hewan Terdekat"  
        elif (38.5 >= float(Suhu) or 40 <= float(Suhu)) and (70 >= float(Detak_Jantung) or 90 <= float(Detak_Jantung)):
            text = "Suhu dan detak jantung tidak normal. Berikut merupakan beberapa kemungkinan penyakit yang diderita oleh kambing :\n1. Stress\n2. Anemia\n3. Gangguan Jantung\n4. Infeksi\n5. Syok\n\nSilahkan hubungi Dokter Hewan untuk diagnosa pasti"
        elif (38.5 >= float(Suhu) or 40 <= float(Suhu)) and (95 >= float(Saturasi_Oksigen) or 100 <= float(Saturasi_Oksigen)):
            text =  "Suhu dan saturasi oksigen tidak normal. Berikut merupakan beberapa kemungkinan penyakit yang diderita oleh kambing :\n1. Infeksi saluran pernapasan/Pneumonia\n2. Gangguan Jantung\n3. Infeksi\n4. Syok\n\nSilahkan hubungi Dokter Hewan untuk diagnosa pasti"
        elif (38.5 >= float(Suhu) or 40 <= float(Suhu)):
            text = "Suhu tidak normal. Berikut merupakan beberapa kemungkinan penyakit yang diderita oleh kambing jika suhu dibawah normal (38.5):\n1. Hipotermia\n2. Toksemia\n\nJika suhu diatas normal (40):\n1. Pneumonia\n2. Infeksi Bakteri atau Virus\n3. Enterotoxemia (Penyakit Pulpy Kidney)\n\nSilahkan hubungi Dokter Hewan untuk diagnosa pasti"
        elif (70 >= float(Detak_Jantung) or 90 <= float(Detak_Jantung)) and (95 >= float(Saturasi_Oksigen) or 100 <= float(Saturasi_Oksigen)):
            text = "Detak jantung dan saturasi oksigen tidak normal. Berikut merupakan beberapa kemungkinan penyakit yang diderita oleh kambing:\n1. Gangguan Pernapasan\n2. Kehilangan Darah\n3. Stress\n4. Gangguan Jantung\n\nSilahkan hubungi Dokter Hewan untuk diagnosa pasti"
        elif (70 >= float(Detak_Jantung) or 90 <= float(Detak_Jantung)):
            text = "Detak Jantung tidak normal. Berikut merupakan beberapa kemungkinan penyakit yang diderita oleh kambing jika detak jantung dibawah normal (70):\n1. Kehilangan Darah\n2. Haemonchosis\n\nJika suhu diatas normal (90):\n1. Stress\n2. Anemia\n3. Gangguan Jantung\n\nSilahkan hubungi Dokter Hewan untuk diagnosa pasti"
        elif (95 >= float(Saturasi_Oksigen) or 100 <= float(Saturasi_Oksigen)):
            text = "Saturasi oksigen tidak normal. Berikut merupakan beberapa kemungkinan penyakit yang diderita oleh kambing jika Saturasi Oksigen dibawah normal (95):\n1. Haemonchosis (Cacing pada pencernaan)\n2. Edema Paru (Water Belly)\n\nJika Saturasi Oksigen diatas normal (100):\n1. Stress\n2. Anemia\n3. Gangguan Jantung\n\nSilahkan hubungi Dokter Hewan untuk diagnosa pasti"
        else:
            text = "-"

        st.success('Kondisi {}'.format(text))
      
if __name__=='__main__': 
    main()
