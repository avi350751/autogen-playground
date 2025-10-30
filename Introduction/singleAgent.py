from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()


async def newAgent():
    print("This is a new agent function.")
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    
    
    agent = AssistantAgent(
                name= "Agent007",
                model_client= model_client)
    
    await Console(agent.run_stream(task="What is the capital of France?"))
    await model_client.close()

asyncio.run(newAgent())
