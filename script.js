const reveals = document.querySelectorAll(".reveal");

const observer = new IntersectionObserver(
  entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
      }
    });
  },
  { threshold: 0.15 }
);

reveals.forEach(reveal => observer.observe(reveal));

const playBtn = document.getElementById("playAudioBtn");

playBtn.addEventListener("click", () => {
  alert("Audio would play here! Backend will handle TTS soon 😉");
});
