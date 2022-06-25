

const mergeArrays = (arr1, arr2) => {
  let i = 0;
  let j = 0;
  const result = [];

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] > arr2[j]) {
      result.push(arr2[j]);
      j++;
    } else {
      result.push(arr1[i]);
      i++;
    }
  }

  while (i < arr1.length) {
    result.push(arr1[i])
    i++;
  }

  while (j < arr2.length) {
    result.push(arr2[j]);
    j++;
  }
  return result;
};

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 3]
// arr1 = [1, 3, 5, 7, 9]
// arr2 = [2, 4, 6, 8, 10]
result = mergeArrays(arr1, arr2);
console.log(result)