#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from auto_startup_ai.crew import AutoStartupAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(query:str):
    """
    Run the crew.
    """
    inputs = {
        'topic': query,
        'current_year': str(datetime.now().year)
    }

    try:
        AutoStartupAi().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ =='__main__':
    run()


## Topic
# Agriculture Harvesting Robots
# AI Factory Monitoring System
# AI agents for startup automation
# AI Startup Studio
# AI Healthcare Diagnostics
# AI Customer Support Agents
# Climate AI Analytics
# AI SaaS for Small Businesses