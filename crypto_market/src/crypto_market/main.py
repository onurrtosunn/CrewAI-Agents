import sys
import warnings
import os
from crypto_market.crew import CryptoMarket

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

def run():
    """
    Run the crypto research crew.
    """
    os.makedirs('memory', exist_ok=True)

    # Friendly check for OpenAI if agent models require it
    if any("openai/" in v for v in [
        "openai/gpt-4o-mini",
        "openai/gpt-4o",
    ]):
        if not os.getenv('OPENAI_API_KEY'):
            print("Missing OPENAI_API_KEY. Agents use OpenAI models; set a valid key or switch models.")
            sys.exit(1)

    inputs = {
        'market_focus': 'DeFi protocols',
    }
    result = CryptoMarket().crew().kickoff(inputs=inputs)

    print("\n\n=== FINAL DECISION ===\n\n")
    print(result.raw)

if __name__ == "__main__":
    run()