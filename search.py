start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

n1 = input("Enter the first part (e.g: 'prog' in 'prog1.c'): ")
n2 = input("Enter the second part (e.g: '.c' in 'prog30.c'): ")

words = input("Enter the possible words present in your file (seperated by a space): ")
w_list = words.split()

i = start
files = []

while(i<=end):
    fname = n1+str(i)+n2
    try:
        handler = open(fname)
        score = 0
        for line in handler:
            for w in w_list:
                if w.lower() in line.lower():
                    score+=1
        if score>0:
            files.append(fname)
        i+=1
    except:
        i+=1
        print(f"File not found, trying the next one: ({n1}{str(i)}{n2})")

print("Here are the files you might be looking for:")
for f in files:
    print(f)
