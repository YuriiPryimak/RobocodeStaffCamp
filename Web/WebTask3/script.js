$(document).ready(function() {
    // Обробник кліку для відображення інформації про спортсмена
    $('.athlete-item').click(function() {
        const athleteInfo = $(this).attr('data-info');
        alert(`Інформація: ${athleteInfo}`);
    });

    // Обробка форми додавання улюблених видів спорту
    $('#add-sport-form').submit(function(e) {
        e.preventDefault();

        const sportName = $('#sport-name').val().trim();
        const sportImage = $('#sport-image').val().trim();

        if (sportName && sportImage) {
            const sportItem = $('<div>').addClass('user-sport-item')
                .append($('<img>').attr('src', sportImage).attr('alt', sportName))
                .append($('<p>').text(sportName));

            $('#user-sports').append(sportItem);
            $('#sport-name, #sport-image').val('');
        } else {
            alert('Переконайтесь, що всі поля заповнені!');
        }
    });
});
