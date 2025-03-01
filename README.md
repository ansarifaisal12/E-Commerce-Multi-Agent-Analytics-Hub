# E-Commerce Multi-Agent AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



## Overview

The **E-Commerce Analytics Dashboard** is a Streamlit-based web application powered by AI agents (using Groq's API) to provide data-driven insights for e-commerce businesses. It includes three specialized AI agents:

1. **Customer Insights Specialist** 👥
2. **Product Intelligence Advisor** 📦
3. **Revenue Growth Strategist** 💰
![Screenshot 2025-02-27 040941](https://github.com/user-attachments/assets/554159d0-4905-4635-9c7f-fbf487f46b0c)

![Screenshot 2025-02-27 041025](https://github.com/user-attachments/assets/db34e358-6ae2-4358-b418-0df7bc9da480)
![Screenshot 2025-02-27 041104](https://github.com/user-attachments/assets/98ad4347-f6ed-4542-b981-a55aca1aa95a)



These agents analyze customer behavior, product performance, and sales trends to deliver actionable recommendations.

## Features

- **Interactive Dashboard**: Visualize key metrics and trends using Plotly charts
- **AI-Powered Insights**: Get data-driven recommendations from specialized AI agents
- **Sample Data Generation**: Automatically generates sample data if no CSV files are found
- **Customizable**: Add your own datasets or modify the existing ones for personalized analysis

## Prerequisites

Before running the application, ensure you have the following:

1. **Python 3.8+** installed
2. A **Groq API key** (sign up at [https://console.groq.com/](https://console.groq.com/))

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ecommerce-analytics-dashboard.git
   cd ecommerce-analytics-dashboard
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Groq API key:**

   **Option 1:** Set an environment variable:
   ```bash
   export GROQ_API_KEY="your_api_key_here"
   ```

   **Option 2:** Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. **(Optional) Add your own CSV files to the project directory:**
   - `customers.csv`
   - `products.csv`
   - `transactions.csv`
   - `inventory_logs.csv`
   - `campaigns.csv`
   - `competitors.csv`
   - `tickets.csv`
   - `analytics.csv`

   If no CSV files are found, the application will generate sample data automatically.

## Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

Open your browser and navigate to the provided URL (usually http://localhost:8501).

Use the dashboard to:
- View key metrics (total customers, monthly revenue, etc.)
- Select an AI agent for analysis
- Ask questions and get insights

## Project Structure

```
ecommerce-analytics-dashboard/
├── app.py                  # Main Streamlit application
├── data_loader.py          # Data loading and preprocessing
├── agents.py               # AI agent classes
├── utils.py                # Helper functions and CSS
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables (optional)
├── README.md               # Project documentation
├── customers.csv           # Sample customer data (optional)
├── products.csv            # Sample product data (optional)
├── transactions.csv        # Sample transaction data (optional)
└── ...                     # Other CSV files
```

## AI Agents

### 1. Customer Insights Specialist 👥
- **Expertise**: Customer segmentation, lifetime value analysis, retention strategies
- **Datasets**: Customers, transactions, support tickets

### 2. Product Intelligence Advisor 📦
- **Expertise**: Inventory optimization, pricing strategy, product mix analysis
- **Datasets**: Products, inventory, competitors

### 3. Revenue Growth Strategist 💰
- **Expertise**: Sales trend analysis, marketing attribution, forecasting
- **Datasets**: Transactions, campaigns, web analytics

## Example Queries

### Customer Insights
- "What are the top customer segments by lifetime value?"
- "How many customers are active in the last 30 days?"

### Product Insights
- "Which products have the highest sales volume?"
- "What is the average price by product category?"

### Sales Insights
- "What is the monthly sales trend?"
- "Which payment method is most popular?"

## Customization

### Add New Agents:
1. Create a new class in `agents.py` by extending the `AnalyticsAgent` class
2. Update the `app.py` file to include the new agent in the UI

### Add New Datasets:
1. Add your CSV files to the project directory
2. Update the `DataLoader` class in `data_loader.py` to load and preprocess the new data

### Modify Visualizations:
- Edit the visualization code in `app.py` to customize charts and metrics

## Troubleshooting

### 1. Groq API Key Not Found
- Ensure the `GROQ_API_KEY` environment variable is set or the key is provided in the code
- Restart the application after setting the environment variable

### 2. CSV Files Not Found
- The application will generate sample data if no CSV files are found
- Add your own CSV files to the project directory for custom analysis

### 3. Dependency Issues
- Ensure all dependencies are installed using:
  ```bash
  pip install -r requirements.txt
  ```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Submit a pull request with a detailed description of your changes

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [Groq](https://groq.com/) for the AI API
- [Agno](https://console.groq.com/keys) for Agents Framework
- [Plotly](https://plotly.com/) for interactive visualizations

---

Created by [Muhammad Faisal](https://github.com/your-username)
