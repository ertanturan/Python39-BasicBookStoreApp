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

import BackEnd


def view_command():
    listOne.delete('0', END)
    for row in BackEnd.view():
        listOne.insert(END, row)

def insert_command():
    BackEnd.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


def search_command():
    listOne.delete('0', END)
    values = BackEnd.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    for value in values:
        listOne.insert(END, value)


def get_selected_row(event):
    index = listOne.curselection()[0]
    selectedTuple = listOne.get(index)
    return selectedTuple


def delete_command():
    BackEnd.delete(get_selected_row()[0])

window = Tk()

labelTitle = Label(window, text="Title")
labelTitle.grid(row=0, column=0)

labelAuthor = Label(window, text="Author")
labelAuthor.grid(row=0, column=2)

labelYear = Label(window, text="Year")
labelYear.grid(row=1, column=0)

labelISBN = Label(window, text="ISBN")
labelISBN.grid(row=1, column=2)

title_text = StringVar()
entryOne = Entry(window, textvariable=title_text)
entryOne.grid(row=0, column=1)

author_text = StringVar()
entryOne = Entry(window, textvariable=author_text)
entryOne.grid(row=0, column=3)

year_text = StringVar()
entryOne = Entry(window, textvariable=year_text)
entryOne.grid(row=1, column=1)

isbn_text = StringVar()
entryOne = Entry(window, textvariable=isbn_text)
entryOne.grid(row=1, column=3)

listOne = Listbox(window, height=6, width=35)
listOne.grid(row=2, column=0, rowspan=6, columnspan=2)

listOne.bind('<<ListboxSelect>>',get_selected_row)

scrollBarOne = Scrollbar(window)
scrollBarOne.grid(row=2, column=2, rowspan=6)

listOne.configure(yscrollcommand=scrollBarOne.set)
scrollBarOne.configure(command=listOne.yview)

viewAllButton = Button(window, text="View All", width=12, command=view_command)
viewAllButton.grid(row=2, column=3)

searchEntryButton = Button(window, text="Search Entry", width=12,command = search_command)
searchEntryButton.grid(row=3, column=3)

addEntryButton = Button(window, text="Add Entry", width=12,command=insert_command)
addEntryButton.grid(row=4, column=3)

updateSelectedButton = Button(window, text="Update Selected", width=12)
updateSelectedButton.grid(row=5, column=3)

deleteSelectedButton = Button(window, text="Delete Selected", width=12 , command = delete_command)
deleteSelectedButton.grid(row=6, column=3)

closeButton = Button(window, text="Close", width=12)
closeButton.grid(row=7, column=3)

window.mainloop()
