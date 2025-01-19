import streamlit as st
import pandas as pd

def render_task_table(scores):
    """Render the productivity scores as a table."""
    st.subheader("Productivity Scores")
    df = pd.DataFrame(scores)
    st.write(df)
