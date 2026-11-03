# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401
# isort: skip_file

import numpy as np
import pandas as pd
from pandas import DataFrame
from datetime import datetime
from typing import Optional

from freqtrade.strategy import (
    IStrategy,
    Trade,
    Order,
    DecimalParameter,
    IntParameter,
    BooleanParameter,
)

import talib.abstract as ta
from technical import qtpylib


class Scalp_RSI_BB_Short(IStrategy):
    """
    AI Crypto Scalping Agent
    Short-enabled Scalping Strategy using RSI + Bollinger Bands (Mean Reversion)
    Supports both Long and Short positions.
    Best used on 5m or 1m timeframe.
    """

    INTERFACE_VERSION = 3

    # Timeframe
    timeframe = "5m"                # Change to "1m" for more aggressive scalping

    # Enable shorting
    can_short = True

    # Fast ROI for scalping
    minimal_roi = {
        "0": 0.012,     # 1.2%
        "8": 0.008,     # 0.8%
        "16": 0.004,    # 0.4%
        "30": 0         # Force exit
    }

    # Tight stoploss
    stoploss = -0.012               # 1.2%

    # Trailing stop
    trailing_stop = True
    trailing_stop_positive = 0.004
    trailing_stop_positive_offset = 0.008
    trailing_only_offset_is_reached = True

    process_only_new_candles = True
    startup_candle_count = 30

    # Order types
    order_types = {
        "entry": "limit",
        "exit": "limit",
        "stoploss": "market",
        "stoploss_on_exchange": False
    }

    order_time_in_force = {
        "entry": "GTC",
        "exit": "GTC"
    }

    # Hyperopt parameters
    buy_rsi = IntParameter(22, 35, default=28, space="buy")
    sell_rsi = IntParameter(65, 80, default=72, space="sell")
    short_rsi = IntParameter(65, 80, default=72, space="sell")
    cover_rsi = IntParameter(22, 35, default=28, space="buy")

    bb_period = IntParameter(16, 24, default=20, space="buy")
    bb_std = DecimalParameter(1.8, 2.4, default=2.0, decimals=1, space="buy")

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # RSI
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=14)

        # Bollinger Bands
        bollinger = qtpylib.bollinger_bands(
            qtpylib.typical_price(dataframe),
            window=self.bb_period.value,
            stds=self.bb_std.value
        )
        dataframe["bb_lower"] = bollinger["lower"]
        dataframe["bb_middle"] = bollinger["mid"]
        dataframe["bb_upper"] = bollinger["upper"]

        # Volume
        dataframe["volume_mean"] = dataframe["volume"].rolling(window=20).mean()

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # === LONG Entry ===
        dataframe.loc[
            (
                (dataframe["rsi"] < self.buy_rsi.value) &
                (dataframe["close"] <= dataframe["bb_lower"]) &
                (dataframe["volume"] > dataframe["volume_mean"] * 0.7) &
                (dataframe["volume"] > 0)
            ),
            "enter_long"
        ] = 1

        # === SHORT Entry ===
        dataframe.loc[
            (
                (dataframe["rsi"] > self.short_rsi.value) &
                (dataframe["close"] >= dataframe["bb_upper"]) &
                (dataframe["volume"] > dataframe["volume_mean"] * 0.7) &
                (dataframe["volume"] > 0)
            ),
            "enter_short"
        ] = 1

        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # === LONG Exit ===
        dataframe.loc[
            (
                (dataframe["rsi"] > self.sell_rsi.value) |
                (dataframe["close"] >= dataframe["bb_middle"])
            ),
            "exit_long"
        ] = 1

        # === SHORT Exit (cover) ===
        dataframe.loc[
            (
                (dataframe["rsi"] < self.cover_rsi.value) |
                (dataframe["close"] <= dataframe["bb_middle"])
            ),
            "exit_short"
        ] = 1

        return dataframe
