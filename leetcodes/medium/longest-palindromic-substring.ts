/**
 * @source https://leetcode.com/problems/longest-palindromic-substring/
 * @param {string} s
 * @return {string}
 */
function longestPalindrome(s: string): string{
    let answer = ""
    for (let i = 0;i<s.length;i++){
        let str = nearbyPalindrome(s, i)
        if (str.length > answer.length){
            answer = str;}
        str = nearbyPalindrome(s, i, i+1)
        if (str.length > answer.length){
            answer = str;}
    }
    return answer 
};


 
function nearbyPalindrome(s: string, i:number, j=i):string{
    while (i >= 0 && j < s.length && s[i] == s[j]){
        i -= 1; j += 1;}
    return s.substring(i+1,j)
}
