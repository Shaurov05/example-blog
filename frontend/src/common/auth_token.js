function get_auth_Token(name){
  if (!document.cookie.get('token')){
    var token = null;
     document.cookie = name + "=" + {} + "; path=/";
  } else {
    token = document.cookie.getItem('token');
  }
  return token;
}

var auth_token = get_auth_Token('auth_token');

export { auth_token };


// function setCookie(name,value,days) {
//     var expires = "";
//     if (days) {
//         var date = new Date();
//         date.setTime(date.getTime() + (days*24*60*60*1000));
//         expires = "; expires=" + date.toUTCString();
//     }
//     document.cookie = name + "=" + (value || "")  + expires + "; path=/";
// }
