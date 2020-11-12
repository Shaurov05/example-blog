import { CSRF_TOKEN } from "./csrf_token.js"
// import { token } from "./csrf_token.js"


function handleResponse(response){
  if (response.status === 204) {
    return "";
  } else if (response.status === 404 ){
    return null;
  } else {
    return response.json();
  }
}



function apiService(endpoint, method, data ){
  var auth_token = localStorage.getItem("token")
  var config = {}
  if (auth_token == "initialized"){
    console.log("api without authorization")
    config = {
      method: method || "GET",
      body: data !== undefined ? JSON.stringify(data) : null,
      headers: {
        'content-type': 'application/json',
        'X-CSRFTOKEN': CSRF_TOKEN,
      }
    }
  } else {
    console.log("api with authorization")
    config = {
      method: method || "GET",
      body: data !== undefined ? JSON.stringify(data) : null,
      headers: {
      'content-type': 'application/json',
      'X-CSRFTOKEN': CSRF_TOKEN,
      Authorization: `bearer ${auth_token}`,
      }
    }
  }

  return fetch(endpoint, config)
        .then(handleResponse)
        .catch(error => console.log(error))
}


export { apiService };
