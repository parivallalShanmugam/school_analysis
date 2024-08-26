import streamlit as st

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError:
    st.error("Some required libraries are not installed. Please run 'pip install -r requirements.txt' to install them.")
    st.stop()

# Rest of your code remains the same
# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("2.Teachers report final.csv")
    df['Needs Attention %'] = df['Needs Attention %'] * 100
    df['Satisfactory %'] = df['Satisfactory %'] * 100
    df['Unsatisfactory %'] = df['Unsatisfactory %'] * 100
    return df

df = load_data()

# Title
st.title('Teachers Report Analysis')


# Basic Information
st.header('1. Basic Information')
st.write('Teachers Report Analysis')

# Descriptive Statistics
st.header('2. Descriptive Statistics')
st.write(df.describe())

# Distribution Analysis
st.header('3. Distribution Analysis')

# Histograms
st.subheader('Histograms of Percentages')
fig, ax = plt.subplots(figsize=(10, 5))
df[['Satisfactory %', 'Needs Attention %', 'Unsatisfactory %']].hist(bins=5, ax=ax)
plt.suptitle('Distribution of Percentages', fontsize=16)
st.pyplot(fig)

# Box plots
st.subheader('Box Plots of Percentage Metrics')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df[['Satisfactory %', 'Needs Attention %', 'Unsatisfactory %']], ax=ax)
plt.title('Box Plot of Percentage Metrics', fontsize=16)
st.pyplot(fig)

# Correlation Heatmap
st.header('4. Correlation Heatmap')
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(df[['Satisfactory %', 'Needs Attention %', 'Unsatisfactory %']].corr(), annot=True, cmap='coolwarm', ax=ax)
plt.title('Correlation Heatmap', fontsize=16)
st.pyplot(fig)

# Comparing Categories
st.header('5. Comparing Categories')
fig, ax = plt.subplots(figsize=(10, 6))
df.set_index('SUB DOMAIN')[['Satisfactory %', 'Needs Attention %', 'Unsatisfactory %']].plot(kind='bar', stacked=True, ax=ax)
plt.title('Comparison of Metrics across Sub Domains', fontsize=16)
plt.ylabel('Percentage')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# Top/Bottom Performing Areas
st.header('6. Top/Bottom Performing Areas')

st.subheader('Top Performing Sub Domains (Satisfactory %)')
st.write(df[['SUB DOMAIN', 'Satisfactory %']].sort_values(by='Satisfactory %', ascending=False).head())

st.subheader('Bottom Performing Sub Domains (Needs Attention %)')
st.write(df[['SUB DOMAIN', 'Needs Attention %']].sort_values(by='Needs Attention %', ascending=False).head())