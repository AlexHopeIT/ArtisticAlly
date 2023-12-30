document.addEventListener('DOMContentLoaded', function() {
    var alertElements = document.querySelectorAll('.alert');
    alertElements.forEach(function(alert) {
        setTimeout(function() {
            alert.style.opacity = '0';
            setTimeout(function() {
                alert.style.display = 'none';
            }, 600);
        }, 3000);
    });
});