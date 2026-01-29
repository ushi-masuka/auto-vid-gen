import streamlit as st





def main():
    client_list=[None ,'BakExcuse','PavWOW','Priya Creation','Sakhi Silai']
    print("Hello from streamlit-demo-social!")

    st.title('hello, bhaiyon!')
    st.subheader('ready for some new vids?')
    st.text("lets make our clients , wallets and girlfriends proud")
    if st.button("add client"):
        st.text("please enter client info")
        new_client=st.text_input("Client Firm name: ")
        client_list.append(new_client)

        
    
    client=st.selectbox("please choose the client:", client_list)
    
    if client:
        st.write(f'great here is all info about {client}')
        st.success(f"great! here is your entire {client} library!")

if __name__ == "__main__":
    main()
