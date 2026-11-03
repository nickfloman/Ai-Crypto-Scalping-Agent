# Ai Crypto Scalping Agent

**Short-enabled AI Crypto Scalping Agent** built on Freqtrade.

A modular scalping system designed for crypto futures that supports both Long and Short positions.

---

## Current Features

- Short-enabled RSI + Bollinger Bands scalping strategy
- Volume + trend filters for higher quality entries
- Tight risk management (stoploss + trailing stop)
- Hyperopt-ready parameters
- Clean project structure

---

## Project Structure

```
Ai-Crypto-Scalping-Agent/
├── README.md
├── config/
│   └── config_futures_example.json
└── strategies/
    └── Scalp_RSI_BB_Short.py
```

---

## Strategy: Scalp_RSI_BB_Short

### Logic
- **Long**: RSI oversold + price near lower Bollinger Band + volume confirmation + mild uptrend filter
- **Short**: RSI overbought + price near upper Bollinger Band + volume confirmation + mild downtrend filter
- **Exits**: Mean reversion to middle band or RSI extremes
- Trailing stop + tight hard stoploss

### Recommended Settings
- Timeframe: `5m` (or `1m` for aggressive mode)
- Trading mode: Futures
- Margin mode: Isolated
- Leverage: Start with 2x–3x

---

## Quick Start

1. Copy the strategy:
   ```bash
   cp strategies/Scalp_RSI_BB_Short.py /path/to/freqtrade/user_data/strategies/
   ```

2. Use the example config (or merge the important settings into your own):
   ```bash
   cp config/config_futures_example.json /path/to/freqtrade/user_data/config.json
   ```

3. Backtest:
   ```bash
   freqtrade backtesting --strategy Scalp_RSI_BB_Short -i 5m
   ```

4. Dry-run:
   ```bash
   freqtrade trade --strategy Scalp_RSI_BB_Short
   ```

---

## Roadmap (Building Together)

- [x] Base short-enabled scalping strategy
- [x] Volume + trend filters
- [x] Basic risk management
- [x] Project structure + example config
- [ ] Aggressive 1-minute version
- [ ] Advanced risk management (daily loss limit, position sizing)
- [ ] FreqAI / Machine Learning integration
- [ ] Better documentation & hyperopt configs

---

## Disclaimer

This project is for educational and research purposes only. Cryptocurrency trading involves substantial risk of loss. Always start with dry-run / paper trading. Never risk money you cannot afford to lose.

---

**Ai Crypto Scalping Agent** – Built step by step.
