import random
import os
import time

# Generate a list of unique numbers with random indentation
bars = []
while len(bars) < 10:  # nummber of elements (bars)
    num = random.randint(0, 100)
    if bars.__contains__(num):
        continue
    else:
        bars.append(" " * num + str(num))

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# if shell sorting take x sec, then 
# shell_sort_in     : x
# quick_sort_in     : 2x +
# merge_sort_in     : 2.5x - 3x
# insertion_sort_in : 3.5x - 5x
# selection_sort_in : 8x - 10x
# bubble_sort_in    : 18x - 20x

def bubble_sorting(bars: list, Time: float =  0.01):
    n = len(bars)
    for _ in range(n):
        for i in range(n - 1):
            clear_screen()
            if bars[i] > bars[i + 1]:
                bars[i], bars[i + 1] = bars[i + 1], bars[i]
                for k in range(n):
                    if k == i:
                        print("\033[48;2;255;100;0m" + bars[k] + "\033[0m")
                    elif k == i + 1:
                        print("\033[48;2;255;0;0m" + bars[k] + "\033[0m")
                    else:
                        print("\033[46m" + bars[k] + "\033[0m")
            else:
                for k in range(n):
                    if k == i:
                        print("\033[48;2;100;255;0m" + bars[k] + "\033[0m")
                    elif k == i + 1:
                        print("\033[48;2;0;225;100m" + bars[k] + "\033[0m")
                    else:
                        print("\033[46m" + bars[k] + "\033[0m")
            time.sleep(Time)
    clear_screen()
    for bar in bars:
        print("\033[46m" + bar + "\033[0m")

def selection_sorting(bars: list, Time: float = 0.01):
    n = len(bars)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            clear_screen()
            if bars[j] < bars[min_index]:
                min_index = j
        
                for k in range(n):
                    if k == min_index:
                        print("\033[48;2;225;200;0m" + bars[min_index] + "\033[0m")
                    elif k == i:
                        print("\033[48;2;225;10;0m" + bars[k] + "\033[0m")
                    else:
                        print("\033[46m" + bars[k] + "\033[0m")
                time.sleep(Time/2)
            else:
                for k in range(n):
                    if k == i:
                        print("\033[48;2;225;200;0m" + bars[min_index] + "\033[0m")
                    elif k == i + 1:
                        print("\033[48;2;0;225;60m" + bars[k] + "\033[0m")
                    else:
                        print("\033[46m" + bars[k] + "\033[0m")
            
        

        bars[i], bars[min_index] = bars[min_index], bars[i]
        clear_screen()
        for bar in bars:
            print("\033[46m" + bar + "\033[0m")
        time.sleep(Time/2)
    
    clear_screen()
    for bar in bars:
        print("\033[46m" + bar + "\033[0m")

def insertion_sorting(bars: list, Time: float =  0.01):
    n = len(bars)
    for i in range(1, n):
        key = bars[i]
        j = i - 1
        while j >= 0 and bars[j] > key:
            clear_screen()
            bars[j + 1] = bars[j]
            for k in range(n):
                if k == j :
                    print("\033[48;2;225;20;0m" + bars[k] + "\033[0m")
                elif k == j + 1:
                    print("\033[48;2;225;10;10m" + bars[k] + "\033[0m")
                else:
                    print("\033[46m" + bars[k] + "\033[0m")
            j -= 1
            time.sleep(Time)
        bars[j + 1] = key
        clear_screen()
        for bar in bars:
            print("\033[46m" + bar + "\033[0m")
    clear_screen()
    for bar in bars:
        print("\033[46m" + bar + "\033[0m")

def merge_sorting(bars: list, Time: float =  0.01):
    def merge_sort(bars, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort(bars, l, m)
            merge_sort(bars, m + 1, r)
            merge(bars, l, m, r)

    def merge(bars, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = bars[l:m + 1]
        R = bars[m + 1:r + 1]

        i = j = 0
        k = l
        while i < n1 and j < n2:
            clear_screen()
            if L[i] <= R[j]:
                bars[k] = L[i]
                i += 1
                for x in range(len(bars)):
                    if l <= x <= r:
                        print("\033[48;2;225;10;0m" + bars[x] + "\033[0m")
                    else:
                        print("\033[46m" + bars[x] + "\033[0m") 
            else:
                bars[k] = R[j]
                j += 1
            k += 1
            clear_screen()
            for x in range(len(bars)):
                if l <= x <= r:
                    print("\033[48;2;255;10;0m" + bars[x] + "\033[0m")
                else:
                    print("\033[46m" + bars[x] + "\033[0m")
            time.sleep(Time)
        while i < n1:
            bars[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            bars[k] = R[j]
            j += 1
            k += 1

    merge_sort(bars, 0, len(bars) - 1)
    clear_screen()
    for bar in bars:
        print("\033[46m" + bar + "\033[0m")

def quick_sorting(bars: list, Time: float = 0.01):
    def quick_sort(bars, low, high):
        if low < high:
            pi = partition(bars, low, high)
            quick_sort(bars, low, pi - 1)
            quick_sort(bars, pi + 1, high)

    def partition(bars, low, high):
        pivot = bars[high]
        i = low - 1
        for j in range(low, high):
            clear_screen()
            if bars[j] < pivot:
                i += 1
                bars[i], bars[j] = bars[j], bars[i]
                for k in range(len(bars)):
                    if k == i or k == j:
                        print("\033[48;2;255;0;0m" + bars[k] + "\033[0m")
                    elif k == high:
                        print("\033[48;2;255;100;0m" + bars[k] + "\033[0m")
                    else:
                        print("\033[46m" + bars[k] + "\033[0m")
            else:
                for k in range(len(bars)):
                    if k == i or k == j:
                        print("\033[48;2;255;0;0m" + bars[k] + "\033[0m")
                    elif k == high:
                        print("\033[48;2;255;100;0m" + bars[k] + "\033[0m")
                    else:
                        print("\033[46m" + bars[k] + "\033[0m")
            time.sleep(Time)
        bars[i + 1], bars[high] = bars[high], bars[i + 1]
        return i + 1

    quick_sort(bars, 0, len(bars) - 1)
    clear_screen()
    for bar in bars:
        print("\033[46m" + bar + "\033[0m")

def shell_sorting(bars: list, Time: float = 0.01):
    n = len(bars)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = bars[i]
            j = i
            while j >= gap and bars[j - gap] > temp:
                clear_screen()
                bars[j] = bars[j - gap]
                j -= gap
                for k in range(n):
                    if k == j or k == j + gap:
                        print("\033[48;2;255;0;0m" + bars[k] + "\033[0m")
                    else:
                        print("\033[46m" + bars[k] + "\033[0m")
                time.sleep(Time)
            bars[j] = temp
        gap //= 2
    clear_screen()
    for bar in bars:
        print("\033[46m" + bar + "\033[0m")


t = 0

input("Bubble Sort [Press enter to continue]")
bubble_sorting(bars.copy(), Time=t)

input("Selection Sort [Press enter to continue]")
selection_sorting(bars.copy(), Time=t)

input("Insertion Sort [Press enter to continue]")
insertion_sorting(bars.copy(), Time=t)

input("Merge Sort [Press enter to continue]")
merge_sorting(bars.copy(), Time=t)

input("Quick Sort [Press enter to continue]")
quick_sorting(bars.copy(), Time=t)

input("Shell Sort [Press enter to continue]")
shell_sorting(bars.copy(), Time=t)
