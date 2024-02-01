document.addEventListener("DOMContentLoaded", function () {
    var modal = document.querySelector('#operations_modal');
    var modalTitle = document.querySelector('#modal_title');
    var modalContent = document.querySelector('#modal_content');
    var modalSubmit = document.querySelector('#modal_submit');
    var modalForm = document.querySelector('.allocate-store-form'); // Select the existing form

    document.body.addEventListener('click', function (event) {
        if (event.target.matches('[data-bs-target="#operations_modal"]')) {
            var empId = event.target.getAttribute('data-employee-id');
            var empName = event.target.getAttribute('data-employee-name');
            var actionType = event.target.getAttribute('data-action-type');
            var actionUrl = event.target.getAttribute('data-action-url');
            var role = event.target.getAttribute('data-bs-role');

            if (actionType === 'enable' || actionType === 'disable') {
                modalTitle.textContent = actionType === "enable" ? "Enable " + role + " - " + empName : "Disable " + role + " - " + empName;
                modalContent.innerHTML = `Are you sure you want to ${actionType} ?<br><strong>${empName}</strong> (ID: ${empId})`;
                modalSubmit.href = actionUrl;
                // Hide the form for non-"Allocate" actions
            } else if (actionType === 'allocate') {
                document.getElementById('footer_div').style.display = 'none';
                modalTitle.textContent = "Allocate store for - " + empName;
                document.getElementById('emp_id').value = empId;
                modalSubmit.href = actionUrl;
                // Show the form for "Allocate" action
            } else if (actionType === 'unallocate') {
                modalTitle.textContent = "Unallocate Store - " + empName;
                modalContent.innerHTML = `Are you sure you want to unallocate the store <br><strong>${event.target.getAttribute('data-store-name')}</strong> for <strong>${empName}</strong> (ID: ${empId})?`;
                modalSubmit.href = actionUrl;
                // Hide the form for "Unallocate" action
            }

            // Use data-bs-toggle and data-bs-target attributes to trigger the modal
            var targetModal = event.target.getAttribute('data-bs-target');
            var backdrop = event.target.getAttribute('data-bs-backdrop');
            modal.setAttribute('data-bs-target', targetModal);
            modal.setAttribute('data-bs-backdrop', backdrop);
        }
    });
});
