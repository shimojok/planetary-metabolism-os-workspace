import asyncio
from agents.base import AgentManager
from agents.hypercycle_agent import HypercycleMonitorAgent
from agents.nutrient_agent import NutrientCascadeAgent
from agents.biodiversity_agent import BiodiversityAgent
from agents.metabolic_agent import MetabolicFlowAgent
from agents.element_agent import ElementTransmutationAgent
from agents.risk_agent import RiskPredictionAgent
from external.safely_chain_agent import QualityFreshnessAgent
from external.pbpe_agent import CarbonPBPEAgent
from control.controller import AgriWareAIController

class AgriWareAISystem:
    """
    Main class for the AgriWare AI System.
    This class integrates the core engine and specialized agent groups.
    """
    def __init__(self):
        self.agent_manager = AgentManager()
        agents_to_register = [
            HypercycleMonitorAgent(), NutrientCascadeAgent(),
            BiodiversityAgent(), MetabolicFlowAgent(),
            ElementTransmutationAgent(), RiskPredictionAgent(),
            QualityFreshnessAgent(), CarbonPBPEAgent()
        ]
        for agent in agents_to_register:
            self.agent_manager.register_agent(agent)
        
        self.controller = AgriWareAIController(self.agent_manager, control_interval_seconds=10)

    async def start(self):
        """Starts the main control loop of the AgriWare system."""
        await self.controller.control_loop()

if __name__ == "__main__":
    system = AgriWareAISystem()
    print("Starting AgriWare AI System. Press Ctrl+C to stop.")
    asyncio.run(system.start())