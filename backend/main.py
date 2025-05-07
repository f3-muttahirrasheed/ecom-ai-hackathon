from fastapi import FastAPI, HTTPException
#from backend.api import agents, tools

app = FastAPI(title="AgentDock MCP Server")

#app.include_router(agents.router, prefix="/agents")
#app.include_router(tools.router, prefix="/tools")

@app.get("/")
def root():
    return {"message": "Welcome to AgentDock MCP Server"}

