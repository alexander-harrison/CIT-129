import csv

def processJailCSV():
    
    file = open('acj.csv', newline='')
    reader = csv.DictReader(file)
    raceCount = {'B':0, 'W':0}
    focusDate = '6/1/2019'
    
    for row in reader:
        
        if row['Date'] == focusDate:
            # ask dict if race key is present
            if row['Race'] == 'B':
                raceCount['B'] = raceCount['B'] + 1
            elif row['Race'] == 'W':
                raceCount['W'] = raceCount['W'] + 1
                
            
            
            
            
            
           
            
                
            
                
              
    file.close()
    print(raceCount) 
    
    
    
    
processJailCSV()
