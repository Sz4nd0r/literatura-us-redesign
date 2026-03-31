const links = document.querySelectorAll('a.link_style');

links.forEach(link => {
    link.classList.add('hover:text-blue-600', 'transition-colors', 'underline');
});

const cards = document.querySelectorAll('a.card_style');

cards.forEach(card => {
    card.classList.add('group', 'bg-white', 'p-1', 'border', 'border-gray-200', 'shadow-sm', 'hover:shadow-xl', 'transition-all', 'duration-300', 'rounded-none', 'relative', 'flex', 'items-center', 'justify-between');
});

const lines = document.querySelectorAll('.line_style');

lines.forEach(line => { // Default line style
    line.classList.add('absolute', 'inset-y-0', 'left-0', 'w-1', 'bg-gray-100', 'group-hover:bg-blue-600', 'transition-colors', 'duration-300');
});

