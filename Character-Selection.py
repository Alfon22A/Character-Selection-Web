import streamlit as st
import numpy as np

def main ():
	
	st.set_page_config(
		page_title="Character Selection",
		page_icon=":smiley:")

	st.title("Character Selection")
	st.write("Alfonso Muñoz Alonso, 2022")
	st.header("Want to know how the computer sees you?")
	st.write("Disclaimer: this shows how the computer perceives you, the only one who can indentify yourself is you.")
						   
	img1 = st.file_uploader("Upload a pic!")	
	img2 = st.camera_input("Or take a pic!")
main()