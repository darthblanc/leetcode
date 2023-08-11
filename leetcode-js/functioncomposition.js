/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        let rv = x;
        for (let i = functions.length - 1; i > -1; i--) {
            rv = functions[i](rv);
            console.log(rv, i);
        }
        return rv;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */

const fn = compose([x => x + 1, x => x * x, x => 2 * x]);
console.log(fn(4));
