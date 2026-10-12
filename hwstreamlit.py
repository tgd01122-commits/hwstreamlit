import streamlit as st
import pandas as pd

st.title("그래프 그리기")

file = st.file_uploader("CSV 파일 선택", type=['csv'])

if file:
    df = pd.read_csv(file)
    st.write("데이터 미리보기:")
    st.dataframe(df)
    st.write("그래프:")
    st.line_chart(df)
