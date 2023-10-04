let inputBook = document.getElementById("input_book");
// The list of all object of the boooks
let listBooks = document.querySelectorAll(".book");
// Show only the books that not borrowed.
listBooks.forEach((book) => {
  if (book.getAttribute("borrowed") == "True") {
    // To show.
    book.style.display = "list-item";
  } else {
    // To not show
    book.style.display = "none";
  }
});
// Add a fonction to the input to chack books.
inputBook.addEventListener("input", () => {
  const text = inputBook.value.toLowerCase();
  listBooks.forEach((book) => {
    const bookTitle = book.textContent.toLowerCase();
    if (bookTitle.includes(text) && book.getAttribute("borrowed") == "True") {
      // To show.
      book.style.display = "list-item";
    } else {
      // To not show.
      book.style.display = "none";
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
  const xhr = new XMLHttpRequest();
  xhr.open("POST", action, true);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  // Send the POST request with the data
  xhr.send("data=" + encodeURIComponent(data));
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Handle the response from the server
      const response = JSON.parse(xhr.responseText);
      console.log(response);
      if (response["data"] == "true") {
        window.location.href = "/show_books";
      }
    }
  };
}
