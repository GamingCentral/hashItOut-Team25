import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

class PredictTempMax:
    def __init__(self):
        self.weather=pd.read_csv("siddipet.csv",index_col="Date",parse_dates=True,dayfirst=True)
        self.weather.index = pd.to_datetime(self.weather.index,format='mixed',dayfirst=True)
        self.weather["actual_tmmr"] = self.weather.shift(-1)["temp_max"]
        self.weather = self.weather.iloc[:-1,:].copy()
    
    def printWeather(self):
        print(self.weather)
    
    def allPlot(self):
        self.weather["rainfall"].plot()
        plt.show()
        self.weather[["temp_max", "temp_min"]].plot()
        plt.show()
    
    def trainTest(self):
        reg = Ridge(alpha=0.1)
        predictors = ["rainfall", "temp_min", "temp_max"]
        train = self.weather.loc[:"2022-12-31"]
        test = self.weather.loc["2023-01-01":]
        #print(train)
        #print(test)
        reg.fit(train[predictors], train["actual_tmmr"])
        self.predictions = reg.predict(test[predictors])
        print(mean_squared_error(test["actual_tmmr"], self.predictions))
        combined = pd.concat([test["actual_tmmr"], pd.Series(self.predictions, index=test.index)], axis=1)
        combined.columns = ["actual", "predictions"]
        combined.plot()
        plt.show()

    def fetchMonthMax(self,reqmonthList):
        self.weather['Year'] = self.weather.index.year
        self.weather['Month'] = self.weather.index.month
        self.avg_max_temp = self.weather.groupby(['Year', 'Month'])['temp_max'].mean()
        monthMax=[]
        for i in reqmonthList:
            monthMaxTemp = self.avg_max_temp.loc[2023, int(i)]
            monthMax.append(monthMaxTemp)
            #average_max_temp_2023 = self.avg_max_temp.loc[2023]
            print("Average Max Temperature for ",str(i),": ",monthMaxTemp)
        return monthMax

class PredictTempMin:
    def __init__(self):
        self.weather=pd.read_csv("siddipet.csv",index_col="Date",parse_dates=True,dayfirst=True)
        self.weather.index = pd.to_datetime(self.weather.index,format='mixed',dayfirst=True)
        self.weather["actual_tmmr"] = self.weather.shift(-1)["temp_min"]
        self.weather = self.weather.iloc[:-1,:].copy()

    def printWeather(self):
        print(self.weather)
    
    def allPlot(self):
        self.weather["rainfall"].plot()
        plt.show()
        self.weather[["temp_max", "temp_min"]].plot()
        plt.show()
    
    def trainTest(self):
        reg = Ridge(alpha=1e-6)
        predictors = ["rainfall", "temp_min", "temp_max"]
        train = self.weather.loc[:"2022-12-31"]
        test = self.weather.loc["2023-01-01":]
        #print(train)
        #print(test)
        reg.fit(train[predictors], train["actual_tmmr"])
        self.predictions = reg.predict(test[predictors])
        print(mean_squared_error(test["actual_tmmr"], self.predictions))
        combined = pd.concat([test["actual_tmmr"], pd.Series(self.predictions, index=test.index)], axis=1)
        combined.columns = ["actual", "predictions"]
        combined.plot()
        plt.show()

    def fetchMonthMin(self,reqmonthList):
        self.weather['Year'] = self.weather.index.year
        self.weather['Month'] = self.weather.index.month
        self.avg_max_temp = self.weather.groupby(['Year', 'Month'])['temp_min'].mean()
        monthmin=[]
        for i in reqmonthList:
            monthMaxTemp = self.avg_max_temp.loc[2023, int(i)]
            monthmin.append(monthMaxTemp)
            #average_max_temp_2023 = self.avg_max_temp.loc[2023]
            print("Average Min Temperature for ",str(i),": ",monthMaxTemp)
        return monthmin

class PredictRainfall:
    def __init__(self):
        self.weather=pd.read_csv("siddipet.csv",index_col="Date",parse_dates=True,dayfirst=True)
        self.weather.index = pd.to_datetime(self.weather.index,format='mixed')
        

    def printWeather(self):
        print(self.weather)
    
    def rainPlot(self):
        self.weather["rainfall"].plot()
        plt.show()

    def fetchMonthAvg(self,reqmonthList):
        self.weather['Year'] = self.weather.index.year
        self.weather['Month'] = self.weather.index.month
        self.avg_max_temp = self.weather.groupby(['Year', 'Month'])['rainfall'].mean()
        for i in reqmonthList:
            monthMaxTemp = self.avg_max_temp.loc[2022, int(i)]
            #average_max_temp_2023 = self.avg_max_temp.loc[2023]
            print("Average rainfall for ",str(i),": ",monthMaxTemp)

class UI:
    def __init__(self):
        self.N=int(input("Enter the Nitrogen: "))
        self.P=int(input("Enter the Phosphorous: "))
        self.K=int(input("Enter the Potassium: "))
        self.startMonth=int(input("Enter the start month index(1-9): "))
        self.endMonth=int(input("Enter the end month index(1-9): "))
    
    def giveNPK(self):
        self.listSoil=[self.N,self.P,self.K]
        return self.listSoil
    
    def giveAvgTemps(self):
        listIndex=[]
        for i in range(self.startMonth,self.endMonth+1):
            listIndex.append[i]
        obj=PredictTempMax()
        listMax=obj.fetchMonthMax(listIndex)
        obj=PredictTempMin()
        listMin=obj.fetchMonthMin(listIndex)
        listAvg=[]
        for i in range(0,len(listMax)):
            listAvg.append((listMax[i]+listMin[i])/2)
        return listAvg
        
        


if __name__=="__main__":
    obj=PredictTempMin()
    obj.fetchMonthMin([1,2,3])
    