import pandas as pd
import streamlit as st
from streamlit_tags import st_tags_sidebar


st.set_page_config(
    page_title="Aptos ledger",
    layout="wide",
)

st.write("# Aptos ledger")


st.session_state.transactions = st_tags_sidebar(
    text="Press enter to addresses",
    label="",
    value=[
        "",
    ],
)

st.sidebar.write("### Input accoutns:")
st.sidebar.write(st.session_state.transactions)
