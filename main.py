import dotenv

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import count_letters

@CrewBase
class TranslatorCrew:
    
  
  @agent
  def translator_agent(self):
    return Agent(
      config= self.agents_config["translator_agent"],
    )
  
  @agent
  def counter_agent(self):
    return Agent(
     config= self.agents_config["counter_agent"],
     tools=[count_letters],
    )
  
  @task
  def translate_task(self):
    return Task(
      config=self.tasks_config["translate_task"],
        )
  
  @task
  def naturalize_translation_task(self):
    return Task(
      config=self.tasks_config["naturalize_translation_task"],
    )
  
  @task
  def counter_task(self):
    return Task(
      config=self.tasks_config["counter_task"],
        )
  
  @crew
  def assemble_crew(self):
    return Crew(
      agents=self.agents,
      tasks=self.tasks,
      verbose=True,
    )
    
TranslatorCrew().assemble_crew().kickoff(
  inputs={
    "sentence": "The film captures the struggles of young adults trying to find their place in a rapidly changing world.",
}) 