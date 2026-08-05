# Playwright + CapSolver Agent examples

[![Demo repository](https://img.shields.io/badge/type-runnable%20demo-0A7BBB)](#repository-scope)
[![CI](https://github.com/capsolver-ai/playwright-capsolver/actions/workflows/ci.yml/badge.svg)](https://github.com/capsolver-ai/playwright-capsolver/actions/workflows/ci.yml)
[![License: ISC](https://img.shields.io/badge/license-ISC-green.svg)](LICENSE)

Runnable examples for CapSolver Agent's Playwright-backed `detect_captchas` and `solve_on_page` tools.

> Examples only: this repository does not publish `playwright-capsolver` or duplicate the browser engine.

## Repository scope

The shared [`capsolver-agent`](https://github.com/capsolver-ai/capsolver-agent) tool executor delegates browser work to `capsolver-core`. This repository demonstrates those public tools and keeps solving opt-in.

## Quick start

```bash
git clone https://github.com/capsolver-ai/playwright-capsolver.git
cd playwright-capsolver
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
playwright install chromium
```

Export [`.env.example`](.env.example) values and run `python examples/quickstart.py`.

By default the demo only detects. Set `CAPSOLVER_RUN_SOLVE=true` only when `TARGET_URL` is a lawful, authorized test page and you intend to make a paid solving request.

## Key integration code

```python
from capsolver_agent import create_executor

executor = create_executor()
detection = await executor.execute("detect_captchas", {"page_url": target_url})
result = await executor.execute("solve_on_page", {
    "page_url": target_url,
    "autofill": True,
})
```

See [`examples/quickstart.py`](examples/quickstart.py) for the guarded flow.

## Project layout

```text
examples/quickstart.py   Browser schema, detection, and opt-in solving demo
requirements.txt         CapSolver browser extras plus Playwright
tests/test_demo.py        Offline validation
.github/workflows/ci.yml  Demo checks
```

## Documentation

- [CapSolver Agent tools](https://docs.capsolver.com/en/guide/ai/agent-tools/)
- [CapSolver Core SDK](https://docs.capsolver.com/en/guide/ai/core-sdk/)
- [CapSolver quick start](https://docs.capsolver.com/en/guide/ai/introduction-and-quick-start/)
- [Playwright Python documentation](https://playwright.dev/python/docs/intro)

## Responsible use

Use browser solving only for lawful, user-authorized workflows that respect target-site terms. Never commit secrets or private target data.

## Contributing, support, and license

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), and [SECURITY.md](SECURITY.md). Licensed under the [ISC License](LICENSE).

Playwright is a third-party project. This repository is maintained by CapSolver and is not affiliated with or endorsed by Microsoft.
