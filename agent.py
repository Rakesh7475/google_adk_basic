"""
Simple Agent using Google Generative AI SDK
This agent demonstrates basic conversation and tool capabilities.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

genai.configure(api_key=api_key)


def process_tool_call(tool_name: str, tool_input: dict) -> str:
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

try:
    import google.generativeai as genai
    genai.configure(api_key=api_key)
    GENAI_AVAILABLE = True
except Exception as e:
    print(f"Note: Google AI SDK connection issue: {e}")
    GENAI_AVAILABLE = False

    """Process tool calls and return results"""
    if tool_name == "calculator":
        operation = tool_input.get("operation")
        a = tool_input.get("a")
        b = tool_input.get("b")
        
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
            return "Error: Unknown operation"
        
        return f"Result: {a} {operation} {b} = {result}"
    
    elif tool_name == "weather_lookup":
        location = tool_input.get("location")
        # Mock weather data
        weather_data = {
            "New York": "Sunny, 72°F",
            "London": "Cloudy, 55°F",
            "Tokyo": "Rainy, 68°F",
            "Sydney": "Clear, 75°F"
        }
        return weather_data.get(location, f"Weather for {location}: Data not available")
    
    elif tool_name == "get_time":
        timezone = tool_input.get("timezone")
        # Mock time data
        time_data = {
            "UTC": "14:30 UTC",
            "EST": "09:30 EST",
            "PST": "06:30 PST",
            "IST": "20:00 IST"
        }
        return time_data.get(timezone, f"Time in {timezone}: Data not available")
    
    return "Error: Unknown tool"


def run_agent_simple(user_message: str) -> str:
    """Run a simple agent that processes natural language queries"""
    print(f"\n{'='*60}")
    print(f"User: {user_message}")
    print(f"{'='*60}")
    
    # Create a simple prompt-based agent
    system_prompt = """You are a helpful assistant with access to these tools:

1. calculator: Performs math operations (add, subtract, multiply, divide)
   - For "25 * 4", use calculator with operation='multiply', a=25, b=4

2. weather_lookup: Gets weather for cities (New York, London, Tokyo, Sydney)
   - For "weather in London", use weather_lookup with location='London'

3. get_time: Gets time in timezones (UTC, EST, PST, IST)
   - For "time in EST", use get_time with timezone='EST'

Answer questions directly when possible. When a tool would be useful, explain which tool would be used and why."""

    model = genai.GenerativeModel(model_name="gemini-pro")
    
    try:
        # Generate response
        full_prompt = f"{system_prompt}\n\nUser: {user_message}\n\nAssistant:"
        response = model.generate_content(full_prompt)
        
        agent_response = response.text
        print(f"Agent: {agent_response}")
        
        return agent_response
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return str(e)


def main():
    """Main function to demonstrate the agent"""
    # Example queries
    queries = [
        "What is 25 multiplied by 4?",
        "Tell me the weather in London",
        "What time is it in EST?",
        "Calculate 100 divided by 5 and tell me the weather in New York",
        "What are the benefits of regular exercise?"
    ]
    
    for query in queries:
        try:
            result = run_agent_simple(query)
            print(f"\n")
        except Exception as e:
            print(f"Error processing query: {e}\n")


if __name__ == "__main__":
    main()
