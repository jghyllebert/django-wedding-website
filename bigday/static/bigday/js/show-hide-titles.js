// NAV transparent
new Waypoint({
  element: document.getElementById('veracruz'),
  handler: function(direction) {
    $('#top-menu').toggleClass('bg-transparent')
    $('#hamburger-menu').toggleClass('bg-transparent')
    $('#top-menu').toggleClass('bg-black')
    $('#hamburger-menu').toggleClass('bg-black')
  },
  offset: 120
})


// SHOW/HIDE FIXED TITLES
new Waypoint({
  element: document.getElementById('veracruz--intro'),
  handler: function(direction) {
    console.log(direction);
    $hidden = $('#veracruz--title__hidden')
    if($hidden.length > 0) {
      $hidden.attr('id', 'veracruz--title')
    } else {
      $('#veracruz--title').attr('id', 'veracruz--title__hidden')
    }
  },
  offset: "40vw"
})

new Waypoint({
  element: document.getElementById('veracruz--todo-malecon'),
  handler: function(direction) {
    console.log(direction);
    $hidden = $('#where-to-stay--title__hidden')
    if($hidden.length > 0) {
      console.log('SHOW TITLE');
      $hidden.attr('id', 'where-to-stay--title')
    } else {
      console.log('HIDE TITLE');
      $('#where-to-stay--title').attr('id', 'where-to-stay--title__hidden')
    }
  },
  offset: "40vw"
})
