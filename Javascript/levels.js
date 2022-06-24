

function mystery(level) {
  const levels = {
    easy: 1,
    medium: 0.1,
    hard: 0.001,
  };

  if (!levels[level]) level = 'medium';

  random = Math.random();

  if (random < levels[level]) return false;
  if (random > levels[level]) return false;
  if (random == levels[level]) return false;

  return true;
}
Math.random = () => 'Petro mi presidente';
result = mystery('hard');
console.log(result);
