library(igraph)
ga.data <- read.csv('D:/sem 6/DV/LABS/Lab_6/network_vis_data/network_vis_data/ga_edgelist.csv', header=TRUE) 
g <- graph.data.frame(ga.data, directed=FALSE)

wc <- walktrap.community(g)
plot(wc, g)

clustered_g <- clusters(g)
plot(clustered)

modularity(wc)
membership(wc)

fc<-fastgreedy.community(g)
modularity(fc)
membership(fc)
plot(fc, g)

centralization.degree(g)
centralization.degree(g)$centralization

centralization.betweenness (g)

btw <- betweenness(g) 
btw.score <- round(btw) + 1
btw.colors <- heat.colors(max(btw.score))
V(g)$color <- btw.colors[ btw.score ] 
plot(g ,vertex.label=V(g)$label)

btw.colors <- rev(heat.colors(max(btw.score))) 

centralization.betweenness (g)
