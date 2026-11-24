let inputSearch = document.getElementById("search-input");
//let iconSearch = document.getElementById("search-icon");
let matchSearch = document.getElementById("search-list");
let mensaje_error = document.getElementById("mensaje-error")
let populateMatchList = (matchList) => {
  // delete previous childs
  while (matchSearch.firstChild) {
    matchSearch.removeChild(matchSearch.firstChild);
  }

  // si no hay coincidencias se muestra el menssaje de error
  if (matchList.length === 0) {
    matchSearch.hidden = true;
    mensaje_error.hidden = false;
    return;
  }

  for (let confTitle of matchList) {
    let option = document.createElement("p");
    
    option.innerText = `${confTitle.ave} Registrado por: ${confTitle.nombre} en:${confTitle.comuna} en la fecha: ${confTitle.dia})`;
    matchSearch.append(option);
  }
  matchSearch.hidden = false;
};



let fetchAJAX = (url) => {
  
  fetch(url, {
    mode: "cors",
    credentials: "include",
  }) // 1 acceder al url
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json(); // 2 parseamos el response a un json
    })
    .then((ajaxResponse) => {
      populateMatchList(ajaxResponse["data"]); // 3 le pasamos el data a populate...()
    })
    .catch((error) => {
      console.error(
        "There has been a problem with your fetch operation:",
        error
      );
    });
};

let ajaxMethod = "fetch";

let ajaxHandlerMapper = {
  fetch: fetchAJAX,
};

let handleAJAX = (event) => {
  let ajaxHandler = ajaxHandlerMapper[ajaxMethod];
  ajaxHandler(`${window.origin}/get-avis/${event.target.value}`);
};

inputSearch.addEventListener("input", handleAJAX);

