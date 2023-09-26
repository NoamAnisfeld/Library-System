let listButtons = document.querySelectorAll(".blue-button");
for (let index = 0; index < listButtons.length; index++) {
  listButtons[index].addEventListener("mouseover", overBoxConnect);
  listButtons[index].addEventListener("mouseout", outBoxConnect);
}

console.log(listButtons);

function overBoxConnect() {
  this.style.backgroundColor = "rgb(84, 105, 221)";
}

function outBoxConnect() {
  this.style.backgroundColor = "rgb(19, 39, 153)";
}
