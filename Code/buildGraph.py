import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


def drawHistogram(dict,title,xlabel,ylabel):
    #This function takes as input a Dictionary containing user and the corresponding network value and plots a histogram
    plt.bar(dict.keys(),dict.values(),color='g')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=90)
    plt.show()


def main():
    csvread=open('data.csv','r')
    Graphtype=nx.DiGraph()
    G=nx.parse_edgelist(csvread,delimiter=',',create_using=Graphtype,nodetype=str)
    pos = nx.spring_layout(G,scale=10,k=0.25)
    nx.draw(G,pos,with_labels=True,node_size=1200,node_shape='s',alpha=0.5,font_size=16)
    plt.show() #Shows the window containing the graph
    degreeCentrality=nx.algorithms.centrality.degree_centrality(G)
    betweeness=nx.algorithms.centrality.betweenness_centrality(G)
    closeness=nx.algorithms.centrality.closeness_centrality(G)
    df=pd.DataFrame([degreeCentrality,betweeness,closeness])
    df=df.rename(index={0:'DegreeCentrality',1:'Betweenness',2:'Closeness'}).transpose()
    drawHistogram(degreeCentrality,"Degree Centrality Histogram","Screen Name","Degree Centrality")
    drawHistogram(betweeness, "Betweeness Histogram", "Screen Name","Betweeness")
    drawHistogram(closeness, "Closeness Histogram", "Screen Name","Closeness")
    df.to_csv('network_measure.csv',header=True)
    print(df.to_string()) #Prints the numerical values of Network Measures of each user in the graph in the console

if __name__ == '__main__':
    main()
