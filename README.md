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
│
├── modules/                              # Per-cloud building blocks
│   ├── contracts/                        # Cloud-agnostic interface contracts
│   │   ├── network.md                    # VPC/VNet with private subnets
│   │   ├── vectorstore.md                # Vector search, BM25, hybrid, metadata filter
│   │   ├── object-store.md               # Encrypted object storage
│   │   └── inference-gateway.md          # LLM chat, embeddings, reranking
│   ├── netops/                           # Network boundary (VPC, subnets, SGs)
│   ├── secops/                           # Keys, identity, guardrails
│   ├── appops/                           # Data and model plane
│   └── devops/                           # State backend and CI/CD
│
├── blueprints/                           # RAG topologies that compose modules
│   ├── rag-naive/                        # Keyword-only (pilot)
│   ├── rag-hybrid/                       # Keyword + vector + reranker (production)
│   ├── rag-graph/                        # Entity-relationship graph retrieval
│   ├── rag-multimodal/                   # Text + image + table retrieval
│   └── rag-agentic/                      # RAG as a tool in multi-agent system
│
├── live/                                 # Real environments, pinned versions
│   ├── _bootstrap/aws/                   # One-time state bucket creation
│   ├── dev/us/rag-hybrid/                # Development
│   ├── staging/                          # Pre-production
│   └── prod/                             # Production
│
├── factory/                              # Stamping machinery
│   ├── scaffold.sh                       # Stamps a blueprint into live/
│   └── catalog.yaml                      # Registry of available patterns
│
├── platform/                             # Agentic RAG reference implementation
│   └── reference-apps/reference-agentic-rag/
│       ├── app/contracts/                # DataLane enum, models, tenancy
│       ├── app/search/                   # FULL search pipeline
│       │   ├── retrievers/               # bm25, dense, hybrid, graph, parent_doc
│       │   ├── reranking/                # cross_encoder, llm_rerank, boost, cascade
│       │   ├── query/                    # classify, rewrite, expand, hyde, decompose
│       │   ├── multi_hop/                # budget, planner, executor, synthesizer
│       │   ├── corrective/               # self_critique, web_fallback
│       │   ├── adaptive/router.py        # Public facade for all search
│       │   └── cache/                    # exact, semantic, redis backend
│       └── data/raw_examples/            # Sample data (indexed, live, structured lanes)
│
├── src/                                  # FastAPI backend (7-layer architecture)
│   ├── gateway/                          # Layer 2: AI Gateway (control plane)
│   │   ├── middleware.py                 # Auth, rate limiting, request routing
│   │   ├── guardrails.py                 # Prompt injection, content safety
│   │   ├── pii_redactor.py               # PII detection and redaction
│   │   ├── token_budget.py               # Per-user/org token limits
│   │   └── audit_trail.py                # Immutable request/response log
│   ├── agent/                            # Layer 3: Agent orchestration
│   │   ├── agentic_workflow_agent_agent.py     # Main agent implementation
│   │   ├── tools.py                      # 5 domain-specific tools
│   │   ├── prompts.py                    # Expert system prompts
│   │   └── orchestrator/                # Plan → Research → Execute → Validate → Respond
│   │       ├── planner.py               # Task decomposition and routing
│   │       ├── researcher.py            # RAG retrieval and knowledge gathering
│   │       ├── executor.py              # Tool execution with retry
│   │       ├── validator.py             # Output verification
│   │       └── guard.py                 # RBAC and destructive action gating
│   ├── tools/                            # Layer 4: Tool integrations
│   │   └── registry.py                  # Domain tool dispatch with permissions
│   ├── data/                             # Company data integration
│   │   └── lanes.py                     # INDEXED / LIVE / STRUCTURED routing
│   ├── memory/                           # Layer 6: Persistent state
│   │   ├── short_term.py                # Redis session context
│   │   ├── long_term.py                 # Vector DB embeddings
│   │   ├── lexical.py                   # PostgreSQL BM25 index
│   │   ├── knowledge_graph.py           # Entity-relationship graph
│   │   ├── decisions.py                 # Durable decision log
│   │   └── manager.py                   # Unified memory interface
│   ├── llm/                              # Layer 7: Multi-model router
│   │   ├── router.py                    # GPT/Claude/Gemini routing + fallbacks
│   │   └── providers/                   # OpenAI, Anthropic, Google providers
│   ├── api/                              # FastAPI routes and middleware
│   ├── rag/                              # RAG pipeline
│   ├── mcp/                              # MCP server (tool exposure)
│   ├── a2a/                              # Agent-to-agent protocol
│   ├── auth/                             # JWT + RBAC + API key auth
│   ├── config/                           # Application settings
│   ├── connectors/                       # Data source connectors
│   └── models/                           # Pydantic schemas
│
├── configs/                              # Environment configurations
│   ├── dev.yaml                          # Local development
│   ├── staging.yaml                      # Pre-production
│   └── prod.yaml                         # Production
│
├── infrastructure/                       # Deployment configurations
│   └── docker/                           # Multi-stage Dockerfiles
│
├── policy/                               # Policy as code
│   ├── opa/                              # Open Policy Agent rules
│   └── checkov/                          # Infrastructure security scanning
│
├── tests/                                # Unit, integration, E2E
├── docs/                                 # Architecture, security, deployment, operations
├── .github/workflows/                    # CI/CD pipelines
├── docker-compose.yml                    # Local development stack
├── pyproject.toml                        # Python dependencies
├── Makefile                              # Developer workflow commands
└── openapi.yaml                          # API specification
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
