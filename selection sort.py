class Solution: 
    #def select(self, arr, i):
        # code here 
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            min= i
            for j in range(i+1, len(arr)):
                if arr[min]>arr[j]:
                    min= j
            arr[i], arr[min]= arr[min],arr[i]
