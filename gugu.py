import os

def GuGu(n):
    print(n)
    
    result = []
    
    for i in range(1, 10):
        result.append(i * 2)
    
    return result

def threefive():
    for n in range(1, 1000):
        if n % 3 == 0 or n % 5 == 0:
            print(n)
            
def getTotalPage(m, n):
    result = int(m / n)
    
    if m % n != 0:
        result += 1
        
    return result

def search(dir):
    
    filenames = os.listdir(dir)
    for name in filenames:
        full_filename = os.path.join(dir, name)
        
        if os.path.isdir(full_filename):
            search(full_filename)
        else:
            ext = os.path.splitext(full_filename)[-1]
            if ext == ".py":
                print(ext)
    
if __name__== "__main__":
    
    #dan = int(input("출력할 단을 입력하세요 : "))
    #print(GuGu(dan))
    
    #hreefive()
    
    #print(getTotalPage(5, 10))
    #print(getTotalPage(15, 10))
    #print(getTotalPage(25, 10))
    #print(getTotalPage(30, 10))
    
    search("c:/")
    
