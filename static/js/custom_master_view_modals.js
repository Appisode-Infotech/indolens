document.addEventListener('DOMContentLoaded', () => {
    document.body.addEventListener('click', (event) => {
        const target = event.target;
        // Check if the clicked element is a view button
        if (target.classList.contains('view-button')) {
            const viewModal = document.getElementById('viewModal');
            const modal = new bootstrap.Modal(viewModal);
            const viewCategoryID = document.getElementById('viewCategoryID');

            const categoryInfo = target.getAttribute('data-category-info');
            const sanitizedCategoryInfo = categoryInfo.replace(/None/g, '""');
            const parsedCategoryInfo = JSON.parse(sanitizedCategoryInfo.replace(/'/g, '"'));

            viewCategoryID.innerHTML = '';

            // Create a table element
            const table = document.createElement('table');
            table.classList.add('table');

            // Loop through the category information object and add key-value pairs to the table
            for (const key in parsedCategoryInfo) {
                if (parsedCategoryInfo.hasOwnProperty(key)) {
                    if (key === 'created_by' || key === 'last_updated_by' || parsedCategoryInfo[key] == '') {
                        continue;
                    }
                    const row = table.insertRow();
                    const cell1 = row.insertCell(0);
                    const cell2 = row.insertCell(1);
                    cell1.innerText = formatKey(key);
                    if (key == 'status' && parsedCategoryInfo[key] == '1') {
                        cell2.innerText = "Active";
                    } else if (key == 'status' && parsedCategoryInfo[key] == '0') {
                        cell2.innerText = "Inactive";
                    } else {
                        cell2.innerText = parsedCategoryInfo[key];
                    }
                }
            }
            viewCategoryID.appendChild(table);
            modal.show();
        }
    });

    function formatKey(key) {
        // Convert key to a more user-friendly format
        const words = key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
        return words;
    }
});
