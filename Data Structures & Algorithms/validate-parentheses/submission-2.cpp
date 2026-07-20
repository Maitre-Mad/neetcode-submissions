class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stacks={};
        std::unordered_map<char,char> bracket_map={
            {'(', ')'}, 
            {'{', '}'}, 
            {'[', ']'}
        };

        for (char character:s){
            if (bracket_map.find(character) != bracket_map.end()){
                stacks.push(bracket_map[character]);
            }
            else{
            if (stacks.empty() || stacks.top() != character){
                return false;
            }
            stacks.pop();

        }}
        return stacks.empty();
        
    }
};
