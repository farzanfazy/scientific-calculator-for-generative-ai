import streamlit as st
import math

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x, base=10):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Factorial not defined for negative numbers"
    return math.factorial(x)

# Streamlit app layout
st.title("Scientific Calculator")

operation = st.selectbox("Select operation:", [
    "Addition", "Subtraction", "Multiplication", "Division",
    "Power", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent", "Factorial"
])

# Inputs based on operation
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num1 = st.number_input("Enter first number:", format="%.2f")
    num2 = st.number_input("Enter second number:", format="%.2f")

    if st.button("Calculate"):
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        elif operation == "Power":
            result = power(num1, num2)
        
        st.write(f"Result: {result}")

elif operation == "Square Root":
    num = st.number_input("Enter number:", format="%.2f")
    if st.button("Calculate"):
        result = sqrt(num)
        st.write(f"Result: {result}")

elif operation == "Logarithm":
    num = st.number_input("Enter number:", format="%.2f")
    base = st.number_input("Enter base (default is 10):", value=10.0, format="%.2f")
    if st.button("Calculate"):
        result = log(num, base)
        st.write(f"Result: {result}")

elif operation == "Sine":
    angle = st.number_input("Enter angle in degrees:", format="%.2f")
    if st.button("Calculate"):
        result = sin(angle)
        st.write(f"Result: {result}")

elif operation == "Cosine":
    angle = st.number_input("Enter angle in degrees:", format="%.2f")
    if st.button("Calculate"):
        result = cos(angle)
        st.write(f"Result: {result}")

elif operation == "Tangent":
    angle = st.number_input("Enter angle in degrees:", format="%.2f")
    if st.button("Calculate"):
        result = tan(angle)
        st.write(f"Result: {result}")

elif operation == "Factorial":
    num = st.number_input("Enter number:", min_value=0, step=1, format="%d")
    if st.button("Calculate"):
        result = factorial(num)
        st.write(f"Result: {result}")
