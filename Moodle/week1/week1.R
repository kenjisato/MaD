# install.packages("exams", repos = "https://r-forge.r-project.org")
library(exams)

directory <- "Moodle/week1"
exercises <- list.files(directory, full.names = TRUE, pattern = "Rmd$")

seed <- sample(1:1000, 1)

set.seed(seed)
exams2html(exercises, n = 3, dir = directory, mathjax = TRUE)


set.seed(seed)
exams2moodle(exercises, n = 3, dir = directory, name = basename(directory))
