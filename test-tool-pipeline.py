"""
requirements: blueprints
"""

import os
import requests
from typing import Literal, List, Optional
from datetime import datetime


from blueprints.function_calling_blueprint import Pipeline as FunctionCallingBlueprint


class Pipeline(FunctionCallingBlueprint):
    class Valves(FunctionCallingBlueprint.Valves):
        # Add your custom parameters/configuration here e.g. API_KEY that you want user to configure etc.
        pass

    class Tools:
        def __init__(self, pipeline) -> None:
            self.pipeline = pipeline

        def calculator(self, equation: str) -> str:
            """
            Calculate the result of an equation.

            :param equation: The equation to calculate.
            """

            try:
                result = eval(equation)
                return f"{equation} = {result} GUARDA CHE BELLA ROBETAH EH"
            except Exception as e:
                print(e)
                return "Invalid equation"

    def __init__(self):
        super().__init__()
        self.name = "My Calculator Tool Pipeline"
        self.valves = self.Valves(
            **{
                **self.valves.model_dump(),
                "pipelines": ["*"],  # Connect to all pipelines
            },
        )
        self.tools = self.Tools(self)
