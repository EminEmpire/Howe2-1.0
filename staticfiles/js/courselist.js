  document.addEventListener('DOMContentLoaded', function () {
        const alphabetLinks = document.querySelectorAll('.alphabet-link');
        const courseLists = document.querySelectorAll('.course-list');

        alphabetLinks.forEach(link => {
            link.addEventListener('click', function (event) {
                event.preventDefault();
                const letter = this.getAttribute('data-letter');

                courseLists.forEach(list => {
                    list.style.display = 'none';
                });

                const activeList = document.getElementById(`list-${letter}`);
                if (activeList) {
                    activeList.style.display = 'block';
                }
            });
        });
    });