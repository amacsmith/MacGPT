async def weather_function(location):
    # Simulate weather API call
    return f"The weather in {location} is sunny."

async def calculator_function(expression):
    return str(eval(expression))

available_functions = {
    "weather": weather_function,
    "calculator": calculator_function,
}