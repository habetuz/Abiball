const callback = function (entries) {
    entries.forEach(entry => {
        if(entry.isIntersecting) entry.target.classList.add("visible")
    });
};

const observer = new IntersectionObserver(callback);

const targets = document.querySelectorAll(".card");
targets.forEach(function (target) {
    observer.observe(target);
});