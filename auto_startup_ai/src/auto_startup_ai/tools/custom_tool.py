import os
from crewai.tools import tool  
# Specialized Tool imports
from crewai_tools import FileWriterTool, TavilySearchTool
from langchain_experimental.utilities import PythonREPL

# =========================================================
# 1. Tools Initialization
# =========================================================
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

# Pre-built tools
tavily_tool = TavilySearchTool()
file_writer = FileWriterTool()

# Custom Wrapped Python Tool (Fixed the shadowing issue)
@tool("python_repl")
def python_repl_tool(command: str) -> str:
    """Execute python code in a REPL. Useful for calculating financial models 
    or processing data. Input should be valid python code."""
    return PythonREPL().run(command)
