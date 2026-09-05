import numpy as np
import pandas as pd

def simulate_strikeouts(pitcher_base_k: float, opponent_k_rate: float, sims: int = 10000):
    """
    Simulates pitcher strikeouts using a simple Poisson/Normal distribution 
    to create the distribution chart seen in the dashboard.
    """
    # Blending pitcher baseline skill with opponent vulnerability
    expected_ks = (pitcher_base_k + (opponent_k_rate * 27)) / 2
    outcomes = np.random.poisson(lam=expected_ks, size=sims)
    
    # Calculate probabilities of hitting over/under common lines
    return outcomes

def evaluate_prop_edge(projected_value: float, sportsbook_line: float):
    """
    Calculates the numerical gap between your model's projection 
    and the sportsbook line (e.g., +1.3 vs line).
    """
    diff = projected_value - sportsbook_line
    if diff >= 2.0:
        return "STRONG OVER", diff
    elif diff <= -2.0:
        return "STRONG UNDER", diff
    else:
        return "NO PLAY / NOISE", diff
