# E-Commerce Multi-Agent Analytics Hub

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg) <!-- Replace with your app's URL -->

This project is an AI-powered analytics dashboard designed for e-commerce businesses. It leverages a *multi-agent architecture* to provide deep insights into customer behavior, product performance, and sales trends, enabling data-driven decision-making.  The system features user feedback, automated evaluation, and A/B testing capabilities for continuous improvement.

<img width="917" alt="image" src="https://github.com/user-attachments/assets/9124c11e-638a-4701-b53b-87e5dcae1a8c" />
<img width="916" alt="image" src="https://github.com/user-attachments/assets/dd0feb11-3704-4a2b-a4e0-cd910dfa0580" />
<img width="917" alt="image" src="https://github.com/user-attachments/assets/2aa39957-1df7-4c54-b2df-57dcad0708f7" />



## Key Features

*   **Multi-Agent System:**  Employs specialized AI agents, each with a distinct role and expertise:
    *   👥 **Customer Insights Specialist:**  Analyzes customer segmentation, lifetime value, retention, and behavior.
    *   📦 **Product Intelligence Advisor:**  Provides insights into product performance, inventory optimization, and competitive positioning.
    *   💰 **Revenue Growth Strategist:**  Focuses on sales trends, marketing campaign effectiveness, and revenue forecasting.

*   **AI-Powered by Groq:** Utilizes Groq's Language Processing Units (LPUs) for exceptionally fast inference, enabling real-time interaction with large language models (LLMs).  Supports models like `mixtral-8x7b` and `deepseek-r1-distill-llama-70b`.

*   **Interactive User Interface:**  Built with Streamlit for a user-friendly and responsive dashboard experience.  Includes interactive charts, data tables, and agent selection.

*   **User Feedback and Evaluation:**
    *   **Thumbs Up/Down Ratings:** Users can rate the quality of agent responses.
    *   **Optional Text Feedback:**  Space for users to provide additional comments.
    *   **Automated Metrics:**  Calculates metrics such as response time and BLEU score (text similarity).

*   **A/B Testing Framework:**
    *   **Agent Variations:**  Easily create and manage different versions of agents (e.g., different models, prompts, data contexts).
    *   **Random Assignment:**  (Currently implemented via session state; see Future Enhancements for database integration).
    *   **Performance Tracking:**  Admin dashboard to compare the performance of different agent variations based on user feedback and automated metrics.

*   **Admin Dashboard:**
    *   **Performance Visualization:**  Charts and metrics to analyze agent ratings, response times, and feedback.
    *   **A/B Testing Configuration:**  Manage agent variations and track their performance.
    *   **Raw Evaluation Data:** Access the underlying evaluation data for detailed analysis.

* **Data Preprocessing and Aggregation:**
   *  Load and preprocess data from several sources.
   *  Perform data cleaning and transformation
   *  Create aggregated views
   *   Create relevant data context

## Technology Stack

*   **Python:**  Primary programming language.
*   **Streamlit:**  Framework for building the interactive web application.
*   **Groq:**  Provides the LPU inference engine for fast LLM execution.
*   **phi-1.5 (or similar):** Used as a foundation for the agent architecture.
*   **Pandas:**  Data manipulation and analysis.
*   **Plotly:**  Interactive data visualization.
*   **NLTK:**  Natural Language Toolkit (for BLEU score calculation).
*   **wordcloud (optional):**  For generating word clouds from feedback text.

## Getting Started

### Prerequisites

*   Python 3.8 or higher
*   A Groq API key (obtain from [Groq's website](https://groq.com/))

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    (You'll need to create a `requirements.txt` file containing the necessary libraries: `streamlit`, `pandas`, `plotly`, `nltk`, `wordcloud`, `phi-1.5` (or equivalent), and any Groq-specific libraries.)

### Configuration

1.  **Groq API Key:**  Set your Groq API key as an environment variable:

    ```bash
    export GROQ_API_KEY=your_groq_api_key
    ```
    (Or, set it directly in your code using `st.secrets`, but this is less secure for public repositories.)

2. **Data Files:**
   * Place the required CSV files (customers.csv, products.csv, transactions.csv, etc) into the same directory as your main.py script. You can find the data schema details in DataLoader Class
   * Option: You can keep the script as is and it will generate sample data, allowing for immediate demonstration of the application's functionality.

### Running the Application

```bash
streamlit run main.py  # Replace main.py with your main app file
