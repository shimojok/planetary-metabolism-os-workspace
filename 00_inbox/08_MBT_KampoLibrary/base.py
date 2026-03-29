import asyncio
from datetime import datetime

class AgentBase:
    """
    All specialized agents inherit from this base class.
    It defines the basic structure for monitoring and reporting.
    """
    def __init__(self, name: str, dependencies: list = None):
        self.name = name
        self.dependencies = dependencies or []
        self.state = {}

    async def monitor(self, ecosystem_state: dict) -> dict:
        """
        Monitors the ecosystem state and returns an assessment.
        This method must be implemented by subclasses.
        """
        raise NotImplementedError("The 'monitor' method must be implemented by subclasses.")

    def calculate_metrics(self) -> dict:
        """Calculates specific metrics based on the agent's state."""
        return {}

class AgentManager:
    """Manages the lifecycle and execution of all registered agents."""
    def __init__(self):
        self.agents: dict[str, AgentBase] = {}

    def register_agent(self, agent: AgentBase):
        """Registers an agent with the manager."""
        self.agents[agent.name] = agent

    async def run_monitoring_cycle(self, ecosystem_data: dict) -> dict:
        """Runs the monitoring cycle for all registered agents."""
        tasks = {name: asyncio.create_task(agent.monitor(ecosystem_data)) for name, agent in self.agents.items()}
        
        results = await asyncio.gather(*tasks.values(), return_exceptions=True)
        
        agent_reports = {}
        for agent_name, result in zip(tasks.keys(), results):
            agent_reports[agent_name] = result if not isinstance(result, Exception) else {'error': str(result)}
                
        return agent_reports