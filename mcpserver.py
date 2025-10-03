from fastmcp import FastMCP
from weatherMCP import app as server

# Create an MCP server from your FastAPI app
mcp = FastMCP.from_fastapi(app=server)

if __name__ == "__main__":
  mcp.run()