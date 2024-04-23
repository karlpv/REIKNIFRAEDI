def til_skiptis(L1,L2):
    new_list = []
    for i in range(len(L1)):
        new_list.append(L1[i])
        new_list.append(L2[i])
    return sorted(new_list)

a = [1,2,3,4]
b = [6,7,8,9]
print(til_skiptis(a,b))

def til_mis(L1,L2):
    L = []
    for i in range(max(len(L1),len(L2))):
        if i < len(L1):
            L.append(L1[i])
        if i < len(L2):
            L.append(L2[i])
    return L
c = [1,2]
print(til_mis(a,c))

def bilar(t1,input):
    new_t1 = {} 
    for key,values in t1.items():
        if input == key:
            new_t1[key] = values
            print(f'{values}')

t1 = {'MSS-42':'Elín','Z-474':'Kristján','XYZ-12':'Ari'}
t2 = {'MSS-42':'Hyndai','Z-474':'Toyota','XYZ-12':'BMW'}

inputings = input()
bilar(t1,inputings)


def bilalisti(t1,t2):
    new_t1 = {} 
    for key,values in t1.items():
        tegund = t2[key]  
        new_t1[key] = tegund + ' sem ' + values + ' á'
    return new_t1

t1 = {'MSS-42':'Elín','Z-474':'Kristján','XYZ-12':'Ari'}
t2 = {'MSS-42':'Hyndai','Z-474':'Toyota','XYZ-12':'BMW'}
print(bilalisti(t1,t2))
