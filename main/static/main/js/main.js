const button = document.querySelector('.button')
const app = document.querySelector('.app')

let draggedItem = null

function addTask() {
  const addBtns = document.querySelectorAll('.add__btn')
  const inputCards = document.querySelectorAll('.add__board-input')

  inputCards.forEach(input => {
    input.addEventListener('input', () => {
      addBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          parent = input.parentNode.parentNode.querySelector('.list')

          if (input.value != '') {
            const newCard = document.createElement('div')
            const cardTitle = document.createElement('div')
            const deleteButton = document.createElement('button')

            deleteButton.innerText = 'X'
            newCard.classList.add('list__item')
            newCard.draggable = true
            cardTitle.textContent = input.value

            cardTitle.addEventListener('click', showMenu)
            deleteButton.addEventListener('click', function(e) {
              e.target.parentNode.remove()
            })

            newCard.append(cardTitle)
            newCard.append(deleteButton)

            inputCards.forEach(inp => {
              inp.value = ''
            })
            // input.value = ''
      
            parent.append(newCard)
            dragNdrop()
          }
        })
      })
    })
  })

  


  
}

function showMenu() {
  const menu = document.createElement('div')
  const menuContainer = document.createElement('div')
  const menuTitle = document.createElement('input')
  const menuDescription = document.createElement('div')

  const saveButton = document.createElement('button')
  const description = document.createElement('textarea')

  //Add class names
  menu.className = 'menu'
  menuContainer.className = 'menuContainer'
  menuTitle.className = 'menuTitle'
  menuDescription.className = 'menuDescription'
  saveButton.innerText = 'Сохранить'
  saveButton.className = 'btn-save'

  //Event listeners
  menuContainer.addEventListener('click', (e) => {
    if (e.target.classList.contains('menuContainer')) {
      menuContainer.remove()
    }
  })

  saveButton.addEventListener('click', () => {
    saveButton.style.display = 'none'
  })

  menuDescription.addEventListener('input', () => {
    saveButton.style.display = 'block'
  })

  //innerText
  menuTitle.value = this.innerText

  //Append
  menuDescription.append(description)
  menuDescription.append(saveButton)
  menu.append(menuTitle)
  menu.append(menuDescription)
  menuContainer.append(menu)
  app.append(menuContainer)
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
    addTask()
    dragNdrop()
  }

  
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

    for (let j = 0; j < lists.length; j++) {
      const list = lists[j]


      list.addEventListener('dragover', function(e) {
        e.preventDefault()
        this.style.backgroundColor = 'rgba(120, 153, 253, 0.5)'

      } )

      list.addEventListener('dragenter', function(e) {
        e.preventDefault()
      })

      list.addEventListener('dragleave', function(e) {
        this.style.backgroundColor = 'rgba(189,206,255,0)'
      })

      list.addEventListener('drop', function(e) {
        this.style.backgroundColor = 'rgba(189,206,255,0)'
        this.appendChild(draggedItem)

      })
    }
  }
}

button.addEventListener('click', addBoard)
addTask()
dragNdrop()

