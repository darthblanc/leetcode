/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    let x = await promise1.then();
    let y = await promise2.then();
    return x + y;
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */


addTwoPromises(Promise.resolve(2), Promise.resolve(2))
    .then(console.log); // 4