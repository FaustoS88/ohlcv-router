"""Command-line interface for ohlcv-hub.

Usage examples:
    ohlcv fetch BTCUSDT
    ohlcv fetch AAPL 1d 30
    ohlcv fetch EURUSD 1h 50 --provider yfinance
    ohlcv fetch BTCUSDT 1d 10 --csv
"""

from __future__ import annotations

import asyncio

import click
from dotenv import load_dotenv

from ohlcv_hub.registry import fetch as _registry_fetch
from ohlcv_hub.registry import pick, teardown as _teardown

load_dotenv()  # load .env from cwd or any parent directory


@click.group()
def main() -> None:
    """ohlcv-hub — fetch OHLCV market data from the command line."""


@main.command()
@click.argument("symbol")
@click.argument("interval", default="1d")
@click.argument("limit", default=100, type=int)
@click.option(
    "--provider",
    "provider_name",
    default=None,
    help="Force a specific provider (binance, yfinance, tiingo, finnhub).",
)
@click.option(
    "--csv",
    "output_csv",
    is_flag=True,
    default=False,
    help="Output rows as CSV instead of a formatted table.",
)
def fetch(
    symbol: str,
    interval: str,
    limit: int,
    provider_name: str | None,
    output_csv: bool,
) -> None:
    """Fetch OHLCV candles for SYMBOL.

    SYMBOL   Ticker symbol — e.g. BTCUSDT, AAPL, EURUSD, WM.TO\n
    INTERVAL Bar size      — 1m 5m 15m 1h 4h 1d 1w  (default: 1d)\n
    LIMIT    Number of bars to return              (default: 100)
    """
    asyncio.run(_run(symbol.upper(), interval, limit, provider_name, output_csv))


async def _run(
    symbol: str,
    interval: str,
    limit: int,
    provider_name: str | None,
    output_csv: bool,
) -> None:
    try:
        if provider_name:
            chain = [p for p in pick(symbol) if p.name == provider_name]
            if not chain:
                available = [p.name for p in pick(symbol)]
                raise click.ClickException(
                    f"Provider '{provider_name}' not in chain for {symbol}. "
                    f"Available: {', '.join(available)}"
                )
            candles = await chain[0].fetch(symbol, interval, limit)
        else:
            candles = await _registry_fetch(symbol, interval, limit)

        if not candles:
            raise click.ClickException(f"No data returned for {symbol} {interval}.")

        if output_csv:
            click.echo("time,open,high,low,close,volume")
            for c in candles:
                click.echo(f"{c.time},{c.open},{c.high},{c.low},{c.close},{c.volume}")
        else:
            click.echo(
                f"\n{'time':>12}  {'open':>10}  {'high':>10}  "
                f"{'low':>10}  {'close':>10}  {'volume':>14}"
            )
            for c in candles:
                click.echo(
                    f"{c.time:>12}  {c.open:>10.4f}  {c.high:>10.4f}  "
                    f"{c.low:>10.4f}  {c.close:>10.4f}  {c.volume:>14.2f}"
                )
    finally:
        await _teardown()
