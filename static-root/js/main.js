
var donateAmount = () => {
        var donateOther = document.getElementById("donateAmountOther");
        if (donateOther != null ) {
            if (document.getElementById("donateAmountOther").checked) {
            document.getElementById("donateOtherAmount").style.display = "block";
            } else {
            document.getElementById("donateOtherAmount").style.display = "none";
            }
        }
  };

  var videoModal = null;

  window.addEventListener("click", donateAmount);
  
  var donatePayment = () => {
    let masterCard = document.getElementById("donateMastercard");
    let echeck = document.getElementById("donateEcheck");
    let donateMastercard = document.getElementById("paymentMastercard");
    let donateEbank = document.getElementById("paymentEbank");
    let donatePaypal = document.getElementById("paymentPaypal");
  
    if (masterCard.checked) {
      donateMastercard.style.display = "block";
      donateEbank.style.display = "none";
      donatePaypal.style.display = "none";
    } else if (echeck.checked) {
      donateMastercard.style.display = "none";
      donateEbank.style.display = "block";
      donatePaypal.style.display = "none";
    } else {
      donateMastercard.style.display = "none";
      donateEbank.style.display = "none";
      donatePaypal.style.display = "block";
    }
  };
  
  window.addEventListener("click", donatePayment);
  
  window.onload = function () {
    document.getElementById("donateAmt").innerHTML = "$ 150";
  };

  var donateAmountFunction = () => {
    let fiftyAmt = document.getElementById("donateAmount1");
    let hundredAmt = document.getElementById("donateAmount2");
    let onefiftyAmt = document.getElementById("donateAmount3");
    let twohundredAmt = document.getElementById("donateAmount4");
    let customAmt = document.getElementById("donateAmountOther");
    let donateAmt = document.getElementById("donateAmt");
    let moreDataAmt = document.getElementById("donateOtherAmt");
    let valueAmt = moreDataAmt.value;
  
    if (fiftyAmt.checked) {
      donateAmt.innerHTML = "$ 50";
    } else if (hundredAmt.checked) {
      donateAmt.innerHTML = "$ 100";
    } else if (onefiftyAmt.checked) {
      donateAmt.innerHTML = "$ 150";
    } else if (twohundredAmt.checked) {
      donateAmt.innerHTML = "$ 200";
    } else if (customAmt.checked) {
      donateAmt.innerHTML = `$ ` + valueAmt;
    }
  };
  window.addEventListener("click", donateAmountFunction);
  
  var readmore = () => {
    let readmore = document.getElementById("readmore");
    let text = document.getElementById("text");
    text.classList.toggle("expanding");
    console.log("wwew");
    if (readmore.innerHTML === "Read More") {
      readmore.innerHTML = "Show Less";
    } else {
      readmore.innerHTML = "Read More";
    }
  };
  

  var popupsModal = function() {

    var popState = false;

    window.addEventListener("click", readmore);
    $('.toast').fadeIn(400).delay(3000).fadeOut(400);
    
    $(document).ready(function() {
        if(sessionStorage.getItem('popState') != 'shown'){
        $("#myModal").modal("show");
            popState = true;
        $('.popup').toggleClass('is--hidden');
        sessionStorage.setItem('popState','shown');
        }

        $('.close').click(function() {
            videoModal.show();
            $('.popup').toggleClass('is--hidden');
        });
    });
    
    $('.popup .cancel').click(function() {
        $('.popup').toggleClass('is--hidden');
    });

    return {
        visible: popState
    }
}();


videoModal = function () {
    let modal = $('.video-modal'),
        video = modal.find('video'),
        holder = $('.video-box.inview'),
        closeBtn = modal.find('.video-cancel .cancel'),
        visible = false;
    function close(evt) {
        video.detach().appendTo(holder);
        modal.addClass("hidden");
        modal.removeClass("show");

        visible = false;
    }

    function show() {
        if ( !visible ) { 
            modal.addClass('show');
            visible  = true;
        }
    }

    closeBtn.click(close);

    if(sessionStorage.getItem('popState') == 'shown') {
        (!popupsModal.visible && show());
    }

    return {
        show: show
    }
}();
  
  
  function cc_format(ccid,ctid) {
    // supports Amex, Master Card, Visa, and Discover
    // parameter 1 ccid= id of credit card number field
    // parameter 2 ctid= id of credit card type field
  
    var ccNumString=document.getElementById(ccid).value;
    ccNumString=ccNumString.replace(/[^0-9]/g, '');
    // mc, starts with - 51 to 55
    // v, starts with - 4
    // dsc, starts with 6011, 622126-622925, 644-649, 65
    // amex, starts with 34 or 37
    var typeCheck = ccNumString.substring(0, 2);
    var cType='';
    var block1='';
    var block2='';
    var block3='';
    var block4='';
    var formatted='';
    var cardType = {
      Visa: 'VISA_CARD',
      MasterCard: 'MASTER_CARD',
      Discover: 'DISCOVER_CARD',
      AmericanExpress: 'AMERICAN_EXPRESS_CARD',
    };
  
    if  (typeCheck.length==2) {
        typeCheck=parseInt(typeCheck);
        if (typeCheck >= 40 && typeCheck <= 49) {
            cType='Visa';
        }
        else if (typeCheck >= 51 && typeCheck <= 55) {
            cType='MasterCard';
        }
        else if ((typeCheck >= 60 && typeCheck <= 62) || (typeCheck == 64) || (typeCheck == 65)) {
            cType='Discover';
        }
        else if (typeCheck==34 || typeCheck==37) {
            cType='AmericanExpress';
        }
        else {
            cType='Invalid';
        }
    }
  
    // all support card types have a 4 digit firt block
    block1 = ccNumString.substring(0, 4);
    if (block1.length==4) {
        block1=block1 + ' ';
    }
  
    if (cType == 'Visa' || cType == 'MasterCard' || cType == 'Discover') {
        // for 4X4 cards
        block2 = ccNumString.substring(4, 8);
        if (block2.length==4) {
            block2=block2 + ' ';
        }
        block3 = ccNumString.substring(8, 12);
        if (block3.length==4) {
            block3=block3 + ' ';
        }
        block4 = ccNumString.substring(12, 16);
    }
    else if (cType == 'AmericanExpress') {
        // for Amex cards
        block2 =  ccNumString.substring(4, 10);
        if (block2.length==6) {
            block2=block2 + ' ';
        }
        block3 =  ccNumString.substring(10, 15);
        block4='';
    }
    else if (cType == 'Invalid') {
        // for Amex cards
        block1 =  typeCheck;
        block2='';
        block3='';
        block4='';
        //alert('Invalid Card Number');
    }
  
    var cardTypeList = $('.card-type-list');
    
    if (cType != '' ) {
      var items = cardTypeList.find('li');
      items.each(function( i ) {
          var el = $( this ),
              card= el.attr('data-logo');
  
          if (card == cardType[cType] && !el.hasClass()) {
              cardTypeList.addClass('selected');
              el.addClass('active');
  
              items.each(function( i ) {
                  var el = $( this ),
                      card= el.attr('data-logo');
                  if (card != cardType[cType]) {
                      el.addClass('inactive');
                  }
              });
          }else {
             
          }
      });
    }else {
      cardTypeList.removeClass('selected');
      cardTypeList.find('li').removeClass('active');
      cardTypeList.find('li').removeClass('inactive');
    }
  
    formatted=block1 + block2 + block3 + block4;
    document.getElementById(ccid).value=formatted;
    ///document.getElementById(ctid).value=cType;
  }
  
  var initPhotoSwipeFromDOM = function(gallerySelector) {
  
      // parse slide data (url, title, size ...) from DOM elements
      // (children of gallerySelector)
      var parseThumbnailElements = function(el) {
          var thumbElements = el.childNodes,
              numNodes = thumbElements.length,
              items = [],
              figureEl,
              linkEl,
              size,
              item;
  
          for(var i = 0; i < numNodes; i++) {
  
              figureEl = thumbElements[i]; // <figure> element
  
              // include only element nodes
              if(figureEl.nodeType !== 1) {
                  continue;
              }
  
              linkEl = figureEl.children[0]; // <a> element
  
              size = linkEl.getAttribute('data-size').split('x');
  
              // create slide object
              item = {
                  src: linkEl.getAttribute('href'),
                  w: parseInt(size[0], 10),
                  h: parseInt(size[1], 10)
              };
  
  
  
              if(figureEl.children.length > 1) {
                  // <figcaption> content
                  item.title = figureEl.children[1].innerHTML;
              }
  
              if(linkEl.children.length > 0) {
                  // <img> thumbnail element, retrieving thumbnail url
                  item.msrc = linkEl.children[0].getAttribute('src');
              }
  
              item.el = figureEl; // save link to element for getThumbBoundsFn
              items.push(item);
          }
  
          return items;
      };
  
      // find nearest parent element
      var closest = function closest(el, fn) {
          return el && ( fn(el) ? el : closest(el.parentNode, fn) );
      };
  
      // triggers when user clicks on thumbnail
      var onThumbnailsClick = function(e) {
          e = e || window.event;
          e.preventDefault ? e.preventDefault() : e.returnValue = false;
  
          var eTarget = e.target || e.srcElement;
  
          // find root element of slide
          var clickedListItem = closest(eTarget, function(el) {
              return (el.tagName && el.tagName.toUpperCase() === 'FIGURE');
          });
  
          if(!clickedListItem) {
              return;
          }
  
          // find index of clicked item by looping through all child nodes
          // alternatively, you may define index via data- attribute
          var clickedGallery = clickedListItem.parentNode,
              childNodes = clickedListItem.parentNode.childNodes,
              numChildNodes = childNodes.length,
              nodeIndex = 0,
              index;
  
          for (var i = 0; i < numChildNodes; i++) {
              if(childNodes[i].nodeType !== 1) {
                  continue;
              }
  
              if(childNodes[i] === clickedListItem) {
                  index = nodeIndex;
                  break;
              }
              nodeIndex++;
          }
  
          if(index >= 0) {
              // open PhotoSwipe if valid index found
              openPhotoSwipe( index, clickedGallery );
          }
          return false;
      };
  
      // parse picture index and gallery index from URL (#&pid=1&gid=2)
      var photoswipeParseHash = function() {
          var hash = window.location.hash.substring(1),
          params = {};
  
          if(hash.length < 5) {
              return params;
          }
  
          var vars = hash.split('&');
          for (var i = 0; i < vars.length; i++) {
              if(!vars[i]) {
                  continue;
              }
              var pair = vars[i].split('=');
              if(pair.length < 2) {
                  continue;
              }
              params[pair[0]] = pair[1];
          }
  
          if(params.gid) {
              params.gid = parseInt(params.gid, 10);
          }
  
          return params;
      };
  
      var openPhotoSwipe = function(index, galleryElement, disableAnimation, fromURL) {
          var pswpElement = document.querySelectorAll('.pswp')[0],
              gallery,
              options,
              items;
  
          items = parseThumbnailElements(galleryElement);
  
          // define options (if needed)
          options = {
  
              // define gallery index (for URL)
              galleryUID: galleryElement.getAttribute('data-pswp-uid'),
  
              getThumbBoundsFn: function(index) {
                  // See Options -> getThumbBoundsFn section of documentation for more info
                  var thumbnail = items[index].el.getElementsByTagName('img')[0], // find thumbnail
                      pageYScroll = window.pageYOffset || document.documentElement.scrollTop,
                      rect = thumbnail.getBoundingClientRect();
  
                  return {x:rect.left, y:rect.top + pageYScroll, w:rect.width};
              }
  
          };
  
          // PhotoSwipe opened from URL
          if(fromURL) {
              if(options.galleryPIDs) {
                  // parse real index when custom PIDs are used
                  // http://photoswipe.com/documentation/faq.html#custom-pid-in-url
                  for(var j = 0; j < items.length; j++) {
                      if(items[j].pid == index) {
                          options.index = j;
                          break;
                      }
                  }
              } else {
                  // in URL indexes start from 1
                  options.index = parseInt(index, 10) - 1;
              }
          } else {
              options.index = parseInt(index, 10);
          }
  
          // exit if index not found
          if( isNaN(options.index) ) {
              return;
          }
  
          if(disableAnimation) {
              options.showAnimationDuration = 0;
          }
  
          // Pass data to PhotoSwipe and initialize it
          gallery = new PhotoSwipe( pswpElement, PhotoSwipeUI_Default, items, options);
          gallery.init();
      };
  
      // loop through all gallery elements and bind events
      var galleryElements = document.querySelectorAll( gallerySelector );
  
      for(var i = 0, l = galleryElements.length; i < l; i++) {
          galleryElements[i].setAttribute('data-pswp-uid', i+1);
          galleryElements[i].onclick = onThumbnailsClick;
      }
  
      // Parse URL and open gallery if it contains #&pid=3&gid=1
      var hashData = photoswipeParseHash();
      if(hashData.pid && hashData.gid) {
          openPhotoSwipe( hashData.pid ,  galleryElements[ hashData.gid - 1 ], true, true );
      }
  };
  
// execute above function
initPhotoSwipeFromDOM('.my-gallery');
  
$(document).ready(function() {
    let donate_name= $('input[name=donateName]:checked', '#donateForm').val();
    update_data(donate_name);
    $('#donateForm input').on('change', function () {
        donate_name= $('input[name=donateName]:checked', '#donateForm').val();
        update_data(donate_name);
    });
});
  