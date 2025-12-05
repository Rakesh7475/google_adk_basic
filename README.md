
# Google ADK Basic Agent Demo

This project demonstrates a simple agent using Google's Generative AI SDK (Gemini) with tool-calling capabilities and a FastAPI web UI.

## Features

- **Tool Integration**: Supports three tools:
   - `calculator`: Basic math operations (add, subtract, multiply, divide)
   - `weather_lookup`: Returns mock weather data for cities
   - `get_time`: Returns mock current time for timezones
- **Conversational AI**: Uses Gemini model for natural language understanding
- **Web UI**: FastAPI app with a simple HTML frontend for interactive queries
- **Extensible**: Easy to add new tools or connect to real APIs

## Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key (optional for demo)
- Copy `.env.example` to `.env`
- Add your Google API key:
   ```
   GOOGLE_API_KEY=your-actual-api-key-here
   ```
- Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 3. Run the agent (CLI)
```bash
python agent.py
```

### 4. Run the web UI (FastAPI)
```bash
uvicorn web_app:app --reload
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Usage Examples

**Math:**
- "What is 25 multiplied by 4?"
- "Calculate 100 divided by 5"

**Weather:**
- "Tell me the weather in London"
- "Weather in New York"

**Time:**
- "What time is it in EST?"
- "Current time in UTC"

**Combined:**
- "Calculate 100 divided by 5 and tell me the weather in New York"

## Project Structure

- `agent.py` — Main agent logic (Gemini + tool calls)
- `agent_demo.py` — Standalone agent with mock tools (no API key needed)
- `web_app.py` — FastAPI web server for local UI
- `static/index.html` — Simple HTML frontend for queries
- `requirements.txt` — Python dependencies
- `.env.example` — API key template
- `.gitignore` — Excludes `.env` and build artifacts

## How It Works

1. User sends a query (CLI or web UI)
2. Agent analyzes the query and selects tools
3. Tool results are generated (mock or real)
4. Gemini model combines results and generates a response
5. Response is returned to the user

## Extending

- Add new tools by editing `process_tool_call` in `agent.py`
- Connect to real APIs by replacing mock data
- Customize the web UI in `static/index.html`

## Environment Variables

- `GOOGLE_API_KEY`: Your Google Generative AI API key (required for Gemini integration)

## License

MIT
