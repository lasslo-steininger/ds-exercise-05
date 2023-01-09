import matplotlib.pyplot as plt


def merge_sort(list):
    '''Recursively sorts a list in ascending order.'''
    # Base case: if the list is only one item or empty, it's already sorted
    if (len(list) > 1):
        # Split the list in half
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        # Sort the left and right halves
        merge_sort(left)
        merge_sort(right)

        # Merge the sorted halves
        l = 0
        r = 0
        i = 0

        # While both lists have items
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                list[i] = left[l]
                l += 1
            else:
                list[i] = right[r]
                r += 1
            i += 1

        # If the left list still has items, add them
        while l < len(left):
            list[i] = left[l]
            l += 1
            i += 1

        # If the right list still has items, add them
        while r < len(right):
            list[i] = right[r]
            r += 1
            i += 1


# Test the merge_sort function
# Create a list of unsorted numbers
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot the unsorted list
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()

# Sort the list
merge_sort(my_list)

# Plot the sorted list
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
