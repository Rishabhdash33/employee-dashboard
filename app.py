import streamlit as st
import pandas as pd

st.title("Employee Work Hours Dashboard")

@st.cache_data
def load_data():
    df = pd.read_excel('data.xlsx')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Total Working Time'] = pd.to_timedelta(df['Total Working Time'])
    return df

df = load_data()

employee = st.selectbox("Select Employee", df['Employee'].unique())

filtered = df[df['Employee'] == employee].sort_values('Date')

st.subheader(f"Work Hours for {employee}")
st.dataframe(filtered[['Date', 'In Time', 'Out Time', 'Total Working Time']])

hours_per_day = filtered.set_index('Date')['Total Working Time'].dt.total_seconds() / 3600
st.bar_chart(hours_per_day)

total_hours = hours_per_day.sum()
st.markdown(f"**Total Hours Worked:** {total_hours:.2f} hours")
