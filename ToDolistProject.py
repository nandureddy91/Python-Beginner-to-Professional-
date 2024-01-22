Todos=[]
while True:
    user_Text = input("choose and type add or delete or show or  exit:")
    match user_Text:
        case "add":
            Todo= input("enter the todo:")
            Todo.title()
            Todos.append(Todo)
        case "show"|"display":
            for item in Todos:
                item=item.title()
                print(item)
        case "delete"|"remove":
            print("Which todo do you want to delete")
            for index, element in enumerate(Todos, start=0):
                print(f"{index}. {element}".title())
            user_delete=int(input("enter the number of the todo you want to delete: \n"))
            if 0<user_delete<len(Todos):
                delete_Todo=Todos.pop(user_delete)
            else:
                print("You have chosen the wrong selection there is nothing to delete")
            
        case "exit":
            print("The Todo List is:")
            break    
print(Todos)


