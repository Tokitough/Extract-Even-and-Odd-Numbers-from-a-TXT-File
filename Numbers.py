# Read a text file
with open("numbers.txt" , "r") as my_file:
    # Create two other text files for odd and even numbers
    with open("odd.txt" , "w") as odd_file , open("even.txt" , "w") as even_file:
        for line in my_file:
            integer = int(line.strip())
            