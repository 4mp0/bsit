
console.log("Console running!");

const main = () => {
    
    "use strict";

    let hello_world = "\nHello World!";
    var hello = hello_world.split(" ",1);
    console.log(hello_world+"\n"+hello[0],"\n");

    function add(x, y) {
        return x + y
    }; console.log(add(1,0),"\n")

    let i=0;
    while (i < 10) {
        console.log(i++)
    }

}; main();