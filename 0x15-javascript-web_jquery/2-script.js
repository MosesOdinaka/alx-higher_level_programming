// Selects the HTML element with the id 'red_header' within a 'DIV'
const clickableElement = $('DIV#red_header');

// Defines the color to be applied
const colorToApply = '#FF0000';

// Defines the action to be performed on click
const onClickAction = function () {
  // Selects the HTML element with the tag name 'HEADER'
  const headerElement = $('HEADER');

  // Applies the color to the selected element
  headerElement.css('color', colorToApply);
};

// Binds the click event to the action
clickableElement.click(onClickAction);
