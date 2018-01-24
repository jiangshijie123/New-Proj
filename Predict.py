import pandas as pd
import tushare as ts
"""
class Get_data (object):

    def __init__ (self, code):
        self.code = code
    
    def Print_data(self):

        #df= pd.read_csv()
        #df = ts.get_hist_data('600848')
        #print df
"""
ts.get_hist_data('600848', start='2018-01-05', end='2018-01-16')