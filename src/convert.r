# RUN COMMAND
# Rscript ./src/convert.r

setwd('~/Documentos/Projetos/db_sinan')

install.packages("readr")
install.packages("read.dbc")
install.packages("dplyr")

library(readr)
library(read.dbc)
library(dplyr)


#df = read.dbc('./data/HANSBR23.dbc')

#write_delim(df, './data/HANSBR23.csv', delim = ';')

files = list.files(pattern = '*.dbc')
tbl = lapply(files, read.dbc) |>
    bind_rows()

write_delim(tbl, './data/hans.csv', delim = ';')
