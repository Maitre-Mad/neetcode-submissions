class Solution {
public:
    bool isPalindrome(string s) {
        int left=0;
        int right=s.length()-1;

        while(left<right){
            //skip non alphamnumeriocc characer from the left
            while(left<right && !std::isalnum(s[left])){
                left++;
            }
            //skip non alphanumeric characters from the right 
            while(left<right && !std::isalnum(s[right])){
                right--;
            }
            //compare characters case insensitively
            if(std::tolower(s[left])!=std::tolower(s[right])){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
