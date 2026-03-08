from langchain_core.tools import tool
import akshare as ak

# @tool("stock_zh_a_daily", return_direct=True)
def stock_zh_a_daily(symbol: str) -> str:
    """获取A股日线数据
    Args:
        symbol: 股票代码，例如 "sh600000    """
    
    df = ak.stock_cy_a_spot_em()
    return df.head().to_string()

if __name__ == "__main__":
    print(stock_zh_a_daily("sh600000"))