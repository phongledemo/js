


const sum = (a, b) => {
    let sum = 0;
    for (let i = 0; i < a; i ++){
        sum += i
    }
    return b + sum;
}

console.log(sum(2,2))