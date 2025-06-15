from langchain_ollama import ChatOllama
from browser_use import Agent
from pydantic import SecretStr

import asyncio
import os

from browser_use import Agent, BrowserSession

# Optional: Disable telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
os.environ["OLLAMA_HOST"] = "http://x.x.x.x:11434"

# If no executable_path provided, uses Playwright/Patchright's built-in Chromium
browser_session = BrowserSession(
    executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    # user_data_dir='~/.config/browseruse/profiles/default'
)

llm=ChatOllama(model="qwen2.5:7b", num_ctx=32000)

# llm = ChatOpenAI(model="gpt-4o")

async def main():
    agent = Agent(
        task="Compare the price of gpt-4o and DeepSeek-V3",
        llm=llm, 
        use_vision=False,
        browser_session =browser_session
        # enable_memory=False
    )
    result = await agent.run()
    print(result)

asyncio.run(main())