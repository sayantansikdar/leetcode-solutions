class Solution {
  public int[] mostCompetitive(int[] nums, int k) {
    int[] ans = new int[k];
    Deque<Integer> stack = new ArrayDeque<>();

    for (int i = 0; i < nums.length; ++i) {
      // If |stack| - 1 + len(nums[i:]) >= k, then it means we still have enough
      // nums, and we can safely pop an element from stack.
      while (!stack.isEmpty() && stack.peekLast() > nums[i] &&
             stack.size() - 1 + nums.length - i >= k)
        stack.pollLast();
      if (stack.size() < k)
        stack.add(nums[i]);
    }

    for (int i = 0; i < k; i++)
      ans[i] = stack.pollFirst();

    return ans;
  }
}
