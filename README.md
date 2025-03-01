\documentclass{article}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{enumitem}

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,
    breaklines=true,
    captionpos=b,
    keepspaces=true,
    numbers=left,
    numbersep=5pt,
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    tabsize=2
}

\lstset{style=mystyle}

\title{E-Commerce Analytics Dashboard}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle

\section*{Overview}
The \textbf{E-Commerce Analytics Dashboard} is a Streamlit-based web application powered by AI agents (using Groq's API) to provide data-driven insights for e-commerce businesses. It includes three specialized AI agents:
\begin{enumerate}
    \item \textbf{Customer Insights Specialist} 👥
    \item \textbf{Product Intelligence Advisor} 📦
    \item \textbf{Revenue Growth Strategist} 💰
\end{enumerate}

These agents analyze customer behavior, product performance, and sales trends to deliver actionable recommendations.

\section*{Features}
\begin{itemize}
    \item \textbf{Interactive Dashboard}: Visualize key metrics and trends using Plotly charts.
    \item \textbf{AI-Powered Insights}: Get data-driven recommendations from specialized AI agents.
    \item \textbf{Sample Data Generation}: Automatically generates sample data if no CSV files are found.
    \item \textbf{Customizable}: Add your own datasets or modify the existing ones for personalized analysis.
\end{itemize}

\section*{Prerequisites}
Before running the application, ensure you have the following:
\begin{enumerate}
    \item \textbf{Python 3.8+} installed.
    \item A \textbf{Groq API key} (sign up at \url{https://console.groq.com/}).
\end{enumerate}

\section*{Installation}
\begin{enumerate}
    \item Clone the repository:
    \begin{lstlisting}[language=bash]
git clone https://github.com/your-username/ecommerce-analytics-dashboard.git
cd ecommerce-analytics-dashboard
    \end{lstlisting}

    \item Install the required dependencies:
    \begin{lstlisting}[language=bash]
pip install -r requirements.txt
    \end{lstlisting}

    \item Set up your Groq API key:
    \begin{itemize}
        \item \textbf{Option 1}: Set an environment variable:
        \begin{lstlisting}[language=bash]
export GROQ_API_KEY="your_api_key_here"
        \end{lstlisting}
        \item \textbf{Option 2}: Create a \texttt{.env} file in the project root:
        \begin{lstlisting}[language=bash]
GROQ_API_KEY=your_api_key_here
        \end{lstlisting}
    \end{itemize}

    \item (Optional) Add your own CSV files to the project directory:
    \begin{itemize}
        \item \texttt{customers.csv}
        \item \texttt{products.csv}
        \item \texttt{transactions.csv}
        \item \texttt{inventory\_logs.csv}
        \item \texttt{campaigns.csv}
        \item \texttt{competitors.csv}
        \item \texttt{tickets.csv}
        \item \texttt{analytics.csv}
    \end{itemize}
    If no CSV files are found, the application will generate sample data automatically.
\end{enumerate}

\section*{Running the Application}
\begin{enumerate}
    \item Start the Streamlit app:
    \begin{lstlisting}[language=bash]
streamlit run app.py
    \end{lstlisting}

    \item Open your browser and navigate to the provided URL (usually \url{http://localhost:8501}).

    \item Use the dashboard to:
    \begin{itemize}
        \item View key metrics (total customers, monthly revenue, etc.).
        \item Select an AI agent for analysis.
        \item Ask questions and get insights.
    \end{itemize}
\end{enumerate}

\section*{Project Structure}
\begin{lstlisting}[language=bash]
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
\end{lstlisting}

\section*{AI Agents}
\subsection*{1. Customer Insights Specialist 👥}
\begin{itemize}
    \item \textbf{Expertise}: Customer segmentation, lifetime value analysis, retention strategies.
    \item \textbf{Datasets}: Customers, transactions, support tickets.
\end{itemize}

\subsection*{2. Product Intelligence Advisor 📦}
\begin{itemize}
    \item \textbf{Expertise}: Inventory optimization, pricing strategy, product mix analysis.
    \item \textbf{Datasets}: Products, inventory, competitors.
\end{itemize}

\subsection*{3. Revenue Growth Strategist 💰}
\begin{itemize}
    \item \textbf{Expertise}: Sales trend analysis, marketing attribution, forecasting.
    \item \textbf{Datasets}: Transactions, campaigns, web analytics.
\end{itemize}

\section*{Example Queries}
\subsection*{Customer Insights}
\begin{itemize}
    \item "What are the top customer segments by lifetime value?"
    \item "How many customers are active in the last 30 days?"
\end{itemize}

\subsection*{Product Insights}
\begin{itemize}
    \item "Which products have the highest sales volume?"
    \item "What is the average price by product category?"
\end{itemize}

\subsection*{Sales Insights}
\begin{itemize}
    \item "What is the monthly sales trend?"
    \item "Which payment method is most popular?"
\end{itemize}

\section*{Customization}
\begin{itemize}
    \item \textbf{Add New Agents}:
    \begin{itemize}
        \item Create a new class in \texttt{agents.py} by extending the \texttt{AnalyticsAgent} class.
        \item Update the \texttt{app.py} file to include the new agent in the UI.
    \end{itemize}

    \item \textbf{Add New Datasets}:
    \begin{itemize}
        \item Add your CSV files to the project directory.
        \item Update the \texttt{DataLoader} class in \texttt{data\_loader.py} to load and preprocess the new data.
    \end{itemize}

    \item \textbf{Modify Visualizations}:
    \begin{itemize}
        \item Edit the visualization code in \texttt{app.py} to customize charts and metrics.
    \end{itemize}
\end{itemize}

\section*{Troubleshooting}
\subsection*{1. Groq API Key Not Found}
\begin{itemize}
    \item Ensure the \texttt{GROQ\_API\_KEY} environment variable is set or the key is provided in the code.
    \item Restart the application after setting the environment variable.
\end{itemize}

\subsection*{2. CSV Files Not Found}
\begin{itemize}
    \item The application will generate sample data if no CSV files are found.
    \item Add your own CSV files to the project directory for custom analysis.
\end{itemize}

\subsection*{3. Dependency Issues}
\begin{itemize}
    \item Ensure all dependencies are installed using:
    \begin{lstlisting}[language=bash]
pip install -r requirements.txt
    \end{lstlisting}
\end{itemize}

\section*{Contributing}
Contributions are welcome! Please follow these steps:
\begin{enumerate}
    \item Fork the repository.
    \item Create a new branch for your feature or bugfix.
    \item Submit a pull request with a detailed description of your changes.
\end{enumerate}

\section*{License}
This project is licensed under the MIT License. See the \texttt{LICENSE} file for details.

\section*{Acknowledgments}
\begin{itemize}
    \item \textbf{Streamlit} (\url{https://streamlit.io/}) for the web framework.
    \item \textbf{Groq} (\url{https://groq.com/}) for the AI API.
    \item \textbf{Agno} (\url{https://console.groq.com/keys}) for Agents Framework.
    \item \textbf{Plotly} (\url{https://plotly.com/}) for interactive visualizations.
\end{itemize}

\section*{Enjoy!}
Enjoy using the E-Commerce Analytics Dashboard! For questions or feedback, please open an issue or contact the maintainers. 🚀

\end{document}