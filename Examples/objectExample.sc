let foo = 500/2;

let val = {
    x: "100",
    foo,
    complex: {
        bar: true
    }
};

let number = add(foo, 20);
let num2 = (foo - 30)*20
print("Result 1: ", number);
print("Result 2: ", num2);