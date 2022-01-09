const button = document.querySelector('.button')
const app = document.querySelector('.app')

let draggedItem = null
// let options = {
//   method: 'GET',
//   headers: { 'X-Requested-With': 'XMLHttpRequest' },
// }

async function addBoard() {
  let url = 'addColumn'

  const ajaxSend = async (formData) => {
    const fetchResp = await fetch(url, {
      method: 'POST',
      body: formData,
    })

    if (!fetchResp.ok) {
      throw new Error(
        `Ошибка по адресу ${url}, статус ошибки ${fetchResp.status}`
      )
    }
    return await fetchResp.text()
  }

  const form = document.getElementById('addBrd')
  const input = document.getElementById('add__board-input')
  const boards = document.querySelector('.boards')

  form.addEventListener('submit', function (e) {
    e.preventDefault()

    if (input.value != '') {
      const formData = new FormData(this)

      //создаем элементы
      const board = document.createElement('div')

      const titleDiv = document.createElement('div')
      const titleInput = document.createElement('input')
      const deleteButton = document.createElement('button')

      const inputDiv = document.createElement('div')
      const cardInput = document.createElement('input')
      const addBtn = document.createElement('button')

      const list = document.createElement('div')

      // Стили
      board.classList.add('boards__item')
      titleInput.classList.add('title')
      inputDiv.classList.add('add__card')
      cardInput.classList.add('add__board-input')
      addBtn.classList.add('add__btn')
      list.classList.add('list')
      titleDiv.classList.add('titleDiv')

      //вставляем значения
      addBtn.innerHTML = `
      <span> + </span>
      `

      cardInput.placeholder = 'Карточка ...'
      titleInput.value = input.value

      deleteButton.innerText = 'X'

      //добавляем слушатель
      deleteButton.addEventListener('click', function (e) {
        //удаляем из БД--------

        e.target.parentNode.parentNode.remove()
      })

      //добавляем элементы
      titleDiv.append(titleInput)
      titleDiv.append(deleteButton)

      inputDiv.append(cardInput)
      inputDiv.append(addBtn)
      board.append(titleDiv)
      board.append(inputDiv)
      board.append(list)
      boards.append(board)

      //Добавляем в БД-------------
      ajaxSend(formData)
        .then((response) => {
          console.log(response)
          form.reset()
        })
        .catch((err) => console.error(err))

      addTask()
      dragNdrop()
    }
  })
}

async function addTask() {
  const addBtns = document.querySelectorAll('.add__btn')
  const inputCards = document.querySelectorAll('.add__board-input')

  inputCards.forEach((input) => {
    input.addEventListener('input', () => {
      addBtns.forEach((btn) => {
        btn.addEventListener('click', () => {
          parent = input.parentNode.parentNode.querySelector('.list')

          if (input.value != '') {
            const newCard = document.createElement('div')
            const cardTitle = document.createElement('div')
            const deleteButton = document.createElement('button')
            const description = document.createElement('p')

            description.className = 'desc'
            description.innerText = ''
            description.style.display = 'none'

            deleteButton.innerText = 'X'
            newCard.classList.add('list__item')
            newCard.draggable = true
            cardTitle.textContent = input.value

            cardTitle.addEventListener('click', showMenu)
            deleteButton.addEventListener('click', function (e) {
              e.target.parentNode.remove()
            })

            newCard.append(description)
            newCard.append(cardTitle)
            newCard.append(deleteButton)

            inputCards.forEach((inp) => {
              inp.value = ''
            })

            parent.append(newCard)
            dragNdrop()
          }
        })
      })
    })
  })
}

async function showMenu() {
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
  saveButton.className = 'btn-save'

  saveButton.innerText = 'Сохранить'
  description.style.resize = 'none'
  description.innerText = this.parentNode.querySelector('.desc').innerText

  //Event listeners
  menuContainer.addEventListener('click', (e) => {
    if (e.target.classList.contains('menuContainer')) {
      menuContainer.remove()
    }
  })

  saveButton.addEventListener('click', () => {
    saveButton.style.display = 'none'
    this.parentNode.querySelector('.desc').innerText = description.value
  })

  menuDescription.addEventListener('input', () => {
    saveButton.style.display = 'block'
  })

  menuTitle.addEventListener('keyup', (e) => {
    // Number 13 is the "Enter"
    if (e.keyCode === 13) {
      e.preventDefault()
      this.innerText = menuTitle.value
      menuTitle.blur()
    }
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

async function dragNdrop() {
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

      list.addEventListener('dragover', function (e) {
        e.preventDefault()
        this.style.backgroundColor = 'rgba(120, 153, 253, 0.5)'
      })

      list.addEventListener('dragenter', function (e) {
        e.preventDefault()
      })

      list.addEventListener('dragleave', function (e) {
        this.style.backgroundColor = 'rgba(189,206,255,0)'
      })

      list.addEventListener('drop', function (e) {
        this.style.backgroundColor = 'rgba(189,206,255,0)'
        this.appendChild(draggedItem)
      })
    }
  }
}

button.addEventListener('click', addBoard)
addTask()
dragNdrop()
