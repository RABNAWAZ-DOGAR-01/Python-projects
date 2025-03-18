import streamlit as st

def calculator():
    st.title("🖩 Simple Streamlit Calculator")

    st.write("### Select an operation:")
    operation = st.radio("Choose:", 
                         {"➕ Addition", "➖ Subtraction", "✖ Multiplication", "➗ Division"})

    num1 = st.number_input("Enter first number:", step=0.01)
    num2 = st.number_input("Enter second number:", step=0.01)

    if st.button("Calculate"):
        if operation == "➕ Addition":
            result = num1 + num2
            st.success(f"Result: {num1} ➕ {num2} = {result}")
        elif operation == "➖ Subtraction":
            result = num1 - num2
            st.success(f"Result: {num1} ➖ {num2} = {result}")
        elif operation == "✖ Multiplication":
            result = num1 * num2
            st.success(f"Result: {num1} ✖ {num2} = {result}")
        elif operation == "➗ Division":
            if num2 == 0:
                st.error("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                st.success(f"Result: {num1} ➗ {num2} = {result}")

    # Add credit at the bottom
    st.markdown("---")
    st.markdown("### Created by **Rabnawaz Dogar** 🎨")

if __name__ == "__main__":
    calculator()
