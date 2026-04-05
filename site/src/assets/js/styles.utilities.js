/**
 * Typography Configuration
 * These variables are tied to CSS variables in index.css
 */
const FONTS = {
    title: "font-['Playfair_Display']",
    body: "font-['Merriweather']",
    quote: "font-['EB_Garamond']",
    ui: "font-['Inter']",
    meta: "font-['Work_Sans']",
};

const COLORS = {
    paper: "bg-[var(--paper-color)]",
    paperDark: "bg-[var(--paper-dark)]",
    text: "text-[var(--text-main)]",
    textMuted: "text-[var(--text-muted)]",
    accent: "text-[var(--accent-color)]",
    border: "border-[var(--border-color)]",
};


// Utility: postick_style (compact, paper-like, for author links)
document.querySelectorAll("a.postick_style").forEach((postick) => {
    postick.classList.add(
        FONTS.title,
        COLORS.paper,
        "border",
        "shadow",
        "hover:shadow-md",
        "transition-all",
        "duration-200",
        "px-3",
        "py-1.5",
        "flex",
        "items-center",
        "gap-2",
        "text-base",
        COLORS.text,
        "no-underline",
        "rounded-none",
        "w-full",
        "cursor-pointer",
        "focus:outline-none",
        "focus:ring-2",
        "focus:ring-blue-200",
        "relative",
        "group",
    );
});
// Utility: link_style
document.querySelectorAll("a.link_style").forEach((link) => {
    link.classList.add(
        "hover:text-blue-600",
        "transition-colors",
        "underline",
        "focus:outline-none",
        "focus:ring-2",
        "focus:ring-blue-400",
        "rounded-sm",
    );
});

// Utility: card_style (paper-like, sharp edges, soft shadow, subtle border, generous padding)
document.querySelectorAll("a.card_style").forEach((card) => {
    card.classList.add(
        "group",
        COLORS.paper,
        "p-5",
        "border",
        "shadow-[0_2px_12px_rgba(0,0,0,0.06)]",
        "hover:shadow-[0_4px_24px_rgba(0,0,0,0.10)]",
        "transition-all",
        "duration-300",
        "rounded-none",
        "relative",
        "flex",
        "items-center",
        "gap-2",
        "justify-between",
        "w-full",
        "min-h-[56px]",
        "sm:p-6",
        "sm:min-h-[64px]",
        FONTS.body,
        COLORS.text,
        'before:content-[""]',
        "before:absolute",
        "before:inset-0",
        "before:bg-[repeating-linear-gradient(135deg,rgba(240,240,220,0.08)_0_2px,transparent_2px_8px)]",
        "before:pointer-events-none",
        "before:opacity-60",
    );
});

// Utility: line_style (mobile-first, DRY)
document.querySelectorAll(".line_style").forEach((line) => {
    line.classList.add(
        "absolute",
        "left-1",
        "h-8",
        "w-1",
        "bg-gray-100",
        "group-hover:bg-blue-600",
        "transition-colors",
        "duration-300",
        "rounded-full",
        "sm:h-10",
    );
});

// bottom line style
document.querySelectorAll(".line_style_bottom").forEach((line) => {
    line.classList.add(
        "absolute",
        "inset-x-0",
        "bottom-0",
        "h-1",
        "w-full",
        "bg-gray-100",
        "group-hover:bg-blue-600",
        "transition-colors",
        "duration-300",
        "rounded-full",
    );
});

// Title style
document.querySelectorAll("h1.title_style").forEach((title) => {
    title.classList.add(
        "text-2xl",
        "sm:text-4xl",
        FONTS.title,
        "font-bold",
        "text-gray-900",
        "leading-tight",
        "mb-4",
    );
});

// Utility: quote_style
document.querySelectorAll(".quote_style").forEach((quote) => {
    quote.classList.add(
        FONTS.quote,
        "italic",
        "text-xl",
        COLORS.text,
        "border-l-4",
        "pl-6",
        "py-2",
        "my-8",
        "leading-relaxed",
    );
});

// Utility: citation_style
document.querySelectorAll(".citation_style").forEach((citation) => {
    citation.classList.add(
        FONTS.meta,
        "text-sm",
        "uppercase",
        "tracking-widest",
        COLORS.textMuted,
        "font-medium",
    );
});

// Utility: button_style
document.querySelectorAll(".button_style").forEach((button) => {
    button.classList.add(
        FONTS.ui,
        "px-6",
        "py-2",
        "bg-[var(--text-main)]",
        "text-[var(--paper-color)]",
        "hover:opacity-90",
        "transition-opacity",
        "duration-200",
        "font-medium",
        "tracking-wide",
    );
});


