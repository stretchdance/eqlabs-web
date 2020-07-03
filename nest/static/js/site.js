
$(function() {

// Get the header
var header = document.getElementById("stickyheadernav");
// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function stickyHeader() {
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}    
// When the user scrolls the page, execute myFunction 
window.onscroll = function() {stickyHeader()};
stickyHeader();

var win = $(window);
var allMods = $(".module");

// Already visible modules
allMods.each(function(i, el) {

var el = $(el);
if (el.visible(true)) {
    el.addClass("already-visible"); 
} 
});

function checkscroll(event) {
    // console.log("Window scrolling...");
    allMods.each(function(i, el) {
        var el = $(el);
        if (el.visible(true)) {
            // console.log("Newly visible element");
            el.addClass("come-in"); 
        } 
    });
}
checkscroll(null);
win.scroll(checkscroll);

});

// function isVis(el) {
//     console.log(`Is ${window.pageYOffset + screen.height} greater than ${el.getBoundingClientRect().top}?`);
//     if ((window.pageYOffset + screen.height) > el.getBoundingClientRect().top) return true;
//     return false;
// }