const getIndex = (arr, number) =>
    arr.reduce((counter, curr) => (number > curr ? ++counter : counter), 0);