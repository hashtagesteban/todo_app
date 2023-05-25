while True:
  user_action = input("Type add, show, edit, complete or exit: ")
  user_action = user_action.strip()

  match user_action:
    case 'add':
      todo = input("Enter a to do: ") + "\n"

      with open('todos.txt', 'r') as file:
        todos = file.readlines()
      
      todos.append(todo)

      with open('todos.txt', 'w') as file:
        file.writelines(todos)

    case 'show':
      with open('todos.txt', 'r')as file:
        todos = file.readlines()
        
      for index, item in enumerate(todos):
        item = item.strip('\n')
        row = f"{index + 1}-{item}"
        print(row)

    case 'edit':
      number = int(input("Number of the todo to edit: "))
      number= number - 1

      with open('todos.txt', 'r') as file:
        todos = file.readlines()
        
      print("Here is to do's existing: ", todos)
        
      new_todo = input('Enter new to do:')
      todos[number] = new_todo + '\n'

      print("Here's how it will be", todos)

      with open('todos.txt', 'w') as file:
        file.writelines(todos)

    case 'complete':
      number = int(input("Number of the todo to complete: "))
      number = number -1
      todos.pop(number)

    case 'exit':
      break

print('Bye')