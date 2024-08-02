import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the web app
st.title('Data Visualization with Streamlit')

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read and display the data
    df = pd.read_csv(uploaded_file)
    st.write("Data Overview:")
    st.write(df.head())

    # Line Chart
    st.subheader('Line Chart of Values Over Time')
    df['date'] = pd.to_datetime(df['date'])
    line_chart = df.pivot(index='date', columns='category', values='value')
    st.line_chart(line_chart)

    # Bar Chart
    st.subheader('Bar Chart of Values by Category')
    bar_chart_data = df.groupby('category').agg({'value': 'sum'}).reset_index()
    st.bar_chart(bar_chart_data.set_index('category'))

    # Scatter Plot
    st.subheader('Scatter Plot of Values Over Time')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='date', y='value', hue='category', palette='deep')
    plt.title('Scatter Plot of Values Over Time')
    st.pyplot(plt)
