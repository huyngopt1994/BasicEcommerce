/*
  This file must be imported immediately-before the close-</body> tag,
  and after JQuery and Underscore.js are imported.
*/
/**
  The number of milliseconds to ignore clicks on the *same* like
  button, after a button *that was not ignored* was clicked. Used by
  `$(document).ready()`.
 
  Equal to <code>500</code>.
 */
var MILLS_TO_IGNORE_LIKES = 500;
/**
   Executes a like click. Triggered by clicks on the various yes/no links.
 */
var processLike = function()  {
 
   //In this scope, "this" is the button just clicked on.
   //The "this" in processServerResponse is *not* the button just clicked
   //on.
   var $button_just_clicked_on = $(this);
 
   //The value of the "data-color_id" attribute.
   var color_id = $button_just_clicked_on.data('color_id');
 
   var processServerResponse = function(sersverResponse_data, textStatus_ignored,
                                        jqXHR_ignored)  {
      //alert("sf sersverResponse_data='" + sersverResponse_data + "', textStatus_ignored='" + textStatus_ignored + "', jqXHR_ignored='" + jqXHR_ignored + "', color_id='" + color_id + "'");
      $('#toggle_color_like_cell_' + color_id).html(sersverResponse_data);
   }
 
   var config = {
      url: LIKE_URL_PRE_ID + color_id + '/',
      dataType: 'html',
      success: processServerResponse
      //Should also have a "fail" call as well.
   };
   $.ajax(config);
};
/**
   The Ajax "main" function. Attaches the listeners to the elements on
   page load, each of which only take effect every
   <link to MILLS_TO_IGNORE_LIKES> seconds.
 
   This protection is only against a single user pressing buttons as fast
   as they can. This is in no way a protection against a real DDOS attack,
   of which almost 100% bypass the client (browser) (they instead
   directly attack the server). Hence client-side protection is pointless.
 
   - http://stackoverflow.com/questions/28309850/how-much-prevention-of-rapid-fire-form-submissions-should-be-on-the-client-side
 
   The protection is implemented via Underscore.js' debounce function:
  - http://underscorejs.org/#debounce
 
   Using this only requires importing underscore-min.js. underscore-min.map
   is not needed.
 */
$(document).ready(function()  {
  /*
    There are many buttons having the class
 
      td__toggle_color_like_button
 
    This attaches a listener to *every one*. Calling this again
    would attach a *second* listener to every button, meaning each
    click would be processed twice.
   */
  $('.td__toggle_color_like_button').click(_.debounce(processLike,
      MILLS_TO_IGNORE_LIKES, true));
  /*
    Warning: Placing the true parameter outside of the debounce call:
 
    $('#color_search_text').keyup(_.debounce(processSearch,
        MILLS_TO_IGNORE_SEARCH), true);
 
    results in "TypeError: e.handler.apply is not a function".
   */
});