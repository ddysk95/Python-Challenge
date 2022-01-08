import os
import csv 

bank_csv = os.path.join("Resources",'budget_data.csv')
#Open and read csv 



with open(bank_csv) as csv_file: 
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader) #header row 
    csv_frow= next(csv_reader) #first data row 

    num_mths= 1 
    data1=float(csv_frow[1]) #capture first data value 
    tot_profloss=data1 #capture first data value in total count 
    totchange=0 #capture total change 
    gincr_num=0 #greatest increase data 
    gincr_date="" #greatest increase date 
    gdecr_num=0 #greatest decrease data 
    gdecr_date="" #greatest decrease data 

    for row in csv_reader:
       #for each row count months 
        num_mths+=1
        #for each row add to total  
        tot_profloss+=float(row[1])
        #change between previous row 
        change= float(row[1]) - data1
        totchange+=change #total change add 
        #reset data1
        data1=float(row[1])

        if change>0 and change>gincr_num:
            gincr_num=change
            gincr_date=row[0]
        if change<0 and change<gdecr_num:
            gdecr_num=change
            gdecr_date=row[0]

    avgtotchange= totchange/(num_mths-1)
    textprint= f"""Financial Analysis 
    ---------------- 
    Total Months : {num_mths}
    Total: ${round(tot_profloss)}
    Average Change: ${round(avgtotchange,2)}
    Greatest Increase in Profits: {gincr_date} (${round(gincr_num)})
    Greatest Decrease in Profits: {gdecr_date} (${round(gdecr_num)})
    """
    print(textprint)

analysis_csv = os.path.join("Analysis",'Analysis.txt')
with open(analysis_csv,'w') as txt_file:
    txt_file.write(textprint)
     
        




