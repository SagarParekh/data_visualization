library(tm)
library(wordcloud)

#create some sample data
sample.tennis = c("Oh, I absolutely love Roger, even he lost to Djokovic in IndianWells Yesterday.",
                  "Tennis! It must be love!", 
                  "USOpen tickets cost about 100 per ticket.",
                  "I love tennis I can  not lie! ")

corp <- Corpus(VectorSource(sample.tennis))
dtm <- DocumentTermMatrix(corp)
inspect(dtm)
wordcloud(corp,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 

#plot word relations
library(igraph)
tdm_r <- TermDocumentMatrix(corp)
tdm_r
tdm = as.matrix(tdm_r)
tdm
termMatrix <- tdm %*% t(tdm)
g <- graph.adjacency(termMatrix, weighted=T, mode = "undirected")
plot(g)

#Text processing
corp <- VCorpus(VectorSource(sample.tennis))
wordcloud(corp,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 
corp <- tm_map(corp, removePunctuation)   
wordcloud(corp,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 
corp <- tm_map(corp, removeNumbers)   
wordcloud(corp,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 
corp <- tm_map(corp, removeWords, stopwords("english"))   
wordcloud(corp,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 
corp <- tm_map(corp, stripWhitespace)   
wordcloud(corp,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 
library(SnowballC)  
corp <- tm_map(corp, stemDocument) 
wordcloud(corp,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 
corp <- tm_map(corp, content_transformer(tolower))
wordcloud(corp,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 
#corp <- tm_map(corp, PlainTextDocument)  #avoid tm 0.6 issue 

#remove your OWN stopwords
myStopwords <- c("can") 
myCorpus <- tm_map(corp, removeWords, myStopwords)
wordcloud(myCorpus,  min.freq=25, color=brewer.pal(6, "Dark2")  ) 
wordcloud(myCorpus, colors=brewer.pal(5,"Set1"),random.order=FALSE, max.words=50)

# trump debate data wordcloud after text processing
text <- read.delim("D:/sem 6/DV/LABS/Lab_7/lab_text-1/lab_text/trump_debate.txt", sep = "\n")
text
corp_don <- VCorpus(VectorSource(text), readerControl = list(language = "en"))
summary(corp_don)
dtm_don <- DocumentTermMatrix(corp_don)
inspect(dtm_don)
wordcloud(corp_don,  min.freq=25, color=brewer.pal(6, "Dark2")) 
corp_don <- tm_map(corp_don, removePunctuation)
corp_don <- tm_map(corp_don, removeNumbers)   
corp_don <- tm_map(corp_don, removeWords, stopwords("english"))  
corp_don <- tm_map(corp_don, stripWhitespace)   
corp_don <- tm_map(corp_don, stemDocument) 
corp_don <- tm_map(corp_don, content_transformer(tolower))
dtm_don <- DocumentTermMatrix(corp_don)
inspect(dtm_don)
wordcloud(corp_don,  min.freq=25, color=brewer.pal(6, "Dark2")) 

# trump tdm
tdm_don <- TermDocumentMatrix(corp_don)
tdm_don
tdm = as.matrix(tdm_don)
tdm
termMatrix <- tdm %*% t(tdm)
termMatrix
g_don <- graph.adjacency(termMatrix,weighted=T, mode = "undirected")
plot(g_don)

# making topic models for trump 
library(lda)
doclines <- lexicalize(corp_don)
result <- lda.collapsed.gibbs.sampler(doclines$documents, 10, doclines$vocab, 
                                      250, 0.1, 0.1, compute.log.likelihood = TRUE)
cloud.data <- sort(result$topics[1, ], decreasing = TRUE)[1:50]
wordcloud(names(cloud.data), freq = cloud.data, scale = c(4, 0.1), min.freq = 1, 
          rot.per = 0, random.order = FALSE,colors=brewer.pal(5,"Set1"))

#clinton debate data wordcloud after text processing
text_hil <- read.delim("D:/sem 6/DV/LABS/Lab_7/lab_text-1/lab_text/clinton_debate.txt", sep = "\t")
text_hil
corp_hil <- VCorpus(VectorSource(text), readerControl = list(language = "en"))
summary(corp_hil)
dtm_hil <- DocumentTermMatrix(corp_hil)
inspect(dtm_hil)
wordcloud(corp_hil,  min.freq=25, color=brewer.pal(6, "Dark2")) 
corp_hil <- tm_map(corp_hil, removePunctuation)
corp_hil <- tm_map(corp_hil, removeNumbers)   
corp_hil <- tm_map(corp_hil, removeWords, stopwords("english"))  
corp_hil <- tm_map(corp_hil, stripWhitespace)   
corp_hil <- tm_map(corp_hil, stemDocument) 
corp_hil <- tm_map(corp_hil, content_transformer(tolower))
dtm_hil <- DocumentTermMatrix(corp_hil)
inspect(dtm_hil)
wordcloud(corp_hil,  min.freq=25, color=brewer.pal(6, "Dark2")) 
