class Solution {
 public:
  int thirdMax(vector<int>& nums) {
    long max1 = LONG_MIN;  // The maximum
    long max2 = LONG_MIN;  // 2nd maximum
    long max3 = LONG_MIN;  // 3rd maximum

    for (const int num : nums)
      if (num > max1) {
        max3 = max2;
        max2 = max1;
        max1 = num;
      } else if (max1 > num && num > max2) {
        max3 = max2;
        max2 = num;
      } else if (max2 > num && num > max3) {
        max3 = num;
      }

    return max3 == LONG_MIN ? max1 : max3;
  }
};
