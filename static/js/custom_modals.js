document.addEventListener("DOMContentLoaded", function () {
    var modal = document.querySelector('#operations_modal');
    var modalTitle = document.querySelector('#modal_title');
    var modalContent = document.querySelector('#modal_content');
    var modalSubmit = document.querySelector('#modal_submit');

    document.body.addEventListener('click', function (event) {
        if (event.target.matches('[data-bs-target="#operations_modal"]')) {
            var empId = event.target.getAttribute('data-employee-id');
            var empName = event.target.getAttribute('data-employee-name');
            var actionType = event.target.getAttribute('data-action-type');
            var actionUrl = event.target.getAttribute('data-action-url');
            var role = event.target.getAttribute('data-bs-role');

            // Clear previous content
            modalContent.innerHTML = '';

            if (actionType === 'enable' || actionType === 'disable') {
                modalTitle.textContent = actionType === "enable" ? "Enable " + role + " - " + empName : "Disable " + role + " - " + empName;
                modalContent.innerHTML = `Are you sure you want to ${actionType} ?<br><strong>${empName}</strong>`;
                modalSubmit.href = actionUrl;
                // Hide the form for non-"Allocate" actions

            } else if (actionType === 'accept' || actionType === 'reject') {
                modalTitle.textContent = actionType === "accept" ? "" + role + " - " + empName : "" + role + " - " + empName;
                modalContent.innerHTML = `Are you sure you want to ${actionType} ?<br><strong>${empName}</strong><br>Requested by store : <strong>${event.target.getAttribute('data-action-by')}</strong><br>Requested by store type : <strong>${event.target.getAttribute('data-action-store-type') === "1" ? 'Own store' : 'Franchise store'}</strong>`;
                modalSubmit.href = actionUrl;
                // Hide the form for non-"Allocate" actions

            }  else if (actionType === 'unallocate') {
                modalTitle.textContent = "Unallocate Store - " + empName;
                modalContent.innerHTML = `Are you sure you want to unallocate the store <br><strong>${event.target.getAttribute('data-store-name')}</strong> for <strong>${empName}</strong>?`;
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
