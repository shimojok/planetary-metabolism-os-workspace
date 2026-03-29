
import math

def healthbook_simulation(
    total_reserve,
    annual_death_benefit,
    annual_medical_benefit,
    mortality_improvement,
    medical_reduction,
    discount_rate,
    years
):
    annual_death_reduction = annual_death_benefit * mortality_improvement
    annual_medical_reduction = annual_medical_benefit * medical_reduction
    total_annual_reduction = annual_death_reduction + annual_medical_reduction
    
    npv = total_annual_reduction * ((1 - (1 + discount_rate) ** (-years)) / discount_rate)
    reserve_reduction_rate = npv / total_reserve
    
    return {
        "annual_death_reduction": annual_death_reduction,
        "annual_medical_reduction": annual_medical_reduction,
        "total_annual_reduction": total_annual_reduction,
        "npv": npv,
        "reserve_reduction_rate": reserve_reduction_rate
    }

if __name__ == "__main__":
    result = healthbook_simulation(
        total_reserve=40000000000000,
        annual_death_benefit=2900000000000,
        annual_medical_benefit=1600000000000,
        mortality_improvement=0.035,
        medical_reduction=0.08,
        discount_rate=0.015,
        years=25
    )
    
    for k, v in result.items():
        print(k, ":", format(v, ","))
