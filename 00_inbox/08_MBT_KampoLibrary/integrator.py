import numpy as np

class EcosystemIntegrator:
    """
    Integrates reports from all agents for a holistic assessment.
    """
    def __init__(self):
        self.ideal_ecosystem_state = np.random.rand(100) # Example ideal state
        self.available_resources = {'water': 1000, 'mbt55': 500}

    def integrate_reports(self, agent_reports: dict) -> dict:
        """Integrates all agent reports into a single assessment."""
        state_vector = self._create_state_vector(agent_reports)
        optimality_score = self._calc_ecosystem_optimality(state_vector)
        integrated_risk = self._integrate_risks(agent_reports)
        
        return {
            'ecosystem_health_score': optimality_score,
            'integrated_risk_assessment': integrated_risk,
            'intervention_priority_list': self._determine_intervention_priority(agent_reports),
            'system_stability_index': self._calc_stability_index(state_vector),
            'state_vector': state_vector,
            'ideal_state': self.ideal_ecosystem_state
        }

    def _normalize(self, report_data: dict) -> np.ndarray:
        if not report_data or not isinstance(report_data, dict): return np.array([])
        return np.array([v for v in report_data.values() if isinstance(v, (int, float))])

    def _create_state_vector(self, agent_reports: dict) -> np.ndarray:
        vectors = [self._normalize(report) for report in agent_reports.values()]
        return np.concatenate([v for v in vectors if v.size > 0])

    def _calc_ecosystem_optimality(self, state_vector: np.ndarray) -> float:
        return 0.85 # Placeholder

    def _integrate_risks(self, agent_reports: dict) -> dict:
        return {"overall_risk": 0.2, "drivers": ["hypercycle"]} # Placeholder

    def _determine_intervention_priority(self, agent_reports: dict) -> list:
        return ["Priority 1: Mitigate hypercycle risk"] # Placeholder

    def _calc_stability_index(self, state_vector: np.ndarray) -> float:
        return 0.92 # Placeholder