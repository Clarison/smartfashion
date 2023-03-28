import streamlit as st
from PIL import Image
import numpy as np
from datetime import datetime
from flask import Flask, request, render_template
from pathlib import Path
from feature_extractor import FeatureExtractor


# Read image features
fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(Path("./static/img") / (feature_path.stem + ".jpg"))
features = np.array(features)


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit by Group 6! 👋")

st.write(features)

