def menu():
    print("===== To-Do-List =====")
    user_task_store = dict()
    while True:
        user_action = int(
            input("1.Input Task\n2.Show Task\n3.Mark done\n4.exit"))

        match user_action:
            case 1:
                user_numtask = int(input("Enter number of Tasks"))
                for rep in range(user_numtask):
                    user_task = input("Enter your Task"+str(rep+1))
                    user_task_store[user_task] = "Undone"
            case 2:
                print("S.N\tTask\tMark\n")
                for id, user_task in enumerate(user_task_store):
                    print(
                        f"{id+1}\t{user_task}\t{user_task_store[user_task]}\n")
            case 3:
                user_donetask = int(
                    input("Enter your done work from 1 to "+str(len(user_task_store))))
                for id, user_task in enumerate(user_task_store):
                    if user_donetask == id+1:
                        user_task_store[user_task] = "Done"
            case 4:
                return 0
            case _:
                print("Invalid Entry")


menu()
