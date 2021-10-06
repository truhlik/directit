import {handleValidators} from '../helpers/validators'

export const state = function() {
 return {
   objectError: {},
   objectValidator: {}
 }
};

export const mutations = {
  setErrorObject (state, objectError) {
    state.objectError = { ...state.objectError, ...objectError };
  },
  cleanErrorObject (state) {
    state.objectError = {}
  },
  removeFromErrorObject(state, property){
    state.objectError = delete state.objectError[property];
  }
};

export const actions = {
  validate ({commit, state}, data){
    //console.log('validate', data)
    const objectError = handleValidators(data.name, data.objectData, data.objectValidator);
    if(objectError[data.name].length){
      commit('setErrorObject', objectError);
    }else{
      commit('removeFromErrorObject', data.name);
    }
  },
  cleanErrorObject({commit}){
    commit('cleanErrorObject');
  }
};

export const errors = {
  namespaced: true,
  state,
  mutations,
  actions
};