
/**
 * Error messages object
 */
const error = {
  EMPTYSTR: 'Error: Cannot process empty or blank strings.',
  MISSINGPARAM: 'Error: Missing required attribute `text`.',
}

/**
 * formatText() returns a formatted text divided into custom separator
 * based on the passed-in parameters
 * @param {String} text
 * @param {Int} limit
 * @param {String} separator
 * @param {Bool} trimLastSeparator
 * @return {String} formattedStr
 */
const formatText = (text, { limit = 0, separator = ',', reversed = false, lowerCase = false } = {}) => {
  try {
    // Check if text is a valid instring that can be formatted
    if (!text || (typeof text !== 'string' && typeof text !== 'object')) {
      return error.EMPTYSTR;
    }
    if (typeof text === 'object' && !text.hasOwnProperty('text')) {
      return error.MISSINGPARAM;
    }

    if (text.trim().length === 0) {
      return error.EMPTYSTR;
    }

    // Lowercase string if required
    if (lowerCase) {
      text = text.toLocaleLowerCase();
    }

    let formattedStr = '';

    let words = text.split(' ');

    // Reverse string if required
    if (reversed) {
      words = words.reverse();
    }

    // Trim string, then filter it by given limit, then join using given separator.
    formattedStr = words.map(word => word.replace(/\s+/g, ' ').trim())
      .filter(word => word.length > limit)
      .join(separator);

    return formattedStr;
  } catch (err) {
    console.error(err);
  }
};

const text = 'this is definitely the amazing Way the world Ends however i am speculation on a variety of artifacs in this particular pharagraph';
const formatterConfig = {
  'limit': 5,
  'separator': ', ',
  'reversed': true,
  'lowercase': true,
};

result = formatText(text, formatterConfig);
console.log(result);
