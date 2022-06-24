function countOddPalindromes(s, center) {
    var count = 0
    var i = 0
    while (center - i >= 0 && center + i < s.length && s[center - i] === s[center + i]) {
        //console.log(`adding odd palindrome with center at ${center} and offset ${i}`)
        count++
        i++
    }
    return count
}
// c|ooc
// s = cooc center 1
function countEvenPalindromes(s, center) {
    var count = 0
    var i = 0
    while (center - i >= 0 && center + i + 1 < s.length && s[center - i] === s[center + i + 1]) {
        //console.log(`adding even palindrome with center at ${center} and offset ${i}`)
        count++
        i++
    }
    return count
}

function countPalindrome(s) {
    var c = 0
    for (var i = 0; i < s.length; i++) {
        //console.log("center ", i)
        c += countOddPalindromes(s, i) + countEvenPalindromes(s, i)
    }
    return c
}

console.log("bob", " ", countPalindrome("bob"))
console.log("anitalavalatina", " ", countPalindrome("anitalavalatina"))
console.log("aaaaaaaaaaaaaaa", " ", countPalindrome("aaaaaaaaaaaaaaa"))
console.log("abc", " ", countPalindrome("abc"))
console.log("conoso", " ", countPalindrome("conoso"))