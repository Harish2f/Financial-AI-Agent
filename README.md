# Financial AI Agent

The Financial AI Agent is a Python-based tool designed to retrieve and summarize financial data and web search results for stocks and companies. It uses the **phi** library to integrate powerful AI models and tools for advanced information retrieval and analysis.

## Features

- **Web Search Agent**:
  - Searches the web for relevant information.
  - Always includes sources for transparency.

- **Financial Agent**:
  - Retrieves stock prices, analyst recommendations, stock fundamentals, and company news.
  - Displays data in tables for better readability.

- **Multi-Agent System**:
  - Combines the Web Search Agent and Financial Agent for comprehensive results.
  - Summarizes information about stocks such as NVIDIA (NVDIA) effectively.

## Prerequisites

1. Python 3.8 or later.
2. Install dependencies using `pip`.
3. An OpenAI API key stored in a `.env` file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Harish2f/Financial-AI-Agent.git
   cd Financial-AI-Agent
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For macOS/Linux
   .venv\Scripts\activate   # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key to a `.env` file:
   ```bash
   echo "OPEN_API_KEY=your_openai_api_key" > .env
   ```

## Usage

Run the script to summarize analyst recommendations and share the latest news for a stock (e.g., NVIDIA):

```bash
python financial_agent.py
```

## Code Structure

- **`web_search_agent`**:
  - Uses `DuckDuckGo` as a tool for web searches.
  - Leverages the Groq AI model for information processing.

- **`finance_agent`**:
  - Utilizes `YFinanceTools` for retrieving financial data and news.

- **`multi_ai_agent`**:
  - Combines both agents to provide a unified response.

## Example Query

The following code snippet executes a query to retrieve financial insights for NVIDIA:

```python
multi_ai_agent.print_response(
    "Summarize the analyst recommendations and share the latest news for stock NVDIA",
    stream=True
)
```

## Notes

- Ensure the `.env` file is correctly configured to avoid API errors.
- Check your OpenAI API usage limits to ensure uninterrupted functionality.

## Troubleshooting

### Common Errors

1. **API Key Error**:
   - Ensure the `.env` file contains the correct `OPEN_API_KEY`.

2. **Model Access Issue**:
   - Verify that your OpenAI account has access to the models being used.

3. **GitHub Push Protection**:
   - Remove sensitive data like API keys before pushing to GitHub.

## Contributing

Feel free to fork the repository, make changes, and submit a pull request. For major changes, please open an issue to discuss your proposed changes first.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


