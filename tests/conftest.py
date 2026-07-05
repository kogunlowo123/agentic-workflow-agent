"""Test configuration for Agentic Workflow Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "agentic-workflow-agent", "category": "AI Engineering"}
