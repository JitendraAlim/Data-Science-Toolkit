###### SETTING PARAMETERS ######

setwd('~')

Sys.setenv(TZ = 'Asia/Calcutta')

options(java.parameters = '-Xmx48g',
        scipen = 999,
        warn = -1)
		
		
###### SHARED DRIVE PATH ######

JIT <- 'FOLDER PATH'


###### LIBRARIES ######

library(data.table)
library(dplyr)
library(tidyr)
library(lubridate)
library(stringr)
library(readxl)
library(writexl)


###### DATABASE CONNECTION ######

try(expr = {
  
  library(RODBC)
  
  BBB  <- odbcDriverConnect('driver={ODBC Driver 17 for SQL Server};server=10.80.44.62,21444;database=BBB;trusted_connection=yes')

  CRM  <- odbcDriverConnect('driver={ODBC Driver 17 for SQL Server};server=10.80.44.62,21444;database=CRM;trusted_connection=yes')
  
  BAAS <- odbcDriverConnect('driver={ODBC Driver 17 for SQL Server};server=10.80.44.62,21444;database=BAAS;trusted_connection=yes')
  
  query <- function(channel, query) {
    
    t1 = Sys.time()
    
    out = sqlQuery(channel, query)
    
    t2 = Sys.time()
    
    print(paste('Execution Time :', format(round(t2 - t1, 2))))
    print(paste('End Time :', format(x = Sys.time(), format = '%Y-%m-%d %H:%M')))
    
    return(out)
    
    }
  
  },
  
  silent = TRUE)


###### DEFINING NAS ######

nas <- c('',
         'NA',
         '#N/A',
         '#REF',
         'N/A',
         '\\N',
         'NULL',
         'null',
         '<NA>',
         'NIL',
         '-',
         'Yet to Launch',
         'TBH')


###### ~~~~~~~~~~ CUSTOM FUNCTIONS ~~~~~~~~~~ ######


###### CLEAN ACCOUNT NUMBER ######

clean_account <- function(Account_Number) {
  
  str_remove_all(string = as.character(Account_Number), pattern = '[^0-9]')
  
}


###### END OF MONTH ######

eomonth <- function(date) {
  
  ceiling_date(x = date, unit = 'month') - days(1)
  
}


###### START OF MONTH ######

somonth <- function(date) {
  
  floor_date(x = date, unit = 'month')

}


###### FY BOUNDARIES ######

fy_boundary <- function(date, boundary) {
  
  fy_lower <- if_else(condition = month(date) <= 3,
                      true = as.Date(paste0(year(date) - 1, '-04-01')),
                      false = as.Date(paste0(year(date)   , '-04-01')))
  fy_upper <- if_else(condition = month(date) <= 3,
                      true = as.Date(paste0(year(date)     , '-03-31')),
                      false = as.Date(paste0(year(date) + 1, '-03-31')))
  
  if (boundary == "lower") {
    return(fy_lower)
  } else if (boundary== "upper") {
    return(fy_upper)
  } else {
    return("Invalid Boundary ('lower' or 'upper')")
  }

}


###### FINANCIAL YEAR ######

financial_year <- function(date) {
  
  if_else(condition = month(date) > 3,
          true = paste0('FY', year(date) + 1),
          false = paste0('FY', year(date)))
  
}


###### STANDARDIZE BRANCH CODE ######

process_branch_code <- function(code) {

  bm = readRDS(file = '//FSCLUS02/HADOOP$/BBB_Master_Files/Branch_Master.RDS') %>% 
    pull(Branch_Code)
  code = as.character(code)
  code = str_remove_all(string = code, pattern = '[^0-9]')
  code = str_pad(string = code, width = 4, side = 'left', pad = '0')
  code = case_when(code %in% bm ~ code)
  return(code)
  
}


###### STANDARDIZE EMPLOYEE CODE ######

process_emp_code <- function(code) {

  code = as.character(code)
  code = str_remove_all(string = code, pattern = '[^0-9]')
  code = str_pad(string = code, width = 5, side = 'left', pad = '0')
  code = case_when(nchar(code) <= 5 ~ code)
  return(code)
  
}

process_bbb_emp_code <- function(code) {
  
  em = readRDS(file = '//FSCLUS02/HADOOP$/BBB_Master_Files/BBB_Employee_Master.RDS') %>% pull(Emp_ID)
  code = as.character(code)
  code = str_remove_all(string = code, pattern = '[^0-9]')
  code = case_when(nchar(code) <= 5 ~ code)
  code = str_pad(string = code, width = 5, side = 'left', pad = '0')
  code = case_when(code %in% em ~ code)
  return(code)
  
}


###### STANDARDIZE EMAIL ######

process_rbl_email <- function(email) {
  
  str_extract(string = str_to_lower(email),
              pattern = '\\b[\\w.%+-]+@rblbank\\.com\\b')
  
}

process_email <- function(email) {
  
  str_extract(string = str_to_lower(email),
              pattern = '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b')
  
}


###### PROCESS MOBILE ######

process_mobile <- function(Mobile) {
  
  Mobile = as.character(Mobile)
  Mobile = str_remove_all(string = Mobile, pattern = '[^0-9]')
  Mobile = str_sub(string = Mobile, start = -10, end = -1)
  Mobile = round(x = as.numeric(x = Mobile), digits = 0)
  Mobile = case_when(Mobile >= 6000000000 & Mobile <= 9999999999 ~ Mobile)
  Mobile = as.character(Mobile)
  return(Mobile)
  
}


###### EXTRACT PAN CARD NUMBER ######

extract_pan <- function(String) {
  
  str_extract(string = str_to_upper(String),
              pattern = '[A-Z]{5}[0-9]{4}[A-Z]{1}')
  
}


###### CLEAN COLUMN HEADERS ######

clean_headers <- function(Data) {
  
  names(Data) = str_to_lower(string = names(Data))
  names(Data) = str_trim(string = names(Data))
  names(Data) = str_remove_all(string = names(Data), pattern = '[^[:alnum:]]+')
  
  return(Data)
  
}


###### CLEAN SHEET NAMES ######

clean_sheet_names <- function(Path) {
  
  sheet_names = excel_sheets(Path)
  clean_headers = sheet_names
  clean_headers = str_to_lower(string = clean_headers)
  clean_headers = str_trim(string = clean_headers)
  clean_headers = str_remove_all(string = clean_headers, pattern = "[^[:alnum:]]+")
  names(sheet_names) = clean_headers
  
  return(sheet_names)
  
}
