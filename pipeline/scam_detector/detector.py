from typing import List, Dict, Any
from .builder import build_prompt
from .executor import LLMExecutor
from .parser import OutputParser
from utils import get_logger

logger = get_logger(__name__)

class ScamDetector:
    """Orchestrates the scam detection pipeline."""

    def __init__(self, strategy: str = "react") -> None:
        """Initializes the pipeline components."""
        self.executor = LLMExecutor()
        self.parser = OutputParser()
        self.strategy = strategy
        logger.info(f"Initialized ScamDetector with strategy: {self.strategy}")

    def detect(self, message: str) -> Dict[str, Any]:
        """Runs scam detection on a single message."""
        logger.info(f"Starting detection for message length: {len(message)}")
        try:
            # The 3-step pipeline
            prompt = build_prompt(message, self.strategy)
            raw_response = self.executor.execute(prompt)
            parsed_result = self.parser.parse_llm_output(raw_response)

            logger.info(f"Detection successful. Result: {parsed_result.get('label', 'Unknown')}")
            return parsed_result

        except Exception as e:
            logger.error(f"Detection pipeline failed: {e}")
            # Re-raise the exception to be handled by the caller (UI layer)
            raise

    def detect_batch(self, messages: List[str]) -> List[Dict[str, Any]]:
        """Runs scam detection on a list of messages."""
        total_messages = len(messages)
        logger.info(f"Starting batch detection for {total_messages} messages.")
       
        results: List[Dict[str, Any]] = []
       
        for i, message in enumerate(messages):
            try:
                result = self.detect(message)
                results.append(result)
            except Exception as e:
                logger.warning(f"Failed to process message {i+1}/{total_messages}: {e}")
                # Append a fallback error result for the failed message
                error_result = {
                    "label": "Uncertain",
                    "reasoning": f"Error processing message: {e}",
                    "intent": "Could not determine",
                    "risk_factors": ["processing_error"]
                }
                results.append(error_result)
       
        successful = sum(1 for r in results if r.get("label") != "Uncertain" or "processing_error" not in r.get("risk_factors", []))
        logger.info(f"Batch processing complete. {successful}/{total_messages} succeeded.")
        return results
