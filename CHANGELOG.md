# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Added
- `KuCoinProvider` — public REST API for crypto OHLCV, no API key required; `BASE-QUOTE` symbol normalisation; reverse-chronological response handling; all standard intervals; up to 1500 bars per request
- Full pytest coverage for `KuCoinProvider` — 30 tests covering normalisation, routing, fetch, and error paths
- Full pytest coverage for `TiingoProvider` — 30 tests covering `supports()`, `fetch()` (daily/weekly, adj fields, limit, auth header), and `_download()` error paths
- Full pytest coverage for `FinnhubProvider` — 33 tests covering stock/forex routing, `_to_forex_symbol()`, `_parse()`, and all error cases

---

## [0.1.0] — 2026-03-14

### Added
- `KuCoinProvider` — public REST API, no key, `BASE-QUOTE` symbol normalisation, all intervals, 1500 bars
- `KrakenProvider` — public REST API for crypto OHLCV, no key required; BTC→XBT symbol mapping; all standard intervals
- `CoinGeckoProvider` — crypto OHLCV with no API key; 4h and 1d granularity via auto-detection
- GitHub Actions release workflow — publishes to PyPI on `v*` tag push

### Fixed
- Logging added to registry fallback chain — silent `None` returns now emit `debug`/`warning` diagnostics

---

## [0.0.5] — 2026-03-03

### Added
- CLI tool: `ohlcv fetch SYMBOL INTERVAL LIMIT [--provider] [--csv]` via click
- `examples/basic_fetch.py` and `examples/multi_provider.py`
- GitHub Actions CI — pytest + ruff on Python 3.11 and 3.12

### Fixed
- Session reuse in `BinanceProvider` — single `aiohttp.ClientSession` per instance
- Close session on CLI exit via `registry.teardown()`
- Move `click` to core dependencies (was optional, broke CLI install)

---

## [0.0.4] — 2026-02-25

### Added
- `FinnhubProvider` — US stock candles and forex quotes via OANDA format
- `TiingoProvider` — daily and weekly bars for stocks and ETFs; requires `TIINGO_API_KEY`
- Tiingo and Finnhub wired into `registry.pick()` routing chains

### Fixed
- `build-backend` value in `pyproject.toml` (`setuptools.build_meta`)
- Replace `respx` with `aioresponses` in dev dependencies

---

## [0.0.3] — 2026-02-23

### Added
- `YFinanceProvider` — stocks, forex, and crypto via yfinance
- `py.typed` marker for typed package consumers

---

## [0.0.2] — 2026-02-22

### Added
- `BinanceProvider` — crypto OHLCV via Binance klines endpoint
- `OHLCVProvider` abstract base class and `Candle` model
- Provider registry with asset-class-based routing

---

## [0.0.1] — 2026-02-22

### Added
- Initial project scaffold — `pyproject.toml`, package structure, README
