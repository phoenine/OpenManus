import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP()


#! 增加@mcp.tool()注解, 用于mcp的客户端自动发现mcp server提供的能力。
@mcp.tool()
def get_desktop_files():
    """获取桌面上的文件列表"""
    return os.listdir(os.path.expanduser("~/Desktop"))


if __name__ == "__main__":
    mcp.run(transport="stdio")
