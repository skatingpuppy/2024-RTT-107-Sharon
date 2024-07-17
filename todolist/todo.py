# module required
import sys
import datetime

# help function
#used to provide the way how a user can use the todo list. Is like the documentation of todo application. 
def help():
    sa = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))


# function to add item in todo list
def add(s):
   
    f = open('todo.txt', 'a')
    f.write(s)
    f.write("\n")
    f.close()
    s = '"'+s+'"'
    print(f"Added todo: {s}")


# Function to print the todo list items
def ls():
   
    try:
 
        nec()
        l = len(d)
        k = l
 
        for i in d:
            sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            l = l-1
 
    except Exception as e:
        raise e
    
# Function to Complete a todo
def done(no):
    try:
 
        nec()
        no = int(no)
        f = open('done.txt', 'a')
        st = 'x '+str(datetime.datetime.today()).split()[0]+' '+d[no]
         
        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked todo #{no} as done.")
         
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
             
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: todo #{no} does not exist.")



# Function to show report/statistics of todo list
def report():
    nec()
    try:
 
        nf = open('done.txt', 'r')
        c = 1
         
        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c = c+1
        print(
            f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')
     
    except:
        print(
            f'{str(datetime.datetime.today()).split()[0]} Pending : {len(d)} Completed : {len(don)}')
        

# Function to delete an item from todo list
def deL(no):
    try:
        no = int(no)
        nec()
 
        # utility function defined in main
        with open("todo.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
             
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
        print(f"Deleted todo #{no}")
 
    except Exception as e:
       
        print(f"Error: todo #{no} does not exist. Nothing deleted.")


# Main function and utility function
def nec():
 
  # utility function used in done and report function
    try:
        f = open('todo.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c+1
    except:
        sys.stdout.buffer.write("There are no pending todos!".encode('utf8'))
 
#main program
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv
         
        if(args[1] == 'del'):
            args[1] = 'deL'
             
        if(args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing todo string. Nothing added!".encode('utf8'))
 
        elif(args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking todo as done.".encode('utf8'))
 
        elif(args[1] == 'deL' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting todo.".encode('utf8'))
        else:
            globals()[args[1]](*args[2:])
 
    except Exception as e:
 
        s = """Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
        sys.stdout.buffer.write(s.encode('utf8'))