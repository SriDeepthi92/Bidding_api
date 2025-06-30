def adjusted_cpc(current_cpc: float, target_roas: float) -> float:
    if current_cpc <= 0 or target_roas <= 0:
        return 0.0
    return round(current_cpc * (target_roas / 100), 4)