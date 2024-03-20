import streamlit as st
import numpy as np

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
st.title('Optimized Percentage Below Calculator')

# Input section
st.subheader('Input Winning Percentages')
winning_percentages = st.text_input('Enter winning percentages separated by commas (e.g., 12, 13, 17, 17):')

# Processing and output section
if winning_percentages:
    winning_percentages = [float(x.strip()) for x in winning_percentages.split(',')]
    optimized_percentage = calculate_optimized_percentage(winning_percentages)
    st.write("The most optimized percentage below to quote:", optimized_percentage)
