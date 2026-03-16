import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Page configuration
st.set_page_config(page_title="Pokémon Analysis Report", layout="wide", initial_sidebar_state="collapsed")

# Custom styling for compact single-page layout
st.markdown("""
    <style>
    .main {
        padding: 0.5rem 0.5rem;
    }
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        margin: 5px;
        font-size: 0.9em;
    }
    .title-section {
        text-align: center;
        padding: 10px 0;
        border-bottom: 2px solid #FF4B4B;
        margin-bottom: 10px;
    }
    h1 {
        color: #FF4B4B;
        font-size: 1.8em;
        margin: 0;
        padding: 0;
    }
    h2 {
        color: #0066cc;
        font-size: 1em;
        margin: 0;
        padding: 0;
    }
    h3 {
        font-size: 0.85em;
        margin: 2px 0;
        padding: 0;
    }
    p {
        font-size: 0.75em;
        margin: 2px 0;
        padding: 0;
    }
    [data-testid="metric-container"] {
        text-align: center;
        justify-content: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Pokemon.csv")
    df.drop('#', axis=1, inplace=True)
    df['Type 2'].fillna(df['Type 1'], inplace=True)
    return df

df = load_data()

# Title Section
st.markdown("""
    <div class="title-section">
        <h1>🎮 Pokémon Data Analysis Report</h1>
        <p style="font-size: 0.9em; color: #555; margin: 3px 0;">Comprehensive Analysis of Pokémon Characteristics, Types, and Stats</p>
    </div>
""", unsafe_allow_html=True)

# Top metrics row - ultra compact
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("<div style='text-align: center;'><p style='font-size: 0.7em; margin: 0;'>Total</p><p style='font-size: 1.5em; font-weight: bold; margin: 0; color: #0668BC;'>" + str(len(df)) + "</p></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='text-align: center;'><p style='font-size: 0.7em; margin: 0;'>Types</p><p style='font-size: 1.5em; font-weight: bold; margin: 0; color: #0668BC;'>" + str(df['Type 1'].nunique()) + "</p></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='text-align: center;'><p style='font-size: 0.7em; margin: 0;'>Gens</p><p style='font-size: 1.5em; font-weight: bold; margin: 0; color: #0668BC;'>" + str(int(df['Generation'].max())) + "</p></div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div style='text-align: center;'><p style='font-size: 0.7em; margin: 0;'>Leg</p><p style='font-size: 1.5em; font-weight: bold; margin: 0; color: #0668BC;'>" + str(int(df['Legendary'].sum())) + "</p></div>", unsafe_allow_html=True)

with col5:
    avg_total = df['Total'].mean()
    st.markdown("<div style='text-align: center;'><p style='font-size: 0.7em; margin: 0;'>Avg</p><p style='font-size: 1.5em; font-weight: bold; margin: 0; color: #0668BC;'>" + str(int(avg_total)) + "</p></div>", unsafe_allow_html=True)

# Add some spacing
st.markdown("<div style='margin: 5px 0;'></div>", unsafe_allow_html=True)

# Row 1: 5 Charts across
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("**📊 Type Dist**")
    type_counts = df['Type 1'].value_counts().head(9)
    fig, ax = plt.subplots(figsize=(2.5, 2.2))
    colors_pie = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22']
    ax.pie(type_counts.values, labels=type_counts.index, autopct='%1.0f%%', 
           colors=colors_pie, startangle=90, textprops={'fontsize': 5})
    ax.set_title('Types', fontweight='bold', fontsize=7)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()

with col2:
    st.markdown("**📈 Attack Stats**")
    stats_by_type = df.groupby('Type 1')[['Attack']].mean().nlargest(5, 'Attack')
    fig, ax = plt.subplots(figsize=(2.5, 2.2))
    ax.barh(stats_by_type.index, stats_by_type['Attack'], color='#FF6B6B')
    ax.set_title('Top Attack', fontweight='bold', fontsize=7)
    ax.set_xlabel('Avg', fontsize=6)
    ax.tick_params(labelsize=5)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()

with col3:
    st.markdown("**🔗 Correlations**")
    corr_cols = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']
    corr_matrix = df[corr_cols].corr()
    fig, ax = plt.subplots(figsize=(2.5, 2.2))
    sns.heatmap(corr_matrix, annot=False, cmap='coolwarm', square=True, cbar=False, ax=ax)
    ax.set_title('Stats Corr', fontweight='bold', fontsize=7)
    plt.xticks(fontsize=4, rotation=45)
    plt.yticks(fontsize=4, rotation=0)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()

with col4:
    st.markdown("**🎯 Generation**")
    gen_stats = df.groupby('Generation')['Total'].mean()
    fig, ax = plt.subplots(figsize=(2.5, 2.2))
    ax.plot(gen_stats.index, gen_stats.values, marker='o', linewidth=1.5, markersize=4, color='#FF4B4B')
    ax.set_title('Gen Stats', fontweight='bold', fontsize=7)
    ax.set_xlabel('Gen', fontsize=6)
    ax.set_ylabel('Total', fontsize=6)
    ax.grid(True, alpha=0.3)
    ax.tick_params(labelsize=5)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()

with col5:
    st.markdown("**👑 Legendary**")
    leg_data = df.groupby('Legendary')['Total'].mean()
    fig, ax = plt.subplots(figsize=(2.5, 2.2))
    ax.bar(['Non-Leg', 'Leg'], leg_data.values, color=['#42A5F5', '#FF7043'])
    ax.set_title('Legendary', fontweight='bold', fontsize=7)
    ax.set_ylabel('Avg', fontsize=6)
    ax.tick_params(labelsize=5)
    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()

# Key Findings Row
water_pct = (df['Type 1'] == 'Water').sum() / len(df) * 100
avg_total = df['Total'].mean()
legendary_avg = df[df['Legendary'] == 1]['Total'].mean()
non_legendary_avg = df[df['Legendary'] == 0]['Total'].mean()
gen3_avg = df[df['Generation'] == 3]['Total'].mean()
dragon_attack = df[df['Type 1'] == 'Dragon']['Attack'].mean()
steel_defense = df[df['Type 1'] == 'Steel']['Defense'].mean()

findings_text = f"""
**KEY FINDINGS:** Water type: {water_pct:.0f}% • Avg Stats: {avg_total:.0f} • Legendary: {legendary_avg:.0f} vs Non-Leg: {non_legendary_avg:.0f} (+{legendary_avg-non_legendary_avg:.0f}) • 
Gen 3 Strongest: {gen3_avg:.0f} • Dragon Attack: {dragon_attack:.0f} • Steel Defense: {steel_defense:.0f} • Water/Normal/Grass dominate • Legendary = High Stats
"""

st.markdown(f"<div style='font-size: 0.75em; line-height: 1.3; text-align: center; padding: 8px; background-color: #f0f2f6; border-radius: 8px; margin-bottom: 5px;'>{findings_text}</div>", unsafe_allow_html=True)

# Footer - compact
st.markdown("""
    <div style='text-align: center; padding: 8px; color: #999; font-size: 0.7em;'>
        Pokémon Data Analysis Report | Generated with Streamlit
    </div>
""", unsafe_allow_html=True)
