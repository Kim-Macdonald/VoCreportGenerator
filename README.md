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

      copy *_QC_lineage_VoC_OrderedFinal.csv AllRuns_combined_QC_lineage_VoC_OrderedFinal.csv 



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

It's also assumed that you'll enter requests for 1 run at a time (if not you can copy the code for the sort and groupby RunNum down here as well). 


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
Save script to your PC. Open and run script in Spyder IDE, or alternative, on your PC. Update paths to files as per your set-up. 

