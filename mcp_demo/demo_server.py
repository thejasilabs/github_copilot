from fastmcp import FastMCP
from datetime import datetime

# Create MCP server instance
mcp = FastMCP("Demo Server")

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool()
def get_greeting(name: str) -> str:
    """Generate a greeting message for a given name."""
    return f"Hello, {name}! Welcome to the MCP demo server."

@mcp.tool()
def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()