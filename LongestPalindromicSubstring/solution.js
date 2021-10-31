const longestPalindrome = function(s) {
    const n = s.length;
    const dpTable = [];
    let longestSubStrBegin = 0;
    let longestSubStrEnd = 0;
    
    //build the dp table
    for (let i = 0; i < n; i++){
        dpTable.push(new Array(n).fill(0));
    }

    //fill the table with all palindromes of length 1
    for (let i = 0; i < n; i++){
        dpTable[i][i] = 1;
    }

    //fill the table with all palindromes of length 2
    for (let i = 0; i < n-1; i++){
        if (s[i] === s[i+1]){
            longestSubStrBegin = i;
            longestSubStrEnd = i+1;
            dpTable[i][i+1] = 1;
        }
    }

    //iterate through all substring lengths and check if those are palindromess
    for (let subStrLen = 2; subStrLen < n; subStrLen++){
        for (let i = 0; i < n; i++){
            if (i + subStrLen >= n){
                break;
            }
            
            if (s[i] === s[i + subStrLen] && dpTable[i + 1][i + subStrLen - 1] === 1){
                longestSubStrBegin = i;
                longestSubStrEnd = i + subStrLen;
                dpTable[i][i + subStrLen] = 1;
            } else {
                dpTable[i][i + subStrLen] = 0;
            }

        }
    }

    return s.substring(longestSubStrBegin, longestSubStrEnd + 1);
};