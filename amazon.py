import json


class Amazon(object):
    def __init__(self, file):
        self.isAvailable = False

        with open(file, "r+") as dataFile:

            # Loading the data from the Json file in to a python dict
            self.data = json.loads(dataFile.read())

    def searchByAuthor(self, data, reqAuthor):
        booksByAuthor = []

        # Goingover each item in the dictionary
        for key in data:

            # Going over each author in every item in the dictionary
            for name in data[key]["author"]:

                # If we found the book by the author 
                if name == reqAuthor:
                    booksByAuthor.append(data[key]["title"])

        # Checking to see if the list is empty
        # Returning the list of books available by the author
        if booksByAuthor:
            self.isAvailable = True
            return "Books by your author: ", booksByAuthor, self.isAvailable
        
        # Default return 
        return "Books by your requested author could not be found", self.isAvailable

    def searchByTitle(self, data, nameOfBook):
        booksWithTitle = []

        # Goingover each item in the dictionary
        for key in data:
            if nameOfBook == data[key]["title"]:
                booksWithTitle.append(data[key])

        # Checking to see if the list is empty
        # Returning the list of books available by the author
        if booksWithTitle:
            self.isAvailable = True
            return booksWithTitle , self.isAvailable
        
        # Default return 
        return "Books by your requested title could not be found", self.isAvailable
        