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
def breaker(interval, data):
    breaker=[]
    for i in range(len(data)):
        if(i+1)% interval == 0:
            breaker.append(data[(i-interval+1):i+1])
    return breaker


def topredict(interval, data):
    topredict=[]
    for i in range(len(data)):
        if(i+1)% interval == 0:
            topredict.append(data[i-interval+1:i-interval+2])
            #beware the second entry ([1]) is the first to be predicted
    return topredict

b=breaker(5, adj_close1)
t=topredict(5, adj_close1)
print(b[0])
print(t[0])