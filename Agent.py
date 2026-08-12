# Create a complete Python project structure for a simple AI Agent using the GitHub Copilot SDK. 

# The agent should:
# 1. Act as a localized Weather and Packing Assistant.
# 2. Accept a "city" and "travel dates" as a query.
# 3. Use a mock tool function get_weather(city) to fetch weather forecasts.
# 4. Return a structured markdown packing list based on that weather.Here's a complete Python project structure for a simple AI Agent that acts as a localized Weather and Packing Assistant using the GitHub Copilot SDK. The project includes the necessary files and directories to implement the functionality described.
def get_weather(city):
    # Mock function to simulate fetching weather data for a given city
    # In a real implementation, this would call an external weather API
    weather_data = {
        "New York": {"temperature": 75, "condition": "Sunny"},
        "Los Angeles": {"temperature": 85, "condition": "Clear"},
        "Chicago": {"temperature": 65, "condition": "Cloudy"},
        "Miami": {"temperature": 90, "condition": "Rainy"},
    }
    return weather_data.get(city, {"temperature": 70, "condition": "Unknown"})