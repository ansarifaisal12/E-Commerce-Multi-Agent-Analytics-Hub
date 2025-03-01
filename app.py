# app.py
import os
from dotenv import load_dotenv
import streamlit as st
from data_loader import DataLoader
from agents import CustomerAnalyticsAgent, ProductAnalyticsAgent, SalesAnalyticsAgent
from utils import inject_custom_css, format_agent_response, display_agent_selector
import plotly.express as px

load_dotenv()  # Load environment variables from .env file

# Ensure set_page_config is the first command
st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    inject_custom_css()

    dl = DataLoader()
    customer_selected, product_selected, sales_selected = display_agent_selector()

    if 'initialized' not in st.session_state:
        st.session_state.update({
            'initialized': True,
            'active_agent': None,
            'agents': {
                "customer": CustomerAnalyticsAgent(),
                "product": ProductAnalyticsAgent(),
                "sales": SalesAnalyticsAgent()
            },
            'chat_history': {}
        })

    st.title("📈 E-Commerce Multi-Agent Analytics Hub")
    st.markdown("## AI-Powered Insights for Data-Driven Decisions")

    # Metrics row
    with st.container():
        cols = st.columns(4)
        metrics = [
            ("Total Customers", f"{dl.data['customers'].shape[0]:,}"),
            ("Monthly Revenue", f"${dl.data['transactions']['total_amount'].sum():,.0f}"),
            ("Avg. Order Value", f"${dl.data['transactions']['total_amount'].mean():.2f}"),
            ("Conversion Rate", f"{dl.data['analytics']['conversion_rate'].mean() * 100:.2f}%")
        ]
        for col, (title, value) in zip(cols, metrics):
            with col:
                st.markdown(f"<div class='metric-card'>{title}<br><span class='highlight'>{value}</span></div>", 
                           unsafe_allow_html=True)

    # Handle agent selection
    if customer_selected: st.session_state.active_agent = "customer"
    if product_selected: st.session_state.active_agent = "product"
    if sales_selected: st.session_state.active_agent = "sales"

    # Agent interaction
    if st.session_state.active_agent:
        agent_type = st.session_state.active_agent
        agent = st.session_state.agents[agent_type]
        
        st.markdown(f"## {agent.icon} {agent.role}")
        st.markdown(f"*{agent.description}*")
        st.markdown(f"**Expertise:** {', '.join(agent.expertise)}")

        with st.form(key='query_form'):
            user_query = st.text_area("Ask your data question:", height=100)
            if st.form_submit_button("Ask Analytics Agent"):
                with st.spinner(f"{agent.icon} Analyzing..."):
                    data_context = dl.get_data_context(agent_type)
                    response = agent.process_query(user_query, data_context)
                    if agent_type not in st.session_state.chat_history:
                        st.session_state.chat_history[agent_type] = []
                    st.session_state.chat_history[agent_type].append({
                        "query": user_query,
                        "response": response
                    })

        if agent_type in st.session_state.chat_history:
            for exchange in st.session_state.chat_history[agent_type]:
                st.markdown(f"**Question:** {exchange['query']}")
                st.markdown(f"<div class='agent-response'>{format_agent_response(exchange['response'])}</div>", 
                           unsafe_allow_html=True)
                st.markdown("---")

        # Visualizations
        if agent_type == "customer":
            with st.expander("📊 Customer Visualizations", expanded=True):
                cols = st.columns(2)
                with cols[0]:
                    fig = px.pie(dl.data['customers'], names='segment', 
                               title="Customer Segments")
                    st.plotly_chart(fig, use_container_width=True)
                with cols[1]:
                    fig = px.box(dl.data['customers'], x='segment', y='lifetime_value',
                               title="LTV by Segment")
                    st.plotly_chart(fig, use_container_width=True)

        elif agent_type == "product":
            with st.expander("📊 Product Visualizations", expanded=True):
                cols = st.columns(2)
                with cols[0]:
                    fig = px.bar(dl.category_performance, x='category', y='sales_volume',
                               title="Sales by Category")
                    st.plotly_chart(fig, use_container_width=True)
                with cols[1]:
                    fig = px.scatter(dl.data['products'], x='price', y='sales_volume',
                                  color='category', title="Price vs Sales")
                    st.plotly_chart(fig, use_container_width=True)

        elif agent_type == "sales":
            with st.expander("📊 Sales Visualizations", expanded=True):
                cols = st.columns(2)
                with cols[0]:
                    fig = px.line(dl.transactions_daily, x='date', y='total_amount',
                                title="Daily Sales Trend")
                    st.plotly_chart(fig, use_container_width=True)
                with cols[1]:
                    fig = px.line(dl.monthly_segment_revenue, x='date', y='total_amount',
                                color='segment', title="Revenue by Segment")
                    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()