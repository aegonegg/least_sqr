from asyncio.format_helpers import _format_callback_source
from asyncio.windows_events import NULL
import yfinance as yahooFinance
import datetime

import numpy as np
from scipy.linalg import solve

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
adj_close2=adj_close1.iloc[1:,:]

#break the data into 30 day intervals\
def breaker(interval, data):
    breaker=[]
    for i in range(len(data)):
        if(i+1)% interval == 0:
            breaker.append(data[(i-interval+1):i+1])
    del breaker[len(breaker)-1] #remove the last interval
    return breaker


def topredict(interval, data):
    topredict=[]
    for i in range(len(data)):
        if(i+1)% interval == 0:
            topredict.append(data[i-interval+1:i-interval+2])
    del topredict[0] #remove the 1st entry
    return topredict

b1= breaker(5, adj_close1) #start at entry 0
Y1= breaker(5, adj_close2) #start at entry 1
tpredict = topredict(5, adj_close2)
#print(b1[0], Y1[0])
#print(tpredict[0])


Y=Y1[0].to_numpy()
b=b1[0].to_numpy()
print(Y)
print(b)
X=solve(b, Y)
print(X)