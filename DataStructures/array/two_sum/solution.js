var assert = require('assert');


const two_sum_ordered = (arr, k) => {
  let i = 0;
  let j = arr.length - 1;

  while (i < j) {
    let acc = arr[i] + arr[j];

    if (acc == k) {
      return true;
    } else if (acc < k) {
      i++;
    } else {
      j--;
    }
  }
  return false;
};

var arr = [1, 2, 3, 9];
var k = 8;
var result = two_sum_ordered(arr, k);

var message = (result === false) ? 'Correct!' : 'Wrong!';
console.log(result, message);


const two_sum = (arr, k) => {
  const mem = {};

  for (let i = 0; i < arr.length; i++) {
    let rest = k - arr[i];

    if (mem[rest]) {
      return [parseInt(mem[rest]), i]
    } else {
      mem[arr[i]] = i.toString();
    }
  }
  return false;
};

var arr = [2, 7, 11, 15]
var k = 9;
var result = two_sum(arr, k);
var message = (result[0] === 0 && result[1] === 1) ? 'Correct!' : 'Wrong!';
console.log(result, message);
