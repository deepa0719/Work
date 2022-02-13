//listen for clicks on the increment button
//increment the count variable when the button is clicked
//chnage the count-el in the HTML to reflect the new count

let countEl = document.getElementById("count-el") //passing in arguments
let count = 0
let saveEl = document.getElementById("save-el")

function increment() {
    count = count+1
    countEl.innerText = count
}

function save() {
    let display = " " + count + " - "
    saveEl.textContent += display
    console.log(count)
}