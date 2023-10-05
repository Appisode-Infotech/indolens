document.addEventListener('DOMContentLoaded', function () {
        // Function to create a preview container for a file
        function createPreviewContainer(file, inputElement, previewsElement) {
            const previewContainer = document.createElement('div');
            previewContainer.classList.add('d-flex', 'mb-3', 'pb-3', 'border-bottom', 'media');

            const imageContainer = document.createElement('div');
            imageContainer.classList.add('border', 'border-300', 'p-2', 'rounded-2', 'me-2');

            if (file.type.startsWith('image/')) {
                // If it's an image, display the image preview
                const image = document.createElement('img');
                image.classList.add('rounded-2', 'dz-image');
                image.src = URL.createObjectURL(file);
                image.onload = function () {
                    URL.revokeObjectURL(image.src);
                };
                image.style.maxWidth = '50px'; // Adjust the maximum width as needed
                image.style.maxHeight = '50px'; // Adjust the maximum height as needed
                imageContainer.appendChild(image);
            } else {
                // If it's not an image, display the file icon
                const fileIcon = document.createElement('i');
                fileIcon.classList.add('fas', 'fa-file'); // Add your file icon classes here
                imageContainer.appendChild(fileIcon);
            }

            previewContainer.appendChild(imageContainer);

            const infoContainer = document.createElement('div');
            infoContainer.classList.add('flex-1', 'd-flex', 'flex-between-center');

            const infoLeft = document.createElement('div');

            const fileName = document.createElement('h6');
            fileName.textContent = file.name;

            const fileInfo = document.createElement('div');
            fileInfo.classList.add('d-flex', 'align-items-center');

            const fileSize = document.createElement('p');
            fileSize.classList.add('mb-0', 'fs--1', 'text-400', 'lh-1');
            fileSize.textContent = formatFileSize(file.size);

            const progressContainer = document.createElement('div');
            progressContainer.classList.add('dz-progress');

            const uploadProgress = document.createElement('span');
            uploadProgress.classList.add('dz-upload');
            uploadProgress.dataset.dzUploadprogress = '';

            progressContainer.appendChild(uploadProgress);

            fileInfo.appendChild(fileSize);
            fileInfo.appendChild(progressContainer);

            const errorMessage = document.createElement('span');
            errorMessage.classList.add('fs--2', 'text-danger');
            errorMessage.dataset.dzErrormessage = '';

            infoLeft.appendChild(fileName);
            infoLeft.appendChild(fileInfo);
            infoLeft.appendChild(errorMessage);

            const dropdownContainer = document.createElement('div');
            dropdownContainer.classList.add('dropdown', 'font-sans-serif');

            const dropdownButton = document.createElement('button');
            dropdownButton.classList.add('btn', 'btn-link', 'text-600', 'btn-sm', 'dropdown-toggle', 'btn-reveal', 'dropdown-caret-none');
            dropdownButton.type = 'button';
            dropdownButton.dataset.bsToggle = 'dropdown';
            dropdownButton.setAttribute('aria-haspopup', 'true');
            dropdownButton.setAttribute('aria-expanded', 'false');

            const ellipsisIcon = document.createElement('span');
            ellipsisIcon.classList.add('fas', 'fa-ellipsis-h');

            dropdownButton.appendChild(ellipsisIcon);

            const dropdownMenu = document.createElement('div');
            dropdownMenu.classList.add('dropdown-menu', 'dropdown-menu-end', 'border', 'py-2');

            const removeFileItem = document.createElement('a');
            removeFileItem.classList.add('dropdown-item');
            removeFileItem.href = '#!';
            removeFileItem.dataset.dzRemove = 'data-dz-remove';
            removeFileItem.textContent = 'Remove File';

            dropdownMenu.appendChild(removeFileItem);

            dropdownContainer.appendChild(dropdownButton);
            dropdownContainer.appendChild(dropdownMenu);

            infoContainer.appendChild(infoLeft);
            infoContainer.appendChild(dropdownContainer);

            previewContainer.appendChild(infoContainer);

            // Add a click event to remove the file preview
            removeFileItem.addEventListener('click', function () {
                previewContainer.remove();

                const currentFiles = Array.from(inputElement.files);
                const currentIndex = currentFiles.indexOf(file);

                if (currentIndex !== -1) {
                    currentFiles.splice(currentIndex, 1);
                    // Create a new FileList with the updated files
                    const newFileList = new DataTransfer();
                    currentFiles.forEach((file) => {
                        newFileList.items.add(file);
                    });
                    // Update the input field's files property with the new FileList
                    inputElement.files = newFileList.files;
                }
            });

            previewsElement.appendChild(previewContainer);
        }

        // Function to format file size for display
        function formatFileSize(size) {
            if (size < 1024) {
                return size + ' B';
            } else if (size < 1024 * 1024) {
                return (size / 1024).toFixed(2) + ' KB';
            } else {
                return (size / (1024 * 1024)).toFixed(2) + ' MB';
            }
        }

        // Attach event listeners for both input elements
        const documentInput1 = document.getElementById('document1');
        const documentPreviews1 = document.getElementById('documentPreviews');
        documentInput1.addEventListener('change', function () {
            const files = documentInput1.files;
            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                createPreviewContainer(file, documentInput1, documentPreviews1);
            }
        });

        const documentInput2 = document.getElementById('document2');
        const documentPreviews2 = document.getElementById('document2Previews');
        documentInput2.addEventListener('change', function () {
            const files = documentInput2.files;
            for (let i = 0; i < files.length; i++) {
                const file = files[i];
                createPreviewContainer(file, documentInput2, documentPreviews2);
            }
        });
    });