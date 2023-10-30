  document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.view-button').forEach(function(button) {
      button.addEventListener('click', function(event) {
      const categoryInfo =event.currentTarget.getAttribute('data-category-info')
       // Populate the modal with the category information
      document.getElementById('viewCategoryID').innerText = categoryInfo;
        // Show the modal without using jQuery
    var viewModal = document.getElementById('viewModal');
    var modal = new bootstrap.Modal(viewModal);
    modal.show();
      });
    });
  });
