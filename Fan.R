library(NLP)
library(tm)
library(descr)
library(qdap)
library("plyr")
library("ggplot2")
library("wordcloud")
library("RColorBrewer")
library("tm")

office365negative <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/office365negative.csv")
office365positive <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/office365positive.csv")

surfacenegative <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/surfacenegative.csv")
surfacepositive <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/surfacepositive.csv")

windowspositive<- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/windowspositive.csv")
windowsnegative <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/windowsnegative.csv")

summary(office365positive$body.username)
summary(office365negative)

#office Positive Talkers
office365positiveUsers <- office365positive$body.username
#summary(office365positiveUsers)
#freq(office365positiveUsers)

users.df <- data.frame(V1 = office365positiveUsers)
users.corpus <- Corpus(DataframeSource(users.df))
users.corpus <- tm_map(users.corpus, removePunctuation)
users.corpus <- tm_map(users.corpus, removeNumbers)
users.corpus <- tm_map(users.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                             "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                             "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                             "fuck", "fucking", "not", "but", "with", "has"))
users.tdm <- TermDocumentMatrix(users.corpus)
matrix.users.tdm <- as.matrix(users.tdm)
summary(matrix.users.tdm)

#Get frequencies of words
v.users <- sort(rowSums(matrix.users.tdm),decreasing=TRUE)
d.users <- data.frame(word = names(v.users),freq=v.users)
head(d.users, 20)

barplot(d.users[1:10,]$freq, las = 2, names.arg = d.users[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Office365 Positive Users")

#Word Cloud
set.seed(1234)
wordcloud(words = d.users$word, freq = d.users$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

####Office365 Positive Posts 
office365positiveTalks <- office365positive$body.post
summary(office365positiveTalks)
freq(office365positiveTalks )

df <- data.frame(V1 = office365positiveTalks)

post.corpus <- Corpus(DataframeSource(df))
post.corpus <- tm_map(post.corpus, removePunctuation)
post.corpus <- tm_map(post.corpus, removeNumbers)
post.corpus <- tm_map(post.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                     "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                     "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                     "fuck", "fucking","not", "but", "with", "has", "one",
                                                   "via", "our", "out", "they", "who", "must", "when", "its", "name",
                                                   "office", "microsoft", "see"))
post.tdm <- TermDocumentMatrix(post.corpus)

matrix.post.tdm <- as.matrix(post.tdm)
summary(matrix.post.tdm)

#Get frequencies of words
v.post <- sort(rowSums(matrix.post.tdm),decreasing=TRUE)
d.post <- data.frame(word = names(v.post),freq=v.post)
head(d.post, 600)

barplot(d.post[1:10,]$freq, las = 2, names.arg = d.post[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Office365 Positive Users")

#Word Cloud
set.seed(1234)
wordcloud(words = d.post$word, freq = d.post$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

tdm <- TermDocumentMatrix(mycorpus)
freq(tdm$dimnames$Terms)

matrix.tdm <- as.matrix(tdm)
summary(matrix.tdm)

#Get frequencies of words
v <- sort(rowSums(matrix.tdm),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 20)

#Word Cloud
set.seed(1234)
wordcloud(words = d$word, freq = d$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
#Tems vs occurances
inspect(tdm)

#####################################
#office Negative Talkers
office365negativeUsers <- office365negative$body.username
summary(office365negativeUsers)
#freq(office365negativeUsers)

users.df <- data.frame(V1 = office365negativeUsers)
users.corpus <- Corpus(DataframeSource(users.df))
users.corpus <- tm_map(users.corpus, removePunctuation)
users.corpus <- tm_map(users.corpus, removeNumbers)
users.corpus <- tm_map(users.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                     "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                     "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                     "fuck", "fucking"))
users.tdm <- TermDocumentMatrix(users.corpus)

matrix.users.tdm <- as.matrix(users.tdm)
summary(matrix.users.tdm)

#Get frequencies of words
v.users <- sort(rowSums(matrix.users.tdm),decreasing=TRUE)
d.users <- data.frame(word = names(v.users),freq=v.users)
head(d.users, 20)

#Word Cloud
set.seed(1234)
wordcloud(words = d.users$word, freq = d.users$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

####Office365 Negative Posts 
office365negativeTalks <- office365negative$body.post
summary(office365negativeTalks)
#freq(office365negativeTalks )

df <- data.frame(V1 = office365negativeTalks)

post.corpus <- Corpus(DataframeSource(df))
post.corpus <- tm_map(post.corpus, removePunctuation)
post.corpus <- tm_map(post.corpus, removeNumbers)
post.corpus <- tm_map(post.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                   "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                   "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                   "fuck", "fucking","not", "but", "with", "has", "one",
                                                   "via", "our", "out", "they", "who", "must", "when", "its", "name",
                                                   "office", "microsoft", "see", "was", "because", "got",
                                                   "didnt", "back", "her", "why", "can", "the"))
post.tdm <- TermDocumentMatrix(post.corpus)

matrix.post.tdm <- as.matrix(post.tdm)
summary(matrix.post.tdm)

#Get frequencies of words
v.post <- sort(rowSums(matrix.post.tdm),decreasing=TRUE)
d.post <- data.frame(word = names(v.post),freq=v.post)
head(d.post, 50)

barplot(d.post[1:10,]$freq, las = 2, names.arg = d.post[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Office365 Positive Users")

#Word Cloud
set.seed(1234)
wordcloud(words = d.post$word, freq = d.post$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

#Tems vs occurances
inspect(tdm)

#####################################
#Surface Positive Talkers
surfacepositiveUsers <- surfacepositive$body.username
summary(surfacepositiveUsers)
#freq(surfacepositiveUsers)

users.df <- data.frame(V1 = surfacepositiveUsers )
users.corpus <- Corpus(DataframeSource(users.df))
users.corpus <- tm_map(users.corpus, removePunctuation)
users.corpus <- tm_map(users.corpus, removeNumbers)
users.corpus <- tm_map(users.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                     "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                     "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                     "fuck", "fucking"))
users.tdm <- TermDocumentMatrix(users.corpus)

matrix.users.tdm <- as.matrix(users.tdm)
summary(matrix.users.tdm)

#Get frequencies of words
v.users <- sort(rowSums(matrix.users.tdm),decreasing=TRUE)
d.users <- data.frame(word = names(v.users),freq=v.users)
head(d.users, 20)

#Word Cloud
set.seed(1234)
wordcloud(words = d.users$word, freq = d.users$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

office365negativeTalks <- office365negative$body.post
summary(office365negativeTalks)
freq(office365negativeTalks )

df <- data.frame(V1 = office365negativeTalks)
mycorpus <- Corpus(DataframeSource(df))
tdm <- TermDocumentMatrix(mycorpus)

#Terms vs occurances
inspect(tdm)

#####################################
#Surface Negative Talkers
surfacenegativeUsers <- surfacenegative$body.username
summary(surfacenegativeUsers)
#freq(surfacenegativeUsers)

users.df <- data.frame(V1 = surfacenegativeUsers )
users.corpus <- Corpus(DataframeSource(users.df))
users.corpus <- tm_map(users.corpus, removePunctuation)
users.corpus <- tm_map(users.corpus, removeNumbers)
users.corpus <- tm_map(users.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                     "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                     "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                     "fuck", "fucking"))
users.tdm <- TermDocumentMatrix(users.corpus)

matrix.users.tdm <- as.matrix(users.tdm)
summary(matrix.users.tdm)

#Get frequencies of words
v.users <- sort(rowSums(matrix.users.tdm),decreasing=TRUE)
d.users <- data.frame(word = names(v.users),freq=v.users)
head(d.users, 20)

#Word Cloud
set.seed(1234)
wordcloud(words = d.users$word, freq = d.users$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

####Surface Positive Posts 
surfacepositiveTalks <- surfacepositive$body.post
summary(surfacepositiveTalks)
freq(surfacepositiveTalks )

df <- data.frame(V1 = surfacepositiveTalks)

post.corpus <- Corpus(DataframeSource(df))
post.corpus <- tm_map(post.corpus, removePunctuation)
post.corpus <- tm_map(post.corpus, removeNumbers)
post.corpus <- tm_map(post.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                   "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                   "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                   "fuck", "fucking","not", "but", "with", "has", "one",
                                                   "via", "our", "out", "they", "who", "must", "when", "its", "name",
                                                   "office", "microsoft", "see", "was", "because", "got",
                                                   "didnt", "back", "her", "why", "can", "the", "just"))
post.tdm <- TermDocumentMatrix(post.corpus)

matrix.post.tdm <- as.matrix(post.tdm)
summary(matrix.post.tdm)

#Get frequencies of words
v.post <- sort(rowSums(matrix.post.tdm),decreasing=TRUE)
d.post <- data.frame(word = names(v.post),freq=v.post)
head(d.post, 200)

barplot(d.post[1:10,]$freq, las = 2, names.arg = d.post[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Office365 Positive Users")

#Word Cloud
set.seed(1234)
wordcloud(words = d.post$word, freq = d.post$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
#Tems vs occurances
inspect(tdm)

####Surface Negative Posts 
surfacenegativeTalks <- surfacenegative$body.post
summary(surfacenegativeTalks)
freq(surfacenegativeTalks )

df <- data.frame(V1 = surfacenegativeTalks)
post.corpus <- Corpus(DataframeSource(df))
post.corpus <- tm_map(post.corpus, removePunctuation)
post.corpus <- tm_map(post.corpus, removeNumbers)
post.corpus <- tm_map(post.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                   "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                   "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                   "fuck", "fucking","not", "but", "with", "has", "one",
                                                   "via", "our", "out", "they", "who", "must", "when", "its", "name",
                                                   "office", "microsoft", "see", "was", "because", "got",
                                                   "didnt", "back", "her", "why", "can", "the"))
post.tdm <- TermDocumentMatrix(post.corpus)

matrix.post.tdm <- as.matrix(post.tdm)
summary(matrix.post.tdm)

#Get frequencies of words
v.post <- sort(rowSums(matrix.post.tdm),decreasing=TRUE)
d.post <- data.frame(word = names(v.post),freq=v.post)
head(d.post, 50)

barplot(d.post[1:10,]$freq, las = 2, names.arg = d.post[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Office365 Positive Users")

#Word Cloud
set.seed(1234)
wordcloud(words = d.post$word, freq = d.post$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
#Tems vs occurances
inspect(tdm)

#####################################
#Windows Positive Talkers
windowspositiveUsers <- windowspositive$body.username
summary(windowspositiveUsers)
#freq(windowspositiveUsers)

users.df <- data.frame(V1 = windowspositiveUsers)
users.corpus <- Corpus(DataframeSource(users.df))
users.corpus <- tm_map(users.corpus, removePunctuation)
users.corpus <- tm_map(users.corpus, removeNumbers)
users.corpus <- tm_map(users.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                     "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                     "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                     "fuck", "fucking"))
users.tdm <- TermDocumentMatrix(users.corpus)

matrix.users.tdm <- as.matrix(users.tdm)
summary(matrix.users.tdm)

#Get frequencies of words
v.users <- sort(rowSums(matrix.users.tdm),decreasing=TRUE)
d.users <- data.frame(word = names(v.users),freq=v.users)
head(d.users, 20)

#Word Cloud
set.seed(1234)
wordcloud(words = d.users$word, freq = d.users$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

####Windows Positive Posts 
windowspositiveTalks <- windowspositive$body.post
summary(windowspositiveTalks)
freq(windowspositiveTalks )

df <- data.frame(V1 = windowspositiveTalks)

post.corpus <- Corpus(DataframeSource(df))
post.corpus <- tm_map(post.corpus, removePunctuation)
post.corpus <- tm_map(post.corpus, removeNumbers)
post.corpus <- tm_map(post.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                   "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                   "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                   "fuck", "fucking","not", "but", "with", "has", "one",
                                                   "via", "our", "out", "they", "who", "must", "when", "its", "name",
                                                   "office", "microsoft", "see", "was", "because", "got",
                                                   "didnt", "back", "her", "why", "can", "the", "just", "for", "most",
                                                   "windows", "had", "microsoft"))
post.tdm <- TermDocumentMatrix(post.corpus)

matrix.post.tdm <- as.matrix(post.tdm)
summary(matrix.post.tdm)

#Get frequencies of words
v.post <- sort(rowSums(matrix.post.tdm),decreasing=TRUE)
d.post <- data.frame(word = names(v.post),freq=v.post)
head(d.post, 1000)

barplot(d.post[1:10,]$freq, las = 2, names.arg = d.post[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Office365 Positive Users")

#Word Cloud
set.seed(1234)
wordcloud(words = d.post$word, freq = d.post$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

mycorpus <- Corpus(DataframeSource(df))
tdm <- TermDocumentMatrix(mycorpus)

#Tems vs occurances
inspect(tdm)

#####################################
#Windows Negative Talkers
windowsnegativeUsers <- windowsnegative$body.username
summary(windowsnegativeUsers)
#freq(windowsnegativeUsers)

users.df <- data.frame(V1 = windowsnegativeUsers )
users.corpus <- Corpus(DataframeSource(users.df))
users.corpus <- tm_map(users.corpus, removePunctuation)
users.corpus <- tm_map(users.corpus, removeNumbers)
users.corpus <- tm_map(users.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                     "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                     "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                     "fuck", "fucking"))
users.tdm <- TermDocumentMatrix(users.corpus)

matrix.users.tdm <- as.matrix(users.tdm)
summary(matrix.users.tdm)

#Get frequencies of words
v.users <- sort(rowSums(matrix.users.tdm),decreasing=TRUE)
d.users <- data.frame(word = names(v.users),freq=v.users)
head(d.users, 20)

#Word Cloud
set.seed(1234)
wordcloud(words = d.users$word, freq = d.users$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

barplot(d.users[1:10,]$freq, las = 2, names.arg = d.users[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Windows Negative Users")

####Windows Negative Posts 
windowsnegativeTalks <- windowsnegative$body.post
summary(windowsnegativeTalks)
freq(windowsnegativeTalks )

df <- data.frame(V1 = windowsnegativeTalks)

post.corpus <- Corpus(DataframeSource(df))
post.corpus <- tm_map(post.corpus, removePunctuation)
post.corpus <- tm_map(post.corpus, removeNumbers)
post.corpus <- tm_map(post.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                   "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                   "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                   "fuck", "fucking","not", "but", "with", "has", "one",
                                                   "via", "our", "out", "they", "who", "must", "when", "its", "name",
                                                   "office", "microsoft", "see", "was", "because", "got",
                                                   "didnt", "back", "her", "why", "can", "the", "just", "for", "most",
                                                   "windows", "had", "microsoft"))
post.tdm <- TermDocumentMatrix(post.corpus)

matrix.post.tdm <- as.matrix(post.tdm)
summary(matrix.post.tdm)

#Get frequencies of words
v.post <- sort(rowSums(matrix.post.tdm),decreasing=TRUE)
d.post <- data.frame(word = names(v.post),freq=v.post)
head(d.post, 500)

barplot(d.post[1:10,]$freq, las = 2, names.arg = d.post[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Office365 Positive Users")

#Word Cloud
set.seed(1234)
wordcloud(words = d.post$word, freq = d.post$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

mycorpus <- Corpus(DataframeSource(df))
tdm <- TermDocumentMatrix(mycorpus)

#Tems vs occurances
inspect(tdm)

#####################################
office365positiveposts <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/office365positiveposts.csv")
df <- data.frame(V1 = office365positiveposts)
mycorpus <- Corpus(DataframeSource(df))

tdm <- TermDocumentMatrix(mycorpus)

findFreqTerms(tdm, 20, 94)
#Terms vs occurances
inspect(tdm)

#Comments Analysis
########################################################################################################

office365positiveposts <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/office365positiveComments.csv")
posts <- office365positiveposts$body.post
df <- data.frame(V1 = posts)

mycorpus <- Corpus(DataframeSource(df))
mycorpus <- tm_map(mycorpus, removePunctuation)
mycorpus <- tm_map(mycorpus, removeNumbers)
mycorpus <- tm_map(mycorpus , removeWords, c("also", "you", "would", "youll", "your", "youre", "https",
                                             "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                             "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office"))
tdm <- TermDocumentMatrix(mycorpus)

findFreqTerms(tdm, 500, 1000)
#Tems vs occurances
inspect(tdm)

########################################################################################################
office365positiveposts <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/office365negativeComments.csv")

posts <- office365positiveposts$body.post

df <- data.frame(V1 = posts)


mycorpus <- Corpus(DataframeSource(df))
mycorpus <- tm_map(mycorpus, removePunctuation)
mycorpus <- tm_map(mycorpus, removeNumbers)
mycorpus <- tm_map(mycorpus , removeWords, c("also", "you", "would", "youll", "your", "youre", "https",
                                             "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                             "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                             "fuck", "fucking"))

tdm <- TermDocumentMatrix(mycorpus)

findFreqTerms(tdm, 2, 1000)
#Tems vs occurances
inspect(tdm)


########################################################################################################

windowspositiveposts <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/WindowsPositiveComments.csv")

posts <- office365positiveposts$body.post


df <- data.frame(V1 = posts)


mycorpus <- Corpus(DataframeSource(df))


mycorpus <- tm_map(mycorpus, removePunctuation)
mycorpus <- tm_map(mycorpus, removeNumbers)


mycorpus <- tm_map(mycorpus , removeWords, c("also", "you", "would", "youll", "your", "youre", "https",
                                             "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                             "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                             "fuck", "fucking"))

tdm <- TermDocumentMatrix(mycorpus)

findFreqTerms(tdm, 2, 1000)
#Tems vs occurances
inspect(tdm)
################################################################################################################
windowspositiveposts <- read.csv("~/pythontut/Dashboard/MS Consumer Report/fan/hololens2.csv")

posts <- windowspositiveposts$Post
summary(posts)

df <- data.frame(V1 = posts)


mycorpus <- Corpus(DataframeSource(df))


mycorpus <- tm_map(mycorpus, removePunctuation)
mycorpus <- tm_map(mycorpus, removeNumbers)


mycorpus <- tm_map(mycorpus , removeWords, c("also", "you", "would", "youll", "your", "youre", "https",
                                             "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                             "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                             "fuck", "fucking", "and", "was", "didnt", "can", "why", "and"))

corpus <- Corpus(VectorSource(mycorpus))

tdm <- TermDocumentMatrix(corpus)

#tdm <- as.matrix(tdm)
colnames(tdm) 

freq(tdm$dimnames$Terms)

findFreqTerms(tdm, 10,80)
freq_terms(findFreqTerms(tdm, 10,80))
freq(findFreqTerms(tdm, 30,80))
freq_terms(findFreqTerms(tdm, 30,80))


#Terms vs occurances
inspect(tdm)

matrix.tdm <- as.matrix(tdm)
summary(matrix.tdm)

#Get frequencies of words
v <- sort(rowSums(matrix.tdm),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)
head(d, 20)

set.seed(1234)
wordcloud(words = d$word, freq = d$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))



##AZURE

azure<- read.csv("~/pythontut/Dashboard/MS Commercial Report/ms365.csv", comment.char="#")
View(azure)

azureTalks <- azure$Post
summary(azureTalks)


df <- data.frame(V1 = azureTalks)

post.corpus <- Corpus(DataframeSource(df))

post.corpus <- tm_map(post.corpus, removePunctuation)
post.corpus <- tm_map(post.corpus, removeNumbers)

post.corpus <- tm_map(post.corpus , removeWords, c("and","also", "you", "would", "youll", "your", "youre", "https",
                                                   "httpst","httpstc","httpstco", "come", "this", "the", "will", "are", "that", "with", "amp", "all", "from", "have",
                                                   "ampamp","please", "our","more", "for", "you", "wont", "within", "without", "with", "were", "which", "office", "any",
                                                   "fuck", "fucking","not", "but", "with", "has", "one",
                                                   "via", "our", "out", "they", "who", "must", "when", "its", "name",
                                                   "office", "microsoft", "see", "was", "because", "got",
                                                   "didnt", "back", "her", "why", "can", "the", "just", "for", "most",
                                                   "windows", "had", "microsoft"))
post.tdm <- TermDocumentMatrix(post.corpus)

matrix.post.tdm <- as.matrix(post.tdm)
summary(matrix.post.tdm)

#Get frequencies of words
v.post <- sort(rowSums(matrix.post.tdm),decreasing=TRUE)
d.post <- data.frame(word = names(v.post),freq=v.post)
head(d.post, 500)

barplot(d.post[1:10,]$freq, las = 2, names.arg = d.post[1:10,]$word,
        col ="lightblue", main ="Most frequent words",
        ylab = "Office365 Positive Users")

#Word Cloud
set.seed(1234)
wordcloud(words = d.post$word, freq = d.post$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))

