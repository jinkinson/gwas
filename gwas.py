import sys
file=open(sys.argv[1])
lines=file.readlines()
output={}
for i in range(1,len(lines)):
    lines[i]=lines[i].split('\t')

unique=[]
for i in range(1,len(lines)):
    output[i]=[lines[i][20],lines[i][21],lines[i][27],lines[i][30],lines[i][31]]
    if lines[i][21] in unique:
        i=i+1
    else:
        unique.append(lines[i][21])
for i in range(1,len(lines)):
    if lines[i][30]<1:
        output[i].append('beta')
    else:
        if lines[i][30]=="":
            output[i].append('blank')
        else:
            if lines[i][30]==1:
                output[i].append('beta')
            else:
                if 'unit' in lines[i][31]:
                    output[i].append('beta')
                else:
                    output[i].append('OR')

#Positive/negative
associations={}
for i in range(1,len(unique)):
    associations[i]=[unique[i]]

for i in range(1,len(output)):
    #First we want to change the p-value so it is formatted correctly
    #Recall that the 3rd item in each output[i] list is the p-value
    #Further, each p-value is now listed as 'xE-y' where x and y are both numbers
    #Anyway we will use a hereafter to represent the position of the minus sign in the p-value field
    #And we will use b to represent the position of the capital E
    a=output[i][2].index('-')
    b=output[i][2].index('E')
    output[i][2]=int(output[i][2][:b])*(10**int(output[i][2][a:]))
    for j in range(1,len(unique)):
        positive=0
        negative=0
        significant=0
        if unique[j]==output[i][1]:
            if output[i][4]=='beta':
                if 'increase' in output[i][5]:
                    positive=positive+1
                else:
                    if 'decrease' in output[i][5]:
                        negative=negative+1
                    else:
                        positive=positive+1
                if output[i][2]>(5*(10**(-8))):
                    significant=significant+1
