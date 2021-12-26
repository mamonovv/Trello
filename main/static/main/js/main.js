const button = document.querySelector('.button')
const lists = document.querySelectorAll('.list')

let draggedItem = null

function addTask() {
const addBtns = document.querySelectorAll('.add__btn')
const inputCards = document.querySelectorAll('.add__board-input')


  inputCards.forEach(input => {
    input.addEventListener('input', () => {
      parent = input.parentNode.parentNode
      addBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          if (input.value != '') {
            const newCard = document.createElement('div')
            newCard.classList.add('list__item')
            newCard.draggable = true
            newCard.textContent = input.value
            input.value = ''
      
            parent.append(newCard)
            dragNdrop()
          }
        })
      })
    })
  })

  
}

function addBoard() {
  const input = document.getElementById('add__board-input')
  const boards = document.querySelector('.boards')

  if (input.value != '') {
    const board = document.createElement('div')
    board.classList.add('boards__item')
    board.innerHTML = `
      <input type="text" class="title" value="${input.value}">

      <div class="add__card">
        <input placeholder="Карточка ..." class="add__board-input"type="text">
        <div class="add__btn"><span> + </span></div>
      </div>

      <div class="list"></div>
  `
    input.value = ''
    boards.append(board)
  }

  addTask()
  dragNdrop()
}

function dragNdrop() {
  const listItems = document.querySelectorAll('.list__item')
  const lists = document.querySelectorAll('.list')

  for (let i = 0; i < listItems.length; i++) {
    const item = listItems[i]

    item.addEventListener('dragstart', () => {
      draggedItem = item
      setTimeout(() => {
        item.style.display = 'none'
      }, 0)
    })

    item.addEventListener('dragend', () => {
      setTimeout(() => {
        item.style.display = 'block'
        draggedItem = null
      }, 0)
    })

    item.addEventListener('dblclick', () => {
      item.remove()
    })

    for (let j = 0; j < lists.length; j++) {
      const list = lists[j]

      list.addEventListener('dragover', (e) => e.preventDefault())

      list.addEventListener('dragenter', function (e) {
        e.preventDefault()
        this.style.backgroundColor = 'rgba(0,0,0,.3)'
      })

      list.addEventListener('dragleave', function (e) {
        this.style.backgroundColor = 'rgba(0,0,0,0)'
      })

      list.addEventListener('drop', function (e) {
        this.style.backgroundColor = 'rgba(0,0,0,0)'
        this.append(draggedItem)
      })
    }
  }
}

button.addEventListener('click', addBoard)
addTask()
dragNdrop()
