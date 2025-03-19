from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeInterpreterTool, FileReadTool
from finance_project.tools.searchtool import SearchTools
from finance_project.tools.filtersearch_tool import FilteredSearchTool
from finance_project.tools.news_tool import NewsAPITool
from langchain_openai import ChatOpenAI
import os

# Set up OpenAI model (use environment variable or default to 'gpt-4o-mini')
llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))

@CrewBase
class FinanceProjectCrew():
	"""FinanceProject crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def market_researcher(self) -> Agent:
		if not self.agents_config:
			raise ValueError("Error: agents_config is None or not loaded properly.")

		return Agent(
			config=self.agents_config.get('market_researcher', {}),
			tools=[
				SearchTools.open_website,
				SearchTools.dataset_search,
				FilteredSearchTool.filtered_search,
				NewsAPITool.fetch_news
			],
			verbose=True,
			llm=llm,
			max_iterations=10
		)

	@agent
	def data_analyst(self) -> Agent:
		if not self.agents_config:
			raise ValueError("Error: agents_config is None or not loaded properly.")

		return Agent(
			config=self.agents_config.get('data_analyst', {}),
			tools=[
				CodeInterpreterTool(),  # Allows execution of Python code
            	FileReadTool(root_dir=".", mode="write")  # Enables saving files
			],
			verbose=True,
			llm=llm,
			max_iterations=10
		)

	@agent
	def report_generator(self) -> Agent:
		if not self.agents_config:
			raise ValueError("Error: agents_config is None or not loaded properly.")

		return Agent(
			config=self.agents_config.get('report_generator', {}),
			tools=[
            FileReadTool(root_dir=".", mode="read_write")  # Allows reading/writing files
        	],
			verbose=True,
			llm=llm,
			max_iterations=10
		)

	@task
	def research_task(self) -> Task:
		if not self.tasks_config:
			raise ValueError("Error: tasks_config is None or not loaded properly.")
		
		task_config = self.tasks_config.get('research_task', {})
		return Task(
			description=task_config.get('description', 'Default task description'),
        	expected_output=task_config.get('expected_output', ''),
			agent=self.market_researcher(),
			output_file="market_research_task_output.md",
		)

	@task
	def data_analysis_task(self) -> Task:
		if not self.tasks_config:
			raise ValueError("Error: tasks_config is None or not loaded properly.")
		
		task_config = self.tasks_config.get('analysis_task', {})

		return Task(
			description=task_config.get('description', 'Default task description'),
        	expected_output=task_config.get('expected_output', ''),
			agent=self.data_analyst(),
			output_file="data_analysis_report.md"
		)


	@task
	def report_task(self) -> Task:
		if not self.tasks_config:
			raise ValueError("Error: tasks_config is None or not loaded properly.")
		
		task_config = self.tasks_config.get('report_task', {})
		return Task(
			description=task_config.get('description', 'Default task description'),
        	expected_output=task_config.get('expected_output', ''),
			agent=self.report_generator(),
			output_file="final_report.md"
		)
			

	@crew
	def crew(self) -> Crew:
		"""Creates the FinanceProject crew"""
		return Crew(
			agents=self.agents,  # Automatically created by the @agent decorator
			tasks=self.tasks,  # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			max_execution_time=600,
			llm=llm  # Assign OpenAI model to the whole Crew
		)
