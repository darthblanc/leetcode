/**
 * @param {Function} fn
 */
function memoize(fn) {
    let map = {};
    return function(...args) {
        if (map.contains([fn, args])){
            return map[[fn, args]];
        }
        let x = fn.apply(0, args);
        map[[fn, args]] = x;
        return x;
    }
}


/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */

let callCount = 0;
const memoizedFn = memoize(function (a, b) {
    callCount += 1;
    return a + b;
})
console.log(memoizedFn(2, 3)); // 5
console.log(memoizedFn(2, 3)); // 5
console.log(callCount) // 1
