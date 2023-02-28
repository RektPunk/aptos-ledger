import pandas as pd
import streamlit as st
from streamlit_tags import st_tags_sidebar
from logic.account_resources import get_account_resources
from logic.transactions import get_account_transactions


st.write("# Account")


st.session_state.addresses = st_tags_sidebar(
    text="Press enter to addresses",
    label="",
    value=[
        "0x17f2f43d81fbb2809c17351b5829d64a73d704d2f0b2786f05084ab1a9248eaa",
    ],
)

st.sidebar.write("### Input accoutns:")
st.sidebar.write(st.session_state.addresses)


account_resources_tab, transactions_tab = st.tabs(["account resources", "transactions"])

with account_resources_tab:
    st.json(
        get_account_resources(
            st.session_state.addresses
        )
    )


with transactions_tab:
    st.json(
        get_account_transactions(
            st.session_state.addresses
        )
    )
