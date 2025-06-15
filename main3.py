import os
import asyncio
from langchain_ollama import ChatOllama
from browser_use import Agent, BrowserSession

# Optional: Disable telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"  # Replace with actual host if remote

browser_session = BrowserSession(
    executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
)

llm = ChatOllama(model="qwen2.5:7b")  # Check if model name matches exactly

async def main():
    agent = Agent(
        task="go to amazon.com and search for scissors.",
        llm=llm, 
        use_vision=False,
        browser_session=browser_session
    )
    result = await agent.run()
    print(result)
    await browser_session.close()

asyncio.run(main())
