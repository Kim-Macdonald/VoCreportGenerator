# VoCreportGenerator
Generates VoC reports (positives by run#, possible by run#, and variant requests (yes/no/possible/failed status, VoC type (e.g. UK (B.1.1.7), SA (B.1.351), Brazil (P.1), Nigerian (B.1.525), Not a VoC, Possible [VoC from ncov watchlist ID], WGS QC Fail) added) from output of mergeQCresults_plusMissing (assuming you move it to your PC, and add an extra column on end for Run#/ID).


# Assumptions: 
You should have the following folders set up on your network/PC (or change the paths in script to reflect where you want your VoC tables/reports saved):

![image](https://user-images.githubusercontent.com/72042148/110599834-242cce80-8138-11eb-85b9-8e507483da65.png)


<b>After running the mergeQCresults_plusMissing.py script on the server:</b> 

You'll transfer the output csv file for each run (from the server to your PC), 

Add the RunNum column to the end and populate it with a Run#/ID (should be unique for each run - e.g. 0001, 0002, 0003 - it'll be used in file sorting and output naming), 

And merge the csv files (append) together into a file that contains results for all runs to-date (See below for merge/append suggestion). 

(you can probably run the VoCreportGenerator script on single output files from the script too (if you add a RunNum (run # or runID) column, or remove it's references from the script)




You can merge multiple files in windows using windows cmd prompt (copy them all to your C drive and run): (Example:)

      copy /b *_QC_lineage_VoC_OrderedFinal.csv AllRuns_combined_QC_lineage_VoC_OrderedFinal.csv 



## Positive VoC tables: 

Based on the combined/merged results file, the script will pull <b>all positive VoC lineages</b> (UK (B.1.1.7), SA (B.1.351), Brazil (P.1), and Nigerian (B.1.525) at the moment) into a new table for positive VoCs. It'll then separate this table by run#/ID (if you added the column at the end), and save individual tables per run, in the Positives folder you created above (at the path you specified in the script). 


Output filenames will look like:

Run72_VoCpositives.csv



## Possible VoC tables (need to be confirmed before reporting using bam alignment in IGV etc):

Based on the combined/merged results file, the script will pull all samples with <b>no lineage assigned AND > 4 observed ncov-watch mutations</b> (you can adjust this in the script too, under conditions) into a new table for possible VoCs. It'll then separate thsi table by run#/ID (if you added the column at the end), and save individual tables per run, in the Possible folder you created above (at the path you specified in the script). 


Output filenames will look like:

Run113_VoCpossibles_ToCheck.csv



## VoC Requests from Clients: 

VoC Requests are pulled from a separate sheet, that you supply. Update the link to and name of this sheet relative to your network/PC. 

It's assumed that this Requests file has 3 columns (sampleID, Run#, FastqID). 

It's also assumed that you'll enter requests for 1 run at a time (if not you can copy the code for the sort and groupby RunNum down here as well, or choose the alternative save method (commented out in the 2nd last line of the script) which will just save by today's date instead of by Run#) (to choose the other method, add a # in front of the save method (at end of script - last line) to comment it out, and remove the # in front of the 2nd last line). 


You'll populate this sheet with the list of samples (sampleID, Run#, FastqID - adjust script as needed to change these) that have VoC WGS testing requests. The script will create a table of these samples and their VoC results assigned (yes/no/possible/failed and type: UK (B.1.1.7) etc, Not a VoC, Possible [VoC from ncov watchlist ID], WGS QC Fail). 


<b>2 columns will be added to this table for reporting</b>: 

<b>VoCYesNo</b> (yes/no/failed/possible) 

and <b>VoCType</b> (e.g. UK (B.1.1.7), Not a VoC, Failed WGS QC, Possible [watchlist ID]). 



The table will be sorted by VoCYesNo, and saved in the Requests folder you created above (at the path you specified in the script). 

The run#/ID you added to the extra column at the end of the csv file(s) will be added to the file name. 


Output filenames will look like:

Run145_VoCrequests.csv



# Example Output:

VoC Positives:



VoC Possibles:



VoC Requests: 



# Usage:

<b>Run mergeQCresults_plusMissing.py on the server, as per mergeQCresults_plusMissing.py instructions</b> (https://github.com/Kim-Macdonald/mergeQCresults_plusMissing )

(replace [MiSeqRunID] with your MiSeqRunID/RunName or Directory for the sequencing run of interest):

      cd sequence/analysis/run/directory/[MiSeqRunID]; conda activate pandas; python3 path/to/mergeQCresults_plusMissing.py; conda deactivate



<b>Add a new column to the above csv file (at the end), and fill it with values for your actual Run#/ID (should be unique for each run - e.g. 0001, 0002, 0003 - it'll be used in file sorting and output naming), and give it the header "RunNum"</b> 

(replace the text 'RunID' (after d=) below with your actual Run#/ID (don't remove the double quotes) (it'll fill each row in the column with that value. The runID should be the same for everything in the file - assuming it was made in a directory of sequences from one miseq/sequencing run) 

(replace [MiSeqRunID] with your MiSeqRunID/RunName that appears in the file created above):

      awk -v d="RunID" 'BEGIN{FS=OFS=","} {print $0, (NR>1?d:"RunNum")}' [MiSeqRunID]_MissingPlus_QC_lineage_VoC_OrderedFinal.csv > [MiSeqRunID]_MissingPlus_QC_lineage_VoC_OrderedFinal_RunNum.csv

Example: 

      awk -v d="0003" 'BEGIN{FS=OFS=","} {print $0, (NR>1?d:"RunNum")}' 210304_M01234_0215_000000000-G6D8F_MissingPlus_QC_lineage_VoC_OrderedFinal.csv > 210304_M01234_0215_000000000-G6D8F_MissingPlus_QC_lineage_VoC_OrderedFinal_RunNum.csv


Output looks like (from viewing with column command) (Example command): 

      column -ts ',' 210304_M01234_0215_000000000-G6D8F_MissingPlus_QC_lineage_VoC_OrderedFinal_RunNum.csv | less -S

(to ensure it worked) (then scroll to the right (using the right arrow key) to see the last column)

![image](https://user-images.githubusercontent.com/72042148/110888572-4beb7600-82a1-11eb-9811-958556ed6dfa.png)

(note that it may look like there are extra, partly filled columns using this command (b/c it converts any comma (even those in values) to a tab - but your actual csv file isn't formatted this way). 


If you open the ...RunNum.csv file in excel, it may display a number you added as 0003, as 3. To reformat this, highlight the RunNum column in Excel, right click -> format cells -> Custom -> Enter 0000 (as in image below) -> OK:
![image](https://user-images.githubusercontent.com/72042148/110895973-852ae280-82af-11eb-90c7-8a525cbf7636.png)


<b>Choose either option A or B below to finish the process (unix vs windows cmd):</b>


### Server option (A):

If you prefer to merge the files in a unix environment (server, mac, etc) (vs in windows cmd below):

Navigate to the analysis directory (1 level above your run directories - e.g. if your runs are in /Path/to/analysis/[MiSeqRunID] then cd to /Path/to/analysis/ )

(replace "Runs1-145" in the output file with whatever makes sense for your runs)

      cat ./*/*_MissingPlus_QC_lineage_VoC_OrderedFinal_RunNum.csv > Runs1-145_combined_QC_lineage_VoC_OrderedFinal.csv


Remove the header rows from all the files except the first: (replace both instances of "Runs1-145" below with whatever you used in your output file above)

      header=$(head -n 1 Runs1-145_combined_QC_lineage_VoC_OrderedFinal.csv); (printf "%s\n" "$header"; grep -vFxe "$header" Runs1-145_combined_QC_lineage_VoC_OrderedFinal.csv) > Runs_CombinedQCsummary.csv


<b>Transfer the Runs_CombinedQCsummary.csv output file for each run from the server to your PC (e.g. via Cyberduck, FileZilla, etc).</b>


<b>Create the Positives, Possible, and Requests folders as shown above (whereever you want to save your VoC files).</b>


<b>Create a spreadsheet (.xlsx) called "VariantRequests.xlsx"  (this is where you'll copy in samples that have been requested for VoC detection/confirmation by WGS). It should have 3 columns (sample, Run#, FastqID). The sampleID used in the sample column, should match that which will appear in your WGS QC results (Runs_CombinedQCSummary.csv)
      
      
<b>Open the csv file (e.g. Runs_CombinedQCsummary.csv) and save as .xlsx.</b>
(or you can edit the script to read it in as a csv (pd.read_csv) instead of xlsx (pd.read_excel))


<b>Update paths to files, in the script, as per your set-up.</b> 


<b>Save script to your PC. Open and run script in Spyder IDE, or alternative, on your PC.</b> 




### Windows cmd option (B) to do on a Windows PC:

<b>Transfer the *_RunNum.csv output file for each run from the server to the same folder on your PC (e.g. via Cyberduck, FileZilla, etc).</b>


<b>Merge the csv files for each run (append) together into 1 file that contains results for all runs to-date.</b>

You can merge multiple files in windows using <b>windows cmd prompt</b> (copy them all to your C drive, open cmd (type cmd in your windows start menu search bar) and run): 

(Example:) (replace the "Runs1-145" with whatever makes sense for your runs) (if you don't use the /b it'll add an arrow/control character to the end. It's annoying)

      navigate in cmd, to your folder with all the *_RunNum.csv files (e.g cd "C:\Users\Kim\Downloads" )
      

      copy /b *_MissingPlus_QC_lineage_VoC_OrderedFinal_RunNum.csv Runs1-145_combined_QC_lineage_VoC_OrderedFinal.csv 


<b>Remove the extra header lines for each of the runs, that were appended, in that file:</b>

(first command pull the header row out of the combined file from above and stores in a file)

(2nd command removes all the header lines from teh above combined file, and creates a new file, with no header. Then it combines the 2 files (copy command) into a new file "Runs_CombinedQCSummary.csv". Then it removes the 2 Temp files. 


      set /p headerrow=< Runs1-145_combined_QC_lineage_VoC_OrderedFinal.csv && >Temp1.csv echo %headerrow% 

      (You'll likely need to run the above command twice to get it to set the variable properly - the first time it may output "%headerrow%" in one cell in the csv file. 
      Open the csv file to check after running, to make sure it worked. If not, run it another time and check again. If your header row is there now, proceed to the next command.
      
      findstr /v "sample" Runs1-145_combined_QC_lineage_VoC_OrderedFinal.csv > Temp2.csv && copy /b Temp*.csv Runs_CombinedQCsummary.csv && del Temp1.csv Temp2.csv




<b>Create the Positives, Possible, and Requests folders as shown above (whereever you want to save your VoC files).</b>


<b>Create a spreadsheet (.xlsx) called "VariantRequests.xlsx  (this is where you'll copy in samples that have been requested for VoC detection/confirmation by WGS. The script will read in this file and match WGS results for those samples). It should have 3 columns (sample, Run#, FastqID). The sampleID used in the sample column, should match that which will appear in your WGS QC results (Runs_CombinedQCSummary.csv)


<b>Open the csv file (e.g. Runs_CombinedQCsummary.csv) and save as .xlsx.</b>
(or you can edit the script to read it in as a csv (pd.read_csv) instead of xlsx (pd.read_excel))


<b>Update paths to files, in the script, as per your set-up.</b> 


<b>Save script to your PC. Open and run script in Spyder IDE, or alternative, on your PC.</b> 


