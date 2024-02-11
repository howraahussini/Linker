// mask 

function showMask() {
  document.getElementById('mask').style.display = 'block';
}

function hideMask() {
  document.getElementById('mask').style.display = 'none';
}


// delete main link

function showConfirm(itemId) {
  event.preventDefault();
  document.getElementById('mask_' + itemId).style.display = 'block';
}

function cancelDeletion(itemId) {
  document.getElementById('mask_' + itemId).style.display = 'none';
}

// copy link

function copyLink(itemId) {
  const inputElement = document.getElementById('copy_' + itemId);

  inputElement.select();
  document.execCommand('copy');

  alert('تم النسخ: ' + inputElement.value);
}



// delete link

function linkShowConfirm(itemId) {
  document.getElementById('link_' + itemId).style.display = 'block';
}

function linkCancelDeletion(itemId) {
  document.getElementById('link_' + itemId).style.display = 'none';
}

// delete text

function textShowConfirm(itemId) {
  event.preventDefault();
  document.getElementById('text_' + itemId).style.display = 'block';
}

function textCancelDeletion(itemId) {
  document.getElementById('text_' + itemId).style.display = 'none';
}

// delete gallery

function galleryShowConfirm(itemId) {
  document.getElementById('gallery_' + itemId).style.display = 'block';
}

function galleryCancelDeletion(itemId) {
  document.getElementById('gallery_' + itemId).style.display = 'none';
}


// delete faq

function faqShowConfirm(itemId) {
  document.getElementById('faq_' + itemId).style.display = 'block';
}

function faqCancelDeletion(itemId) {
  document.getElementById('faq_' + itemId).style.display = 'none';
}

// show answer button

function showAnswer(itemId) {
  const answer = document.getElementById('answer_' + itemId);
  if (answer.style.display === 'none' || answer.style.display === '') {
    answer.style.display = 'block';
  }
  else {
    answer.style.display = 'none';
  }
}

// delete email

function emailShowConfirm(itemId) {
  document.getElementById('email_' + itemId).style.display = 'block';
}

function emailCancelDeletion(itemId) {
  document.getElementById('email_' + itemId).style.display = 'none';
}


// delete phone

function phoneShowConfirm(itemId) {
  document.getElementById('phone_' + itemId).style.display = 'block';
}

function phoneCancelDeletion(itemId) {
  document.getElementById('phone_' + itemId).style.display = 'none';
}

// delete instagram

function instagramShowConfirm(itemId) {
  document.getElementById('instagram_' + itemId).style.display = 'block';
}

function instagramCancelDeletion(itemId) {
  document.getElementById('instagram_' + itemId).style.display = 'none';
}

// delete telegram

function telegramShowConfirm(itemId) {
  document.getElementById('telegram_' + itemId).style.display = 'block';
}

function telegramCancelDeletion(itemId) {
  document.getElementById('telegram_' + itemId).style.display = 'none';
}

// delete youtube

function youtubeShowConfirm(itemId) {
  document.getElementById('youtube_' + itemId).style.display = 'block';
}

function youtubeCancelDeletion(itemId) {
  document.getElementById('youtube_' + itemId).style.display = 'none';
}

// delete whatsapp

function whatsappShowConfirm(itemId) {
  document.getElementById('whatsapp_' + itemId).style.display = 'block';
}

function whatsappCancelDeletion(itemId) {
  document.getElementById('whatsapp_' + itemId).style.display = 'none';
}

// delete x

function xShowConfirm(itemId) {
  document.getElementById('x_' + itemId).style.display = 'block';
}

function xCancelDeletion(itemId) {
  document.getElementById('x_' + itemId).style.display = 'none';
}

// delete facebook

function facebookShowConfirm(itemId) {
  document.getElementById('facebook_' + itemId).style.display = 'block';
}

function facebookCancelDeletion(itemId) {
  document.getElementById('facebook_' + itemId).style.display = 'none';
}

// delete linkedin

function linkedinShowConfirm(itemId) {
  document.getElementById('linkedin_' + itemId).style.display = 'block';
}

function linkedinCancelDeletion(itemId) {
  document.getElementById('linkedin_' + itemId).style.display = 'none';
}

// delete snapchat

function snapchatShowConfirm(itemId) {
  document.getElementById('snapchat_' + itemId).style.display = 'block';
}

function snapchatCancelDeletion(itemId) {
  document.getElementById('snapchat_' + itemId).style.display = 'none';
}

// delete tiktok

function tiktokShowConfirm(itemId) {
  document.getElementById('tiktok_' + itemId).style.display = 'block';
}

function tiktokCancelDeletion(itemId) {
  document.getElementById('tiktok_' + itemId).style.display = 'none';
}
