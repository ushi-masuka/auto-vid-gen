#code written by me

import streamlit as st
import pandas as pd


client_list=[None ,'BakExcuse','PavWOW','Priya Creation','Sakhi Silai']
print("Hello from streamlit-demo-social!")

st.title("Auto-Vid-Gen (Streamlit-Demo)")
st.header('Hello bhaiyon!')
st.subheader('ready for some new vids?')
st.text("lets make our clients , wallets and girlfriends proud")

st.divider()

if st.button("add client"):
    st.text("please enter client info")
    new_client=st.text_input("Client Firm name: ")
    if new_client:
        client_list.append(new_client)

    file=st.file_uploader("please upload client file",accept_multiple_files=True,type=['csv'])

    if file:
        client_db=pd.read_csv(file)
        st.subheader('Data preview')
        st.dataframe(client_db)        
    
st.divider()
client=st.selectbox("please choose the client:", client_list)

    
    
if client:
    st.write(f'great here is all info about {client}')
    st.success(f"great! here is your entire {client} library!")
        

