###### SETTING PARAMETERS ######

setwd('~')

Sys.setenv(TZ = 'Asia/Calcutta')

options(java.parameters = '-Xmx48g',
        scipen = 999,
        warn = -1)


###### LIBRARIES ######

library(data.table)
library(dplyr)
library(tidyr)
library(lubridate)
library(stringr)
library(readxl)
library(writexl)


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

###### CLEAN UNIQUE ID ######

remove_prefix <- function(id) {
  str_remove(string = id, pattern = '~')
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

branchid <- function(id, id_chars_branch, valid_branches = NA) {
  
  id = as.character(id)
  id = str_remove_all(string = id, pattern = '[^0-9]')
  id = str_pad(string = id, width = id_chars_branch, side = 'left', pad = '0')
  
  if (any(!is.na(valid_branches))) {
    id = case_when(id %in% valid_branches ~ id)
  }
  
  return(id)
  
}


###### STANDARDIZE EMPLOYEE CODE ######

empid <- function(id, id_chars_emp, valid_empids = NA) {
  
  id = as.character(id)
  id = str_remove_all(string = id, pattern = '[^0-9]')
  id = str_pad(string = id, width = id_chars_emp, side = 'left', pad = '0')
  id = case_when(nchar(id) <= id_chars_emp ~ id)
  
  if (any(!is.na(valid_empids))) {
    id = case_when(id %in% valid_empids ~ id)
  }
  
  return(id)
  
}


###### EMAIL ######

email <- function(id, valid_emails = NA, domains = NA) {
  
  if (any(is.na(domains))) {
    id = str_extract(string = str_to_lower(id),
                     pattern = '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b')
  } else {
    id = str_extract(string = str_to_lower(id),
                     pattern = paste0('\\b[\\w.%+-]+@(', paste0(domains, collapse = '|'), ')\\b'))
  }
  
  if (any(!is.na(valid_emails))) {
    id = case_when(id %in% valid_emails ~ id)
  }
  
  return(id)
  
}


###### MOBILE ######

mobile <- function(x) {
  
  x = as.character(x)
  x = str_remove_all(string = x, pattern = '[^0-9]')
  x = str_sub(string = x, start = -10, end = -1)
  x = round(x = as.numeric(x = x), digits = 0)
  x = case_when(x >= 6000000000 & x <= 9999999999 ~ x)
  x = as.character(x)
  return(x)
  
}


###### EXTRACT PAN CARD NUMBER ######

extract_pan <- function(x) {
  str_extract(string = str_to_upper(x),
              pattern = '[A-Z]{3}[ABCFGHLJPT][A-Z]\\d{4}[A-Z]{1}')
}


###### CLEAN COLUMN HEADERS ######

clean_headers <- function(df) {
  
  names(df) = str_to_lower(string = names(df))
  names(df) = str_trim(string = names(df))
  names(df) = str_remove_all(string = names(df), pattern = '[^[:alnum:]]+')
  
  names_df = data.frame(Order = 1:length(names(df)),
                        Names = names(df)) %>% 
    group_by(Names) %>% 
    mutate(Row_Number = row_number(),
           Row_Number = Row_Number - 1,
           New_Names = paste0(Names, Row_Number),
           New_Names = if_else(condition = str_sub(string = New_Names,
                                                   start = -1,
                                                   end = -1) == '0',
                               true = as.character(Names),
                               false = as.character(New_Names)))
  
  names(df) = names_df$New_Names
  return(df)
  
}


###### CLEAN SHEET NAMES ######

clean_sheet_names <- function(path) {
  
  sheet_names = excel_sheets(path)
  clean_headers = sheet_names
  clean_headers = str_to_lower(string = clean_headers)
  clean_headers = str_trim(string = clean_headers)
  clean_headers = str_remove_all(string = clean_headers, pattern = "[^[:alnum:]]+")
  names(sheet_names) = clean_headers
  
  return(sheet_names)
  
}
