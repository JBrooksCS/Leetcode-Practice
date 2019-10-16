console.log("Hello Worlddd")

///
/*
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
*/

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var arr = [1,2,2,1,1,3];

function uniqueOrNot(arr) {
    
    let obj = {};
    arr.forEach(n => {
        obj[n] = (obj[n] || 0) + 1;
    })
    
    let data = Object.values(obj)
    var uniqueArray = [...new Set(data)]
        
    let unique = false;

    if (uniqueArray.length === data.length){
        unique = true;
    }
    return unique;
};

console.log("Unique? ", uniqueOrNot(arr));