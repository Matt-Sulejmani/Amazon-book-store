# Imports
import json

# File Imports
import amazon

# Main Function

def main():
    running = True

    # Creating an instance of the amazon class
    amazonStore = amazon.Amazon("data.json")

    # Main application loop
    while running:
        print("Welcome to your online amazon store")
        print("Choose an action")
        print("1. Search book by title")
        print("2. Search book by author")
        print("3. Calculate your total")
        print("4. Close application")

        action = int(input("Enter your input: "))

        if action == 1:
            bookAuthor = input("Whose book are you loking for? ")

            booksByAuthor = amazonStore.searchByAuthor(amazonStore.data, bookAuthor)

            print(booksByAuthor[:2])
            isValidInput = False

            while not isValidInput:            
                userInput = input("Would you liek to add it to your wishlist? (y/n) ")

                if userInput == "y":
                    addToWishlist(amazonStore, bookAuthor)
                    isValidInput = True

                else:
                    print("Invalid input, try y/n")


        if action == 2:
            bookTitle = input("What book are you loking for? ")

            booksByTitle = amazonStore.searchByTitle(amazonStore.data, bookTitle)

            print(booksByTitle[0], "\n \n")

        if action == 3:
            # Adding something to the wishlist
            newBuyer = addToWishlist(amazonStore, "Sidrit", " ", booksByAuthor, booksByTitle)

            calculatePrice(newBuyer)

        if action == 4:
            running = False


def addToWishlist(store, authorName, bookTitle=None, booksByAuthor=None, booksByTitle=None):
    buyerName = input("Please enter your name: ")
    wishlist = {buyerName: []}
    
    # Adding the desired book to the buyer's wishlist
    for key in store.data:
        for name in store.data[key]["author"]:
            if authorName == name:
                wishlist[buyerName].append(store.data[key])

        break

    # Appending the new order to the existing list of orders
    with open("wishlist.json", "r+") as file:
        fileData = json.load(file)

        fileData['orders'].append(wishlist)
        file.seek(0)

        json.dump(fileData, file)

    return buyerName


def calculatePrice(buyerName):
    paymentTotal = 0

    with open("wishlist.json", "r") as file:
        data = json.load(file)

        # Finding the person's order and then adding up the price of all their purchases
        for order in data["orders"]:
            if buyerName in order:
                for bookPurchased in order[buyerName]:
                    paymentTotal += bookPurchased["price"]

    return paymentTotal

#! Code run

if __name__ == "__main__":
    main()