class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int low = 0, up = arr.size() - 1;
        while (low + 2 <= up)
        {
            int mid = (low + up) / 2;
            if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1])
                return mid;
            else if (arr[mid] > arr[mid - 1] && arr[mid + 1] > arr[mid])
                low = mid + 1;
            else if (arr[mid] < arr[mid - 1] && arr[mid] > arr[mid + 1])
                up = mid - 1;
        }
        return (arr[low] < arr[up] ? up:low);
    }
};