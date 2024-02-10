import streamlit as st 

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.title("YOLO V5 Hand Sign Detection App")
st.caption('This web application demostrate Hand Sign Detection')

# Content
st.markdown("""
### This App detects Hand Signs from Images
- Automatically detects 6 Hand Signs from image
- [Click here for App](/YOLO_for_image/)  

Below give are the object the our model will detect
'Hello', 'IloveYou', 'No', 'Please', 'Thanks', 'Yes'  
            """)