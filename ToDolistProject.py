Todos=[]
while True:
    user_Text = input("choose and type add or delete or exit:")
    match user_Text:
        case "add":
            Todo= input("enter the todo:")
            Todos.append(Todo)
            print(Todos)
        case "delete":
            Todo=Todos.pop()
        case "exit":
            print("the todo list is:")
            break    
print(Todos)


