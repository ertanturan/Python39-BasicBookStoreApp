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

from Bookstore.BackEnd import DatabaseOperations

databaseOp = DatabaseOperations("Bookstore\\books.db")


class BookStoreWindow(object):

    def __init__(self,window):
        self.labelTitle = Label(window, text="Title")
        self.labelTitle.grid(row=0, column=0)

        self.labelAuthor = Label(window, text="Author")
        self.labelAuthor.grid(row=0, column=2)

        self.labelYear = Label(window, text="Year")
        self.labelYear.grid(row=1, column=0)

        self.labelISBN = Label(window, text="ISBN")
        self.labelISBN.grid(row=1, column=2)

        self.title_text = StringVar()
        self.titleEntry = Entry(window, textvariable=self.title_text)
        self.titleEntry.grid(row=0, column=1)

        self.author_text = StringVar()
        self.authorEntry = Entry(window, textvariable=self.author_text)
        self.authorEntry.grid(row=0, column=3)

        self.year_text = StringVar()
        self.yearEntry = Entry(window, textvariable=self.year_text)
        self.yearEntry.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.isbnEntry = Entry(window, textvariable=self.isbn_text)
        self.isbnEntry.grid(row=1, column=3)

        self.listOne = Listbox(window, height=6, width=35)
        self.listOne.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.listOne.bind('<<ListboxSelect>>', self.get_selected_row)

        self.scrollBarOne = Scrollbar(window)
        self.scrollBarOne.grid(row=2, column=2, rowspan=6)

        self.listOne.configure(yscrollcommand=self.scrollBarOne.set)
        self.scrollBarOne.configure(command=self.listOne.yview)

        viewAllButton = Button(window, text="View All", width=12, command=self.view_command)
        viewAllButton.grid(row=2, column=3)

        searchEntryButton = Button(window, text="Search Entry", width=12, command=self.search_command)
        searchEntryButton.grid(row=3, column=3)

        addEntryButton = Button(window, text="Add Entry", width=12, command=self.insert_command)
        addEntryButton.grid(row=4, column=3)

        updateSelectedButton = Button(window, text="Update Selected", width=12, command=self.update_command)
        updateSelectedButton.grid(row=5, column=3)

        deleteSelectedButton = Button(window, text="Delete Selected", width=12, command=self.delete_command)
        deleteSelectedButton.grid(row=6, column=3)

        closeButton = Button(window, text="Close", width=12, command=window.destroy)
        closeButton.grid(row=7, column=3)


    def view_command(self):
        self.listOne.delete('0', END)
        for row in databaseOp.view():
            self.listOne.insert(END, row)

    def insert_command(self):
        databaseOp.insert(self.title_text.get(), self.author_text.get(),
                          self.year_text.get(), self.isbn_text.get())

    def search_command(self):
        self.listOne.delete('0', END)
        values = databaseOp.search(self.title_text.get(), self.author_text.get(),
                                   self.year_text.get(), self.isbn_text.get())
        for value in values:
            listOne.insert(END, value)

    def get_selected_row(self,event):
        global selectedTuple
        try:

            index = self.listOne.curselection()[0]
            selectedTuple = self.listOne.get(index)

            self.titleEntry.delete(0, END)
            self.authorEntry.delete(0, END)
            self.yearEntry.delete(0, END)
            self.isbnEntry.delete(0, END)

            self.titleEntry.insert(END, selectedTuple[1])
            self.authorEntry.insert(END, selectedTuple[2])
            self.yearEntry.insert(END, selectedTuple[3])
            self.isbnEntry.insert(END, selectedTuple[4])
        except IndexError:
            pass

    def delete_command(self):
        databaseOp.delete(selectedTuple[0])

    def update_command(self):
        print("update")
        databaseOp.update(selectedTuple[0],
                          self.title_text.get(),
                          self.author_text.get(),
                          self.year_text.get(),
                          self.isbn_text.get())





window = Tk()
window.wm_title("BookStore")

BookStoreWindow(window)
window.mainloop()
