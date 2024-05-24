# RUN COMMAND
# Rscript ./src/convert.r

setwd('~/Documentos/Projetos/db_sinan')

install.packages("readr")
install.packages("read.dbc")
install.packages("dplyr")

library(readr)
library(read.dbc)
library(dplyr)


files = list.files(pattern = '*.dbc')
tbl = lapply(files, read.dbc) |>
    bind_rows()

write_delim(tbl, './data/hans.csv', delim = ';')
