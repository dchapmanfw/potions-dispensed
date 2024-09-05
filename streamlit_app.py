import streamlit as st

def main():
    st.title("Brewmaster's Bin")
    
    name = st.text_input("Enter your brew:")
    description = st.text_area("Describe your brew:")
    
    if st.button("Submit"):
        st.write("Name:", name)
        st.write("Description:", description)

    st.write("##")
    
    if st.button("PICK YOUR POISON"):
        pass

main()