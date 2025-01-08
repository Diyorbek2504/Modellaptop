import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

with open('laptopprice.pkl', 'rb') as file:
    model = pickle.load(file)
    
st.title("Noutbook narxi")
st.write("Bu dastur sizning kiritgan ma'lumotlaringizga asoslanib noutbokingizni taxminiy narxini bashorat qiladi!")

mm = st.text_input("Noutbok nomi")
PrimaryStorageType = st.selectbox("Hotira turi", ["SSD", "HDD",	"Flash Storage", "Hybrid"])
if PrimaryStorageType=="SSD":
    PrimaryStorageType=3
elif PrimaryStorageType=="HDD":
    PrimaryStorageType=1
elif PrimaryStorageType=="Flash Storage":
    PrimaryStorageType=0
elif PrimaryStorageType=="Hybrid":
    PrimaryStorageType=2
PrimaryStorage = st.number_input("Hotira (GB)")
ram = st.number_input("RAM")
Screen = st.selectbox("Ekran sifati", ["Full HD", "Standard", "4K Ultra HD", "Quad HD+"])
if Screen=="Full HD":
    Screen=1
elif Screen=="Standard":
    Screen=3
elif Screen=="4K Ultra HD":
    Screen=0
elif Screen=="Quad HD+":
    Screen=2
ScreenW = st.number_input("Ekran kengligi (piksel)")
ScreenH = st.number_input("Ekran balandligi (piksel)")
CPU_freq = st.number_input("Markaziy protsessor (CPU) tezligi")

   
if st.button("Bashorat qilish"):
    df =pd.DataFrame([{
        'Ram': ram,
        'Screen': Screen,
        'ScreenW': ScreenW,
        'ScreenH': ScreenH,
        'CPU_freq': CPU_freq,
        'PrimaryStorage': PrimaryStorage,
        'PrimaryStorageType': PrimaryStorageType
    }]) 
    prediction = model.predict(df)[0]
    st.success(f"{mm} noutbokingizni taxminiy narxi: ${prediction:.2f}$ {"$"}")