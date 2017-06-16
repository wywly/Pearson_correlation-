
def Pearson_correlation(sample1,sample2):
    Mean_sample1 = Mean(sample1)
    Mean_sample2 = Mean(sample2)
    
    Numerator = 0
    denominator = 0
    i=0
    while i < len(sample1):
        Numerator += (sample1[i] - Mean_sample1) * (sample2[i] - Mean_sample2)
        i += 1

    i = 0
    tmp1=tmp2=0
    while i < len(sample1):
        tmp1 += (sample1[i] - Mean_sample1)**2
        tmp2 += (sample2[i] - Mean_sample2)**2
        i += 1

    denominator = (tmp1**0.5) * (tmp2**0.5)

    return (Numerator / denominator)
    
#******************************************************************************    
    
def Mean(sample):
    Count_of_elements = len(sample)
    mean = 0
    for number in sample:
        mean += (number / Count_of_elements)
        
    return mean

#******************************************************************************

#Test for X and Y
X = [30,40,40,20,12,31,10]
Y = [160,160,170,150,110,160,100]

print("Pearson Correlation is : %s" %(Pearson_correlation(X,Y)))


