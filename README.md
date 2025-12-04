# Google AI SDK Simple Agent

A simple agent implementation using Google's Generative AI SDK that demonstrates tool calling capabilities.

## Features

- **Tool Integration**: The agent can use three different tools:
  - `calculator`: Performs basic math operations (add, subtract, multiply, divide)
  - `weather_lookup`: Returns mock weather data for locations
  - `get_time`: Returns current time in specified timezones

- **Conversational AI**: Uses Google's Gemini model for natural language understanding
- **Function Calling**: Automatically selects and executes appropriate tools based on user queries

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Key**:
   - Copy `.env.example` to `.env`
   - Add your Google API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your-actual-api-key-here
     ```
   - Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

3. **Run the agent**:
   ```bash
   python agent.py
   ```

## Usage

The agent processes natural language queries and uses available tools to answer questions:

- **Math**: "What is 25 multiplied by 4?"
- **Weather**: "Tell me the weather in London"
- **Time**: "What time is it in EST?"
- **Combined**: "Calculate 100 divided by 5 and tell me the weather in New York"

## Architecture

The agent uses:
- **Google Generative AI SDK**: For LLM capabilities and tool orchestration
- **Tool Schema Definition**: JSON schemas that describe available tools
- **Tool Processing**: A function that executes tool calls and returns results
- **Multi-turn Conversation**: Maintains context across agent interactions

## Example Flow

1. User sends a message
2. Agent calls Gemini model with available tools
3. Model analyzes the query and decides which tools to use
4. Tools are executed and results are returned
5. Agent provides a final response combining tool outputs

## Environment Variables

- `GOOGLE_API_KEY`: Your Google Generative AI API key (required)

## License

MIT
