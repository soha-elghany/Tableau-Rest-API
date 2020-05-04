

# Write a Python script that uses the Tableau Server Client library that:
# Sign-in to your site - using access token
# Requests a list of all the workbooks (and owners) on the site
# Writes this list out as a CSV file 

import tableauserverclient as TSC 
import pandas as pd
import numpy as np

USERNAME = ' ' - write your usernmae here
PAT = ' ' - write your access token here
SITE= ' ' - write your site name
SERVERURL = ' ' - write the url of your server

server = TSC.Server(SERVERURL, use_server_version=True)
tableau_auth = TSC.PersonalAccessTokenAuth("Test", PAT, site_id=SITE)

with server.auth.sign_in(tableau_auth):

    all_workbooks, pagination_item = server.workbooks.get()
    workbook_data = [{"workbook_name": workbook.name,
                      "size": workbook.size,
                      "created_at":workbook.created_at,
                      "owner_id":workbook.owner_id,
                      "owner_name": server.users.get_by_id(workbook.owner_id).name}
                     for workbook in all_workbooks]
    
    print(workbook_data)
    
#saving into a csv file
df = pd.DataFrame.from_dict(workbook_data)
df

df.to_csv('workbook.csv', sep ='\t', header = True)
df.to_csv(r'C://Users/Username/Documents/workbookx.csv') - put in the file path

server.auth.sign_out()