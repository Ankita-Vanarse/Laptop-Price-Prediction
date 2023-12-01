import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Predictor')

# brand
company = st.selectbox('Brand',df['Company'].unique())

# type of laptop
type = st.selectbox('Type',df['TypeName'].unique())


# Ram
ram = st.selectbox('Ram(in GB)',[2,4,6,8,12,16,24,32,64])

# Weight
weight = st.number_input('Weight  of the laptop')

# TouchScreen
touchScreen = st.selectbox('TouchScreen',['No','Yes'])


# IPS 
ips = st.selectbox('IPS',['No','Yes'])

# screen size
screen_size = st.number_input('Screen Size')

# resolution
resolution = st.selectbox('Screen Resolution',['1366x768', '1440x900', '1600x900', '1920x1080', 
                                               '1920x1200', '2160x1440', '2256x1504', '2304x1440', 
                                               '2400x1600', '2560x1440', '2560x1600', '2736x1824', 
                                               '2880x1800', '3200x1800', '3840x2160'])


# cpu
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

hdd = st.selectbox('HDD in GB',[0,128,256,512,1024,2024])
ssd = st.selectbox('SSD in GB',[0,8,128,256,512,1024])


gpu = st.selectbox('GPU',df['Gpu brand'].unique())
os = st.selectbox('OS',df['os'].unique())



if st.button('Predict Prize'):
    ppi = None
    if touchScreen == 'Yes':
        touchScreen = 1
    else:
        touchScreen = 0
    if ips == 'Yes':
        ips =1
    else:
        ips =0

    X_res = int(resolution.split('x')[0])  
    Y_res = int(resolution.split('x')[1])       
    ppi = ((X_res**2)+(Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchScreen,ips,ppi,cpu,hdd,ssd,gpu,os])
     
    query = query.reshape(1,12)
    st.title('The Predicted price of this configuration is    ' +  str(int(np.exp(pipe.predict(query)[0]))) + ' Rs')
















