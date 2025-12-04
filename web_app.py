from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from agent_demo import SimpleAgent
import os

app = FastAPI(title="Agent Demo UI")

# Mount the static folder
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.isdir(static_dir):
    os.makedirs(static_dir, exist_ok=True)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

agent = SimpleAgent()


@app.get("/", response_class=FileResponse)
async def index():
    index_file = os.path.join(static_dir, "index.html")
    return FileResponse(index_file)


@app.post("/api/query")
async def api_query(request: Request):
    payload = await request.json()
    query = payload.get("query", "")
    if not query:
        return JSONResponse({"error": "No query provided"}, status_code=400)

    # Call the local agent
    result = agent.process_query(query)

    return JSONResponse(result)


# Run with: uvicorn web_app:app --reload
