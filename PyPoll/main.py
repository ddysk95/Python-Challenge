import os
import csv 

poll_csv = os.path.join("Resources",'election_data.csv')
#Open and read csv 

with open(poll_csv) as csv_file: 
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader) #header row  

    candidates=[] #empy list for candidates 
    voteseach=[] #empty list to capture candidate votes by index 
    totalvotes=0

    for row in csv_reader:
        totalvotes+=1
        #candidate IS NOT in candidates list 
        if (row[2] not in candidates):
            candidates.append(row[2])
            voteseach.append(1)
        else: #candidate IS IN candidates list
            ind= candidates.index(row[2])
            #index where candidate is in list, add to respective vote count  
            voteseach[ind]+=1

    candpercentage =[]
    
    text_print=f"""" 
        Election Results 
        ----------------
        Total Votes: {totalvotes}
        ----------------
        """

    print(text_print)

    for candidate in candidates: 
        #index of candidate in candidate list 
        ind2=candidates.index(candidate)
        candpercentage.append(1)
        candpercentage[ind2] = (voteseach[ind2]/totalvotes) * 100
        print(f"{candidate}: {round((candpercentage[ind2]),3)}% ({voteseach[ind2]})")
    
    #find winner
    maxind=voteseach.index(max(voteseach))
    winner= candidates[maxind]    

    text_print2=f"""
        ----------------
        Winner: {winner}
        ----------------"""
    print(text_print2)

analysis_csv = os.path.join("Analysis",'Analysis.txt')
with open(analysis_csv,'w') as txt_file:
    txt_file.write(text_print)
    for candidate in candidates: 
        #index of candidate in candidate list 
        ind2=candidates.index(candidate)
        txt_file.write(f"{candidate}: {round((candpercentage[ind2]),3)}% ({voteseach[ind2]}) \n")
    txt_file.write(text_print2)
        



  

    

    


