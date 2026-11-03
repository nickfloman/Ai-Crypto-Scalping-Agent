# Ai Crypto Scalping Agent

**Short-enabled Freqtrade scalping strategy** powered by RSI + Bollinger Bands.

This project contains a ready-to-use Freqtrade strategy that can trade both **Long** and **Short** positions on crypto futures markets.

## Strategy Overview

**Name:** `Scalp_RSI_BB_Short`

### Logic
- **Long Entry**: RSI oversold + price at/near lower Bollinger Band + volume confirmation
- **Short Entry**: RSI overbought + price at/near upper Bollinger Band + volume confirmation
- **Exits**: Mean reversion back to middle band or RSI extremes
- Tight stoploss + trailing stop designed for scalping

### Best used on
- Timeframe: `5m` (or `1m` for more aggressive scalping)
- Markets: Crypto Futures (Binance Futures, Bybit, etc.)

## Quick Start with Freqtrade

1. Copy the strategy file into your Freqtrade `user_data/strategies/` folder:
   ```bash
   cp strategies/Scalp_RSI_BB_Short.py /path/to/freqtrade/user_data/strategies/
   ```

2. Make sure your `config.json` has shorting enabled:
   ```json
   "trading_mode": "futures",
   "margin_mode": "isolated",
   "can_short": true
   ```

3. Backtest:
   ```bash
   freqtrade backtesting --strategy Scalp_RSI_BB_Short -i 5m
   ```

4. Dry-run / Live:
   ```bash
   freqtrade trade --strategy Scalp_RSI_BB_Short
   ```

## Project Structure

```
Ai-Crypto-Scalping-Agent/
├── README.md
└── strategies/
    └── Scalp_RSI_BB_Short.py
```

## Disclaimer

This is an experimental strategy for educational purposes. Cryptocurrency trading involves significant risk of loss. Always start with dry-run / paper trading. Past performance is not indicative of future results.

---

Created as part of the **Ai Crypto Scalping Agent** project.
