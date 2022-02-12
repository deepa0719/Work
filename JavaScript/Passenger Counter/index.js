//listen for clicks on the increment button
//increment the count variable when the button is clicked
//chnage the count-el in the HTML to reflect the new count

let countEl = document.getElementById("count-el") //passing in arguments

console.log(countEl)

let count = 0

function increment() {
    count = count+1
    countEl.innerText = count
}