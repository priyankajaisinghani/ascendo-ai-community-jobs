import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Ascendo AI Community Jobs")

st.title("Ascendo AI Community Jobs")
st.write("Find Field Service jobs in one place")

df = pd.read_csv("jobs.csv")

st.write("Last refreshed at:", df["last_refreshed"][0])

st.write("### Job Listings")

for i in range(len(df)):
    st.write(df["job_title"][i])
    st.write(df["company"][i], "-", df["location"][i], "-", df["seniority"][i])
    st.write("Source:", df["source"][i])
    st.write("Apply:", df["apply_link"][i])
    st.write("---")

if st.button("Refresh Jobs"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    df["last_refreshed"] = now
    df.to_csv("jobs.csv", index=False)
    st.success("Jobs refreshed")
    st.experimental_rerun()
