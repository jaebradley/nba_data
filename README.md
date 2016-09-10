# NBA Stats Client

[![Coverage Status](https://coveralls.io/repos/github/jaebradley/nba_data/badge.svg?branch=configure-coveralls)](https://coveralls.io/github/jaebradley/nba_data?branch=configure-coveralls)
[![Build Status](https://travis-ci.org/jaebradley/nba_data.svg?branch=master)](https://travis-ci.org/jaebradley/nba_data)

# Introduction
Getting (free) NBA statistics, even the most basic, can be a real pain. Luckily, the NBA Stats API (http://stats.nba.com/stats/)
can provide many of these statistics. This project, and more specifically, this client, serves as an abstraction on top
of the NBA Stats API.

# Challenges
Unfortunately, the NBA Stats API makes no guarantees about uptime, breaking changes, and does not have much (i.e. any)
documentation around it, so identifying all the available endpoints and their implementation is non-trivial.

Thus, this client similarly makes no guarantees.

Additionally, this client is by no means complete, and will be in active development.

# Client API Details

## Installation
This project is available on [PyPi]().

To install
```
pip install nba_data
```

## API Methods

* `get_players_for_season(season, league=League.nba, current_season_only=CurrentSeasonOnly.yes)`

* `get_games_for_team(season, team, season_type=SeasonType.regular_season)`

## API Method Parameters

* season: A `Season` enum value
* league: A `League` enum value.
* current_season_only: A `CurrentSeasonOnly` enum value.


## Example Usage


