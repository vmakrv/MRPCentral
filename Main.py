import streamlit as st
import pandas as pd
import plotly.express as px

# Set wide layout for immersive experience
st.set_page_config(page_title="Mill River Park Central", layout="wide")

# Inject custom HTML & CSS
st.markdown("""
    <style>
    html, body, .stApp {
        overflow-x: hidden;
        margin: 0;
        padding: 0;
        background-color: #0E1117;
    }

    .custom-title {
        font-size: 160px;
        color: #ffffff;
        text-align: center;
        margin-top: 40px;
        margin-bottom: 30px;
        font-weight: bold;
    }

    .wide-text {
        width: 100%;
        padding: 0 5vw;
        font-size: 32px;
        color: #ffffff;
        line-height: 1.8;
        text-align: center;
        box-sizing: border-box;
    }

    .donate-button {
        display: flex;
        justify-content: center;
        margin-top: 50px;
        margin-bottom: 100px; /* Added spacing below the button */
    }

    .donate-button a {
        background-color: #2E8B57;
        color: white;
        padding: 20px 40px;
        font-size: 24px;
        text-decoration: none;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }

    .donate-button a:hover {
        background-color: #246b45;
    }

    .gallery-title {
        color: #ffffff;
        text-align: center;
        font-size: 72px;
        margin-top: 150px;
        margin-bottom: 25px;
        font-weight: bold;
    }

    .park-image {
        display: flex;
        justify-content: center;
        margin-bottom: 60px;
    }

    .park-image img {
        max-width: 70vw;
        height: auto;
        border-radius: 20px;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
    }
    </style>

    <div class='custom-title'>WELCOME</div>
    <div class='wide-text'>
        Since 2003, Mill River Park Collaborative has been guided by a mission to enrich Stamford's community through accessible nature, education, and recreation. This site provides an interactive experience where visitors can explore the park, learn about our work, and find ways to contribute.
    </div>

    <div class='donate-button'>
        <a href='https://millriverpark.org/donate/' target='_blank'>Donate Here</a>
    </div>

    <div class='gallery-title'>Photo Gallery</div>

    <div class='park-image'>
        <img src='https://millriver.wpenginepowered.com/wp-content/uploads/2019/03/About-Us.jpg' alt='Mill River Park'>
    </div>

    <div class='park-image'>
        <img src='https://www.arcgis.com/sharing/rest/content/items/2291bd52abd74b70a94a2de7636bb892/resources/Mill%20River%20Park%2050__1533565813842__w1500.jpg' alt='Park View 3'>
    </div>

    <div class='park-image'>
        <img src='https://millriver.wpenginepowered.com/wp-content/uploads/2019/01/cropped-bunny.jpg' alt='Park View 3'>
    </div>

    <div class='park-image'>
        <img src='https://millriver.wpenginepowered.com/wp-content/uploads/2019/02/DSC_0207-header-crop.jpg' alt='Park View 1'>
    </div>

    <div class='park-image'>
        <img src='https://millriver.wpenginepowered.com/wp-content/uploads/2019/07/IMG_6381-1500x1000.jpg' alt='Park View 3'>
    </div>

    <div class='park-image'>
        <img src='https://millriver.wpenginepowered.com/wp-content/uploads/2022/08/AAR57143-2048x1366.jpg' alt='Park View 3'>
    </div>

    <div class='park-image'>
        <img src='https://millriver.wpenginepowered.com/wp-content/uploads/2019/02/party-carousel.jpg' alt='Park View 2'>
    </div>

""", unsafe_allow_html=True)
