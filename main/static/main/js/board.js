const button = document.querySelector('.button')
const app = document.querySelector('.app')
const csrft = window.csrf_token
  .split(' ')[3]
  .split('=')[1]
  .replace('"', '')
  .slice(0, -2)

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

const ajaxGet = async (url) => {
  const fetchResp = await fetch(url)

  if (!fetchResp.ok) {
    throw new Error(
      `Ошибка по адресу ${url}, статус ошибки ${fetchResp.status}`
    )
  }
  return await fetchResp.json()
}

const addColumn = () => {
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

        const inputForm = document.createElement('form')
        const csrf = document.createElement('input')
        const cardInput = document.createElement('input')
        const addBtn = document.createElement('button')

        const list = document.createElement('div')

        //Добавляем в БД-------------
        ajaxSend(formData, url)
          .then((response) => {
            board.id = response.pk + '-column'
          })
          .catch((err) => console.error(err))

        //props
        titleInput.disabled = true
        //csrf
        csrf.type = 'hidden'
        csrf.name = 'csrfmiddlewaretoken'
        csrf.value = csrft

        // Стили
        board.classList.add('boards__item')
        titleInput.classList.add('title')
        inputForm.classList.add('add__card')
        cardInput.classList.add('add__board-input')
        cardInput.classList.add('cardInput')
        cardInput.type = 'text'
        cardInput.name = 'name'
        addBtn.classList.add('add__btn')
        list.classList.add('list')
        titleDiv.classList.add('titleDiv')
        deleteButton.classList.add('deleteBoard')

        //вставляем значения
        addBtn.innerHTML = `
        <span> + </span>
        `

        cardInput.placeholder = 'Карточка ...'
        titleInput.value = input.value

        deleteButton.innerText = 'X'

        //добавляем элементы
        titleDiv.append(titleInput)
        titleDiv.append(deleteButton)

        inputForm.appendChild(csrf)
        inputForm.append(cardInput)
        inputForm.append(addBtn)
        board.append(titleDiv)
        board.append(inputForm)
        board.append(list)
        boards.append(board)

        //Слушатель
        deleteButton.addEventListener('click', delColumn)
        inputForm.addEventListener('submit', addCard(inputForm))

        input.value = ''
      },
      { once: true }
    )
  }
}

const delColumn = (e) => {
  e.preventDefault()
  let column_id = parseInt(e.target.parentNode.parentNode.id)
  let url = 'deleteColumn/' + column_id

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
}

const deleteColumnOnLoad = () => {
  const deleteBtns = document.querySelectorAll('.deleteBoard')

  deleteBtns.forEach((del) => {
    del.addEventListener('click', delColumn)
  })
}

const addCard = (form) => (e) => {
  e.preventDefault()

  let input = e.target.querySelector('.cardInput').value

  if (input != '') {
    const formData = new FormData(form)

    let column_id = parseInt(e.target.parentNode.id)
    let url = 'addCard/' + column_id

    let parent = e.target.parentNode.querySelector('.list')

    const newCard = document.createElement('div')
    const cardTitle = document.createElement('div')
    const deleteButton = document.createElement('button')
    const description = document.createElement('p')

    description.className = 'desc'
    description.innerText = ''
    description.classList.add('none')

    deleteButton.innerText = 'X'
    deleteButton.classList.add('deleteCard')

    newCard.classList.add('list__item')
    newCard.draggable = true

    cardTitle.textContent = input
    cardTitle.classList.add('cardTitle')

    deleteButton.addEventListener('click', delCard)
    cardTitle.addEventListener('click', showMenu(cardTitle))

    newCard.append(description)
    newCard.append(cardTitle)
    newCard.append(deleteButton)

    newCard.addEventListener('dragstart', dragNdrop(newCard))

    //Добавляем в БД-------------

    ajaxSend(formData, url)
      .then((response) => {
        console.log(response)
        newCard.id = response.pk + '-card'
        form.reset()
      })
      .catch((err) => console.error(err))

    e.target.querySelector('.cardInput').value = ''

    parent.append(newCard)
  }
}

const addCardOnLoad = () => {
  const forms = document.querySelectorAll('.add__card')

  forms.forEach((form) => {
    form.addEventListener('submit', addCard(form))
  })
}

const delCard = (e) => {
  let card_id = parseInt(e.target.parentNode.id)
  let url = 'deleteCard/' + card_id

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
}

const deleteCardOnLoad = () => {
  const deleteBtns = document.querySelectorAll('.deleteCard')

  deleteBtns.forEach((del) => {
    del.addEventListener('click', delCard)
  })
}

const showMenu = (card) => async (e) => {
  const menuContainer = document.createElement('div')
  const menu = document.createElement('div')

  const form = document.createElement('form')
  const csrf = document.createElement('input')
  const menuTitle = document.createElement('input')
  // const menuDescription = document.createElement('div')
  const descCard = document.createElement('textarea')
  const deadline = document.createElement('input')

  const photoDiv = document.createElement('div')
  const photo = document.createElement('input')
  const photoImg = document.createElement('img')

  const btns = document.createElement('div')
  const saveButton = document.createElement('button')
  const cancelButton = document.createElement('button')

  let card_id = parseInt(card.parentNode.id)

  let photo_url = null

  //Get запрос
  let url = 'GetCard/' + card_id
  ajaxGet(url).then((resp) => {
    console.log(resp)
    menuTitle.value = resp.name
    descCard.value = resp.content
    deadline.value = resp.deadline

    if (resp.photo) {
      photoImg.src = resp.photo
    }
  })

  //Add properties
  descCard.style.resize = 'none'
  deadline.type = 'date'

  form.enctype = 'multipart/form-data'

  photo.type = 'file'
  photo.id = 'upload'

  cancelButton.type = 'cancel'
  cancelButton.innerText = 'Отменить'

  saveButton.type = 'submit'
  saveButton.innerText = 'Сохранить'

  descCard.placeholder = 'Эта карточка...'

  menuTitle.required = 'true'

  //Names
  menuTitle.name = 'name'
  descCard.name = 'content'
  deadline.name = 'deadline'
  photo.name = 'photo'

  //csrf
  csrf.type = 'hidden'
  csrf.name = 'csrfmiddlewaretoken'
  csrf.value = csrft

  //Add class names
  form.className = 'popUpForm'
  menu.className = 'menu'
  menuContainer.className = 'menuContainer'
  menuTitle.className = 'menuTitle'
  // menuDescription.className = 'menuDescription'
  saveButton.className = 'btn-save'
  cancelButton.className = 'btn-cancel'
  descCard.className = 'popUpArea'
  btns.className = 'popUpBtns'

  photoImg.className = 'photoPopUp'
  photoDiv.className = 'photoDiv'

  deadline.className = 'popUpDate'
  photo.className = 'popUpFile'

  card.parentNode.querySelector('.desc').innerText = descCard.value

  //Append
  btns.append(saveButton)
  btns.append(cancelButton)

  form.append(menuTitle)
  form.append(descCard)
  form.append(deadline)
  photoDiv.append(photo)
  photoDiv.append(photoImg)
  form.append(photoDiv)
  form.append(btns)
  form.appendChild(csrf)

  menu.append(form)
  menuContainer.append(menu)
  app.append(menuContainer)

  //Event listeners
  menuContainer.addEventListener('click', (e) => {
    if (e.target.classList.contains('menuContainer')) {
      menuContainer.remove()
    }
  })

  cancelButton.addEventListener('click', (e) => {
    e.preventDefault()
    menuContainer.remove()
  })

  form.addEventListener('submit', popUpSave(form, card_id, menuContainer, card))
}

const showMenuOnLoad = () => {
  const cards = document.querySelectorAll('.cardTitle')

  cards.forEach((card) => {
    card.addEventListener('click', showMenu(card))
  })
}

const dragNdrop = (card) => (e) => {
  const lists = document.querySelectorAll('.list')
  let curCard = null
  let newParent = null
  draggedItem = card

  setTimeout(() => {
    card.style.display = 'none'
  }, 0)

  card.addEventListener(
    'dragend',
    (e) => {
      setTimeout(() => {
        card.style.display = 'block'

        newParent = parseInt(e.target.parentNode.parentNode.id)
        curCard = parseInt(e.target.id)
        url = `moveCard/${newParent}/${curCard}`

        fetch(url, {
          method: 'POST', // or 'PUT'
          headers: {
            'X-CSRFToken': csrft,
            'Content-Type': 'application/json',
          },
        })
          .then((response) => response.json())
          .catch((err) => console.error('Error:', err))

        draggedItem = null
        curCard = null
        newParent = null
      }, 0)
    },
    { once: true }
  )

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

const dragNdropOnLoad = () => {
  const listItems = document.querySelectorAll('.list__item')
  const lists = document.querySelectorAll('.list')
  let curCard = null
  let newParent = null

  listItems.forEach((card) => {
    card.addEventListener('dragstart', dragNdrop(card))
  })
}

const getCookie = (name) => {
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

const popUpSave = (form, card_id, menuContainer, card) => (e) => {
  e.preventDefault()

  const formData = new FormData(form)

  let url = 'popUpSave/' + card_id

  ajaxSend(formData, url)
    .then((response) => {
      console.log(response)
      if (!('Errors' in response)) {
        card.innerText = response.name
      }
      form.reset()
      menuContainer.remove()
    })
    .catch((err) => {
      console.error(err)
    })
}

addCardOnLoad()
dragNdropOnLoad()
deleteColumnOnLoad()
deleteCardOnLoad()
showMenuOnLoad()

button.addEventListener('click', addColumn)
