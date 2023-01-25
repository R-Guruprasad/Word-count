# Word-count
## AIM:
To write a python program for getting the word count from a text.
## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7
## ALGORITHM: 
### Step 1:
To write a python program for getting the word count from a text file
### Step 2: 
Open the required file by using the function "with". 
### Step 3:
Then use the laptop to assign the i value in the file.
### Step 4:  
Using split function to spilt the words
### Step 5: 
Finding the given length of the words by using len() fuction.
### Step 6: 
Calling the function and Printing the number of words.
## PROGRAM:
```python
'''
Python program for getting the word count from a text file
Developed by: R.Guruprasad
Ref no: 22006697

'''
num_word=0
with open ("textfile.txt",'r') as f:
    for i in f:
        word=i.split()
        num_word+=len(word)
print("number of words ={}".format(num_word))

```

### OUTPUT:
![1](/pic1.png)
![2](/pic2.png)
![3](/pic3.png)



## RESULT:
Thus the program is written to find the word count from a text.
