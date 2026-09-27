// Toggle animation on click
const flag = document.getElementById('flag');
const chakra = document.querySelector('.chakra');
flag.addEventListener('click', ()=>{
  const paused = flag.classList.toggle('paused');
  if(paused){
    chakra.style.animationPlayState = 'paused';
  } else {
    chakra.style.animationPlayState = 'running';
  }
});
