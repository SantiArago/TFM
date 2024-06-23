# DATOS A COMPLETAR: son datos que saco de SQL 

user="root"
host="127.0.0.1"
pass="root"
bbdd="futbol"
port=8889



install.packages('rjson')
install.packages('data.table')
install.packages('reshape')
install.packages('purrr')
install.packages('mice')
install.packages('anytime')

library(rjson)
library(data.table)
library(dplyr)
library(reshape)
library(purrr)
library(DBI)
library(RMySQL)
library(stringi)
library(stringr)
library(readxl)
library(mice) #necesaria para Power BI
library(httr) #peticion (GET) a la API #transformar JSON a dataframe
library(vctrs) #unir dataframes por filas
library(lubridate) #transformar columna fecha (caracter) a yyyy-MM-dd (date)
library(tidyr) #expandir listas de dataframe
library(anytime) #transformar formato fecha a UNIX

"%!in%" <- function(x,y)!("%in%"(x,y))






con <- dbConnect(MySQL(),user=user,host=host,password = pass,db = bbdd,port = port)
encoding <- if(grepl(pattern = 'utf8|utf-8',x = Sys.getlocale(),ignore.case = T)) 'utf8' else 'latin1'
dbGetQuery(con,paste("SET names",encoding))
dbGetQuery(con,paste0("SET SESSION character_set_server=",encoding))
dbGetQuery(con,paste0("SET SESSION character_set_database=",encoding))
dbGetQuery(con,"SET GLOBAL local_infile = true;")
DBI::dbWriteTable(con,"premierLeague2324", premierLeagueClean23.24, overwrite = TRUE, append=FALSE, row.names = FALSE,temporary= FALSE)
dbDisconnect(con)

