import pandas as pd
import matplotlib.pyplot as plt

class PredictRainfall:
    def __init__(self):
        self.weather = pd.read_csv("siddipet.csv", index_col="Date", parse_dates=True, dayfirst=True)
        self.weather.index = pd.to_datetime(self.weather.index, format="%d-%m-%Y")

    def printWeather(self):
        print(self.weather)
    
    def rainPlot(self):
        self.weather["rainfall"].plot()
        plt.show()

    def fetchMonthAvg(self, reqmonthList):
        self.weather['Year'] = self.weather.index.year
        self.weather['Month'] = self.weather.index.month
        self.avg_rainfall = self.weather.groupby(['Year', 'Month'])['rainfall'].mean()
        for i in reqmonthList:
            monthAvgRainfall = self.avg_rainfall.loc[2022, int(i)]
            print("Average rainfall for", i, ":", monthAvgRainfall)

if __name__ == "__main__":
    obj = PredictRainfall()
    obj.rainPlot()
