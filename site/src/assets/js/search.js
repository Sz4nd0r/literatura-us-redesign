const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => document.querySelectorAll(selector);

const search_button = $("#search_button");
const clear_button = $("#clear");
const search_input = $("#search_input");

search_button.addEventListener("click", search);
clear_button.addEventListener("click", clear);


function search(event) {
    event.preventDefault();
    const query = search_input.value;
    const text_items = $$(".search-term");

    text_items.forEach((text_item) => {
        // 1. Normalize to separate characters from accents
        // 2. Use regex [\u0300-\u036f] to target and remove the accent marks
        const cleanText = text_item.textContent.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

        if (cleanText.toLowerCase().includes(query.toLowerCase())) {
            text_item.parentElement.style.display = "block";
        } else {
            text_item.parentElement.style.display = "none";
        }
    });
}

function clear(event) {
    search_input.value = "";
    search(event);
}
