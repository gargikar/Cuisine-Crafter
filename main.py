import streamlit as st
import langchain_helper
from PIL import Image


st.title("Cuisine Crafter")
img = Image.open('img2.jpg')
st.image(img,width=0.1,use_column_width=True)


#for sidebar
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American" , "Thai" ,"Chinese" , 
                                                  "Japanese" , "French" , "Spanish" , "Korean" , "Greek" , "Turkish"))

st.sidebar.subheader("Made by [Gargi Kar]")
st.sidebar.write("Connect with me :")
st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/gargi-kar-4a236a201/)")
st.sidebar.write("[Github](https://github.com/gargikar/)")

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)

