// Force light theme on React-Select dropdowns
// Dash's dcc.Dropdown uses React-Select which sets inline styles
// that override CSS. This script monitors and forces light styles.

(function() {
    var LIGHT_BG = '#FFFFFF';
    var LIGHT_TEXT = '#1E293B';
    var MUTED = '#64748B';
    var ACCENT = '#2563EB';
    var ACCENT_BG = 'rgba(37, 99, 235, 0.1)';
    var BORDER = 'rgba(0, 0, 0, 0.1)';

    function applyLightStyles() {
        // Select controls (the visible dropdown button)
        document.querySelectorAll('.Select-control').forEach(function(el) {
            el.style.backgroundColor = LIGHT_BG;
            el.style.borderColor = BORDER;
            el.style.color = LIGHT_TEXT;
            el.style.borderRadius = '8px';
        });

        // Value labels
        document.querySelectorAll('.Select-value-label').forEach(function(el) {
            el.style.color = LIGHT_TEXT;
            el.style.fontSize = '12px';
        });

        // Dropdown menus
        document.querySelectorAll('.Select-menu-outer').forEach(function(el) {
            el.style.backgroundColor = LIGHT_BG;
            el.style.borderColor = BORDER;
            el.style.borderRadius = '8px';
            el.style.boxShadow = '0 12px 40px rgba(0,0,0,0.1)';
            el.style.zIndex = '9999';
        });

        document.querySelectorAll('.Select-menu').forEach(function(el) {
            el.style.backgroundColor = LIGHT_BG;
        });

        // Options
        document.querySelectorAll('.Select-option').forEach(function(el) {
            el.style.backgroundColor = LIGHT_BG;
            el.style.color = MUTED;
        });

        // Focused/hovered options
        document.querySelectorAll('.Select-option.is-focused').forEach(function(el) {
            el.style.backgroundColor = ACCENT_BG;
            el.style.color = ACCENT;
        });

        // Selected options
        document.querySelectorAll('.Select-option.is-selected').forEach(function(el) {
            el.style.backgroundColor = ACCENT_BG;
            el.style.color = ACCENT;
            el.style.fontWeight = '600';
        });

        // Arrow
        document.querySelectorAll('.Select-arrow-zone').forEach(function(el) {
            el.style.color = '#64748B';
        });

        // Input search
        document.querySelectorAll('.Select-input input').forEach(function(el) {
            el.style.color = LIGHT_TEXT;
        });

        // No results
        document.querySelectorAll('.Select-noresults').forEach(function(el) {
            el.style.backgroundColor = LIGHT_BG;
            el.style.color = '#64748B';
        });
    }

    // Run on mutations (when dropdowns open/close)
    var observer = new MutationObserver(function() {
        applyLightStyles();
    });

    // Start observing once DOM is ready
    function init() {
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ['class', 'style']
        });
        applyLightStyles();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
