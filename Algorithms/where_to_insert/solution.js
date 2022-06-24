const getIndex = (arr, number) => {
  const nums = arr.sort((a, b) => {
    return a - b
  })
  for (var i = 0; i < nums.length; i++) {
    if (number < nums[i]) {
      nums.splice(i, 0, number);
      return i;
    }
  }
  return arr.length
}

var arr = [16, 4, 5]
var number = 13

result = getIndex(arr, number)
console.log(result)