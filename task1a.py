def reducer(file):
   
    output = ''
    (last_key, sum_val) = (None, 0)
    file = open(file)
    for line in file.readlines():
        (key, val) = line.strip().split(",") #use "," as delimiter instead of '$
        if last_key and last_key != key:
            output = output + last_key+","+str(sum_val)+"\n"
            (last_key, sum_val) = (key, int(val))
        else:
            (last_key, sum_val) = (key, sum_val + int(val))

    if last_key:
        output = output + last_key + "," + str(sum_val) + "\n"
    with open('Book1.txt','w') as f:
        f.write(output)
    return 'Book1.txt'

def printTopWords(file):
    '''
    Finds top 20 most frequently occurring terms in a file. 
    Input file expected to come from reducer.py output. Returns output in plain$
    '''

    fullArray = []
    numArray = []
    file = open(file)
    for line in file.readlines():
        line = line.strip()
        fullArray = fullArray + [line]    #create list with all lines as elemen$
    for element in sorted(fullArray):
        numArray = numArray + [int(element[element.find(",")+1:])]    #extract $
    numArray.sort(reverse=True)      #sort numbers into descending order
    for element in fullArray:
        for num in numArray[0:19]:    #find items in fullarray whose final digi$
            if int(element[element.find(",")+1:]) == num:    
                if element in fullArray:
                    fullArray.remove(element)    #remove element in order to pr$
        print(element)


