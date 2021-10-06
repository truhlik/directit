export default function handleErrorResponse(response) {

  if (response.status === 401) {
    window.location.href = '/login/'
  }

  // if (response.status !== 400 || !response.data && !response.data.detail) {
  //   return {message: 'Server error', errorObject: {}}
  // }

  let fieldViolations;

  try {
    fieldViolations = response.data;
  }
  catch {
    // TODO handle more cases than field violations if necessary
    return {message: response.data.message || 'Invalid request', errorObject: {}}
  }

  let errorObject = {};
  let messagesString = '';

  for (let key in fieldViolations){
    errorObject[key.toLowerCase()] = fieldViolations[key];
    //if(key !== 'non_field_errors')
      //messagesString += `${key}:`;
    messagesString += `${fieldViolations[key]}<br>`;
  }

  return {
    message: messagesString,
    errorObject: errorObject
  }
}
