# Source http://gbeced.github.io/pyalgotrade/docs/v0.17/html/bitcoincharts_example.html
# Accessd 06/25/16 @ 1048Z

from pyalgotrade.bitcoincharts import barfeed
from pyalgotrade.tools import resample
from pyalgotrade import bar

import datetime


def main():
    barFeed = barfeed.CSVTradeFeed()
    barFeed.addBarsFromCSV("bitstampUSD.csv", fromDateTime=datetime.datetime(2014, 1, 1))
    resample.resample_to_csv(barFeed, bar.Frequency.MINUTE*30, "30min-bitstampUSD.csv")


if __name__ == "__main__":
    main()
