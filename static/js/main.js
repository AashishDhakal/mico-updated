
donateAmount = () => {
  if (document.getElementById("donateAmountOther").checked) {
    document.getElementById("donateOtherAmount").style.display = "block";
  } else {
    document.getElementById("donateOtherAmount").style.display = "none";
  }
};
window.addEventListener("click", donateAmount);

donatePayment = () => {
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

donateAmountFunction = () => {
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

readmore = () => {
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

window.addEventListener("click", readmore);
$('.toast').fadeIn(400).delay(3000).fadeOut(400);

$(document).ready(function() {
  if(sessionStorage.getItem('popState') != 'shown'){
    $("#myModal").modal("show");
    $('.popup').toggleClass('is--hidden');
    sessionStorage.setItem('popState','shown');
  }
  $('.close').click(function() // You are clicking the close button
  {
    $('.popup').toggleClass('is--hidden');
  });
});

$('.cancel').click(function() {
  $('.popup').toggleClass('is--hidden');
});
