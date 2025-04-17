# Taka a task
tasks = input("Enter a task: ")

# Write a task
with open("task_sever", "a") as file:
    file.write(tasks + '\n')

    print(tasks)
    print("Task saved!")

    print("All saved tasks:")
    with open("task_sever", "r") as file:
        all_tasks = file.read()
        print(all_tasks)


