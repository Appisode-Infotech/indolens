document.addEventListener("DOMContentLoaded", function () {
    var modal = document.querySelector('#allocate_multi_store_modal');
    var modalTitle = document.querySelector('#allocate_modal_title');
    var modalContent = document.querySelector('#modal_content');
    var modalSubmit = document.querySelector('#modal_submit');
    var modalForm = document.querySelector('.allocate-store-form2'); // Select the existing form

    document.body.addEventListener('click', function (event) {
        if (event.target.matches('[data-bs-target="#allocate_multi_store_modal"]')) {
            var empId = event.target.getAttribute('data-employee-id');
            var empName = event.target.getAttribute('data-employee-name');
            var actionType = event.target.getAttribute('data-action-type');
            var actionUrl = event.target.getAttribute('data-action-url');
            var formAction = event.target.getAttribute('data-bs-action');
            var role = event.target.getAttribute('data-bs-role');

          if (actionType === 'allocate') {
          modalForm.action = formAction;
                modalTitle.textContent = "Allocate store for - " + empName;
                document.getElementById('emp_id').value = empId;
            }

            // Use data-bs-toggle and data-bs-target attributes to trigger the modal
            var targetModal = event.target.getAttribute('data-bs-target');
            var backdrop = event.target.getAttribute('data-bs-backdrop');
            modal.setAttribute('data-bs-target', targetModal);
            modal.setAttribute('data-bs-backdrop', backdrop);
        }
    });
});
