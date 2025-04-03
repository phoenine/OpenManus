import asyncio
import sys

from app.agent.manus import Manus
from app.logger import logger


async def main():
    agent = Manus()
    try:
        # prompt = input("Enter your prompt: ")
        prompt = sys.stdin.read().strip()
        if not prompt.strip():
            logger.warning("Empty prompt provided.")
            return

        logger.warning("Processing your request...")
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")


if __name__ == "__main__":
    asyncio.run(main())
