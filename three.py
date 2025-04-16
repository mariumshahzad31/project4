# 01 Write a function that takes a list of numbers and returns the sum of those numbers.
def sum_of_numbers(numbers):
    return sum(numbers)

# 02 Write a program that doubles each element in a list of numbers.
def double_elements(numbers):
    return [x * 2 for x in numbers]

# 03 Implement an 'eraser' on a canvas (in a conceptual form as there is no GUI implementation here).
def eraser_on_canvas(canvas, eraser_rect):
    for i in range(len(canvas)):
        for j in range(len(canvas[i])):
            if (i >= eraser_rect[0] and i < eraser_rect[2] and
                j >= eraser_rect[1] and j < eraser_rect[3]):
                canvas[i][j] = 'white'  # Set the cell to white
    return canvas

# 04 Immutable vs Mutable data types: Adding three copies of data to a list.
def add_three_copies(lst, data):
    lst.extend([data, data, data])

# 05 Get first element of the list.
def get_first_element(lst):
    print(lst[0])

# 06 Get last element of the list.
def get_last_element(lst):
    print(lst[-1])

# 07 Continuously ask the user to enter values and store them in a list.
def user_input_list():
    user_list = []
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)
    print("Here's the list:", user_list)

# 08 Shorten the list to a maximum length and remove elements from the end.
MAX_LENGTH = 3
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print(f"Removed: {removed_element}")
    print(f"List after shortening: {lst}")

# Main function to run the examples
def main():
    # 01 Example
    print("Sum of numbers:", sum_of_numbers([1, 2, 3, 4]))

    # 02 Example
    print("Doubled elements:", double_elements([1, 2, 3, 4]))

    # 03 Example - Canvas Eraser
    canvas = [['blue' for _ in range(5)] for _ in range(5)]
    eraser_rect = [1, 1, 4, 4]  # Eraser coordinates (start_x, start_y, end_x, end_y)
    new_canvas = eraser_on_canvas(canvas, eraser_rect)
    print("Canvas after eraser:", new_canvas)

    # 04 Example - Add three copies
    lst = []
    add_three_copies(lst, "Hello world!")
    print("List after adding three copies:", lst)

    # 05 Example - First element
    get_first_element([1, 2, 3, 4])

    # 06 Example - Last element
    get_last_element([1, 2, 3, 4])

    # 07 Example - User input list
    user_input_list()

    # 08 Example - Shorten list
    shorten([1, 2, 3, 4, 5])

if __name__ == "__main__":
    main()
