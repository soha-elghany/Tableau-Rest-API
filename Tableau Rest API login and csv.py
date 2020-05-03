

# Write a Python script that uses the Tableau Server Client library that:
# Sign-in to your site - using access token
# Requests a list of all the workbooks (and owners) on the site
# Writes this list out as a CSV file 
# Manually login to your site and:

pip install tableauserverclient

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

    request_options = TSC.RequestOptions(pagesize=500)
    all_workbooks_items, pagination_item = server.workbooks.get(request_options)
    workbook_id = [workbook.id for workbook in all_workbooks_items]
    workbook_name = [workbook.name for workbook in all_workbooks_items]
    url = [workbook.content_url for workbook in all_workbooks_items]
    owner_id = [workbook.owner_id for workbook in all_workbooks_items]
    project_name = [workbook.project_name for workbook in all_workbooks_items]
    tags = [workbook.tags for workbook in all_workbooks_items]
    description = [workbook.description for workbook in all_workbooks_items]
    
    print(workbook_name)
    print(owner_id)
    
#saving into a csv file
df = pd.DataFrame({'workbook name':workbook_name, 'owner ID':owner_id})
df

df.to_csv('workbook.csv', sep ='\t', header = True)
df.to_csv(r'C://Users/Username/Documents/workbookx.csv') - put in the file path
