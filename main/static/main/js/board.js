const button = document.querySelector('.button')
const app = document.querySelector('.app')

let draggedItem = null

const ajaxSend = async (formData, url) => {
  const fetchResp = await fetch(url, {
    method: 'POST',
    body: formData,
  })

  if (!fetchResp.ok) {
    throw new Error(
      `Ошибка по адресу ${url}, статус ошибки ${fetchResp.status}`
    )
  }
  return await fetchResp.json()
}

function addColumn() {
  let url = 'addColumn'

  const form = document.getElementById('addBrd')
  const input = document.getElementById('add__board-input')
  const boards = document.querySelector('.boards')

  if (input.value != '') {
    form.addEventListener(
      'submit',
      function (e) {
        e.preventDefault()

        const formData = new FormData(this)

        //создаем элементы
        const board = document.createElement('div')

        const titleDiv = document.createElement('form')
        const titleInput = document.createElement('input')
        const deleteButton = document.createElement('button')

        const inputDiv = document.createElement('form')
        const cardInput = document.createElement('input')
        const addBtn = document.createElement('button')

        const list = document.createElement('div')

        const pk = document.createElement('p')

        //Добавляем в БД-------------
        ajaxSend(formData, url)
          .then((response) => {
            pk.innerText = response.pk
          })
          .catch((err) => console.error(err))

        // Стили
        board.classList.add('boards__item')
        titleInput.classList.add('title')
        inputDiv.classList.add('add__card')
        cardInput.classList.add('add__board-input')
        cardInput.classList.add('cardInput')
        addBtn.classList.add('add__btn')
        list.classList.add('list')
        titleDiv.classList.add('titleDiv')
        deleteButton.classList.add('deleteBoard')
        pk.classList.add('pk')

        //вставляем значения
        addBtn.innerHTML = `
        <span> + </span>
        `

        cardInput.placeholder = 'Карточка ...'
        titleInput.value = input.value

        deleteButton.innerText = 'X'

        //добавляем слушатель
        // deleteButton.addEventListener('click', function (e) {
        //   //удаляем из БД--------

        //   e.target.parentNode.parentNode.remove()
        // })

        //добавляем элементы
        titleDiv.append(titleInput)
        titleDiv.append(deleteButton)

        inputDiv.append(cardInput)
        inputDiv.append(addBtn)
        board.append(pk)
        board.append(titleDiv)
        board.append(inputDiv)
        board.append(list)
        boards.append(board)

        input.value = ''
        addCard()
        dragNdrop()
        deleteColumn()
      },
      { once: true }
    )
  }
}

function deleteColumn() {
  const deleteBtns = document.querySelectorAll('.deleteBoard')

  deleteBtns.forEach((del) => {
    del.addEventListener('click', (e) => {
      let pk = e.target.parentNode.parentNode.querySelector('.pk').innerText
      let url = 'deleteColumn/' + pk

      fetch(url, {
        method: 'DELETE',
        credentials: 'same-origin',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
        },
      })
        .then((res) => res.text()) // or res.json()
        .then((res) => console.log(res))
      e.target.parentNode.parentNode.remove()
    })
  })
}

function addCard() {
  const forms = document.querySelectorAll('.add__card')
  const inputs = document.querySelectorAll('.cardInput')

  forms.forEach((form) => {
    form.addEventListener('submit', function (e) {
      e.preventDefault()

      let input = e.target.querySelector('.cardInput').value

      const formData = new FormData(this)
      let column_id = e.target.parentNode.querySelector('.pk').innerText
      let url = 'addCard/' + column_id

      let parent = e.target.parentNode.querySelector('.list')

      const newCard = document.createElement('div')
      const cardTitle = document.createElement('div')
      const deleteButton = document.createElement('button')
      const description = document.createElement('p')
      const pk = document.createElement('p')

      description.className = 'desc'
      description.innerText = ''
      description.style.display = 'none'

      pk.classList.add('pk')

      deleteButton.innerText = 'X'
      deleteButton.classList.add('deleteCard')
      newCard.classList.add('list__item')
      newCard.draggable = true
      cardTitle.textContent = input

      cardTitle.addEventListener('click', showMenu)

      newCard.append(pk)
      newCard.append(description)
      newCard.append(cardTitle)
      newCard.append(deleteButton)

      //Добавляем в БД-------------
      ajaxSend(formData, url)
        .then((response) => {
          pk.innerText = response.pk
          form.reset()
        })
        .catch((err) => console.error(err))

      e.target.querySelector('.cardInput').value = ''

      parent.append(newCard)
      dragNdrop()
      deleteCard()
    })
  })
}

function deleteCard() {
  const deleteBtns = document.querySelectorAll('.deleteCard')

  deleteBtns.forEach((del) => {
    del.addEventListener('click', (e) => {
      let pk = e.target.parentNode.querySelector('.pk').innerText
      let url = 'deleteCard/' + pk

      fetch(url, {
        method: 'DELETE',
        credentials: 'same-origin',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
        },
      })
        .then((res) => res.text()) // or res.json()
        .then((res) => console.log(res))
      e.target.parentNode.remove()
    })
  })
}

function deleteTask() {}

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

function getCookie(name) {
  var cookieValue = null
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';')
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim()
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

button.addEventListener('click', addColumn)
addCard()
dragNdrop()
deleteColumn()
deleteCard()
