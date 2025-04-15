import streamlit as st
import pandas as pd

st.title("📊 Data Analysis App")

# File Upload
file_update = st.file_uploader("📁 Upload a CSV file", type=["csv"])

if file_update is not None:
    df = pd.read_csv(file_update)
    st.success("✅ File uploaded successfully!")

    # Data Preview
    st.subheader("🔍 Data Preview")
    st.write(df.head())

    # Data Summary
    st.subheader("📌 Data Summary")
    st.write(df.describe(include="all"))

    # Data Filter
    st.subheader("🔎 Filter Data")

    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to filter by", columns)

    values = df[selected_column].unique().tolist()
    selected_value = st.selectbox("Select a value", values)

    filter_df = df[df[selected_column] == selected_value]

    st.write(f"📄 Showing {len(filter_df)} rows for **{selected_column} = {selected_value}**")
    st.dataframe(filter_df)

    # Plot Graph
    st.subheader("📈 Plot Graph")

    # Identify numeric columns only for plotting
    numeric_columns = filter_df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_columns) >= 1:
        x_column = st.selectbox("Select x-axis column", columns)
        y_column = st.selectbox("Select numeric column for y-axis", numeric_columns)

        if st.button("Generate Plot"):
            if y_column in numeric_columns:
                try:
                    st.line_chart(filter_df[[x_column, y_column]].set_index(x_column))
                except Exception as e:
                    st.error(f"❌ Error plotting graph: {e}")
            else:
                st.warning("⚠️ Selected y-axis column must be numeric.")
    else:
        st.warning("⚠️ No numeric columns available in filtered data.")
else:
    st.info("📌 Please upload a CSV file to begin.")
