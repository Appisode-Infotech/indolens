document.addEventListener("DOMContentLoaded", function () {
    var operationsButtons = document.querySelectorAll('[data-bs-target="#operations_modal"]');
    var modal = document.getElementById('operations_modal');
    var modalTitle = document.getElementById('modal_title');
    var modalContent = document.getElementById('modal_content');
    var modalSubmit = document.getElementById('modal_submit');
    var modalForm = document.querySelector('.allocate-store-form'); // Select the existing form

    operationsButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            var empId = event.currentTarget.getAttribute('data-employee-id');
            var empName = event.currentTarget.getAttribute('data-employee-name');
            var actionType = event.currentTarget.getAttribute('data-action-type');
            var actionUrl = event.currentTarget.getAttribute('data-action-url');
            var role = event.currentTarget.getAttribute('data-bs-role');

            if (actionType === 'enable' || actionType === 'disable') {
                modalTitle.textContent = actionType === "enable" ? "Enable " +role+" - " + empName : "Disable " +role+ "- " + empName;
                modalContent.innerHTML = `Are you sure you want to ${actionType} ?<br><strong>${empName}</strong> (ID: ${empId})`;
                modalSubmit.href = actionUrl;
                // Hide the form for non-"Allocate" actions
                modalForm.style.display = 'none';
            } else if (actionType === 'allocate') {
                document.getElementById('footer_div').style.display = 'none';
                modalTitle.textContent = "Allocate store for - " + empName;
                document.getElementById('emp_id').value = empId;
                modalSubmit.href = actionUrl;
                // Show the form for "Allocate" action
                modalForm.style.display = 'block';
            } else if (actionType === 'unallocate') {
                modalTitle.textContent = "Unallocate Store - " + empName;
                modalContent.innerHTML = `Are you sure you want to unallocate the store <br><strong>${event.currentTarget.getAttribute('data-store-name')}</strong> for <strong>${empName}</strong> (ID: ${empId})?`;
                modalSubmit.href = actionUrl;
                // Hide the form for "Unallocate" action
                modalForm.style.display = 'none';
            }

             // Use data-bs-toggle and data-bs-target attributes to trigger the modal
            var targetModal = event.currentTarget.getAttribute('data-bs-target');
            var backdrop = event.currentTarget.getAttribute('data-bs-backdrop');
            modal.setAttribute('data-bs-target', targetModal);
            modal.setAttribute('data-bs-backdrop', backdrop);
        });
    });
});
