import streamlit as st

def main():
    st.title("Keypad Calculator")
    
    # Display input field
    expression = st.text_input("Enter your expression:", key="expression")
    
    # Define keypad layout
    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", "C", "=", "+"]
    ]
    
    # Arrange buttons in a grid
    cols = st.columns(4)
    for row in buttons:
        for i, button in enumerate(row):
            if cols[i].button(button, key=button):
                handle_button_click(button)

def handle_button_click(button):
    if button == "C":
        st.session_state.expression = ""
    elif button == "=":
        try:
            st.session_state.expression = str(eval(st.session_state.expression))
        except Exception:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += button

if "expression" not in st.session_state:
    st.session_state.expression = ""

main()
