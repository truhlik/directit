export function handleValidators(inputName, objectData, validatorObject){
  let objectError = {};
  objectError[inputName] = [];
  let message;

  if(!validatorObject[inputName].hasOwnProperty('rules')) return;
  for(let rule in validatorObject[inputName].rules){
    let ruleFunction = validatorObject[inputName].rules[rule];
    message = validatorFunctions[ruleFunction](inputName, objectData, validatorObject[inputName]).message;

    if(message.length)
      objectError[inputName].push(message);
  }
  return objectError
}

export const validatorFunctions = {
  required(inputName, objectData, validator) {
    if (objectData[inputName] === undefined || objectData[inputName] === '') return {state: null, valid: false, message: 'Toto pole je povinné'};
    return {state: !!objectData[inputName], valid: !!objectData[inputName], message: ''};
  },
  minLength(inputName, objectData, validator) {
    if (objectData[inputName] === undefined || (objectData[inputName].length < validator.minLength && objectData[inputName].length > 0))
      return {state: false, valid: false, message: 'Length must be greater than ' + validator.minLength};

    return {state: true, valid: true, message: ''};
  },
  email(inputName, objectData, validator) {
    if (objectData[inputName] === undefined || objectData[inputName] === '') return {state: null, valid: false, message: ''};
    const regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if(regex.test(objectData[inputName].toLowerCase()))
      return {state: true, valid: true, message: ''};

    return {state: false, valid: false, message: 'E-mail není ve správném formátu.'};
  },
  sameAs(inputName, objectData, validator) {
    if (objectData[inputName] === undefined) return {state: null, valid: false, message: ''};
    if (objectData[inputName].length > 5 && objectData[inputName] === objectData[validator.sameAs])
      return {state: true, valid: true, message: ''};

    return {state: false, valid: false, message: 'Hodnota musí být stejná jako hodnota pole ' + validator.sameAs};
  },
  password(inputName, objectData, validator) {
    if (objectData[inputName] === undefined) return {state: null, valid: false, message: ''};
    if(objectData[inputName].length > 5)
      return {state: true, valid: true, message: ''};

    return {state: false, valid: false, message: 'Heslo musí být rovno nebo delší než 8 znaků'};
  }
};

export function validateDummy(value) {
  if (value === undefined) return {state: null, valid: true};
  return {state: true, valid: true};
}

export function validateRequiredIfField(value, condition) {
  if (value === undefined || !condition) return {state: null, valid: true};
  return {state: !!value, valid: !!value};
}

export function validateBetween(value, minValue, maxValue) {
  if (value === undefined) return {state: null, valid: false};
  const valid = minValue <= value && value <= maxValue;
  return {state: !!valid, valid: !!valid};
}
