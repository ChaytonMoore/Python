#Average Generator

Data = []

while True:
    number = input("What number do you want to add to the list.")
    try:
        number = int(number)
        valid = True
    except:
        print("Sorry that wasn't a valid input.")
        valid = False
        if number == "quit":
            break
            exit()
    
    if valid == True:
        #Time to order the data
        if len(Data) == 0:
            Data.append(number)
        elif len(Data) == 1:
            if number > Data[0]:
                Data.append(number)
            else:
                Data.insert(0, number)
        elif number>Data[len(Data)-1]:
            Data.append(number)
        else:
            for i in range(0, len(Data)-2):
                if number > Data[i] and number <= Data[i+1]:
                    idx = i
                    if number == Data[i+1]:
                        idx += 1
            Data.insert(idx, number)
        
        print(Data)
            
        
        
        mean = 0
        for i in Data:
            mean += i
        mean = mean / len(Data)
        print("The mean is", mean)
        median = ((len(Data)+1)/2)
        
        if median == int(median):
            median = Data[int(median)-1]
        else:
            median = (Data[int(median)] + Data[int(median)-1])/2
        
        print("The median is",median)
        
        print("The max value is",Data[len(Data)-1])
        print("The min value is",Data[0])
        print("The range is",Data[len(Data)-1] - Data[0])
        l_quart = ((len(Data)+1)/4)
        u_quart = median + (((len(Data) - median))/2)
        
        if l_quart == int(l_quart):
           l_quart = Data[int(l_quart)-1]
        else:
            l_quart = (Data[int(l_quart)] + Data[int(l_quart)-1])/2
        
        if u_quart == int(u_quart):
           u_quart = Data[int(u_quart)-1]
        else:
            u_quart = (Data[int(u_quart)] + Data[int(u_quart)-1])/2
        
        print("The lower Quartile is",l_quart)
        print("The upper Quartile is",u_quart)
            