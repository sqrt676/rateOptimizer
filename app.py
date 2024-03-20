import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set custom style for Streamlit app
sns.set_style("whitegrid")

# Function to calculate optimized percentage below
def calculate_optimized_percentage(winning_percentages):
    # Calculate the mean of winning percentages
    mean_percentage = np.mean(winning_percentages)
    
    # Define a range of possible percentages below the mean to consider
    possible_percentages_below = np.arange(0, mean_percentage, 0.1)  # You can adjust the step size if needed
    
    # Calculate the total cost for each possible percentage below the mean
    total_costs = [(mean_percentage - percentage) for percentage in possible_percentages_below]
    
    # Find the minimum total cost and corresponding percentage below the mean
    min_total_cost = min(total_costs)
    optimized_percentage_below = possible_percentages_below[total_costs.index(min_total_cost)]
    
    return optimized_percentage_below

# Streamlit UI
st.set_page_config(page_title="Winning Tender Optimization Tool", page_icon=":moneybag:")

# Custom CSS for improved UI design
st.markdown(
    """
    <style>
    .stApp {
        max-width: 800px;
        padding: 2rem;
    }
    .stTextArea > div > div > label {
        font-size: 18px;
        color: #333;
    }
    .stTextArea > div > textarea {
        font-size: 16px;
        color: #555;
    }
    .stButton button {
        font-size: 16px;
        font-weight: bold;
        color: #fff;
        background-color: #0066cc;
        border-color: #0066cc;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #005cbf;
        border-color: #005cbf;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title and description
st.title('Winning Tender Optimization Tool')
st.markdown('''
Optimize your bidding strategy with data-driven insights. Maximize your chances of securing tenders while optimizing profitability.
''')

# Input section
st.sidebar.header('Input Winning Percentages')
winning_percentages = st.sidebar.text_area('Enter winning percentages separated by commas (e.g., 12, 13, 17, 17):')

# Button to calculate optimized percentage below
calculate_button = st.sidebar.button('Calculate Optimized Percentage Below')

# Processing and output section
if calculate_button and winning_percentages:
    winning_percentages = [float(x.strip()) for x in winning_percentages.split(',')]
    optimized_percentage = calculate_optimized_percentage(winning_percentages)
    
    # Display optimized percentage below
    st.success(f"The most optimized percentage below to quote: {optimized_percentage}%")
