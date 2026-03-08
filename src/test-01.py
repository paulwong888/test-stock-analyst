import akshare as ak
import pandas as pd

def test_stock_zh_a_daily():
    df = ak.stock_zh_a_daily(symbol="sh600000")
    assert not df.empty
    print(df.head())

def test_stock_zh_a_daily_adjust():
    df = ak.stock_zh_a_hist_tx(
            symbol="sz000001",
            # period="daily",
            start_date="20260301",
            end_date="20260308",
            adjust="qfq"
        )
    assert not df.empty
    # df.set_index("date", inplace=True)
    # df.sort_index(ascending=False, inplace=True)
    df["date"] = pd.to_datetime(df["date"])
    print(df)
    print(df.dtypes)

def test_stock_zh_a_spot_em():
    df = ak.stock_sz_a_spot_em()
    assert not df.empty
    print(df.head())
    

if __name__ == "__main__":
    # test_stock_zh_a_daily()
    # test_stock_zh_a_daily_adjust()
    test_stock_zh_a_spot_em()