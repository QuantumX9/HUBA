import streamlit as st

def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return "Error"

st.title("Calculator")

expression = st.text_input("Enter Expression:", "")

if st.button("Calculate"):
    result = calculate(expression)
    st.write(f"Result: {result}")
