from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

import os
from crewai.tools import tool  
from crewai_tools import FileWriterTool, TavilySearchTool
from langchain_experimental.utilities import PythonREPL
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, api_key=os.getenv("OPENAI_API_KEY"))

os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

tavily_tool = TavilySearchTool()
file_writer = FileWriterTool()

@tool("python_repl")
def python_repl_tool(command: str) -> str:
    """Execute python code in a REPL. Useful for calculating financial models 
    or processing data. Input should be valid python code."""
    return PythonREPL().run(command)

@CrewBase
class AutoStartupAi():
    """AutoStartupAi crew - fully automated startup generator"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # =========================
    # Agents
    # =========================
    @agent
    def trend_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_agent'], # type: ignore[index]
            verbose=True,
            tools=[tavily_tool],
            llm=llm
        )

    @agent
    def market_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['market_agent'], # type: ignore[index]
            tools=[tavily_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def idea_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['idea_agent'], # type: ignore[index]
            tools=[tavily_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def critic_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['critic_agent'], # type: ignore[index]
            tools=[tavily_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def product_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['product_agent'], # type: ignore[index]
            tools=[tavily_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def marketing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['marketing_agent'], # type: ignore[index]
            tools=[tavily_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def finance_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['finance_agent'], # type: ignore[index]
            tools=[python_repl_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def tech_architect_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_architect_agent'], # type: ignore[index]
            tools=[tavily_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def code_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['code_agent'], # type: ignore[index]
            tools=[python_repl_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def website_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['website_agent'], # type: ignore[index]
            tools=[tavily_tool],
            verbose=True,
            llm=llm
        )

    @agent
    def pitch_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['pitch_agent'], # type: ignore[index]
            tools=[tavily_tool],
            verbose=True
        )

    @agent
    def report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['report_agent'], # type: ignore[index]
            tools=[file_writer],
            verbose=True,
            llm=llm
        )

    # =========================
    # Tasks
    # =========================
    @task
    def trend_task(self) -> Task:
        return Task(
            config=self.tasks_config['trend_task'], # type: ignore[index]
        )

    @task
    def market_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_task'], # type: ignore[index]
        )

    @task
    def idea_task(self) -> Task:
        return Task(
            config=self.tasks_config['idea_task'], # type: ignore[index]
        )

    @task
    def critic_task(self) -> Task:
        return Task(
            config=self.tasks_config['critic_task'], # type: ignore[index]
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task'], # type: ignore[index]
        )

    @task
    def marketing_task(self) -> Task:
        return Task(
            config=self.tasks_config['marketing_task'], # type: ignore[index]
        )

    @task
    def finance_task(self) -> Task:
        return Task(
            config=self.tasks_config['finance_task'], # type: ignore[index]
        )

    @task
    def architecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['architecture_task'], # type: ignore[index]
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'], # type: ignore[index]
        )

    @task
    def website_task(self) -> Task:
        return Task(
            config=self.tasks_config['website_task'], # type: ignore[index]
            output_file='index.html'
        )

    @task
    def pitch_task(self) -> Task:
        return Task(
            config=self.tasks_config['pitch_task'], # type: ignore[index]
        )

    @task
    def final_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_task'], # type: ignore[index]
            output_file='research/startup_blueprint.md'
        )

    # =========================
    # Crew
    # =========================
    @crew
    def crew(self) -> Crew:
        """Creates the AutoStartupAi crew"""
        return Crew(
            agents=self.agents,  # automatically collected from @agent decorators
            tasks=self.tasks,    # automatically collected from @task decorators
            process=Process.sequential,  # run tasks sequentially
            verbose=True,
        )