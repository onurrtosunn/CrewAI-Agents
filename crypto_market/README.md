# CryptoMarket Crew

A multi-agent crypto research assistant built on crewAI. Agents collaborate across news discovery, fundamentals/technical analysis, risk assessment, and final investment decision-making via a layered, configurable architecture.
 
## Installation
Prerequisites:
- Python >= 3.10, < 3.14
- [UV](https://docs.astral.sh/uv/) for dependency management

Install UV if needed:
```bash
pip install uv
```

Install project dependencies:
```bash
uv sync
```

## Quick Start
1) Create a `.env` file and add the required keys (see below).
2) Memory directories are created automatically on first run.
3) Start the crew:
```bash
uv run run_crew
```


## Configuration (.env)
Create a `.env` file at the project root. Example template:

```env
# LLM (OpenAI)
OPENAI_API_KEY=sk-...

# Search Tool (Serper)
SERPER_API_KEY=serper-...

# LLM model preferences (must align with agents.yaml)
LLM_MODEL_DEFAULT=openai/gpt-4o-mini
LLM_MODEL_MANAGER=openai/gpt-4o

# Embeddings / Memory
ENABLE_MEMORY=true
EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=text-embedding-3-small
MEMORY_PATH=./memory/
LTM_DB_PATH=./memory/long_term_memory_storage.db
```

Notes:
- `SERPER_API_KEY` is required because the project uses `SerperDevTool`.
- `agents.yaml` defaults to OpenAI models (`openai/gpt-4o-mini`, `openai/gpt-4o`). If you do not plan to use OpenAI, switch models to a supported provider and supply the corresponding credentials.
- Setting `ENABLE_MEMORY=false` disables short-term/entity memory. Long-term memory (SQLite) remains available.

## Architecture & Design Principles
The project is modular and follows SOLID principles:
- `src/crypto_market/config/settings.py`: Centralized application configuration (Single Responsibility). Loads `.env` and exposes settings.
- `src/crypto_market/memory_factory.py`: Factory that builds memory components (Open/Closed, Dependency Inversion). Provider/model changes do not require `crew.py` edits.
- `src/crypto_market/crew.py`: Wires agents, tasks, and memory. It does not know provider details—delegates to the factory.
- `src/crypto_market/config/agents.yaml`: Agent definitions and LLM models.
- `src/crypto_market/config/tasks.yaml`: Task pipeline and output locations.
- `src/crypto_market/main.py`: Entry point, key checks, and flow trigger.

## Agents & Tasks
- Agents (`agents.yaml`):
  - crypto_news_analyst: News/trend discovery (llm: `openai/gpt-4o-mini`)
  - defi_researcher: Technical/fundamental analysis (llm: `openai/gpt-4o-mini`)
  - risk_analyst: Regulatory/technical/market risk (llm: `openai/gpt-4o-mini`)
  - portfolio_manager: Final decision maker (llm: `openai/gpt-4o`)
- Tasks (`tasks.yaml`):
  - find_trending_cryptos → research_crypto_fundamentals → assess_crypto_risks → select_crypto_investment

## Outputs
Defined in `tasks.yaml` and written to disk:
- `output/trending_cryptos.json`
- `output/crypto_research.json`
- `output/risk_assessment.json`
- `output/investment_decision.md`

Output directories are created automatically when needed.

## Troubleshooting
- “Please provide an OpenAI API key” / “Incorrect API key”:
  - Ensure `OPENAI_API_KEY` is valid. If not using OpenAI, switch models in `agents.yaml` and/or set `ENABLE_MEMORY=false` (if embeddings also use OpenAI).
- Serper-related errors:
  - Verify `SERPER_API_KEY`.
- Pydantic deprecation warnings:
  - Originates from dependencies; does not block execution.
- Network / rate limits:
  - Retry with a short delay; consider switching model/provider if limits persist.

## Useful Commands
- Install dependencies:
```bash
uv sync
```
- Run the crew:
```bash
uv run run_crew
```
- Alternatively via crewAI CLI (depending on scripts):
```bash
crewai run
```