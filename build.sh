#!/bin/bash
RUN !pip install streamlit \
    && !pip install sklearn
RUN streamlit run app.py