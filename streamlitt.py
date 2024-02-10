import numpy as np
import pandas as pd
import streamlit as st 
import joblib

model = joblib.load("my_model3.pkl")
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

        if output == 1:
            text = "Detak jantung dan saturasi oksigen tidak normal"
        elif output == 2:
          text = "Saturasi oksigen tidak normal"
        elif output == 5:
          text = "Suhu dan saturasi oksigen tidak normal"
        elif output == 6:
          text = "Suhu tidak normal"
        elif output == 3:
          text = "Sehat"
        elif output == 0:
          text = "Detak Jantung tidak normal"
        elif output == 7:
          text = "Suhu,detak jantung, dan saturasi oksigen tidak normal"  
        elif output == 4:
            text = "Suhu dan detak jantung tidak normal"
        else:
           text = "-"

        st.success('Kondisi {}'.format(text))
      
if __name__=='__main__': 
    main()
