import streamlit as st
import pandas as pd

# Title
st.title("📊 Dataset Explorer")

# Upload dataset
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Show basic dataset info
    st.subheader("Preview of Dataset")
    st.write(df.head())

    # Dataset shape
    st.write(f"**Shape of dataset:** {df.shape[0]} rows × {df.shape[1]} columns")

    # Column selection
    st.subheader("Select Columns to View")
    columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
    st.write(df[columns].head())

    # Show summary
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Missing values
    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    # Data visualization
    st.subheader("Quick Visualization")
    chart_type = st.selectbox("Choose a chart type", ["None", "Bar Chart", "Line Chart", "Area Chart"])
    column_to_plot = st.selectbox("Choose a column to visualize", df.columns)

    if chart_type == "Bar Chart":
        st.bar_chart(df[column_to_plot].value_counts())
    elif chart_type == "Line Chart":
        st.line_chart(df[column_to_plot])
    elif chart_type == "Area Chart":
        st.area_chart(df[column_to_plot])
