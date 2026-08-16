from pathlib import Path
from utils import load_file

 # Directory paths
PROMPTS_DIR = Path(__file__).parent / "prompts"

 # Load prompt templates from external files
def load_prompt(filename: str) -> str:
        """Load a prompt template from file."""
        return load_file(PROMPTS_DIR / filename)

 # Available prompt templates
PROMPT = load_prompt("react.md") # <-- Edit this to use different prompts

def generate_prompt(user_input: str) -> str:
    template = PROMPT
    return f"{template}\n\nUser Message:\n{user_input.strip()}"
