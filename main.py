from Smoker import Smoker

class Program(object):
    def __init__(self):
        self.smoker = Smoker()

    def run(self):
        while True:
            option = self.getOption()
            if option == "1":
                self.printStatistics()
            elif option == "2":
                count = int(input ("    How many packs you have bought? "))
                self.smoker.addPacksCount(count)
                self.printStatistics()
            elif option == "3":
                price = float (input ("    Input you cigarette price in drams "))
                nicotine = float (input ("    Input you cigarette nicotine in milligrams "))
                self.smoker.addCiggaretType(price,nicotine)
            elif option == "4":
                answer = input("If you want to input paremeters of the cigarette you are smoking type 'add', otherwhise the program will close itself: ")
                self.smoker.deleteData()
                if answer != "add":
                    exit()
                self.smoker.createNewSmokerProfile()
            elif option == "5":
                exit()
            else:
                print ("Wrong input please enter 1, 2, 3 or 4")

    def printStatistics(self):
        (total_money,total_nicotine,total_packs_count) = self.smoker.getTotalStatistics()
        print ("\nYou have smoked " + str(total_packs_count * 20) + " cigarettes, which contained total of " + str(total_nicotine) + " milligrams of nicotine and spent " + str(total_money) + " AMD on that.")


    def getOption(self):
        print("\nHi "+self.smoker.getName())
        print("\nplease select one of the following")
        print("1 - Get statistics.\n2 - Add count of packs you bought.\n3 - Change the type of cigarettes you somke.\n4 - Delete current data.\n5 - Exit\n")
        return input("Type here option you want -> ")

if __name__ == "__main__":
    program = Program()
    program.run()

    #I need to open Json file then to read it, use the integers in Name which is in Json, but I couldn't do it.
    # I had to use those integers to construct binary search tree, and as there cannot be the same integers, so my worke becomes easier to implement
#I know the theoretical part but I didn't manage to practice as much as I needed
# So I Put the values by hand) Task is accomplished but not as it was needed


