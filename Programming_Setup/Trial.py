import re
import numpy as np

def process_email(id, domains = None, valid_emails = None):
    id = id.lower()
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_match = re.search(pattern, id)
    if email_match:
        extracted_email = email_match.group()
        return extracted_email
    else:
        return np.NaN

import pandas as pd 
  
a = [1,2,3]
b = ['jitendra', 'jitendra.Alim@gmail.com', 'jitendra.alim@rblbank.com']

dict = {'Sr': a, 'Email': b} 
    
df = pd.DataFrame(dict)

df['Email_Processed'] = df['Email'].apply(process_email)

print(df.head())
