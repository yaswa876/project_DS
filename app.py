import streamlit as st
import pandas as pd
import numpy as np

st.title("My Sample Streamlit App")
st.write("Hello — type something and move the slider!")

txt = st.text_input("Your message", "Streamlit is fun!")
n = st.slider("Choose a number", 1, 10, 3)

st.write("You typed:", txt)
df = pd.DataFrame({"A": np.random.randn(n), "B": np.random.randn(n)})
st.line_chart(df)
