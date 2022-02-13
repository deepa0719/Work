let firstCard = getRandomCard()
let secondCard = getRandomCard()
let sum = firstCard + secondCard
let cards = [firstCard, secondCard]
let hasBlackJack = false
let isAlive = true
let message = ""
let messageEl = document.getElementById("message-el")
let sumEl = document.getElementById("sum-el")
// 2. Store the cards paragraph in a variable called cardsEl
let cardsEl = document.getElementById("cards-el")

function getRandomCard() {
    let randomNum = Math.floor(Math.random()*13)+1 //1 - 13
    if (randomNum === 1) {
        return 11
    }
    else if (randomNum > 10) {
        return 10
    }
    else {
        return randomNum
    }
}

function startGame() {
    renderGame()
}

function renderGame() {
    cardsEl.textContent = "Cards: "
    for (let i = 0; i<cards.length; i+=1) {
        cardsEl.textContent += cards[i] + " "

    }
    sumEl.textContent = "Sum: " + sum
    if (sum <= 20) {
        message = "Do you want to draw a new card?"
    } else if (sum === 21) {
        message = "You've got Blackjack!"
        hasBlackJack = true
    } else {
        message = "You're out of the game!"
        isAlive = false
    }
    messageEl.textContent = message
}

function newCard(){
    let card = getRandomCard() 
    sum += card
    cards.push(card)
    renderGame()
}