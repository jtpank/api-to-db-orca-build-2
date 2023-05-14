#!/usr/bin/env python3
import os
from application import create_app, db
#add routes
# 'https://api.the-odds-api.com/v4/sports/basketball_nba/odds-history';
# process.env.REACT_APP_ODDS_API_API_KEY;
# `${oddsAPI}?apiKey=${apiKey}&regions=us&markets=h2h,spreads&dateFormat=iso&oddsFormat=american&date=${dateStr}`;
# this is 20 requests
# 
# https://api.the-odds-api.com/v4/sports/basketball_nba/odds-history
# ?apiKey=f2c87d0ea0ee1e114c5e603c9693aa7b
# &regions=us
# &markets=h2h,spreads
# &bookmakers=draftkings,fanduel,bovada
# &dateFormat=iso
# &oddsFormat=american
# &date=2023-05-10T00:00:00Z

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0')





#every 30 seconds
# pull live odds data for todays date
# this gets stored in the corresponding sports database
# is 3 requests per 30 seconds

# 31 days per month
# 24*60*2 is requests per day base
# 3 for h2h, spreads, ou
# 267,840 = 31*24*60*2*3
# 267,840 requests per month live data per sport
