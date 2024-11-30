#!/usr/bin/env python
import sys
import warnings

from consumer_product_research.crew import ConsumerProductResearch

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        "product_category": "Smartphones",
        "target_brands": "Apple, Samsung, Google",
        "needs_features": "High-resolution photography, Long-lasting battery, Minimum 128GB storage, Budget range $500-$1000"
    }
    ConsumerProductResearch().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "product_category": "Smartphones",
        "target_brands": "Apple, Samsung, Google",
        "needs_features": "High-resolution photography, Long-lasting battery, Minimum 128GB storage, Budget range $500-$1000"
    }
    try:
        ConsumerProductResearch().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ConsumerProductResearch().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "product_category": "Smartphones",
        "target_brands": "Apple, Samsung, Google",
        "needs_features": "High-resolution photography, Long-lasting battery, Minimum 128GB storage, Budget range $500-$1000"
    }
    try:
        ConsumerProductResearch().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
