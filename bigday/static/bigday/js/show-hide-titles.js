// NAV transparent
new Waypoint({
  element: document.getElementById('our-story'),
  handler: function(direction) {
    $('#top-menu').toggleClass('bg-transparent')
    $('#top-menu').toggleClass('bg-black')
  },
  offset: 120
})


// SHOW/HIDE FIXED TITLES
new Waypoint({
  element: document.getElementById('our-story--story'),
  handler: function(direction) {
    $hidden = $('#our-story--title__hidden')
    if($hidden.length > 0) {
      $hidden.attr('id', 'our-story--title')
      $('#veracruz--title').attr('id', 'veracruz--title__hidden')
    } else {
      $('#our-story--title').attr('id', 'our-story--title__hidden')
      $('#veracruz--title__hidden').attr('id', 'veracruz--title')
    }
  },
  offset: "40vw"
})

new Waypoint({
  element: document.getElementById('veracruz--intro'),
  handler: function(direction) {
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
    $hidden = $('#where-to-stay--title__hidden')
    if($hidden.length > 0) {
      $hidden.attr('id', 'where-to-stay--title')
    } else {
      $('#where-to-stay--title').attr('id', 'where-to-stay--title__hidden')
    }
  },
  offset: "40vw"
})
