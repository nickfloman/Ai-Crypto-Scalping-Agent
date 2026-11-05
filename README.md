# Ai Crypto Scalping Agent

**Short-enabled AI Crypto Scalping Agent** built on Freqtrade.

A modular scalping system for crypto futures with Long + Short support and advanced risk management.

---

## Strategies

| Strategy                      | Timeframe | Style          | Risk Management      |
|-------------------------------|-----------|----------------|----------------------|
| `Scalp_RSI_BB_Short`          | 5m        | Balanced       | Full protections     |
| `Scalp_RSI_BB_Short_1m`       | 1m        | Aggressive     | Full protections     |

---

## Advanced Risk Management Features

Both strategies now include:

### 1. Dynamic Position Sizing
- Sizes each trade so a stoploss hit loses a fixed % of your total balance (default 1% on 5m, 0.8% on 1m), at the strategy's fixed leverage (default 1x)
- Automatically calculates stake size based on stoploss distance
- Hard cap on stake amount (default $100 on 5m, $80 on 1m). The stake is the **lesser** of the risk-based size and the cap, so on small accounts the cap binds: with a $1,000 balance the real risk per trade is about 0.12% (5m) and 0.064% (1m). Raise or remove `max_stake_amount` if you want the full risk percentage.

### 2. Protections (built-in)
- **CooldownPeriod** → Per-pair pause after a trade closes (prevents overtrading)
- **StoplossGuard** → Pauses after consecutive losses
- **MaxDrawdown** → Stops trading if drawdown exceeds limit (8% on 5m / 6% on 1m)
- **LowProfitPairs** → Avoids repeatedly trading losing pairs (5m version)

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

## Quick Start

```bash
# Copy strategy
cp strategies/Scalp_RSI_BB_Short.py user_data/strategies/

# Backtest
freqtrade backtesting --strategy Scalp_RSI_BB_Short -i 5m

# Dry-run
freqtrade trade --strategy Scalp_RSI_BB_Short
```

---

## Roadmap

- [x] Base short-enabled scalping strategy (5m)
- [x] Volume + Trend filters
- [x] Basic risk management
- [x] Project structure + example config
- [x] Aggressive 1-minute version
- [x] Advanced risk management (position sizing + protections)
- [ ] FreqAI / Machine Learning integration
- [ ] Better documentation & hyperopt configs

---

## Disclaimer

This project is for educational and research purposes only. Cryptocurrency trading involves substantial risk of loss. Always start with dry-run / paper trading. Never risk money you cannot afford to lose.

---

**Ai Crypto Scalping Agent** – Built step by step.
