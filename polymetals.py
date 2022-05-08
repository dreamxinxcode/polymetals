#!/usr/bin/env python

from yahoo_fin import stock_info as si
import argparse

class PolyMetals():
    
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-usd", '--usd', help='price in US dollars.', action="store_true")
        parser.add_argument("-cad", '--cad', help='price in Canadian dollars.', action="store_true")
        parser.add_argument("-g", '--gold', help='price per ounce of gold.', action="store_true")
        parser.add_argument("-s", '--silver', help='price per ounce of silver.', action="store_true")
        parser.add_argument("-pl", '--platinum', help='price per ounce of platinum.', action="store_true")
        parser.add_argument("-pa", '--palladium', help='price per ounce of palladium.', action="store_true")
        parser.add_argument("-c", '--copper', help='price per ounce of copper.', action="store_true")
        self.args = parser.parse_args()
        self.round_to = 2
        self.result = '| '
        self.metals = {
            'GC=F': 'Gold',
            'SI=F': 'Silver', 
            'PL=F': 'Platinum', 
            'PA=F': 'Palladium', 
            'HG=F': 'Copper'
        }

    def get_price(self, symbol):
        try:
            data = str(round(si.get_live_price(symbol), self.round_to))
            self.result += f'{self.metals[symbol]} - ${data} | '
        except:
            self.result += f'{self.metals[symbol]} - $0.00 | '

    def get_prices(self):
        if self.args.gold:
            self.get_price('GC=F')
        if self.args.silver:
            self.get_price('SI=F')   
        if self.args.platinum:
            self.get_price('PL=F')
        if self.args.palladium:
            self.get_price('PA=F')
        if self.args.copper:
            self.get_price('HG=F')    
        print(self.result)

polymetals = PolyMetals()
polymetals.get_prices()