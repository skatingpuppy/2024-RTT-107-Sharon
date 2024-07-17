#FILE OBJECTS

f = open('test.txt')

#for reading
f = open('test.txt', 'r')
#to write to a file
f = open('test.txt', 'w')
#append to file
f = open('test.txt', 'a')
#read and write to file
f = open('test.txt', 'r+')

f = open('test.txt', 'r')
print(f.name)

#close file after using
f.close()


#check mode that it was opened
print(f.mode) #e.g. could print r


#when using a context manager
#allow us to work with files within one block, and after executing, automatically exits file
with open('test.txt', 'r') as f:   #variable name is f
    pass

print(f.closed) #would then print True
print(f.read()) #valueerror: i/o operation on closed file. need to work within the context manager block above

#read file within the context manager
with open('test.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)   #this prints out all contents of file

#what if we have a v big file and don't want to load everything?
with open('test.txt', 'r') as f:
    f_contents = f.readlines()
    print(f.contents)   #list of all lines in file

with open('test.txt', 'r') as f:
    f_contents = f.readline()
    print(f.contents)    #grab only first line of file

    f_contents = f.readline()
    print(f.contents)    #grabs second line of file. and etc

    f_contents = f.readline()
    print(f.contents, end='')  #it'll look cleaner

#to not run out of memory w/ a large file:
with open('test.txt', 'r') as f:
    for line in f:       #make a for loop
        print(line, end='')
#this is efficient bc it goes through one line at a time from file

#for even more control over what yo're reading from file:
with open('test.txt', 'r') as f:
    f_contents = f.read(100) #first 100 characters of file printed, not all
    print(f_contents, end='')

    f_contents = f.read(100) #this would print out the next 100 characters
    print(f_contents, end='')

#loop that iterates over small chunks at a time
with open('test.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read) #kicks us back out of the while loop to check if we've hit end of file. if no more in file, it'll print empty string, and not meet the conditional, so it'll stop

with open('test.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*') #the asterisk would help identify the start/end of each chunk
        f_contents = f.read(size_to_read)

with open('test.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)
    print(f.tell())   #how many characters were read in

with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f_contents = f.read(size_to_read)  #picks up at the 10th position
    print(f_contents)

#if you want the second read to start back at beginning of file
with open('test.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f.seek(0) #sets position back to beginning of file. can also choose any position in file

    f_contents = f.read(size_to_read)
    print(f_contents)

with open('test.txt', 'r') as f:
    f.write('Test')  #error: not writable bc in read mode

with open('test2.txt', 'w') as f:  #if file doesn't exist, will create. if does exist, will overwrite it. be careful
    f.write('Test') 

with open('test2.txt', 'a') as f:  #if you don't want to overwrite existing file, use a (append)
    f.write('Test') 

with open('test2.txt', 'w') as f: 
    f.write('Test')
    f.write('Test')  #will append another "Test" backtoback, so "TestTest"

with open('test2.txt', 'w') as f: 
    f.write('Test')
    f.seek(0)
    f.write('Test')   #with seek, it'll overwrite Test. output: "Test"

with open('test2.txt', 'w') as f: 
    f.write('Test')
    f.seek(0)
    f.write('R')  #only overwrites first letter. basically only overwrites what it needs to. output: "Rest"

#go back to first test file
#working with multiple files
with open('test.txt', 'r') as rf: 
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)           #makes a copy of the test.txt file

with open('bronx.jpg', 'r') as rf:
    with open('bronx_copy.jpg', 'w') as wf:
        for line in rf:
            wf.write(line)   #will give error for images, not text

#for images, need to use binary mode
with open('bronx.jpg', 'rn') as rf:
    with open('bronx_copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)   #just need to add b to the read and write modes. it'll then copy the image w/o issues

#for more control of copying images, instead of doing line by line, use chunks
with open('bronx.jpg', 'rn') as rf:
    with open('bronx_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)  #so that it isn't an infinite loop
#same as for the text files, this will successfully make copy of image using chunks
