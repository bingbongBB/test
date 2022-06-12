import twstock
import time
import random
sid = '2330'
data=twstock.Stock(sid)
#用fetch_from抓取資料，指定日期放入dataframe裡
print(data.fetch_from(2021,6))
def fetch_from(self,year:int,month:int):
    self.raw_data=[]
    self.data=[]
    today = datetime.datetime.today()
    for year,month in self._month_year_iter(month,year,today.month,today.year):
        self.raw_data.append(self.fetcher.fetch(year,month,self.sid))
        self.data.extend(self.raw_data[-1]['data'])
        time.sleep(random.randint(5,10))
    return self.data