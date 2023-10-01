let listButtons = document.querySelectorAll(".blue-button");
for (let index = 0; index < listButtons.length; index++) {
  listButtons[index].addEventListener("mouseover", overBoxConect);
  listButtons[index].addEventListener("mouseout", outBoxConect);
}

console.log(listButtons);

function overBoxConect() {
  this.style.backgroundColor = "rgb(84, 105, 221)";
}

function outBoxConect() {
  this.style.backgroundColor = "rgb(19, 39, 153)";
}
