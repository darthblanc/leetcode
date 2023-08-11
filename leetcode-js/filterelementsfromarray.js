/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArray = [];
    for (let item in arr) {
        if (fn(arr[item], parseInt(item))){
            newArray.push(arr[item]);
        }
    }
    return newArray;
};

let fn = function greaterThan10(n){return n > 10;}
console.log(filter([0,10,20,30], fn));