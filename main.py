# Optional: Disable telemetry
# os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Optional: Set the OLLAMA host to a remote server
# os.environ["OLLAMA_HOST"] = "http://x.x.x.x:11434"

import asyncio
# import os
# import sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# from dotenv import load_dotenv

# load_dotenv()

from langchain_ollama import ChatOllama

from browser_use import Agent
# from browser_use.agent.views import AgentHistoryList


async def run_search() -> str:
	agent = Agent(
		task="Search for a 'python documentation'",
		llm=ChatOllama(
			# model='llama3.2:1b',
            # model='llama3.2',    
            model='qwen2.5:7b',    
			num_ctx=32000,
		),
	)

	result = await agent.run()
	return result


async def main():
	result = await run_search()
	print('\n\n', result)


if __name__ == '__main__':
	asyncio.run(main())