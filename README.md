# Automated Industry Marketing Report with CrewAI

This project generates **automated industry marketing reports** using CrewAI. It utilizes a collaborative approach, where three specialized agents handle research, data analysis, and report generation. The result is a structured and data-driven marketing insights report tailored to specific industries.

---

## 📁 Project Structure

- **Agents**: The team of three agents—Market Researcher, Data Analyst, and Report Generator—each perform specialized tasks:
  - **Market Researcher**: Gathers data from online sources using tools tailored for comprehensive market research.
  - **Data Analyst**: Interprets and analyzes the collected data to identify trends and insights.
  - **Report Generator**: Compiles a structured and executive-level marketing report.

- **Configuration Files:**
  - `agents.yaml` and `tasks.yaml`: Define the agents' prompts and their respective tasks.

- **Tools:**
  - A set of utilities available to each agent for data extraction and research.

- **Core Scripts:**
  - `crew.py`: Configures and initializes the CrewAI agents, tasks, and tools.
  - `main.py`: Runs the entire project and coordinates agent interactions.

- **Outputs:**
  - `market_research_task_output.md`: Raw market research data.
  - `data_analysis_report.md`: Analytical insights and interpretations.
  - `final_report.md`: A polished, executive-level marketing report.

---

## ⚙️ Requirements

To run this project on your local machine, ensure you have:

1. **Python** (version 3.10 - 3.13)
2. **Docker**
3. **CrewAI**
4. **Poetry**
5. **API Keys**:
   - **Serper API**
   - **OpenAI Platform API**
   - **LangSmith API**
   - **NewsAPI**

---

## 🛠️ Installation & Setup

### 1. Install CrewAI
```bash
pip install crewai
```

### 2. Install Poetry
```bash
pip install poetry
```

### 3. Install Dependencies
```bash
poetry lock
poetry install
```

### 4. Configure Environment Variables
- Create a `.env` file in the project's root directory.
- Add your API keys:
```env
OPENAI_API_KEY=<your_openai_api_key>
LANGSMITH_API_KEY=<your_langsmith_api_key>
SERPER_API_KEY=<your_serper_api_key>
NEWSAPI_KEY=<your_newsapi_key>
```

### 5. Run the Project
```bash
poetry run finance_project
```
- When prompted, input the **industry** you want to research.

---

## ✅ Validation & Testing
To ensure the agents' outputs are accurate and consistent:
- Check the generated markdown files (`.md`) to verify data accuracy.
- Review the raw data before analysis to ensure it aligns with the requested industry and parameters.
- Confirm each agent's output logically follows from the previous step.

---

## 📄 License & Contributions
- This project is intended for educational and research purposes.
- Feel free to contribute or raise issues for improvements.

If you need any further assistance or encounter issues, don't hesitate to reach out!

