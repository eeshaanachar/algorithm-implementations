#include <iostream>
#include <ctime>

void swap(int& x, int& y)
{
    int temp = x;
    x = y;
    y = temp;
}

int partition(int *arr, int leftBound, int rightBound)
{
    int i = leftBound + 1;
    int j = rightBound;
    while (i < j)
    {
        for ( ; i <= rightBound && arr[i] <= arr[leftBound]; i++);
        for ( ; arr[j] > arr[leftBound]; j--);
        if (i < j)
            swap(arr[i], arr[j]);
    }
    swap(arr[leftBound], arr[i - 1]);
    return i - 1;
}

void quicksort(int *arr, int leftBound, int rightBound)
{
    if (rightBound <= leftBound)
        return;

    if (rightBound - leftBound == 1)
    {
        if (arr[leftBound] > arr[rightBound])
            swap(arr[leftBound], arr[rightBound]);
        return;
    }
    
    int partitionIndex = partition(arr, leftBound, rightBound);
    quicksort(arr, leftBound, partitionIndex - 1);
    quicksort(arr, partitionIndex + 1, rightBound);
}

int main()
{
    int arr[10];
    srand(time(NULL));

    for (int i = 0; i < 10; i++)
    {
        arr[i] = rand() % 100;
        std::cout << arr[i] << "\t";
    }
    std::cout << std::endl;

    quicksort(arr, 0, sizeof(arr) / sizeof(arr[0]) - 1);

    for (int& num : arr)
        std::cout << num << "\t";
    std::cout << std::endl;
}