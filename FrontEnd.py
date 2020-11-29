""" A program that stores this book information:
    Title
    Author
    Year
    ISBN
User can:
    Wiel all records
    Search an entry
    Add entry
    Update entry
    Delete
    Close
    """

from tkinter import *

from BackEnd import DatabaseOperations

databaseOp = DatabaseOperations("books.db")


def view_command():
    listOne.delete('0', END)
    for row in databaseOp.view():
        listOne.insert(END, row)


def insert_command():
    databaseOp.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def search_command():
    listOne.delete('0', END)
    values = databaseOp.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    for value in values:
        listOne.insert(END, value)


def get_selected_row(event):
    global selectedTuple
    try:

        index = listOne.curselection()[0]
        selectedTuple = listOne.get(index)

        titleEntry.delete(0, END)
        authorEntry.delete(0, END)
        yearEntry.delete(0, END)
        isbnEntry.delete(0, END)

        titleEntry.insert(END, selectedTuple[1])
        authorEntry.insert(END, selectedTuple[2])
        yearEntry.insert(END, selectedTuple[3])
        isbnEntry.insert(END, selectedTuple[4])
    except IndexError:
        pass


def delete_command():
    databaseOp.delete(selectedTuple[0])


def update_command():
    print("update")
    databaseOp.update(selectedTuple[0],
                      title_text.get(),
                      author_text.get(),
                      year_text.get(),
                      isbn_text.get())


window = Tk()

window.wm_title("BookStore")

labelTitle = Label(window, text="Title")
labelTitle.grid(row=0, column=0)

labelAuthor = Label(window, text="Author")
labelAuthor.grid(row=0, column=2)

labelYear = Label(window, text="Year")
labelYear.grid(row=1, column=0)

labelISBN = Label(window, text="ISBN")
labelISBN.grid(row=1, column=2)

title_text = StringVar()
titleEntry = Entry(window, textvariable=title_text)
titleEntry.grid(row=0, column=1)

author_text = StringVar()
authorEntry = Entry(window, textvariable=author_text)
authorEntry.grid(row=0, column=3)

year_text = StringVar()
yearEntry = Entry(window, textvariable=year_text)
yearEntry.grid(row=1, column=1)

isbn_text = StringVar()
isbnEntry = Entry(window, textvariable=isbn_text)
isbnEntry.grid(row=1, column=3)

listOne = Listbox(window, height=6, width=35)
listOne.grid(row=2, column=0, rowspan=6, columnspan=2)

listOne.bind('<<ListboxSelect>>', get_selected_row)

scrollBarOne = Scrollbar(window)
scrollBarOne.grid(row=2, column=2, rowspan=6)

listOne.configure(yscrollcommand=scrollBarOne.set)
scrollBarOne.configure(command=listOne.yview)

viewAllButton = Button(window, text="View All", width=12, command=view_command)
viewAllButton.grid(row=2, column=3)

searchEntryButton = Button(window, text="Search Entry", width=12, command=search_command)
searchEntryButton.grid(row=3, column=3)

addEntryButton = Button(window, text="Add Entry", width=12, command=insert_command)
addEntryButton.grid(row=4, column=3)

updateSelectedButton = Button(window, text="Update Selected", width=12, command=update_command)
updateSelectedButton.grid(row=5, column=3)

deleteSelectedButton = Button(window, text="Delete Selected", width=12, command=delete_command)
deleteSelectedButton.grid(row=6, column=3)

closeButton = Button(window, text="Close", width=12, command=window.destroy)
closeButton.grid(row=7, column=3)

window.mainloop()
