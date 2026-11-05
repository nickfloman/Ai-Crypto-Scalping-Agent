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

Both strategies include:

### 1. Dynamic Position Sizing
- Risks a fixed % of total balance per trade (default 1% on 5m, 0.8% on 1m)
- Stake is calculated from stoploss distance and leverage
- Hard cap on stake amount (default $100 on 5m, $80 on 1m)

### 2. Protections
- **CooldownPeriod** — per-pair pause after a trade closes
- **StoplossGuard** — pauses after consecutive losses
- **MaxDrawdown** — stops trading if drawdown exceeds limit (8% on 5m / 6% on 1m)
- **LowProfitPairs** — avoids repeatedly trading losing pairs (5m version)

---

## Project Structure

```
Ai-Crypto-Scalping-Agent/
├── README.md
├── LICENSE
├── config/
│   ├── config_futures_example.json   # Ready-to-use futures config
│   └── hyperopt_ranges.md            # Recommended hyperopt settings
└── strategies/
    ├── Scalp_RSI_BB_Short.py
    └── Scalp_RSI_BB_Short_1m.py
```

---

## Quick Start

```bash
# 1. Copy strategy
cp strategies/Scalp_RSI_BB_Short.py user_data/strategies/

# 2. Use the example futures config (VolumePairList enabled)
cp config/config_futures_example.json user_data/config.json

# 3. Download data
freqtrade download-data --exchange binance --timeframes 5m --days 60 -c user_data/config.json

# 4. Backtest
freqtrade backtesting --strategy Scalp_RSI_BB_Short -i 5m --timerange 20250901-

# 5. Dry-run
freqtrade trade --strategy Scalp_RSI_BB_Short
```

### Pair Selection
The example config uses **VolumePairList** (top 20 by quote volume) + AgeFilter + PriceFilter + SpreadFilter instead of a static list. This is better for scalping.

---

## Hyperopt

See `config/hyperopt_ranges.md` for recommended commands and parameter ranges.

Example:
```bash
freqtrade hyperopt --strategy Scalp_RSI_BB_Short --hyperopt-loss SharpeHyperOptLoss --spaces buy sell -i 5m -e 300
```

---

## Backtest Notes

Before going live (or even serious dry-run):

1. Run backtests with realistic fees (Binance futures taker ~0.04%).
2. Use a hold-out period you did **not** optimize on.
3. Compare 5m vs 1m versions under the same conditions.
4. Check max drawdown, profit factor, and average trade duration.

> No strategy results are published here yet. Always validate yourself.

---

## Roadmap

- [x] Base short-enabled scalping strategy (5m)
- [x] Volume + Trend filters
- [x] Basic risk management
- [x] Project structure + example config
- [x] Aggressive 1-minute version
- [x] Advanced risk management (position sizing + protections)
- [x] VolumePairList + better filters
- [x] Hyperopt ranges documentation
- [x] MIT License
- [ ] Published sample backtest results
- [ ] FreqAI / Machine Learning integration

---

## Disclaimer

This project is for educational and research purposes only. Cryptocurrency trading involves substantial risk of loss. Always start with dry-run / paper trading. Never risk money you cannot afford to lose.

---

**Ai Crypto Scalping Agent** – Built step by step.
