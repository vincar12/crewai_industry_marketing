#!/usr/bin/env python
import sys
from finance_project.crew import FinanceProjectCrew
import datetime

def run():
    """
    Run the crew.
    """
    inputs = {
        'industry': input('Enter industry here: '),
        'current_date': datetime.datetime.now().strftime('%Y-%m-%d')
    }
    FinanceProjectCrew().crew().kickoff(inputs=inputs)
