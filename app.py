import streamlit as st
import datetime
from PIL import Image
import requests
from io import BytesIO
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from PIL import Image
import requests
from streamlit_option_menu import option_menu
import hydralit_components as hc
# from turtle import distance
from streamlit_lottie import st_lottie
import pandas as pd

st.set_page_config(page_title="CM_PROJECT", page_icon=":maple_leaf:", layout="wide")
def streamlit_menu(example=2):

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "about-us","contact-us"],  # required
            icons=["house", "book", "envelope", "file","contact"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "000000"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "black"},
            },
        )
        return selected


selected = streamlit_menu(example=3)
st.sidebar.success("")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_wait = load_lottieurl("https://lottie.host/91395377-a866-4d16-8200-84aae03d52e1/R2XCTX0Tkk.json")
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_hsabbeks.json")
lottie_coding_email = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5wr08scz.json")
lottie_sidebar = load_lottieurl("https://lottie.host/df9ffd6d-f938-4591-a5f4-6c90c6518f50/lcqfCJhY8I.json")
lottie_facebook = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_xwabp3dh.json")
lottie_twiter = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_5mhyg2hz.json")
lottie_insta = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_86afyky0.json")
lottie_you = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ej2lfhv2.json")
lottie_bottom= load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_zeoxz8eo.json")
lottie_submit=load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_3ghvm6sn.json")
lottie_login=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_7GoiCvHm8v.json")
lottie_ency=load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_9bLBSn/locked.json")
lottie_decy=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_twduwlzj.json")


if selected =="contact-us":
    # st.markdown("## 123A mall road AP building Gurugram Haryana")
    with st.container():
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css")
        with st.container():
            st.write("---")
            st.header("Get In Touch With Us!")
            st.write("##")

           # Documention: https://formsubmit.co/aman20492@iiitd.ac.in
            contact_form = """
            <form action="https://formsubmit.co/aman20492@iiitd.ac.in" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st_lottie(lottie_coding_email, height=300, key="email")
    with st.container():
        face_col, twiter_col, insta_col, you_col = st.columns(4)
        with face_col:
            st_lottie(lottie_facebook, height=100, key="lottie_facebook")
        with twiter_col:
            st_lottie(lottie_twiter, height=100, key="lottie_twiter")
        with insta_col:
            st_lottie(lottie_insta, height=100, key="lottie_insta")
        with you_col:
            st_lottie(lottie_you, height=100, key="lottie_you")

    # st_lottie(lottie_bottom, height=300,width=1000, key="lottie_bottom")  

if selected == "about-us":
    st.markdown("""
       ### Our Founders
       ##### Aman Kumar, 2020492, IIIT Delhi   
       ##### Shelja Agarwal, 2020470, IIIT Delhi
       ##### Aditya Anand, 2020488, IIIT Delhi
       ##### Muskan Yadav, 2020087, IIIT Delhi
       ##### Chirag, 2020367, IIIT Delhi
       ##### Vasu, 2020482, IIIT Delhi
       ##### Vaibhav, 2020257, IIIT Delhi
              
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            
         
    """, True)

    st.subheader("Add your feedback")
    feedback_name = st.text_input("Enter your name: ")
    feedback_text = st.text_area("Write about us: ")
    
    if st.button("submit"):
        query="insert into feedback values('{}','{}')".format(feedback_name, feedback_text)
        st.success("Feedback submitted successfully!")
        

    


if selected=="Home":
    # st_lottie(lottie_wait, height=300, key="lottie_sidebar")  
    c1, c2 = st.columns([7, 1])
    st.write("TODAYS DATE & TIME")
    st.write(datetime.datetime.now())
    # st.write(list1)
    st.header("Upload your X-ray to find out you have pneumonia or not")
    input_img=st.file_uploader("")


    

    
    



        
        
with st.sidebar:
    st_lottie(lottie_sidebar, height=300, key="lottie_sidebar")  