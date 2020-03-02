


input_string = input("Enter Tasks separated by coma ")
task_list  = input_string.split(",")
print("Printing all Task For Today")
for task in task_list:
    for i, task in enumerate(task_list,1):
       print(i, '. ' + task, sep='',end='i')

      