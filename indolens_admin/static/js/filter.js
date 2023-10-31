$(document).ready(function() {
        updateCategoryDisplay();
        $('ul.nav-links a').click(function() {
            var selectedCategory = $(this).attr('href').substring(8); // Get the category name after '#filter-'
            var $tableRows = $('table tbody tr');
            if (selectedCategory !== "all") {
                $tableRows.hide().filter('[data-category="' + selectedCategory + '"]').show();
            } else {
                $tableRows.show();
            }
            $('ul.nav-links a').removeClass('active');
            $(this).addClass('active');
            updateDataListInfo();
        });
        function updateDataListInfo() {
            var $visibleRows = $('table tbody tr:visible');
            var totalRows = $visibleRows.length;
            var startIndex = Math.min(totalRows, 1);
            var endIndex = Math.min(totalRows, totalRows);
            $('[data-list-info]').text(startIndex + ' to ' + endIndex + ' Items of ' + totalRows);
        }
        function updateCategoryDisplay() {
            var currentHash = window.location.hash.substring(8) || "all"; // Get the category name after '#filter-'
            $('.nav-link.filter[href="#filter-' + currentHash + '"]').addClass("active");
            var $tableRows = $('table tbody tr');
            if (currentHash !== "all") {
                $tableRows.hide().filter('[data-category="' + currentHash + '"]').show();
            }

            // Call the function to update data-list-info
            updateDataListInfo();
        }
    });