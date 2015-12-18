$(document).ready(function(){
    $('.ns-list-dropdown').hide();
    $('#ns-btn-dropdown').click(
        function(){
            $('.ns-list-dropdown').slideToggle()
        }
    );
});
