documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
}


def get_name():
  pass_num = input("Введите номер документа человека, имя которого хотите узнать ")
  for passes in documents:
    if pass_num == passes["number"]:
      return passes["name"]
  else:
    return "Такого человека нет в базе"

def get_num_shelf():
  pass_num = input("Введите номер документа человека для доступа к информации о расположении документа в архиве ")
  for keys, values in directories.items():
    if pass_num in values:
      return keys
  else:
    return "Вы ввели некорректные данные документа"

def get_docs_as_list():
  for passes in documents:
    type_ = passes["type"]
    number_ = passes["number"]
    name_ = passes["name"]
    print(type_, number_, name_)

def add_docs_on_shelf():
  user_type = input("Введите тип документа ")
  user_pass = input("Введите номер документа ")
  user_name = input("Введите Ваше имя ")
  shelf_num = input("Введите номер полки ")
  if shelf_num not in directories.keys():
    print("Вы не можете добавить документ на эту полку")
  else:
    form = {"type": user_type , "number": user_pass, "name": user_name}
    form["type"] = user_type
    form["number"] = user_pass
    form["name"] = user_name
    directories[shelf_num].append(form["number"])
    documents.append(form)
    return directories, documents

def delete_doc():
  pass_num = input("Введите номер документа, который хотите удалить ")
  for passes in documents:
    if pass_num in passes.values():
      documents.remove(passes)
      for passes in directories.items():
        if pass_num in passes[1]:
          a = passes[1].index(pass_num)
          del directories[passes[0]][a]
          return documents, directories
  else:
    return "Такого человека нет в базе"

def add_shelf():
  shelf_num = input("Введите номер полки, которую хотите добавить ")
  for keys in directories.keys():
    if shelf_num not in directories.keys():
      directories.setdefault(shelf_num, [])
      return directories
    else:
      return "Такая полка уже существует!"

def move_to_shelf():
  shelf_num = input("Введите номер полки, на которую хотите переместить документ ")
  if shelf_num not in directories.keys():
    return "Такой полки нет"
  else:
    pass_num = input("Введите номер документа, который хотите переместить ")
    for passes in directories.items(): #(('1', []), ('2', []) ...)
      if pass_num in passes[1]:
        directories[shelf_num].append(pass_num)
        a = passes[1].index(pass_num)
        del directories[passes[0]][a]
        break
    return directories

def commands(docs, dirs):
  while True:
    command = input("Введите команду ")
    if command == "p":
      print(get_name())
    elif command == "s":
      print(get_num_shelf())
    elif command == "l":
      print(get_docs_as_list())
    elif command == "a":
      print(add_docs_on_shelf())
    elif command == "d":
      print(delete_doc())
    elif command == "as":
      print(add_shelf())
    elif command == "m":
      print(move_to_shelf())
commands(documents, directories)