#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_zero_sum(head):
    # Create a dummy node to handle edge cases
    dummy = Node(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sum_map = {}
    current = dummy

    while current:
        prefix_sum += current.data

        if prefix_sum in prefix_sum_map:
            # Remove elements between prefix_sum_map[prefix_sum] and current
            prev = prefix_sum_map[prefix_sum].next
            temp_sum = prefix_sum + prev.data

            while prev != current:
                del prefix_sum_map[temp_sum]
                prev = prev.next
                temp_sum += prev.data

            prefix_sum_map[prefix_sum].next = current.next
        else:
            prefix_sum_map[prefix_sum] = current

        current = current.next

    return dummy.next


# In[2]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list_in_groups(head, k):
    current = head
    next = None
    prev = None
    count = 0

    # Reverse first k nodes of the linked list
    while current and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    # Recursively call for the remaining list
    if next is not None:
        head.next = reverse_linked_list_in_groups(next, k)

    # prev is the new head of the reversed list
    return prev


# In[3]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_alternate(head1, head2):
    if head1 is None:
        return head2

    if head2 is None:
        return head1

    current1 = head1
    current2 = head2

    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        current2.next = next1

        current1 = next1
        current2 = next2

    return head1


# In[4]:


def count_pairs_with_sum(arr, target):
    count = 0
    complement_map = {}

    for num in arr:
        complement = target - num
        if complement in complement_map:
            count += complement_map[complement]

        if num in complement_map:
            complement_map[num] += 1
        else:
            complement_map[num] = 1

    return count


# In[5]:


def find_duplicates(arr):
    duplicates = []
    num_map = {}

    for num in arr:
        if num in num_map:
            duplicates.append(num)
        else:
            num_map[num] = 1

    return duplicates


# In[6]:


import heapq

def find_kth_largest_smallest(arr, k):
    kth_largest = heapq.nlargest(k, arr)[-1]
    kth_smallest = heapq.nsmallest(k, arr)[-1]
    return kth_largest, kth_smallest


# In[7]:


def move_negatives(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0 and arr[right] >= 0:
            right -= 1
        else:
            left += 1
            right -= 1

    return arr


# In[8]:


def reverse_string(string):
    stack = []
    for char in string:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# In[9]:


def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for char in expression:
        if char not in operators:
            stack.append(int(char))
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if char == '+':
                result = num1 + num2
            elif char == '-':
                result = num1 - num2
            elif char == '*':
                result = num1 * num2
            elif char == '/':
                result = num1 / num2

            stack.append(result)

    return stack.pop()


# In[10]:


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()

        return None

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0


# In[ ]:




