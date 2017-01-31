
# coding: utf-8

# In[ ]:

'''
Enter a number and have the program generate the Fibonacci sequence to Nth number .
'''


# In[3]:

def getfi(limit):
    count=2
    a=0
    b=1
    yield a
    yield b
    while count!=limit+1:
        yield a+b
        a,b=b,a+b
        count+=1


# In[4]:

def inputnumber():
    while True:
        try:
            number = int(raw_input("How many numbers do you want your fibonacci sequence to have? "))
            break
        except(TypeError, ValueError):
            print ("You did not enter a number, please try again!")
    return number
            


# In[5]:

def main():
    number=inputnumber()
    for i in getfi(number):
        print i,
        


# In[6]:

main()


# In[ ]:

'''
Enter a number and have the program generate the Fibonacci sequence up to the entered number .
'''


# In[10]:

def getfi(limit):
    count=2
    a=0
    b=1
    yield a
    yield b
    while a+b<limit:
        yield a+b
        a,b=b,a+b
        count+=1


# In[11]:

def inputnumber():
    while True:
        try:
            number = int(raw_input("Until what number would you like to calculate the fibonacci sequence? "))
            break
        except(TypeError, ValueError):
            print ("You did not enter a number, please try again!")
    return number
            


# In[12]:

def main():
    number=inputnumber()
    for i in getfi(number):
        print i,
        


# In[14]:

main()


# In[ ]:



