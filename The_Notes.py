import json
import os
import datetime

def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена.")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст: ")
            note["title"] = new_title
            note["body"] = new_body
            note["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена.")
            return
    print("Заметка с указанным ID не найдена.")

def list_notes():
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Время создания: {note['timestamp']}")
            print(f"Текст: {note['body']}")
            print("----------------------------")

notes = load_notes()

while True:
    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Просмотреть заметки")
    print("5. Выход")
    choice = input("Введите номер действия: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        edit_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        list_notes()
    elif choice == "5":
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите существующее действие.")