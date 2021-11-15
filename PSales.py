import streamlit as st
#from tkinter import *
#from functools import partial


"""
# PartnerSales Collection Hub

"""

#st.title('PartnerSales Collection Hub')
st.write('Login Page')

Uname = st.text_input('Username')
Pwd = st.text_input('Password')

#Login_button = st.button('Login')

if st.button('Login'):
	if len(Uname) > 1 or len(Pwd) > 1:
		st.write('Logging in...')

#if len(Uname) > 1 or len(Pwd) > 1:
	#st.write ('Logging in...')

