import streamlit as st
from utils.loader import load_data
from utils.calculator import calculate_rtp
from utils.flatten_data import flatten_data
from components.uploader import render_uploader
from components.task_table import render_task_table
from components.charts import render_charts
import pandas as pd

st.title("Real-Time Productivity Tracker")

# Upload JSON file
uploaded_file = render_uploader()

if uploaded_file:
    data = load_data(uploaded_file)

    flattened_data = flatten_data(data)

    # Convert the flattened data into a DataFrame
    df = pd.DataFrame(flattened_data)

    # Display the DataFrame in the Streamlit app
    st.write("User Task Data:")
    st.dataframe(df)

    # Calculate productivity scores
    scores = calculate_rtp(data)

    # Render task table
    render_task_table(scores)

    # Render charts
    render_charts(data, scores)
