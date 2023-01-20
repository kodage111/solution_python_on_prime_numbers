from my_defined_functions import primeNumbers

def writeToFile(nameFile, data):
    try:
        with open(nameFile, "a") as file:
            file.write("Prime Numbers\n\n")
            number_cells = 0
            for element in data:
                file.write(f"{ str(element)}")
                if(number_cells == 4):
                    file.write("\n")
                    number_cells = 0
                else:
                    file.write(",")
                    number_cells+=1
            file.write("\n\n")
            file.close()
        return True
    except Exception as e:
        print(f"❌ {e.__str__()}")
        return False

if __name__ == "__main__":

    if((writeToFile("primeNumbers.txt", primeNumbers(250)))):
        print("Writting to the file was successful 👍")

