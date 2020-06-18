# install.packages("exams", repos = "https://r-forge.r-project.org")
library(exams)

directory <- "Moodle/week5"
exercises <- list.files(directory, full.names = TRUE, pattern = "Rmd$")

seed <- sample(1:1000, 1)
n <- 40

#set.seed(seed)
#exams2html(exercises, n = 3, dir = directory, mathjax = TRUE)


set.seed(seed)
exams2moodle(exercises, n = n, dir = directory, name = basename(directory))
