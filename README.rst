NBA Stats Client
================

|Coverage Status| |Build Status|

Introduction
============

Getting (free) NBA statistics, even the most basic, can be a real pain.
Luckily, the NBA Stats API (base uri: http://stats.nba.com/stats/) can
provide many of these statistics. This project, and more specifically,
this client, serves as an abstraction on top of the NBA Stats API.

Challenges
==========

Unfortunately, the NBA Stats API makes no guarantees about uptime,
breaking changes, and does not have much (i.e. any) documentation around
it, so identifying all the available endpoints and their implementation
is non-trivial.

Thus, due to these contraints this client is only as dependable and
consistent as the NBA Stats service.

Additionally, this client is by no means complete, and will be in active
development.

Client API Details
==================

Installation
------------

This project is available on `PyPi`_.

To install

::

    pip install nba_data

API Methods
-----------

-  ``get_players_for_season(season, league=League.nba, current_season_only=CurrentSeasonOnly.yes)``

-  ``get_games_for_team(season, team, season_type=SeasonType.regular_season)``

-  ``get_player_info(player_id)``

-  ``get_advanced_box_score(game_id)``

API Method Parameters
---------------------

-  ``season``: A ``Season`` enum value. Represents the specific season
   to query for.
-  ``league``: A ``League`` enum value. Generally speaking, will always
   want to use ``League.nba``.
-  ``current_season_only``: A ``CurrentSeasonOnly`` enum value. When
   ``yes``, disregards the ``sesaon`` parameter and returns all players
   across all seasons
-  ``season_type``: A ``SeasonType`` enum value that represents which
   section of a season to query (regular season, playoffs, etc.)
-  ``player_id``: The unique id that NBA Stats assigns to each player.
-  ``game_id``: The unique id that NBA Stats assigns to each game.

Example Usage
-------------

Get Players For Season
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from nba_data.client import Client
    from nba_data.data.season import Season
    from nba_data.data.current_season_only import CurrentSeasonOnly


    def get_players_for_2015_season():
        return Client.get_players_for_season(season=Season.season_2015)


    def get_players_for_every_season():
        return Client.get_players_for_season(season=Season.season_2015, current_season_only=CurrentSeasonOnly.no)

Get Games For Team
~~~~~~~~~~~~~~~~~~

\`\`\`python from nba\_data.client import Client from
nba\_data.data.season import Season from nba\_data.data.season\_type
import SeasonType from nba\_data.data.team import Team

def get\_regular\_season\_games\_for\_2015\_boston\_celtics(): return
Client.get\_games\_for\_team(season=Season.season\_2015,
team=Team.boston\_celtics)

def get\_playoff\_for\_2015\_bost

.. _PyPi: https://pypi.python.org/pypi/nba_data/0.6

.. |Coverage Status| image:: https://coveralls.io/repos/github/jaebradley/nba_data/badge.svg?branch=configure-coveralls
   :target: https://coveralls.io/github/jaebradley/nba_data?branch=configure-coveralls
.. |Build Status| image:: https://travis-ci.org/jaebradley/nba_data.svg?branch=master
   :target: https://travis-ci.org/jaebradley/nba_data