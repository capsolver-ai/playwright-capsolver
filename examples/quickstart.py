"""Exercise CapSolver Agent's Playwright-backed browser tools."""

import asyncio
import json
import os

from capsolver_agent import create_executor, get_all_tools


async def main() -> None:
    target_url = os.getenv("TARGET_URL", "https://example.com")
    executor = create_executor()

    browser_tools = {
        tool.name: tool.to_json_schema()
        for tool in get_all_tools()
        if tool.name in {"detect_captchas", "solve_on_page"}
    }
    print("Browser tool schemas:")
    print(json.dumps(browser_tools, indent=2))

    detection = await executor.execute("detect_captchas", {"page_url": target_url})
    print("Detection result:")
    print(json.dumps(detection, indent=2))

    if os.getenv("CAPSOLVER_RUN_SOLVE", "false").lower() == "true":
        solved = await executor.execute(
            "solve_on_page",
            {"page_url": target_url, "autofill": True},
        )
        print("Solve result:")
        print(json.dumps(solved, indent=2))
    else:
        print("Solve skipped. Set CAPSOLVER_RUN_SOLVE=true only for an authorized test page.")


if __name__ == "__main__":
    asyncio.run(main())
