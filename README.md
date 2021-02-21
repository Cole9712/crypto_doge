# Crypto Doge <img src="./doge-deal-with-it.png" alt="doge" width="80"/>

A discord bot that allows users to interact and get real time cryptocurrency information with simple commands.

This is a project for StormHacks 2021 by Hao Wu & Ross Shen

## Features

-   Basic informations about the cryptocurrency, such as name, logo, current price, price change, etc.
-   Detailed description about the cryptocurrency
-   Visual representation of the recent market price chart
-   More coming soon...

## Installation

1. Please install [Discord](https://discord.com) first
2. Then use
   [this link](https://discord.com/api/oauth2/authorize?client_id=812810587167522826&permissions=257088&scope=bot)
   to invite crypto doge into your own channel
3. Done. EZ 😉

## Usage

**Use `-doge` prefix to any command with crypto doge**

-   Use Capitalized ticker symbol to access basic informations
    -   e.g. `-doge BTC`
-   React to the arrow emojis below the message to flip through different pages
    -   Use ➡️ to go to left page
        -   The visual representation of recent trend if from the home page
    -   Use ⬅️ to go to right page
        -   Full detailed description of the cryptocurrency if from the home page
-   More coming soon...

## Deployment Technology

[Google Cloud](https://cloud.google.com) with Compute Engine

## API Used

-   [Discord Developer Portal](https://discord.com/developers/applications)
-   [Matplotlib: Visualization with Python](https://matplotlib.org/stable/index.html)
-   [Nomics Cryptocurrency & Bitcoin API](https://nomics.com)

## Some Dependency Used

| Dependency | Version |
| ---------- | ------- |
| discord.py | 1.6.0   |
| numpy      | 1.20.1  |
| sigfig     | 1.1.8   |
| requests   | 2.25.1  |
