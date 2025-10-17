
function multiArray() {
   const multiArray = [
    [10, 200, 3],
    [4, 50, 600],
    [70, 8, 90]
    ];

    function printMatrix(arr) {
    let output = "";
        for (let i = 0; i < arr.length; i++) {
            let rowString = "";
            for (let j = 0; j < arr[i].length; j++) {
            rowString += String(arr[i][j]).padEnd(5); // Pad for alignment
            }
            output += rowString + "\n";
        }
        console.log(output);
    }

    printMatrix(multiArray);
}

function strIntArray() {
    const data = [
    { name: 'Alice', age: 30 },
    { name: 'Bob', age: 24 },
    { name: 'Charlie', age: 35 }
    ];
    console.table(data);
}