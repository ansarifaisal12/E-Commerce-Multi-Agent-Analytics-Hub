# agents.py
from phi.agent import Agent
from phi.model.groq import Groq

class AnalyticsAgent:
    def __init__(self, role: str, expertise: list, datasets: list, icon: str, description: str, groq_model: str = "deepseek-r1-distill-llama-70b"):
        self.agent = Agent(model=Groq(id=groq_model), markdown=True)
        self.role = role
        self.expertise = expertise
        self.datasets = datasets
        self.icon = icon
        self.description = description
        self.system_prompt = self._create_system_prompt()
        self.chat_history = []
        
    def _create_system_prompt(self):
        return f"""You are {self.icon} {self.role}, an expert analytics agent with deep knowledge in {', '.join(self.expertise)}. 
        You have access to: {', '.join(self.datasets)}.
        Analyze provided data and give concise, data-driven insights with actionable recommendations.
        Cite specific metrics, keep responses professional, highlight key metrics.
        Format numbers appropriately ($, %, rounding).
        Limit to 3-5 key insights unless asked for more detail."""
    
    def process_query(self, user_query, data_context):
        full_prompt = f"{self.system_prompt}\n\nData Context:\n{data_context}\n\nUser Query: {user_query}"
        self.chat_history.append({"role": "user", "content": user_query})
        response = self.agent.run(full_prompt).content
        self.chat_history.append({"role": "assistant", "content": response})
        return response

class CustomerAnalyticsAgent(AnalyticsAgent):
    def __init__(self, groq_model="deepseek-r1-distill-llama-70b"):
        super().__init__(
            role="Customer Insights Specialist",
            expertise=["Customer Segmentation", "Lifetime Value Analysis", "Retention Strategies"],
            datasets=['customers', 'transactions', 'tickets'],
            icon="👥",
            description="Analyzes customer behavior and retention strategies",
            groq_model=groq_model
        )

class ProductAnalyticsAgent(AnalyticsAgent):
    def __init__(self, groq_model="deepseek-r1-distill-llama-70b"):
        super().__init__(
            role="Product Intelligence Advisor", 
            expertise=["Inventory Optimization", "Pricing Strategy", "Product Mix Analysis"],
            datasets=['products', 'inventory', 'competitors'],
            icon="📦",
            description="Provides product performance and inventory insights",
            groq_model=groq_model
        )

class SalesAnalyticsAgent(AnalyticsAgent):
    def __init__(self, groq_model="deepseek-r1-distill-llama-70b"):
        super().__init__(
            role="Revenue Growth Strategist",
            expertise=["Sales Trend Analysis", "Marketing Attribution", "Forecasting"],
            datasets=['transactions', 'campaigns', 'analytics'],
            icon="💰",
            description="Analyzes sales patterns and campaign effectiveness",
            groq_model=groq_model
        )