from pathlib import Path
import sys
from pipeline.scam_detector.detector import ScamDetector
from utils import get_logger

# Add project root to path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

logger = get_logger(__name__)

def main():
    """Test the scam detection system with dynamic message."""
    detector = ScamDetector()
   
    test_msg = str(input("Enter your Message: "))
   
    try:
        logger.info("Running scam detection")
        result = detector.detect(test_msg)
       
        print(f"Test Message: {test_msg}")
        print(f"Detection Result: {result}")
       
    except Exception as e:
        logger.error(f"Detection failed: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
