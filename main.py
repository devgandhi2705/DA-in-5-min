import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("housing.csv")
profile = ProfileReport(df)
profile.to_file(output_file="housing.html")
