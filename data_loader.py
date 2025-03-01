# data_loader.py
import pandas as pd
import numpy as np
import json
import streamlit as st
from datetime import datetime

class DataLoader:
    def __init__(self):
        self._load_or_generate_data()
        self._preprocess_data()

    def _load_or_generate_data(self):
        """Load data from CSV files or generate sample data if files are not found."""
        try:
            self.data = {
                'customers': pd.read_csv('customers.csv', parse_dates=['registration_date', 'last_login']),
                'products': pd.read_csv('products.csv'),
                'transactions': pd.read_csv('transactions.csv', parse_dates=['date']),
                'inventory': pd.read_csv('inventory_logs.csv', parse_dates=['timestamp']),
                'campaigns': pd.read_csv('campaigns.csv', parse_dates=['start_date', 'end_date']),
                'competitors': pd.read_csv('competitors.csv', parse_dates=['date_scraped']),
                'tickets': pd.read_csv('tickets.csv', parse_dates=['created_date', 'resolved_date']),
                'analytics': pd.read_csv('analytics.csv', parse_dates=['date'])
            }
        except FileNotFoundError:
            self._generate_sample_data()

    def _generate_sample_data(self):
        """Generate sample data if CSV files are not found."""
        self.data = {}

        # Customers Data
        registration_dates = pd.date_range(start='2022-01-01', periods=1000, freq='D')
        last_login_dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='D')

        self.data['customers'] = pd.DataFrame({
            'customer_id': range(1, 1001),
            'segment': np.random.choice(['High Value', 'Mid Value', 'Low Value', 'New', 'Churned'], 1000),
            'lifetime_value': np.random.pareto(2, 1000) * 100,
            'purchase_count': np.random.poisson(5, 1000),
            'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 1000),
            'registration_date': np.random.choice(registration_dates, 1000),
            'last_login': np.random.choice(last_login_dates, 1000),
            'browsing_history': [
                [f"prod_{np.random.randint(1, 500)}" for _ in range(np.random.randint(1, 10))]
                for _ in range(1000)
            ]
        })

        # Products Data
        self.data['products'] = pd.DataFrame({
            'product_id': range(1, 201),
            'name': [f"Product {i}" for i in range(1, 201)],
            'category': np.random.choice(['Electronics', 'Clothing', 'Home Goods', 'Beauty', 'Food & Beverage'], 200),
            'price': np.random.gamma(5, 10, 200),
            'stock': np.random.poisson(50, 200),
            'sales_volume': np.random.negative_binomial(10, 0.5, 200),
            'features': [
                [f"feature_{np.random.randint(1, 20)}" for _ in range(np.random.randint(1, 5))]
                for _ in range(200)
            ]
        })

        # Transactions Data
        transaction_dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
        self.data['transactions'] = pd.DataFrame({
            'transaction_id': range(1, 5001),
            'customer_id': np.random.randint(1, 1001, 5000),
            'date': np.random.choice(transaction_dates, 5000),
            'total_amount': np.random.gamma(5, 20, 5000),
            'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Apple Pay', 'Bank Transfer'], 5000),
            'line_items': [
                [f"prod_{np.random.randint(1, 200)}" for _ in range(np.random.randint(1, 5))]
                for _ in range(5000)
            ]
        })

        # Inventory Data
        inventory_timestamps = pd.date_range(start='2023-01-01', end='2023-12-31', freq='H')
        self.data['inventory'] = pd.DataFrame({
            'log_id': range(1, 1001),
            'product_id': np.random.randint(1, 201, 1000),
            'timestamp': np.random.choice(inventory_timestamps, 1000),
            'action': np.random.choice(['restock', 'sale', 'return', 'adjustment'], 1000),
            'quantity': np.random.randint(-10, 50, 1000)
        })

        # Campaigns Data
        self.data['campaigns'] = pd.DataFrame({
            'campaign_id': range(1, 31),
            'name': [f"Campaign {i}" for i in range(1, 31)],
            'start_date': pd.date_range(start='2023-01-01', periods=30, freq='2W'),
            'end_date': pd.date_range(start='2023-01-15', periods=30, freq='2W'),
            'budget': np.random.gamma(10, 1000, 30),
            'impressions': np.random.poisson(10000, 30),
            'clicks': np.random.poisson(1000, 30),
            'conversions': np.random.poisson(100, 30)
        })

        # Competitors Data
        competitor_dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
        self.data['competitors'] = pd.DataFrame({
            'competitor_id': range(1, 101),
            'product_id': np.random.randint(1, 201, 100),
            'competitor_name': [f"Competitor {i}" for i in range(1, 101)],
            'price': np.random.gamma(5, 10, 100),
            'date_scraped': np.random.choice(competitor_dates, 100)
        })

        # Tickets Data
        created_dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
        resolved_dates = pd.date_range(start='2023-01-15', end='2024-01-15', freq='D')
        self.data['tickets'] = pd.DataFrame({
            'ticket_id': range(1, 501),
            'customer_id': np.random.randint(1, 1001, 500),
            'subject': np.random.choice(['Delivery Issue', 'Product Quality', 'Return Request', 'Account Issue'], 500),
            'priority': np.random.choice(['Low', 'Medium', 'High'], 500),
            'status': np.random.choice(['Open', 'In Progress', 'Resolved', 'Closed'], 500),
            'created_date': np.random.choice(created_dates, 500),
            'resolved_date': np.random.choice(resolved_dates, 500)
        })

        # Analytics Data
        self.data['analytics'] = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', end='2023-12-31'),
            'page_views': np.random.poisson(5000, 365),
            'unique_visitors': np.random.poisson(2000, 365),
            'bounce_rate': np.random.beta(2, 10, 365),
            'conversion_rate': np.random.beta(1, 30, 365),
            'avg_session_duration': np.random.gamma(3, 60, 365)
        })

    def _preprocess_data(self):
        """Preprocess and transform the data for analysis."""
        # Convert datetime columns to pandas Timestamp if they are numpy datetime64
        for df_name in self.data:
            for col in self.data[df_name].columns:
                if pd.api.types.is_datetime64_any_dtype(self.data[df_name][col]):
                    self.data[df_name][col] = pd.to_datetime(self.data[df_name][col])

        # Create aggregated views
        self.transactions_daily = self.data['transactions'].groupby(
            pd.Grouper(key='date', freq='D')
        )['total_amount'].sum().reset_index()

        customer_transactions = pd.merge(
            self.data['transactions'],
            self.data['customers'][['customer_id', 'segment']],
            on='customer_id'
        )
        self.monthly_segment_revenue = customer_transactions.groupby(
            [pd.Grouper(key='date', freq='M'), 'segment']
        )['total_amount'].sum().reset_index()

        self.category_performance = self.data['products'].groupby('category').agg({
            'price': 'mean',
            'stock': 'sum',
            'sales_volume': 'sum'
        }).reset_index()

        self.data['campaigns']['ctr'] = self.data['campaigns']['clicks'] / self.data['campaigns']['impressions']
        self.data['campaigns']['cvr'] = self.data['campaigns']['conversions'] / self.data['campaigns']['clicks']
        self.data['campaigns']['cpa'] = self.data['campaigns']['budget'] / self.data['campaigns']['conversions']

        self.data['tickets']['resolution_time'] = (
            self.data['tickets']['resolved_date'] - self.data['tickets']['created_date']
        ).dt.total_seconds() / (60 * 60 * 24)  # Convert to days

    def get_data_context(self, agent_type):
        """Create relevant data context for different agent types."""
        context = ""
        
        if agent_type == "customer":
            context += f"Customer Segments Overview:\n"
            context += f"{self.data['customers']['segment'].value_counts().to_dict()}\n\n"
            
            context += f"Lifetime Value Statistics by Segment:\n"
            context += f"{self.data['customers'].groupby('segment')['lifetime_value'].agg(['mean', 'median', 'min', 'max'])}\n\n"
            
            last_month = pd.Timestamp.now() - pd.Timedelta(days=30)
            active = (self.data['customers']['last_login'] > last_month).mean()
            context += f"Active Customers (last 30 days): {active:.2%}\n\n"
            
            context += f"Top 5 Customer Locations:\n"
            context += f"{self.data['customers']['city'].value_counts().head(5).to_dict()}\n\n"
            
        elif agent_type == "product":
            context += f"Product Category Overview:\n"
            context += f"{self.category_performance.to_dict('records')}\n\n"
            
            low_stock = (self.data['products']['stock'] < 10).mean()
            context += f"Products with Low Stock (<10 units): {low_stock:.2%}\n\n"
            
            context += f"Price Range by Category:\n"
            context += f"{self.data['products'].groupby('category')['price'].agg(['min', 'max', 'mean'])}\n\n"
            
            context += f"Top 5 Selling Products:\n"
            context += f"{self.data['products'].nlargest(5, 'sales_volume')[['name', 'category', 'price', 'sales_volume']].to_dict('records')}\n\n"
            
        elif agent_type == "sales":
            monthly_sales = self.data['transactions'].groupby(pd.Grouper(key='date', freq='M'))['total_amount'].sum()
            context += f"Monthly Sales Trend:\n{monthly_sales.to_dict()}\n\n"
            
            context += f"Payment Method Distribution:\n"
            context += f"{self.data['transactions']['payment_method'].value_counts(normalize=True).to_dict()}\n\n"
            
            context += f"Campaign Performance:\n"
            context += f"{self.data['campaigns'][['name', 'budget', 'impressions', 'clicks', 'conversions', 'ctr', 'cvr', 'cpa']].head(5).to_dict('records')}\n\n"
            
            monthly_aov = self.data['transactions'].groupby(pd.Grouper(key='date', freq='M'))['total_amount'].mean()
            context += f"Monthly Average Order Value Trend:\n{monthly_aov.to_dict()}\n\n"
            
        return context