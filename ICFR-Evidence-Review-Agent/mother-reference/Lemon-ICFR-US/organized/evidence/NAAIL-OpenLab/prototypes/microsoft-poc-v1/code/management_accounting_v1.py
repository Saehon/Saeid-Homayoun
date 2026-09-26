def capacity_cost_rate(resource_cost_per_hour, practical_capacity_minutes_per_hour=48):
    return resource_cost_per_hour / practical_capacity_minutes_per_hour

def tdabc_cost(rate_per_minute, required_minutes):
    return rate_per_minute * required_minutes

def activity_based_cost(activity_rate, driver_quantity):
    return activity_rate * driver_quantity

def cost_per_verified_output(total_cost, verified_outputs):
    if verified_outputs <= 0:
        raise ValueError('verified_outputs must be positive')
    return total_cost / verified_outputs
