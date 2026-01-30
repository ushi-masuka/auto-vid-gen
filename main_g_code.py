#code written by gemini when I asked for tutorial

import streamlit as st

def main():
    st.title('🚀 VibeScale AOS')
    st.subheader('Ready for some new vids?')

    # --- STEP 1: INITIALIZE STATE ---
    # We check if 'clients' exists in the "backpack". If not, we put it there.
    if 'clients' not in st.session_state:
        st.session_state.clients = ['BakExcuse', 'PavWOW', 'Priya Creation', 'Sakhi Silai']

    # --- STEP 2: ADD CLIENT (SIDEBAR) ---
    with st.sidebar:
        st.header("Add New Client")
        # We use a form so the page doesn't reload on every keystroke
        with st.form("add_client_form"):
            new_client_name = st.text_input("Client Name")
            submitted = st.form_submit_button("Add to Database")
            
            if submitted and new_client_name:
                # Append to the STATE list, not a local variable
                st.session_state.clients.append(new_client_name)
                st.success(f"Added {new_client_name}!")

    # --- STEP 3: MAIN INTERFACE ---
    # Read from the STATE list
    client = st.selectbox("Please choose the client:", st.session_state.clients)

    if client:
        st.divider() # Adds a nice visual line
        st.write(f'### 📂 Workspace: {client}')
        st.info(f"Loaded assets for {client}. Let's make their wallet proud.")

if __name__ == "__main__":
    main()