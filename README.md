# AgentDock MCP Server

## Overview

AgentDock is a FastAPI-based server to register, manage, and interact with intelligent agents.

## Requirements

- Python 3.10+
- Docker (for containerized run)

## Local Setup

```bash
pip3 install -r requirements.txt
python3 -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 5000
