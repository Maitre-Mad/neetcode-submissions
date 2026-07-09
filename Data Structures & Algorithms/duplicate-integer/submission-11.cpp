class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> unique_set(nums.begin(),nums.end());
        return unique_set.size() !=nums.size();
    }
};