# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:37:21 2021

@author: kmacdonald
"""

#import packages I may need
import os
import pandas as pd
import numpy as np

# Store current date in a variable (For file naming, if desired):
from datetime import datetime
Today = datetime.today().strftime('%Y-%m-%d')   # output is like '2021-01-26'  

# Read in the combined/merged QCsummary excel file (Sheet1):
df_QCsummary = pd.read_excel('Path/ToMergedFile/CombinedQCsummary.xlsx', sheet_name=0)  #will read in the first sheet in the excel file
#print(df_QCsummary)


#-------------VARIANT POSITIVES---------
# Keep only rows with VoC Positives:
# Make variable to store values for positives (lineages of concern):
Positive_values = ['B.1.1.7', 'B.1.351', 'P.1', 'B.1.525']
df_VoCpos0 = df_QCsummary.loc[df_QCsummary['lineage_x'].isin(Positive_values)]
#print(df_VoCpos0)  #correct (# rows of VoCs expected and obtained) Test with your data

# # Connect to any other sheets/sources you may need (to match patient metadata, etc): (I haven't done this yet)

# # Merge metadata from the above files (left join) with the VoC positives list samples only:

# # Only keep the columns of interest for VoC checking/reporting:

    
#split table by Run#s:
df_VoCpos1 = df_VoCpos0.sort_values(by=['RunNum', 'sample'])
#print(df_VoCpos1)
for i, g in df_VoCpos1.groupby('RunNum'):
        #print(g)  #correct
        # save separate files of Positive VoCs, split by Run#/ID:
        # remove duplicates - only keep one line of Run#, and only want last column (the Run# column):
        RunNum = g.drop_duplicates(subset=['RunNum'], keep='first').iloc[:, 31:32] 
        #print(RunNum.iloc[:, -1].to_string(index=False)) #worked (just prints the run # for each table)
        # remove Headers and index to store just the Run# in the RunNum2 variable:
        RunNum2 = RunNum.iloc[:, -1].to_string(index=False)
        #print(RunNum2) #works
        # Only create new VoC files for those runs that don't already exist:
        Filecheck = os.path.join('Path/To/Output/Files/Positives/' + 'Run' + RunNum2.strip() + '_' + 'VoCpositives.csv')
        #print(Filecheck)  #works
        if not os.path.exists(Filecheck):
            #print(g)  #works
            g.reset_index().to_csv('Path/To/Output/Files/Positives/' + 'Run' + RunNum2.strip() + '_' + 'VoCpositives.csv')
             #works (won't save run files if already exist) (use strip to remove whitespace from run#)
             
                 
            # # SPLIT BY Health Authority: (need to connect to other data sources with patient data, and then merge them, for this)
             #for i, h in g.groupby('HA'):
                 #print(h)
            # # Any positives that don't have a HA, or one of these, goes into an "Other" table/file:

            # # Store HA from tables in variable (grab just the column with HA) (for naming output files etc):
                # HA = g.drop_duplicates(subset=['HA'], keep='first').iloc[:, 31:32] 
                # HA2 = HA.iloc[:, -1].to_string(index=False)
        

            # # Save files separated by Run# AND HA: (replace/comment out the above save, with this one, if HA data is added)
                #h.to_csv('Path/To/Output/Files/Positives/' + Today + '_' + + 'Run' + RunNum2.strip() + '_' + HA2.strip() + '_' + 'VoCpositives.csv')


#-----------------VARIANT POSSIBLE------------------
#Keep only rows with VoC Possibles (Need to confirm, with IGV etc):
# Make variable to store values for positives (lineages of concern):
df_VoCposs0 = df_QCsummary.loc[(df_QCsummary['lineage_x'] == 'none') & (df_QCsummary['num_observed_mutations'] > 4)]
#Example: df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]
#print(df_VoCposs0)  #is correct (# rows of VoCs expected and obtained)

#split table by Run #s:
df_VoCposs1 = df_VoCposs0.sort_values(by=['RunNum', 'sample'])
#print(df_VoCposs1)
for i, j in df_VoCposs1.groupby('RunNum'):
        #print(j)  #correct
        # SAVE file to check output:
        # remove duplicates - only keep one line of Run#, and only want last column (the Run# column):
        RunNum3 = j.drop_duplicates(subset=['RunNum'], keep='first').iloc[:, 31:32] 
        #print(RunNum.iloc[:, -1].to_string(index=False)) #worked (just prints the run # for each table)
        # remove Headers and index to store just the Run# in the RunNum4 variable:
        RunNum4 = RunNum3.iloc[:, -1].to_string(index=False)
        #print(RunNum4) #works
        # Only create new VoC files for those runs that don't already exist:
        Filecheck1 = os.path.join('Path/To/Output/Files/Possible/' + 'Run' + RunNum4.strip() + '_' + 'VoCpossibles_ToCheck.csv')
        #print(Filecheck1)  #works
        if not os.path.exists(Filecheck1):
            #print(j) 
            j.reset_index().to_csv('Path/To/Output/Files/Possible/' + 'Run' + RunNum4.strip() + '_' + 'VoCpossibles_ToCheck.csv')
             #works (won't save run files if already exist)
             
  
            # # SPLIT BY Health Authority: (need to connect to other data sources with patient data, and then merge them, for this)
             #for i, k in j.groupby('HA'):
                 #print(k)
            # # Any positives that don't have a HA, or one of these, goes into an "Other" table/file:

            # # Store HA from tables in variable (grab just the column with HA) (for naming output files etc):
                # HA3 = j.drop_duplicates(subset=['HA'], keep='first').iloc[:, 31:32] 
                # HA4 = HA.iloc[:, -1].to_string(index=False)
        

            # # Save files separated by Run# AND HA: (replace/comment out the above save, with this one, if HA data is added)
                #k.to_csv('Path/To/Output/Files/Positives/' + Today + '_' + + 'Run' + RunNum4.strip() + '_' + HA4.strip() + '_' + 'VoCpositives.csv')




    
#-----------------VARIANT REQUESTS-------------------    
# Read in VARIANT REQUESTS Sheet (Sheet1):
df_VariantReq = pd.read_excel('Path/To/SheetWithVariantRequests/VariantRequests.xlsx', sheet_name=0)   # Reads in the first sheet (0) of the excel file
#print(df_VariantReq)  #correct

# Match Requests to VoC Results (Neg,Failed only - pos are in above table - I'm pulling them all for now though) (left join):   
df_VariantReqMatch0 = pd.merge(df_VariantReq, df_QCsummary.iloc[:, 1:32], how='left', left_on='sample', right_on='sample')
#print(df_VariantReqMatch0)  #(correct - # rows expected and obtained)

# Create 2 columns for VariantYesNo and VariantType: 
df_VariantReqMatch0.insert(1, "VariantYesNo", "")
df_VariantReqMatch0.insert(2, "VariantType", "")
#print(df_VariantReqMatch0)

# Fill VariantYesNo Column with Yes/No/Failed/Possible values based on criteria:
conditions = [
    (df_VariantReqMatch0['lineage_x'].isin(Positive_values)),
    (df_VariantReqMatch0['lineage_x'].eq('none')) & (df_VariantReqMatch0['num_observed_mutations'] > 4),
    (df_VariantReqMatch0['lineage_x'].eq('none')) & (df_VariantReqMatch0['pct_covered_bases'] < 85.00),
    (df_VariantReqMatch0['lineage_x'] != 'none')
]

choices = ['Yes','Possible','Failed','No']

df_VariantReqMatch0['VariantYesNo'] = np.select(conditions, choices, default='No')
#print(df_VariantReqMatch0)  #correct


# Fill VariantType Column with values based on criteria:
conditions2 = [
    (df_VariantReqMatch0['lineage_x'] == "B.1.1.7"),
    (df_VariantReqMatch0['lineage_x'] == "B.1.351"),
    (df_VariantReqMatch0['lineage_x'] == "P.1"),
    (df_VariantReqMatch0['lineage_x'] == "B.1.525"),
    (df_VariantReqMatch0['VariantYesNo'].eq('Failed')),
    (df_VariantReqMatch0['VariantYesNo'].eq('Possible')),
    (df_VariantReqMatch0['VariantYesNo'].eq('No'))
]

#conditions = str(conditions)
choices2 = ['UK (B.1.1.7)','SA (B.1.351)','Brazil (P.1)','Nigerian (B.1.525)','Failed WGS QC',('Possible ' + df_VariantReqMatch0['watchlist_id']),'Not a VoC']

df_VariantReqMatch0['VariantType'] = np.select(conditions2, choices2, default='Not a VoC')
#print(df_VariantReqMatch0)  #correct

#sort df by VariantYesNo column (ascending by default - Failed, No, Possible at top. Yes at bottom):
df_VariantReqMatch1 = df_VariantReqMatch0.sort_values(by=['VariantYesNo', 'sample'])  

# Store Run#/ID as a variable for file naming (not used for table splitting here):
# remove duplicates - only keep one line of Run#, and only want last column (the Run# column) (are 2 extra columns for this table, that were added above):
RunNum5 = df_VariantReqMatch1.drop_duplicates(subset=['RunNum'], keep='first').iloc[:, 34:35] 
#print(RunNum5.iloc[:, -1].to_string(index=False)) #worked (just prints the run # for each table)
# remove Headers and index to store just the Run# in the RunNum6 variable:
RunNum6 = RunNum5.iloc[:, -1].to_string(index=False)
#print(RunNum6) #works

    
# split by HA (don't need to split by run# b/c are entered into the query sheet only for the current runs of interest - may cause an error if more than 1 run#/ID is in the sheet? We'll see):


# Save output to file:
#df_VariantReqMatch1.to_csv('Path/To/Output/Files/Requests/' + Today + '_' + 'VoCrequests.csv')    # Alternate file save if you don't want Run#/ID used, and Today's date instead
df_VariantReqMatch1.to_csv('Path/To/Output/Files/Requests/' + 'Run' + RunNum6.strip() + '_' + 'VoCrequests.csv')
