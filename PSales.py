import streamlit as st
#from tkinter import *
#from functools import partial


"""
# PartnerSales Collection Hub

"""

#st.title('PartnerSales Collection Hub')

TRimage = Image.open("C:/Users/u6075712/Downloads/New folder/ReutersLogo.png")


st.write('Login Page')

Uname = st.text_input('Username')
Pwd = st.text_input('Password')

#Login_button = st.button('Login')

if st.button('Login'):
	if len(Uname) >= 1 or len(Pwd) >= 1:
		st.write('Logging in...')
		st.set_page_config(
			page_title = 'PartnerSales report upload',
			page_icon = st.image(TRimage, width=300),
			layout="wide",
        	initial_sidebar_state="expanded")
	else:
		st.write('Username or Password cannot be empty')

#if len(Uname) > 1 or len(Pwd) > 1:
	#st.write ('Logging in...')
