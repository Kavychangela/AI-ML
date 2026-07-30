import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name=st.text_input("Enter your name: ")

age=st.slider("Select your age: ",0,100,25)

options=["Python","java","c","c++"]

choice=st.selectbox("Choose your favourite language", options)

st.write(f"You selected {choice}")

if name:
    st.write(f"Hello {name}" )

if age:
    st.write(f"your age is {age}" )


data={
    "Name": ["kavy", "Atul", "Seema", "Nivya"],
    "Age": [1000,2000,3000,4000],
    "City":["Pune","Pune","Pune","Pune"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv") 
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    st.write(df)