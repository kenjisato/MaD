library(tidyverse)

FILE <- 'Raw Data/SNA/30s2n_jp.xlsx'
OUTFILE <- 'Lecture Notes/Data/30s2n_jp.csv'
GRAPHICS_DIR <- 'Graphics'


get_year <- function(sheet, year_cell = 'B4'){
  cell <- readxl::read_xlsx(FILE, sheet = sheet, range = year_cell, 
                            col_names = FALSE, .name_repair = 'minimal')[[1, 1]]
  year <- str_match(cell, '\\((.*)\\)')[[1, 2]]
  as.integer(year)
}

sheet_names <- readxl::excel_sheets(FILE)
nkinds <- 30
years <- integer(length(sheet_names))
mat <- matrix(0.0, nrow = length(sheet_names), ncol = nkinds)

for (i in seq_along(sheet_names)) {
  sheet_name <- sheet_names[[i]]
  sheet <- readxl::read_xlsx(FILE, col_names = FALSE, sheet = sheet_name,
                             skip = 7, .name_repair = "unique")
  years[[i]] <- get_year(sheet_name)
  mat[i, ] <- sheet$...4[seq_len(nkinds)]
}

mat <- mat / 1000
colnames(mat) <- sheet$...1[seq_len(nkinds)]

df <- as_tibble(mat) %>% 
  mutate(西暦 = years) %>% 
  select(西暦, everything()) %>% 
  select(-c(5:18))


write_excel_csv(df, OUTFILE)
