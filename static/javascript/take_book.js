let inputBook = document.getElementById("input_book");
// The list of all object of the boooks
let listBooks = document.querySelectorAll(".book[data-borrowed='False']");
// Add a fonction to the input to chack books.
inputBook.addEventListener("input", () => {
  const text = inputBook.value.toLowerCase();
  listBooks.forEach((book) => {
    const bookTitle = book.textContent.toLowerCase();
    if (bookTitle.includes(text)) {
      book.hidden = true;
    } else {
      book.hidden = false;
    }
  });
});

// Add the click on the button that send information to the server.
let listButtonsBooks = document.querySelectorAll(".book > button");
for (let i = 0; i < listButtonsBooks.length; i++) {
  const element = listButtonsBooks[i];
  element.addEventListener("click", () => {
    sendDateToTheServer(i, "/take_book");
  });
}

function sendDateToTheServer(data, action) {
  fetch(action, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: "data=" + encodeURIComponent(data),
  })
    .then((res) => res.json())
    .then((res) => {
      if (res.data === true) {
        window.location.href = "/show_books";
      }
    });
}
