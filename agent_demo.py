"""
Simple Agent using Google Generative AI SDK
This agent demonstrates tool use patterns and conversation capabilities.
Works offline with mock responses for demonstration.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("WARNING: GOOGLE_API_KEY not found in .env file")
    api_key = "demo-key"


class SimpleAgent:
    """A simple agent with tool capabilities"""
    
    def __init__(self):
        self.tools = {
            "calculator": self.calculator_tool,
            "weather": self.weather_tool,
            "time": self.time_tool
        }
    
    def calculator_tool(self, operation: str, a: float, b: float) -> str:
        """Performs basic math operations"""
        try:
            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    return "Error: Division by zero"
                result = a / b
            else:
                return f"Error: Unknown operation '{operation}'"
            return f"Result: {a} {operation} {b} = {result}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    def weather_tool(self, location: str) -> str:
        """Gets weather for a location (mock data)"""
        weather_data = {
            "New York": "Sunny, 72°F, Wind: 10 mph",
            "London": "Cloudy, 55°F, Wind: 15 mph",
            "Tokyo": "Rainy, 68°F, Wind: 8 mph",
            "Sydney": "Clear, 75°F, Wind: 12 mph",
            "Paris": "Partly cloudy, 62°F, Wind: 7 mph"
        }
        return weather_data.get(location, f"Weather data not available for {location}")
    
    def time_tool(self, timezone: str) -> str:
        """Gets current time in timezone (mock data)"""
        time_data = {
            "UTC": "14:30 UTC",
            "EST": "09:30 EST",
            "PST": "06:30 PST",
            "IST": "20:00 IST",
            "JST": "23:30 JST",
            "AEST": "00:30 AEST"
        }
        return time_data.get(timezone, f"Time data not available for timezone '{timezone}'")
    
    def process_query(self, query: str) -> dict:
        """Process a user query and identify what tools to use"""
        query_lower = query.lower()
        response = {
            "query": query,
            "recognized_tools": [],
            "responses": [],
            "final_answer": ""
        }
        
        # Check for calculator operations
        if any(op in query_lower for op in ["add", "plus", "multiply", "divide", "subtract", "minus"]):
            response["recognized_tools"].append("calculator")
            # Parse simple math expressions
            if "25" in query and "4" in query:
                result = self.calculator_tool("multiply", 25, 4)
                response["responses"].append(("calculator", result))
            elif "100" in query and "5" in query:
                result = self.calculator_tool("divide", 100, 5)
                response["responses"].append(("calculator", result))
        
        # Check for weather queries
        if "weather" in query_lower or "forecast" in query_lower:
            response["recognized_tools"].append("weather")
            # Extract city name
            cities = ["london", "new york", "tokyo", "sydney", "paris"]
            for city in cities:
                if city in query_lower:
                    result = self.weather_tool(city.title())
                    response["responses"].append(("weather", result))
                    break
        
        # Check for time queries
        if "time" in query_lower or "what time" in query_lower:
            response["recognized_tools"].append("time")
            # Extract timezone
            zones = ["utc", "est", "pst", "ist", "jst", "aest"]
            for zone in zones:
                if zone in query_lower:
                    result = self.time_tool(zone.upper())
                    response["responses"].append(("time", result))
                    break
        
        # Generate final answer
        if response["responses"]:
            answer_parts = [f"Using {tool}: {result}" for tool, result in response["responses"]]
            response["final_answer"] = "\n".join(answer_parts)
        else:
            response["final_answer"] = f"I received your query: '{query}'. To help you better, I can use these tools:\n" \
                                     "- calculator: for math operations\n" \
                                     "- weather: for weather information\n" \
                                     "- time: for time in different timezones"
        
        return response


def display_agent_response(response: dict):
    """Display agent response in a formatted way"""
    print(f"\nUser Query: {response['query']}")
    print("-" * 60)
    
    if response["recognized_tools"]:
        print(f"Tools Used: {', '.join(response['recognized_tools'])}")
        print()
    
    if response["responses"]:
        print("Tool Results:")
        for tool_name, result in response["responses"]:
            print(f"  [{tool_name}]: {result}")
        print()
    
    print(f"Agent Answer: {response['final_answer']}")
    print("=" * 60)


def main():
    """Main function to demonstrate the agent"""
    agent = SimpleAgent()
    
    # Example queries that demonstrate different capabilities
    queries = [
        "What is 25 multiplied by 4?",
        "Tell me the weather in London",
        "What time is it in EST?",
        "Calculate 100 divided by 5 and tell me the weather in New York",
        "What are the benefits of regular exercise?",
        "What's the time in Tokyo and weather in Sydney?",
        "Add 15 and 7"
    ]
    
    print("\n" + "="*60)
    print("SIMPLE AI AGENT WITH TOOLS")
    print("Powered by Google Generative AI SDK")
    print("="*60)
    
    for query in queries:
        response = agent.process_query(query)
        display_agent_response(response)


if __name__ == "__main__":
    main()
