

const mergeArrays = (arr1, arr2) => {
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] > arr2[j]) {
      arr1.splice(i, 0, arr2[j]);
      i++;
      j++;
    } else {
      i++;
    }
  }

  if (j < arr2.lengt) {
    arr1 = [...arr2]
  }

  return arr1;
};

// arr1 = [1, 2, 3, 4, 5]
// arr2 = [6, 7, 8, 9, 10]
arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
result = mergeArrays(arr1, arr2);
console.log(result)