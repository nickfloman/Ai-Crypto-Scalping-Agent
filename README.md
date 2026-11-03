# Ai Crypto Scalping Agent

**Short-enabled AI Crypto Scalping Agent** built on Freqtrade.

A modular scalping system designed for crypto futures that supports both Long and Short positions.

---

## Strategies Included

| Strategy                      | Timeframe | Style              | Description                                      |
|-------------------------------|-----------|--------------------|--------------------------------------------------|
| `Scalp_RSI_BB_Short`          | 5m        | Balanced           | Main strategy with volume + trend filters        |
| `Scalp_RSI_BB_Short_1m`       | 1m        | Aggressive         | Faster version optimized for 1-minute scalping   |

---

## Project Structure

```
Ai-Crypto-Scalping-Agent/
├── README.md
├── config/
│   └── config_futures_example.json
└── strategies/
    ├── Scalp_RSI_BB_Short.py
    └── Scalp_RSI_BB_Short_1m.py
```

---

## Strategy Details

### 1. Scalp_RSI_BB_Short (5m - Recommended starting point)
- RSI + Bollinger Bands
- Volume filter + EMA trend filter
- Stoploss: 1.2% | Trailing stop enabled

### 2. Scalp_RSI_BB_Short_1m (Aggressive)
- Faster RSI (period 10) and Bollinger Bands
- Tighter stoploss (0.8%) and faster ROI
- Designed for higher trade frequency on 1m candles
- More sensitive entries

---

## Quick Start

1. Copy the strategy you want:
   ```bash
   cp strategies/Scalp_RSI_BB_Short.py /path/to/freqtrade/user_data/strategies/
   # or
   cp strategies/Scalp_RSI_BB_Short_1m.py /path/to/freqtrade/user_data/strategies/
   ```

2. Use the example futures config:
   ```bash
   cp config/config_futures_example.json /path/to/freqtrade/user_data/config.json
   ```

3. Backtest example (5m):
   ```bash
   freqtrade backtesting --strategy Scalp_RSI_BB_Short -i 5m
   ```

4. Backtest example (1m):
   ```bash
   freqtrade backtesting --strategy Scalp_RSI_BB_Short_1m -i 1m
   ```

---

## Roadmap

- [x] Base short-enabled scalping strategy (5m)
- [x] Volume + Trend filters
- [x] Basic risk management
- [x] Project structure + example config
- [x] Aggressive 1-minute version
- [ ] Advanced risk management (daily loss limit, position sizing)
- [ ] FreqAI / Machine Learning integration
- [ ] Better documentation & hyperopt configs

---

## Disclaimer

This project is for educational and research purposes only. Cryptocurrency trading involves substantial risk of loss. Always start with dry-run / paper trading. Never risk money you cannot afford to lose.

---

**Ai Crypto Scalping Agent** – Built step by step.
