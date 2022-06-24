function balancedParentheses(str) {
  str = str.split(' ').join('')
  const next = []
  const brackets = {
    '{': '}',
    '(': ')',
    '[': ']',
  }

  if (!str || str.length === 0 || !brackets.hasOwnProperty(str[0])) {
    return false
  }

  next[0] = brackets[str[0]]

  for (var i = 1; i < str.length; i++) {
    if (!brackets.hasOwnProperty(str[i])) {
      if (str[i] !== next[next.length - 1]) {
        return false
      }
      next.pop()
    } else {
      next.push(brackets[str[i]])
    }
  }
  if (next.length === 0) {
    return true
  }
}
// var str = '{ [ ] ( ) }'
var str = '{ [ ( ] ) }'
result = balancedParentheses(str)
console.log(result)