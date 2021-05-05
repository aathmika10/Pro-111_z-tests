import csv
import pandas as pd
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
articles=df["reading_time"].to_list()

meanOfPopulation=statistics.mean(articles)
stdDev=statistics.stdev(articles)
print("mean of population: ",meanOfPopulation)
print("standard deviation of population: ",stdDev)

def randomMean(counter):
    articlesSet=[]
    for i in range (0,counter):
        randIndex=random.randint(0,len(articles)-1)
        value=articles[randIndex]
        articlesSet.append(value)
    mean=statistics.mean(articlesSet)
    return mean

def showFig(meanList):
    df=meanList
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="mean"))
    fig.show()

def setup():
    meanList=[]
    for i in range(0,100):
        set_of_means=randomMean(30)
        meanList.append(set_of_means)
    showFig(meanList)
    mean=statistics.mean(meanList)
    stdDev1=statistics.stdev(meanList)
    print("mean of sampling distribution: ",mean)
    print("standard deviation of sampling distribution: ",stdDev1)

setup()

firstStart,firstEnd=meanOfPopulation-stdDev,meanOfPopulation+stdDev
secondStart,secondEnd=meanOfPopulation-(2*stdDev),meanOfPopulation+(2*stdDev)
thirdStart,thirdEnd=meanOfPopulation-(3*stdDev),meanOfPopulation+(3*stdDev)

listOf1stStdDev=[result for result in articles if result >firstStart and result<firstEnd]
listOf2ndStdDev=[result for result in articles if result>secondStart and result<secondEnd]
listOf3rdStdDev=[result for result in articles if result >thirdStart and result<thirdEnd]

print("{}% of articles lies within 1 standard deviation".format(len(listOf1stStdDev)*100.0/len(articles)))
print("{}% of articles lies within 2 standard deviation".format(len(listOf2ndStdDev)*100.0/len(articles)))
print("{}% of articles lies within 3 standard deviation".format(len(listOf3rdStdDev)*100.0/len(articles)))

df =pd.read_csv("medium_data.csv")
articles=df["reading_time"].to_list()

meanOfSample=statistics.mean(articles)
stdDev=statistics.stdev(articles)
print("mean of the sample population: ",meanOfSample)
print("standard deviation of sample population: ",stdDev)

fig=ff.create_distplot([articles],[" reading time"],show_hist=False)
fig.add_trace(go.Scatter(x=[meanOfPopulation,meanOfPopulation],y=[0,0.17],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample,meanOfSample],y=[0,0.17],mode="lines",name="MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x=[firstEnd,firstEnd],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[secondEnd,secondEnd],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))

zScore=(meanOfSample-meanOfPopulation)/stdDev
print("z-score: ",zScore)