// breadcrumbs.js
document.addEventListener('DOMContentLoaded', function() {
    updateBreadcrumbs();
});

function updateBreadcrumbs() {
    var pathArray = window.location.pathname.split('/').filter(Boolean);
    var contentDivs = document.getElementsByClassName('content');

    // Check if there are multiple elements with the 'content' class
    if (contentDivs.length > 0) {
        // Assuming you want to update the first 'content' div found
        var contentDiv = contentDivs[0];
        var breadcrumbsContainer = createBreadcrumbsContainer(pathArray);

        // Insert breadcrumbs before the existing content
        contentDiv.insertBefore(breadcrumbsContainer, contentDiv.firstChild);
    } else {
        console.error("Element with class 'content' not found");
    }
}

function createBreadcrumbsContainer(pathArray) {
    var breadcrumbsContainer = document.createElement('nav');
    breadcrumbsContainer.setAttribute('aria-label', 'breadcrumb');

    var olElement = document.createElement('ol');
    olElement.classList.add('breadcrumb', 'mb-3');

     var liElement = document.createElement('li');
     liElement.classList.add('breadcrumb-item');
    // Create a span for the left arrow
    var arrowSpan = document.createElement('span');
    arrowSpan.innerHTML = '&#9664; '; // You can customize the arrow symbol

    liElement.appendChild(arrowSpan);

    var currentPath = '/';
    var liElement = document.createElement('li');
    liElement.classList.add('breadcrumb-item');
    var aElement = document.createElement('a');
    aElement.href = 'javascript:void(0);';
    aElement.onclick = function() {
    window.history.back();
    };
    aElement.textContent = 'Go back'; // Update this to the actual text
    liElement.appendChild(arrowSpan);
    liElement.appendChild(aElement);
    olElement.appendChild(liElement);


    breadcrumbsContainer.appendChild(olElement);

    return breadcrumbsContainer;
}
