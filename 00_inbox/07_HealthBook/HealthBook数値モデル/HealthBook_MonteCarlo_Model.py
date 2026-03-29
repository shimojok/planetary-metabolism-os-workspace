
import numpy as np

def monte_carlo_simulation(
    total_reserve=40000000000000,
    annual_death_benefit=2900000000000,
    annual_medical_benefit=1600000000000,
    mortality_mean=0.035,
    mortality_std=0.01,
    medical_mean=0.08,
    medical_std=0.02,
    discount_rate=0.015,
    years=25,
    simulations=10000
):
    results = []

    for _ in range(simulations):
        mortality_improvement = np.random.normal(mortality_mean, mortality_std)
        medical_reduction = np.random.normal(medical_mean, medical_std)

        mortality_improvement = max(mortality_improvement, 0)
        medical_reduction = max(medical_reduction, 0)

        annual_reduction = (
            annual_death_benefit * mortality_improvement +
            annual_medical_benefit * medical_reduction
        )

        npv = annual_reduction * ((1 - (1 + discount_rate) ** (-years)) / discount_rate)
        reduction_rate = npv / total_reserve

        results.append(reduction_rate)

    return {
        "mean_reduction": np.mean(results),
        "percentile_5": np.percentile(results, 5),
        "percentile_95": np.percentile(results, 95)
    }


if __name__ == "__main__":
    result = monte_carlo_simulation()
    for k, v in result.items():
        print(k, ":", v)
