from asyncio.format_helpers import _format_callback_source
from asyncio.windows_events import NULL
import yfinance as yahooFinance
import datetime

def adj_close(stock):
    amazon=yahooFinance.Ticker(stock)
    startDate= datetime.datetime(2017,1,1)
    endDate = datetime.datetime(2021,12,31)
    rawd=amazon.history(start=startDate, end=endDate)
    adj_close=rawd.iloc[:,[3]]
    adj_close.to_csv('data.csv')
    return adj_close

adj_close1=adj_close('AMZN')

#print(adj_close)


#break the data into 30 day intervals\
def breaker(intervals, data):
    breaker=[]
    for i in range(len(data)):
        if(i+1)%intervals == 0:
            breaker.append(data[i-intervals:i+1])
    return breaker

breaker(30, adj_close1)