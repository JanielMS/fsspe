const menuBnt = document.getElementById("nav_menu_btn");
const navLinks = document.getElementById("nav_links");
const links = document.querySelectorAll(".nav-link");
const menuBtnIcon = document.querySelector("i");

console.log(links)
menuBnt.addEventListener("click", (e) => {
    navLinks.classList.toggle("open");

    const isOpen = navLinks.classList.contains("open");
    menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});
//     navLinks.classList.remove("open");
//     menuBtnIcon.setAttribute("class", "ri-menu-line");
// });

links.forEach(link => {
    link.addEventListener("click", (e) => {
        navLinks.classList.remove("open");
        menuBtnIcon.setAttribute("class", "ri-menu-line");
    });
}
);