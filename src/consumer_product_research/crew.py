from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff

# Uncomment the following line to use an example of a custom tool
# from consumer_product_research.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, YoutubeVideoSearchTool

@CrewBase
class ConsumerProductResearch():
	"""ConsumerProductResearch crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@before_kickoff # Optional hook to be executed before the crew starts
	def pull_data_example(self, inputs):
		# Example of pulling data from an external API, dynamically changing the inputs
		inputs['extra_data'] = "This is extra data"
		return inputs

	@after_kickoff # Optional hook to be executed after the crew has finished
	def log_results(self, output):
		# Example of logging results, dynamically changing the output
		print(f"Results: {output}")
		return output

	@agent
	def analyst_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['analyst_agent'],
			tools=[SerperDevTool(), ScrapeWebsiteTool(), YoutubeVideoSearchTool()],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def researcher_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher_agent'],
			tools=[SerperDevTool(), ScrapeWebsiteTool(), YoutubeVideoSearchTool()],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def summary_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['summary_agent'],
			tools=[],
			allow_delegation=True,
			verbose=True
		)

	@agent
	def reporting_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_agent'],
			tools=[],
			allow_delegation=True,
			verbose=True
		)

	@task
	def analyze_product_comparison_framework_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_product_comparison_framework_task'],
			agent=self.analyst_agent(),
		)

	@task
	def research_product_information_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_product_information_task'],
			agent=self.researcher_agent(),
		)

	@task
	def synthesize_product_insights_task(self) -> Task:
		return Task(
			config=self.tasks_config['synthesize_product_insights_task'],
			agent=self.summary_agent(),
		)

	@task
	def generate_product_recommendations_task(self) -> Task:
		return Task(
			config=self.tasks_config['generate_product_recommendations_task'],
			agent=self.reporting_agent(),
			output_file='product_recommendations.md',
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ConsumerProductResearch crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
