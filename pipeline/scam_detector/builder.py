from llm.prompts import generate_prompt

def build_prompt(message: str, strategy: str = "react") -> str:
        if strategy == "react":
            return generate_prompt(message)
        else:
            raise NotImplementedError(f"Strategy '{strategy}' is not supported yet.") 
