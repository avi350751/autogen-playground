import os
import asyncio
from autogen_core import Image
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console
from autogen_agentchat.messages import MultiModalMessage

load_dotenv()


async def newAgent():
    print("This is a new agent function.")
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
    image = Image.from_file(".//Introduction//files//ImageDiscussion1.jpg")
    multimodal_msg = MultiModalMessage(
        content=["What do you understand from this image?",
                 image], source="user"
    )
    
    agent = AssistantAgent(
                name= "MultiModalAgent",
                model_client= model_client)
    
    await Console(agent.run_stream(task=multimodal_msg))
    await model_client.close()

asyncio.run(newAgent())