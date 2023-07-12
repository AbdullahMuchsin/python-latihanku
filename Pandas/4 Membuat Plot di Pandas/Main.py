import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('dataair.csv', index_col=0, parse_dates=True)
plt.figure("Data 1")
plt.plot(data)
plt.figure("Data 2")
plt.plot(data["station_london"])
plt.figure("station_antwerp vs station_paris")
plt.scatter(x=data["station_antwerp"],y=data["station_paris"], alpha=0.5)
plt.show()