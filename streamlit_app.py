import streamlit
import pandas
streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry Oatmeal")


my_fruit_list = pandas.read_text("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
