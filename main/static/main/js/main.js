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

const delBoard = (e) => {
  console.log(e.target.parentNode.parentNode.id)
  let board_id = parseInt(e.target.parentNode.parentNode.id)
  let url = 'deleteBoard/' + board_id

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

const deleteBoardOnLoad = () => {
  const deleteBtns = document.querySelectorAll('.btn-del')
  console.log(deleteBtns)

  deleteBtns.forEach((del) => {
    del.addEventListener('click', delBoard)
  })
}

deleteBoardOnLoad()
