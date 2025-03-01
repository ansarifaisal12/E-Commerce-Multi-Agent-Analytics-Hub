# utils.py
import re
import streamlit as st

CUSTOM_CSS = """
<style>
.agent-selector {background-color: #f8f9fa; border-radius: 10px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);}
.agent-card {background-color: #fff; border-radius: 8px; padding: 15px; margin: 10px 0; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); transition: transform 0.2s ease, box-shadow 0.2s ease;}
.agent-card:hover {transform: translateY(-2px); box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);}
.agent-response {background-color: #f0f7ff; border-left: 4px solid #3498db; padding: 15px; border-radius: 0 8px 8px 0; margin: 15px 0;}
.metric-card {background-color: #fff; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); text-align: center;}
.highlight {color: #3498db; font-weight: bold;}
</style>
"""

def format_agent_response(response):
    response = re.sub(r'##\s+(.*?)\n', r'<h3 style="color:#3498db;">\1</h3>\n', response)
    response = re.sub(r'###\s+(.*?)\n', r'<h4 style="color:#2980b9;">\1</h4>\n', response)
    response = re.sub(r'\$[\d,]+\.?\d*', r'<span class="highlight">\g<0></span>', response)
    response = re.sub(r'\d+\.?\d*%', r'<span class="highlight">\g<0></span>', response)
    response = re.sub(r'\n\*\s+(.*?)\n', r'\n<li>\1</li>\n', response)
    response = response.replace('<li>', '<ul><li>').replace('</li>\n\n', '</li></ul>\n\n')
    return response

def inject_custom_css():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def display_agent_selector():
    st.markdown("<div class='agent-selector'>", unsafe_allow_html=True)
    st.subheader("💬 Choose Your AI Analytics Advisor")
    col1, col2, col3 = st.columns(3)
    with col1:
        customer_selected = st.button("👥 Customer Insights Specialist", key="customer_btn")
    with col2:
        product_selected = st.button("📦 Product Intelligence Advisor", key="product_btn")
    with col3:
        sales_selected = st.button("💰 Revenue Growth Strategist", key="sales_btn")
    st.markdown("</div>", unsafe_allow_html=True)
    return customer_selected, product_selected, sales_selected