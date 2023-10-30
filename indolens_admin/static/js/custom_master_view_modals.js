document.addEventListener('DOMContentLoaded', () => {
  const viewButtons = document.querySelectorAll('.view-button');
  const viewModal = document.getElementById('viewModal');
  const modal = new bootstrap.Modal(viewModal);
  const viewCategoryID = document.getElementById('viewCategoryID');

  viewButtons.forEach((button) => {
    button.addEventListener('click', (event) => {
      const categoryInfo = event.currentTarget.getAttribute('data-category-info');
      const parsedCategoryInfo = JSON.parse(categoryInfo.replace(/'/g, '"'));

      viewCategoryID.innerHTML = '';

      // Create a table element
      const table = document.createElement('table');
      table.classList.add('table');

      // Loop through the category information object and add key-value pairs to the table
      for (const key in parsedCategoryInfo) {
        if (parsedCategoryInfo.hasOwnProperty(key)) {
          const row = table.insertRow();
          const cell1 = row.insertCell(0);
          const cell2 = row.insertCell(1);
          cell1.innerText = formatKey(key);
          cell2.innerText = parsedCategoryInfo[key];
        }
      }

      viewCategoryID.appendChild(table);

      modal.show();
    });
  });

  function formatKey(key) {
    // Convert key to a more user-friendly format
    const words = key.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    return words;
  }
});
