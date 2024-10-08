import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("CSV Data Simplify")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    
    # Filter columns based on data type
    numeric_columns = df.select_dtypes(include=["float", "int"]).columns.tolist()
    all_columns = df.columns.tolist()
    
    x_column = st.selectbox("Select x-axis column", all_columns)
    y_column = st.selectbox("Select y-axis column", numeric_columns)
    
    plot_type = st.selectbox("Select plot type", ["Line Plot", "Scatter Plot", "Bar Chart", "Histogram"])

    # Additional plot customizations
    st.subheader("Plot Customizations")
    grid = st.checkbox("Show Grid")
    color = st.color_picker("Pick a plot color", "#00f900")
    
    if st.button("Generate Plot"):
        plt.figure(figsize=(10, 6))

        try:
            if plot_type == "Line Plot":
                plt.plot(filtered_df[x_column], filtered_df[y_column], marker='o', color=color)
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f'{y_column} vs {x_column} - Line Plot')

            elif plot_type == "Scatter Plot":
                plt.scatter(filtered_df[x_column], filtered_df[y_column], marker='o', color=color)
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f'{y_column} vs {x_column} - Scatter Plot')

            elif plot_type == "Bar Chart":
                plt.bar(filtered_df[x_column], filtered_df[y_column], color=color)
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f'{y_column} vs {x_column} - Bar Chart')

            elif plot_type == "Histogram":
                plt.hist(filtered_df[y_column], bins=30, color=color)
                plt.xlabel(y_column)
                plt.ylabel("Frequency")
                plt.title(f'Histogram of {y_column}')
            
            if grid:
                plt.grid(True)

            st.pyplot(plt.gcf())
        
        except Exception as e:
            st.error(f"An error occurred: {e}")

else:
    st.write("Waiting on file upload...")
