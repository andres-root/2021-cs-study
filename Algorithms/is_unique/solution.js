

const isUnique = (string) => {
  const mem = {};

  for (const c of string) {
    if (mem.hasOwnProperty(c)) {
      return false;
    }
    mem[c] = c;
  }

  return true;
};

const test = (stringList) => {
  const string = 'abcd';

  for (const string of stringList) {
    const result = isUnique(string);
    console.log(`Testing ${string}: ${result}`)
  }
};

const stringList = [
  'abcd',
  'a',
  'abccd',
  'abcbd'
];

test(stringList);
