###### BASIC LIBRARIES ######

import io
import os
import re
import pickle
import pyodbc
import math
import numpy as np
import pandas as pd
from datetime import datetime

print("""
Loaded Package:
- import io
- import os
- import re
- import pickle
- import pyodbc
- import math
- import numpy as np
- import pandas as pd
- from datetime import datetime
""")


###### PANDAS CONFIGURATION ######

pd.set_option('display.float_format', '{:.2f}'.format)
pd.options.display.max_columns = None

print("""
Pandas Configurations:
pd.set_option('display.float_format', '{:.2f}'.format)
pd.options.display.max_columns = None
""")


###### NAS ######

nas = ['',
       '-',
       'Not Available',
       'NA',
       '#N/A',
       'N/A',
       '<NA>',
       '\\N',
       'NULL',
       'null',
       'NIL',
       '#REF']


###### FINANCIAL YEAR ######

def financial_year(date):
    if date.month >= 4:
        return ('FY' + str(date.year + 1))
    else:
        return ('FY' + str(date.year + 0))


###### PROCESS MOBILE NUMBER ######

def process_mobile(mobile):
    mobile = 0 if math.isnan(mobile) else mobile
    mobile = int(mobile)
    mobile = str(mobile)
    mobile = re.sub(r'[^0-9]', '', mobile)
    mobile = mobile[-10:]
    mobile = int(mobile)
    if 6000000000 < mobile < 9999999999:
        return str(mobile)
    else:
        return np.NaN
    

###### EXTRACT PAN ######

def extract_pan(string):
	"""
 	Description:
    ------------
    This function is used to extract PAN number from string.
    
    Parameter(s):
    -------------
    string(str): Data consisting PAN number
    
    Return(s):
    ----------
    PAN Number
    """
    string = string.upper()
    pattern = r'[A-Z]{3}[ABCFGHLJPT][A-Z]\d{4}[A-Z]{1}'
    pan_match = re.search(pattern, string)
    if pan_match:
        pan = pan_match.group()
        return pan
    else:
        return np.NaN


###### PROCESS EMAIL ######

def process_email(email):
    email = email.lower()
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_match = re.search(pattern, email)
    if email_match:
        extracted_email = email_match.group()
        return extracted_email
    else:
        return np.NaN
    

###### PROCESS RBL EMAIL ######

def process_office_email(email):
    email = email.lower().strip()
    pattern = r'\b[\w.%+-]+@rblbank\.com\b'
    office_email_match = re.search(pattern, email)
    if office_email_match:
        office_email = office_email_match.group()
        return office_email
    else:
        return np.NaN


###### PROCESS BRANCH CODE ######

def process_branch_code(code):
    with open('//FSCLUS02/HADOOP$/BBB_Master_Files/Branch_Master.pkl', 'rb') as f:
        bm = pickle.load(f)
    code = 0 if math.isnan(code) else code
    code = int(code)
    code = str(code)
    code = re.sub('[^0-9]', '', code)
    code = code.rjust(4, '0')
    if code in bm['Branch_Code'].values:
        return code
    else:
        return np.NaN


###### PROCESS EMPLOYEE ID ######

def process_emp_id(code):
    code = 0 if math.isnan(code) else code
    code = int(code)
    code = str(code)
    code = re.sub('[^0-9]', '', code)
    code = code.rjust(5, '0')
    if code == "00000":
        return np.NaN
    else:
        return code


###### PROCESS BBB EMPLOYEE ID ######

def process_bbb_emp_id(code):
    with open('//FSCLUS02/HADOOP$/BBB_Master_Files/BBB_Employee_Master.pkl', 'rb') as f:
        em = pickle.load(f)
    code = 0 if math.isnan(code) else code
    code = int(code)
    code = str(code)
    code = re.sub('[^0-9]', '', code)
    code = code.rjust(5, '0')
    if code in em['Emp_ID'].values:
        return code
    else:
        return np.NaN
