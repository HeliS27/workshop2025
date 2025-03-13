import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Cluod App")

st.write("A sample DataFrame: ")

df = pd.DataFrame(np.random.randn(10,2),columns=['Col1','Col2'])  # DataFrame creation 10 rows 2 columns name col1 and col2

st.dataframe(df)