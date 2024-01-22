Todos=[]
while True:
    user_Text = input("choose and type add or delete or show or  exit:")
    match user_Text:
        case "add":
            Todo= input("enter the todo:")
            Todos.append(Todo)
        case "show":
            for item in Todos:
                print(item)
        case "delete":
            print("Which todo do you want to delete")
            for index, element in enumerate(Todos, start=0):
                print(f"{index}. {element}")
            user_delete=int(input("enter the number of the todo you want to delete: \n"))
            if 0<user_delete<len(Todos):
                delete_Todo=Todos.pop(user_delete)
            else:
                print("You have chosen the wrong selection")
            
        case "exit":
            print("The Todo List is:")
            break    
print(Todos)


