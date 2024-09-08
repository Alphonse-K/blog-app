document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        // Check if the current page URL matches the link's href
        if (link.href === window.location.href) {
            // Remove .active class from all links
            navLinks.forEach(link => link.classList.remove('active'));

            // Add .active class to the matching link
            link.classList.add('active');
        }
    });
});


// create article
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('formSubmitBtn').addEventListener('click', function(e) {
        e.preventDefault();

        const form = document.getElementById("parentFormSubmitBtn");
        // const form = e.target

        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': form.querySelector('[name="csrfmiddlewaretoken"]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const primaryModal = new bootstrap.Modal(document.getElementById("exampleModal"));
                primaryModal.show(); // Hide the primary modal

            } else {
                const errors = data.errors;
                for (const field in errors) {
                    const errorList = errors[field];
                    const errorHtml = errorList.map(error => `<div class="alert alert-danger">${error.message}</div>`).join('');
                    const fieldElement = document.querySelector(`[name="${field}"]`);
                    if (fieldElement) {
                        // Clear existing error messages for this field
                        const errorContainers = fieldElement.closest('.mb-3').querySelectorAll('.alert.alert-danger');
                        errorContainers.forEach(el => el.remove());
    
                        // Insert new error messages
                        fieldElement.closest('.mb-3').insertAdjacentHTML('beforeend', errorHtml);
                    }
                }                
            }
        })
        .catch(() => {
            alert('An error occurred while submitting the form.');
        });
    });

})


// update article
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submitBtnModalArticleUpdate').addEventListener('click', function(e) {
        e.preventDefault();
        const form = document.getElementById("parentFormSubmitBtnUpdateArticle");
        

        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': form.querySelector('[name="csrfmiddlewaretoken"]').value
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const primaryModal = new bootstrap.Modal(document.getElementById("exampleModalArticleUpdate"));
                primaryModal.show(); // Hide the primary modal

            } else {
                const errors = data.errors;
                for (const field in errors) {
                    const errorList = errors[field];
                    const errorHtml = errorList.map(error => `<div class="alert alert-danger">${error.message}</div>`).join('');
                    const fieldElement = document.querySelector(`[name="${field}"]`);
                    if (fieldElement) {
                        // Clear existing error messages for this field
                        const errorContainers = fieldElement.closest('.mb-3').querySelectorAll('.alert.alert-danger');
                        errorContainers.forEach(el => el.remove());
    
                        // Insert new error messages
                        fieldElement.closest('.mb-3').insertAdjacentHTML('beforeend', errorHtml);
                    }
                }                
            }
        })
        .catch(() => {
            alert('An error occurred while submitting the form.');
        });
    });

})


// delete article
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('articleDeleteBtn').addEventListener('click', function(e) {
        e.preventDefault();

        const form = document.getElementById("articleDeleteBtnForm");
        const nestedModal = new bootstrap.Modal(document.getElementById('nestedModalDeleteArticle'), {});
        const primaryModal = document.getElementById('exampleModalLong');
        const permission = new bootstrap.Modal(document.getElementById('1223345ModalArticleUpdate'));
  
        const formData = new FormData(form);

        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': form.querySelector('[name="csrfmiddlewaretoken"]').value
            }
        })
        .then(response => {
            if (!response.ok) {
                if (response.status === 403) {
                    throw new Error('Permission denied: You do not have the required permission to delete this artist.');
                } else {
                    throw new Error(response.status)
                }             
            }
            return response.json()
        })
        .then(data => {
            if (data.success) {
            primaryModal.style.display = 'none';         
            nestedModal.show();   
        } else {
                alert('An error occurred: ' + JSON.stringify(data.errors));
            }
        })
        .catch((error) => {
            if (error.message.includes('Permission denied')) {
                console.log('deleting')
                primaryModal.style.display = 'none';         
                permission.show()
            } else {
                alert('An error occurred while submitting the form.');
            }
        });
    });


});



