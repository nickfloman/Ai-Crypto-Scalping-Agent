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


class Scalp_RSI_BB_Short_1m(IStrategy):
    """
    AI Crypto Scalping Agent - Aggressive 1-Minute Version
    
    Optimized for 1m timeframe scalping.
    Faster indicators, tighter stops, and higher trade frequency.
    Supports both Long and Short.
    """

    INTERFACE_VERSION = 3

    # Aggressive timeframe
    timeframe = "1m"
    can_short = True

    # Very fast ROI for 1m scalping
    minimal_roi = {
        "0": 0.008,     # 0.8%
        "3": 0.005,     # 0.5% after 3 minutes
        "6": 0.003,     # 0.3% after 6 minutes
        "12": 0         # Force exit after 12 minutes
    }

    # Tighter stoploss for 1m
    stoploss = -0.008               # 0.8%

    # Faster trailing stop
    trailing_stop = True
    trailing_stop_positive = 0.003
    trailing_stop_positive_offset = 0.005
    trailing_only_offset_is_reached = True

    process_only_new_candles = True
    startup_candle_count = 40

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

    # Faster Hyperopt parameters for 1m
    buy_rsi = IntParameter(18, 32, default=25, space="buy")
    sell_rsi = IntParameter(68, 82, default=75, space="sell")
    short_rsi = IntParameter(68, 82, default=75, space="sell")
    cover_rsi = IntParameter(18, 32, default=25, space="buy")

    bb_period = IntParameter(12, 20, default=14, space="buy")
    bb_std = DecimalParameter(1.6, 2.2, default=1.9, decimals=1, space="buy")

    volume_factor = DecimalParameter(0.5, 1.1, default=0.7, decimals=2, space="buy")

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Faster RSI
        dataframe["rsi"] = ta.RSI(dataframe, timeperiod=10)

        # Faster Bollinger Bands
        bollinger = qtpylib.bollinger_bands(
            qtpylib.typical_price(dataframe),
            window=self.bb_period.value,
            stds=self.bb_std.value
        )
        dataframe["bb_lower"] = bollinger["lower"]
        dataframe["bb_middle"] = bollinger["mid"]
        dataframe["bb_upper"] = bollinger["upper"]

        # Faster trend filter
        dataframe["ema_fast"] = ta.EMA(dataframe, timeperiod=9)
        dataframe["ema_slow"] = ta.EMA(dataframe, timeperiod=21)

        # Volume
        dataframe["volume_mean"] = dataframe["volume"].rolling(window=15).mean()

        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # === LONG Entry (Aggressive) ===
        dataframe.loc[
            (
                (dataframe["rsi"] < self.buy_rsi.value) &
                (dataframe["close"] <= dataframe["bb_lower"]) &
                (dataframe["volume"] > dataframe["volume_mean"] * self.volume_factor.value) &
                (dataframe["ema_fast"] > dataframe["ema_slow"]) &
                (dataframe["volume"] > 0)
            ),
            "enter_long"
        ] = 1

        # === SHORT Entry (Aggressive) ===
        dataframe.loc[
            (
                (dataframe["rsi"] > self.short_rsi.value) &
                (dataframe["close"] >= dataframe["bb_upper"]) &
                (dataframe["volume"] > dataframe["volume_mean"] * self.volume_factor.value) &
                (dataframe["ema_fast"] < dataframe["ema_slow"]) &
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

        # === SHORT Exit ===
        dataframe.loc[
            (
                (dataframe["rsi"] < self.cover_rsi.value) |
                (dataframe["close"] <= dataframe["bb_middle"])
            ),
            "exit_short"
        ] = 1

        return dataframe
