// /**
//  * @param {number[]} nums
//  * @param {Function} fn
//  * @param {number} init
//  * @return {number}
//  */
// var reduce = function(nums, fn, init) {
//     if (nums.length === 0){
//         return init;
//     }
//     let rv = fn(init, nums[0]);
//     return reduce(nums.slice(1, nums.length), fn, rv);
// };

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    for (let i = 0; i < nums.length; i++) {
        init = fn(init, nums[i]);
    }
    return init;
};


// /**
//  * @param {number[]} nums
//  * @param {Function} fn
//  * @param {number} init
//  * @return {number}
//  */
// var reduce = function(nums, fn, init) {
//     let val = init;
//     for (let i = 0; i < nums.length; i++) {
//         val = fn(val, nums[i]);
//     }
//     return val;
// };

let fn = function sum(accum, curr){return accum + curr;}
console.log(reduce([1,2,3,4], fn, 0));

let fn2 = function sum(accum, curr) { return accum + curr * curr; }
console.log(reduce([1,2,3,4], fn2, 100));