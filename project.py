import pandas as pd 
import csv 
import statistics 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv("StudentsPerformance.csv")
Rs_list = df["readingScore"].tolist()
Rs_mean = statistics.mean(Rs_list)
Rs_median = statistics.median(Rs_list)
Rs_mode = statistics.mode(Rs_list)
Rs_std = statistics.stdev(Rs_list)

print("The mean is {} , median is {} , mode is {} , Standard Deviation is {}".format(Rs_mean,Rs_median,Rs_mode,Rs_std))

Score_std1_start,Score_std1_end = Rs_mean - Rs_std,Rs_mean+Rs_std
Score_std2_start,Score_std2_end = Rs_mean - (2 * Rs_std),Rs_mean+(2*Rs_std)
Score_std3_start,Score_std3_end = Rs_mean - (3 * Rs_std),Rs_mean+(3*Rs_std)

Score_list_within_std1 = [result for result in Rs_list if result > Score_std1_start and result < Score_std1_end] 
Score_list_within_std2 = [result for result in Rs_list if result > Score_std2_start and result < Score_std2_end]
Score_list_within_std3 = [result for result in Rs_list if result > Score_std3_start and result < Score_std3_end]

print("{}% of data for Score within Standard Deviation 1".format (len(Score_list_within_std1) * 100 / len (Rs_list)))
print("{}% of data for Score within Standard Deviation 2".format (len(Score_list_within_std2) * 100 / len (Rs_list)))
print("{}% of data for Score within Standard Deviation 3".format (len(Score_list_within_std3) * 100 / len (Rs_list)))


fig = ff.create_distplot([Rs_list], ["readingScores"], show_hist=False)
fig.add_trace(go.Scatter(x=[Score_std1_start,Score_std1_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))