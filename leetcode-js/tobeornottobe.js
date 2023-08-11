/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe(other) {
            if (other === val){
                return true
            }
            throw new Error("Not Equal")
        },
        notToBe(other){
            if (other === val){
                throw new Error("Not Equal")
            }
            return true
        }
    }
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */

console.log(expect("5").toBe("5"));
