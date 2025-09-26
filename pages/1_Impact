pages/1_Impact.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

#Title
st.markdown(
    """
    <div style='text-align: center;'>
        <div style='font-size:120px; font-weight:700; margin-bottom:0px;'>What We Do</div>
        <div style='font-size:25px;'>
            Discover how donations and volunteering efforts help bring the Collaborative’s mission of creating a world-class park in the heart of downtown Stamford to life. Every dollar and helping hand directly support environmental restoration, community programming, and STEM education – we hope you'll join us in turning this vision into reality.
        </div>
        <div style='margin-top:150px;'></div>
    </div>
    """, unsafe_allow_html=True)



#Community Impact
data = {
    "Program": [
        "Sunday Funday",
        "Fun Saturday Mornings",
        "Ice Skating in the Park",
        "Movies in the Park",
        "Swing in the Park",
        "Fitness Fun",
        "Easter & Halloween Trails",
        "TEEN Programs"
    ],
    "Attendees": [1305, 918, 11672, 549, 222, 1483, 4500, 175]
}

df = pd.DataFrame(data)
df["Label"] = df["Program"] + " (" + df["Attendees"].astype(str) + ")"

fig = px.pie(
    df,
    names="Label",
    values="Attendees",
    hole=0.1,
    title="Community Impact: Program Attendance",
    color_discrete_sequence=px.colors.qualitative.Prism
)

fig.update_traces(
    textinfo='label',
    textfont_size=18,
    textfont_color='white',
    insidetextorientation='radial'
)


fig.update_layout(
    showlegend=True,
    height=850,
    width=850,
    title_font_size=48
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("<div style='margin-top:100px;'></div>", unsafe_allow_html=True)



#Educational Impact
labels = [
    "Total Students (6487)",
    "Day Camp (167)",
    "Vacation Camp (76)",
    "After School (30)",
    "Field Trips (4073)",
    "Henkel Researchers' World (2141)"
]

sources = [0, 0, 0, 0, 0]  # All flows originate from "Total Students"
targets = [1, 2, 3, 4, 5]  # Each flow goes to a specific program
values = [167, 76, 30, 4073, 2141]  # Number of students in each program

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=20,
        thickness=30,
        line=dict(color="black", width=0.5),
        label=labels,
        color="lightblue"
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color=["#03fc6f", "#023bad", "#0b9917", "#049142", "#18a4f0"]
    )
)])

fig.update_layout(
    title="Educational Impact: K-12 Outreach",
    title_font_size=48,
    font_size=18,
    height=800
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("<div style='margin-top:100px;'></div>", unsafe_allow_html=True)



#Environmental Impact
st.markdown(
    """
    <div style='text-align: left;'>
        <div style='font-size:60px; font-weight:700;'>Environmental Impact: The Restoration</div>
    </div>
    <div style='font-size:22px; text-align:justify; margin-top:20px;'>
        Mill River Park has undergone a remarkable transformation — from a neglected floodplain to a vibrant green space that supports biodiversity, improves water quality, and offers a sanctuary for both people and wildlife. Restoration efforts include native plantings, riverbank stabilization, and the creation of pollinator habitats. Once choked by invasive species and urban runoff, the river was re-engineered to flow freely, reconnecting with its natural floodplain and improving water quality. Over 1,000 native trees and shrubs were planted to stabilize the banks, reduce erosion, and create habitats for birds, pollinators, and aquatic life. Today, the park is a thriving ecosystem in the heart of Stamford — a living classroom for environmental education, a refuge for wildlife, and a green oasis for the community.
    </div>
    <div style='margin-top:15px;'></div>
    """, unsafe_allow_html=True
)

image_path = "https://www.heystamford.com/downloads/475/download/IMG_4247.jpg?cb=ae8063ad73c67531e3256dba121b5262&w=450&h="
st.image(image_path, caption="Mill River Park Restoration", width='stretch')

st.markdown("<div style='margin-top:100px;'></div>", unsafe_allow_html=True)
