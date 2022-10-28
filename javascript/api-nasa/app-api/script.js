const url = "https://api.nasa.gov/planetary/apod?api_key=";
const api_key = "o0Gj2vkpNJxv2ftUnj6TWwiuLdinVHkuOt93LphB";

function pesquisarImagem() {
  let dataImagem = document.getElementById("dataImagem").value;
  console.log(dataImagem);
  fetchNASAData();
}


const fetchNASAData = async () => {
  try {

    const dataImg = dataImagem.value;
    const response = await fetch(`${url}${api_key}&date=${dataImg}`);
    const data = await response.json();
    console.log("APOD", data);
    displayData(data);
    if(data.code == 400) {
      const erro = document.getElementById('msnError')
      erro.innerHTML = data.msg
    }
  } catch (error) {
    console.log(error);
  }
};

const displayData = (data) => {
  document.getElementById("title").textContent = data.title;
  document.getElementById("date").textContent = data.date;
  document.getElementById("picture").src = data.hdurl;
  document.getElementById("explanation").textContent = data.explanation;
};



