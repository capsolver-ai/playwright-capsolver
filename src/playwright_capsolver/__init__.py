from __future__ import annotations

from typing import Any

from capsolver_core import Capsolver


class CapsolverPage:
    """Attach CapSolver detection and recovery to an existing Playwright page."""

    def __init__(self, page: Any, api_key: str | None = None) -> None:
        self.page = page
        self.client = Capsolver(api_key=api_key)

    async def detect(self) -> list[Any]:
        return await self.client.detect(self.page)

    async def solve(self, *, autofill: bool = True, **kwargs: Any) -> list[Any]:
        from capsolver_core import SolveOnPageOptions

        options = SolveOnPageOptions(autofill=autofill, **kwargs)
        return await self.client.solve_on_page(self.page, options)


async def solve_page(page: Any, api_key: str | None = None, **kwargs: Any) -> list[Any]:
    """Detect, solve, and fill all supported challenges on ``page``."""
    return await CapsolverPage(page, api_key).solve(**kwargs)

__version__ = "0.1.0"
