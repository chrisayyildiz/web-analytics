# dashboard/app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="Web User Behaviour Analytics",
    page_icon="📊",
    layout="wide"
)

# --- Data Loading ---
@st.cache_data # Cache the data to improve performance
def load_data(path):
    """Loads the processed data from a CSV file."""
    df = pd.read_csv(path)
    df['local_time'] = pd.to_datetime(df['local_time'])
    # Ensure categorical types are set for filtering and plotting
    df['time_of_day_bin'] = pd.Categorical(df['time_of_day_bin'], categories=['Morning', 'Afternoon', 'Evening', 'Night'], ordered=True)
    return df

df = load_data('data/processed_user_data.csv')

# --- Dashboard Title ---
st.title("Web User Behaviour Analytics Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")
selected_regions = st.sidebar.multiselect(
    "Geographic Region",
    options=df['geo_region'].unique(),
    default=df['geo_region'].unique()
)
selected_devices = st.sidebar.multiselect(
    "Device Type",
    options=df['device_type'].unique(),
    default=df['device_type'].unique()
)

# Filter the dataframe based on selection
df_filtered = df[df['geo_region'].isin(selected_regions) & df['device_type'].isin(selected_devices)]

if df_filtered.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# --- Key Metrics ---
st.header("Overall Performance")
total_sessions = df_filtered.shape[0]
total_conversions = df_filtered['conversion'].sum()
overall_conversion_rate = total_conversions / total_sessions if total_sessions > 0 else 0
avg_session_length = df_filtered['session_length_minutes'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sessions", f"{total_sessions:,}")
col2.metric("Total Conversions", f"{total_conversions:,}")
col3.metric("Conversion Rate", f"{overall_conversion_rate:.2%}")
col4.metric("Avg. Session Length (Min)", f"{avg_session_length:.2f}")

# --- Dashboard Tabs ---
tab1, tab2, tab3 = st.tabs(["User & Session Overview", "Engagement Analysis", "Conversion Analysis"])

with tab1:
    st.header("User & Session Overview")
    col1, col2 = st.columns(2)
    
    with col1:
        # Device Mix
        device_dist = df_filtered['device_type'].value_counts().reset_index()
        fig_device = px.pie(device_dist, names='device_type', values='count', title="Device Type Distribution")
        st.plotly_chart(fig_device, use_container_width=True)

    with col2:
        # Sessions by Region
        region_dist = df_filtered['geo_region'].value_counts().reset_index()
        fig_region = px.bar(region_dist, x='geo_region', y='count', title="Sessions by Geographic Region")
        st.plotly_chart(fig_region, use_container_width=True)

with tab2:
    st.header("Engagement Analysis")
    
    # Time of Day Analysis
    time_analysis = df_filtered['time_of_day_bin'].value_counts().sort_index().reset_index()
    fig_time = px.bar(time_analysis, x='time_of_day_bin', y='count', title="Session Volume by Time of Day")
    st.plotly_chart(fig_time, use_container_width=True)
    
    # Session Length vs. Pages Visited
    fig_scatter = px.scatter(
        df_filtered.sample(n=min(1000, len(df_filtered))), # Sample to avoid overplotting
        x='session_length_minutes', 
        y='pages_visited', 
        color='conversion',
        title="Session Length vs. Pages Visited",
        labels={'conversion': 'Converted'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab3:
    st.header("Conversion Analysis")
    col1, col2 = st.columns(2)

    with col1:
        # Conversion Rate by Device
        conv_by_device = df_filtered.groupby('device_type')['conversion'].mean().reset_index()
        fig_conv_device = px.bar(conv_by_device, x='device_type', y='conversion', title="Conversion Rate by Device Type")
        st.plotly_chart(fig_conv_device, use_container_width=True)

    with col2:
        # Conversion Rate by Campaign Source
        conv_by_campaign = df_filtered.groupby('campaign_source')['conversion'].mean().sort_values(ascending=False).reset_index()
        fig_conv_campaign = px.bar(conv_by_campaign, x='campaign_source', y='conversion', title="Conversion Rate by Campaign Source")
        st.plotly_chart(fig_conv_campaign, use_container_width=True)