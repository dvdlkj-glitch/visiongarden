"""
Vision Garden · Phase 5 — Streamlit deployment wrapper.

This project is a static HTML/CSS/JS website (see index.html). Streamlit Community
Cloud needs a Python entry point, so this file embeds the live site full-window.

The site's images and promo video are served from GitHub Pages, which keeps this
Streamlit app tiny and fast (nothing heavy is loaded into the Python process).
"""

import streamlit as st
import streamlit.components.v1 as components

# ---- URL of the deployed static site (GitHub Pages) --------------------------
SITE_URL = "https://dvdlkj-glitch.github.io/visiongarden/"

# ---- Page config -------------------------------------------------------------
st.set_page_config(
    page_title="Vision Garden · Phase 5",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---- Strip Streamlit chrome & padding so the site fills the whole window ------
st.markdown(
    """
    <style>
      #MainMenu, header[data-testid="stHeader"], footer,
      [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none !important; }
      [data-testid="stAppViewContainer"] > .main { padding: 0 !important; }
      .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
      [data-testid="stAppViewBlockContainer"], .stMainBlockContainer { padding: 0 !important; }
      .stApp { background: #14171b; }
      iframe { display: block; border: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- Embed the live landing page ---------------------------------------------
# `height` is the visible window height in pixels; the page scrolls inside it.
# Bump this number if you want a taller viewport on large screens.
components.iframe(SITE_URL, height=900, scrolling=True)
