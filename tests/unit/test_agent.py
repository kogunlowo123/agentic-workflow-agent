"""Agentic Workflow Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_design_workflow():
    """Test Design a multi-agent workflow graph from requirements."""
    tools = AgentTools()
    result = await tools.design_workflow(task_description="test", agent_roles="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_deploy_agents():
    """Test Deploy a configured set of agents with specified roles and tools."""
    tools = AgentTools()
    result = await tools.deploy_agents(workflow_config="test", runtime="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_execute_workflow():
    """Test Execute an agentic workflow with input data."""
    tools = AgentTools()
    result = await tools.execute_workflow(workflow_id="test", input_data="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_add_checkpoint():
    """Test Add a human-in-the-loop checkpoint to a workflow step."""
    tools = AgentTools()
    result = await tools.add_checkpoint(workflow_id="test", step_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.agentic_workflow_agent_agent import AgenticWorkflowAgentAgent
    agent = AgenticWorkflowAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
