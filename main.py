import streamlit as st





def main():
    print("Hello from streamlit-demo-social!")

    st.title('hello, bhaiyon!')
    st.subheader('ready for some new vids?')
    st.text("lets make our clients and our wallets and our girlfriends proud")
    st.write("please enter client info")
    client=st.selectbox("please choose the client:",['BakExcuse','PavWOW','Priya Creation'])
    st.write(f'great here is all info about {client}')

    st.success(f"great! here is your entire {client} library!")

if __name__ == "__main__":
    main()
