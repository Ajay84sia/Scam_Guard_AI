from typing import Dict, Any
from utils import get_logger, extract_json_from_text

logger = get_logger(__name__)

class OutputParser:
    """Parses LLM output into structured format."""
   
    def parse_llm_output(self, llm_output: str) -> Dict[str, Any]:
        logger.info(f"Parsing LLM output of length: {len(llm_output)}")
       
        # Try to extract JSON using utils function
        parsed_json = extract_json_from_text(llm_output)
       
        if parsed_json:
            logger.info("Successfully parsed LLM output to JSON.")
            return parsed_json
        else:
            logger.warning("No JSON found in LLM output.")
            # Return fallback result
            fallback_result = {
                "label": "Uncertain",
                "reasoning": "Failed to parse response: No JSON found",
                "intent": "Could not determine",
                "risk_factors": []
            }
            return fallback_result
