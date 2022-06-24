/**
 * @param {string} s
 * @return {number}
 */
const isPalindrome = (s, fi, ti) => {
  for (var i = 0; i < ti - fi; i++) {
    if (s[fi + i] !== s[ti - 1 - i]) {
      return false
    }
  }
  return true
}

var countSubstrings = (s) => {
  var c = 0
  for (var i = 0; i < s.length; i++) {
    for (var j = i + 1; j <= s.length; j++) {
      c += isPalindrome(s, i, j);
    }
  }
  return c
};