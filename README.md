
# MCP Demo Server

This repository demonstrates how to create and run a Model Context Protocol (MCP) server using Python. MCP is a protocol that enables seamless integration between AI assistants and external tools, allowing for enhanced functionality and capabilities.

This demo provides a simple example server implementation with basic mathematical operations and utility functions, serving as a foundation for building more complex MCP integrations.

## Getting Started

1. Clone this repository
2. Navigate to the language of your choice
3. Follow the instructions in the language-specific README

## MCP Demo Server Setup

This guide explains how to create and run a simple MCP server using the `fastmcp` Python package.

### Prerequisites

- Python 3.8 or newer
- pip (Python package manager)

### Setting up virtual ennvironment
1.
    ```bash
    python -m venv venv
    ```
2. Activate scripts 
    ```bash
    .\venv\Scripts\activate
    ```

### Installation
1. Install the `fastmcp` package:
   ```bash
   pip install fastmcp
   ```

2. Create a new directory for your demo server (optional):
   ```bash
   mkdir mcp_demo
   cd mcp_demo
   ```

### Creating the MCP Server

Create a file called `demo_server.py` with the following content:

```python
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
```

### Running the Server

Run the server with:
```bash
python demo_server.py
```

### Example Tool Usage

Once the server is running, you can call the following tools:

- `add_numbers(a, b)`: Returns the sum of two numbers.
- `get_current_time()`: Returns the current date and time as a string.
- `get_greeting(name)`: Returns a greeting message for the given name.
- `multiply(x, y)`: Returns the product of two numbers.


## Available MCP Commands and Example Usage

The following commands are available in your MCP demo server:

| Command           | Description                                 | Example Usage (Python shell)           |
|-------------------|---------------------------------------------|----------------------------------------|
| add_numbers       | Add two numbers together                    | add_numbers(2, 3)                      |
| get_current_time  | Get the current date and time               | get_current_time()                     |
| get_greeting      | Generate a greeting message for a name      | get_greeting("User")                   |
| multiply          | Multiply two numbers                        | multiply(4, 5)                         |

### Example Output

For example, calling `get_greeting("User")` will return:
```
Hello, User! Welcome to the MCP demo server.
```

---

## How to Add a New Command/Tool to Your MCP Server

To add a new command (tool) to your MCP server, follow these steps:

1. **Define a Python function** for your new command. For example:
    ```python
    def subtract(a: float, b: float) -> float:
         """Subtract two numbers."""
         return a - b
    ```

2. **Register the function as a tool** using the `@mcp.tool()` decorator:
    ```python
    @mcp.tool()
    def subtract(a: float, b: float) -> float:
         """Subtract two numbers."""
         return a - b
    ```

3. **Restart your MCP server** to make the new tool available:
    ```bash
    python demo_server.py
    ```

4. **Call your new tool** using the MCP client or API:
    - Example: `subtract(10, 3)` will return `7`.

You can add as many tools as you need by repeating these steps. Each tool should have a unique function name and a clear docstring describing its purpose.

For more information, see the [fastmcp documentation](https://pypi.org/project/fastmcp/).
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

