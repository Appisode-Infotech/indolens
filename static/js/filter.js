document.addEventListener('DOMContentLoaded', function () {
    updateCategoryDisplay();

    var navLinks = document.querySelectorAll('ul.nav-links a');
    navLinks.forEach(function (link) {
        link.addEventListener('click', function () {
            var selectedCategory = this.getAttribute('href').substring(8);
            var tableRows = document.querySelectorAll('table tbody tr');
            if (selectedCategory !== "all") {
                tableRows.forEach(function (row) {
                    row.style.display = 'none';
                });
                Array.from(tableRows).forEach(function (row) {
                    if (row.getAttribute('data-category') === selectedCategory) {
                        row.style.display = 'table-row';
                    }
                });
            } else {
                tableRows.forEach(function (row) {
                    row.style.display = 'table-row';
                });
            }

            navLinks.forEach(function (navLink) {
                navLink.classList.remove('active');
            });
            this.classList.add('active');
//        updateListControls after filter
        });
    });


    function updateCategoryDisplay() {
        var currentHash = window.location.hash.substring(8) || "all";
        var filterLink = document.querySelector('.nav-link.filter[href="#filter-' + currentHash + '"]');
        if (filterLink) {
            filterLink.classList.add("active");
        }

        var tableRows = document.querySelectorAll('table tbody tr');
        if (currentHash !== "all") {
            tableRows.forEach(function (row) {
                row.style.display = 'none';
            });
            Array.from(tableRows).forEach(function (row) {
                if (row.getAttribute('data-category') === currentHash) {
                    row.style.display = 'table-row';
                }
            });
        }
//        updateListControls after filter
    }
});
