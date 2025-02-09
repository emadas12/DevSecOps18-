def task1():
    def print_divisors(num):
        if num <= 0:
            print("enter a positive number.")
            return

        print(f"Divisors of {num}:")
        for i in range(1, num + 1):
            if num % i == 0:
                print(i, end=" ")

    number = int(input("Enter a number: "))
    print_divisors(number)


def task2():
    def sum_and_average():
        numbers = []
        count = 0

        while True:
            num = float(input(f"enter number #{count + 1}: "))
            if num < 0:
                print("Thank you. Goodbye.")
                break

            numbers.append(num)
            count += 1
            current_sum = sum(numbers)
            current_avg = current_sum / count

            print(f"enter number #{count + 1} (avg={current_avg:.2f}, Sum={current_sum}): ")

    sum_and_average()


def task3():
    def word_twice():
        words = set()

        while True:
            word = input("please type a word: ").strip().lower()
            if word in words:
                print(f"You entered the word '{word}' twice. Good bye...")
                break
            words.add(word)

    word_twice()


def task4():
    def compare_lists(list1, list2):
        if len(list1) != len(list2):
            print("Lists must be same length.")
            return

        count1 = 0
        count2 = 0

        for i in range(len(list1)):
            if list1[i] > list2[i]:
                count1 += 1
            elif list2[i] > list1[i]:
                count2 += 1

        if count1 > count2:
            print("List 1 has more larger numbers.")
        elif count2 > count1:
            print("List 2 has more larger numbers.")
        else:
            print("Both lists have the same number of larger numbers.")

    def input_list(list_name):
        lst = []
        print(f"Enter numbers for {list_name}. Type 'done' to finish.")
        while True:
            num = input(f"Enter a number for {list_name}: ")
            if num.lower() == 'done':
                break
            try:
                lst.append(int(num))
            except ValueError:
                print("Invalid input. Please enter a number or 'done' to finish.")
        return lst

    # Input lists from the user
    list1 = input_list("List 1")
    list2 = input_list("List 2")

    # Compare the lists
    compare_lists(list1, list2)


def main():
    while True:
        print("\n- Homework 1 -")
        print("1. Task 1: Print all divisors of a number")
        print("2. Task 2: Sum and average of numbers until a negative number is entered")
        print("3. Task 3: Stop when a word is entered twice")
        print("4. Task 4: Compare two lists and count larger numbers")
        print("5. Exit")

        choice = input("Enter the task number to run (1-5): ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()