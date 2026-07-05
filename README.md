# Agentic Workflow Agent

[![CI](https://github.com/kogunlowo123/agentic-workflow-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/agentic-workflow-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Multi-agent orchestration engine that designs, deploys, and monitors agentic workflows with tool-calling, planning loops, memory management, human-in-the-loop checkpoints, and automatic error recovery.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `design_workflow` | Design a multi-agent workflow graph from requirements |
| `deploy_agents` | Deploy a configured set of agents with specified roles and tools |
| `execute_workflow` | Execute an agentic workflow with input data |
| `add_checkpoint` | Add a human-in-the-loop checkpoint to a workflow step |
| `monitor_execution` | Monitor running workflow execution and trace agent decisions |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/workflows/design` | Design a workflow |
| `POST` | `/api/v1/workflows/deploy` | Deploy agents |
| `POST` | `/api/v1/workflows/{workflow_id}/execute` | Execute workflow |
| `POST` | `/api/v1/workflows/{workflow_id}/checkpoints` | Add checkpoint |
| `GET` | `/api/v1/executions/{execution_id}/trace` | Monitor execution |

## Features

- Workflow Design
- Agent Orchestration
- Tool Integration
- Human In Loop
- Error Recovery

## Integrations

- Langgraph
- Crewai
- Autogen
- Openai Agents
- Langsmith

## Architecture

```
agentic-workflow-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── agentic_workflow_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LangGraph + CrewAI + AutoGen + OpenAI Agents SDK**

---

Built as part of the Enterprise AI Agent Platform.
