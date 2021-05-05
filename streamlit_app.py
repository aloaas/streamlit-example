import time
from collections import namedtuple
import altair as alt
import math

import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire.

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
"""

"""
# Test app
Minimal use case of uploading audio and playing:
"""



uploaded_file = st.file_uploader("Choose a file", type=['mp3', 'wav'])
if uploaded_file is not None:
    st.audio(uploaded_file)


