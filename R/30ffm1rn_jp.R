library(tidyverse)

FILE <- 'Raw Data/SNA/30ffm1rn_jp.xlsx'
OUTFILE <- 'Raw Data/SNA/30ffm1rn_jp.csv'

xls <- readxl::read_excel(FILE, skip = 6, 
                          col_names = FALSE, n_max = 42, .name_repair = 'universal')

years <- as.integer(xls[1, 2:ncol(xls)])
name <- xls[2:nrow(xls), 1] %>% pull()

frame <- xls[2:nrow(xls), 2:ncol(xls)] %>% 
  as.matrix() %>% 
  t() %>% 
  as_tibble(column_names = name)


df <- frame %>% 
  mutate(year = years,
         C = V1, 
         I = V17 + V25,
         G = V11 + V20 + V30,
         EX = V34,
         IM = -V37) %>% 
  select(year, C, I, G, EX, IM)


write_csv(df, 'Assignments/Data/week04.csv')
