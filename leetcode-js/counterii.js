/**
 * @param {number} init
 * @return {{decrement(): *, increment(): *, reset(): number}}
 */
var createCounter = function(init) {
    let change = init;
    return {
        increment(){
            change += 1;
            return change;
        },
        reset(){
            change = init;
            return init;
        },
        decrement(){
            change -= 1;
            return change;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

const counter = createCounter(5)
console.log(counter.increment()); // 6
console.log(counter.reset()); // 5
console.log(counter.decrement()); // 4