/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let newArr = [];
    for (let item in arr) {
        newArr.push(fn(arr[item], parseInt(item)));
    }
    return newArr;
};

let fn = function plusone(n) {return n + 1;}
console.log(map([1,2,3], fn));

let fn2 = function plusI(n, i) {return n + i;}
console.log(map([1,2,3], fn2));