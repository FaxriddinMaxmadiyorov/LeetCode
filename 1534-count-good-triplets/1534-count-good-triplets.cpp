class Solution {
  public:
      int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
          int ans = 0;
          for (int i = 0; i < arr.size(); i++)
          {
              for (int j = i + 1; j < arr.size(); j++)
              {
                  int t1 = abs(arr[i] - arr[j]);
                  for (int k = j + 1; k < arr.size(); k++)
                  {
                      int t2 = abs(arr[j] - arr[k]);
                      int t3 = abs(arr[i] - arr[k]);
                      if (t1 <= a && t2 <= b && t3 <= c)
                          ans++;
                  }
              }
          }
          return ans;
      }
  };