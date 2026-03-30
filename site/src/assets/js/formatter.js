const author_content = document.querySelector('#reader-author')
const story_content = document.querySelector('#reader-story')

function format_author_content() {
    const cleaned_content = author_content.innerHTML.slice(0, author_content.innerHTML.indexOf("Obras:"))
    author_content.innerHTML = cleaned_content
}

function format_story_content() {
    const cleaned_content = story_content.innerHTML.slice(0, story_content.innerHTML.indexOf("Volver al autor"))
    story_content.innerHTML = cleaned_content
}

if (author_content) {
    format_author_content()
} else if (story_content) {
    format_story_content()
}
