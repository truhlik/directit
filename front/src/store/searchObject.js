export const state = function(){
  return {
    searchedTags: [],
  }
};

export const actions = {};

export const mutations = {
  clearSeachedTags(state) {
    state.searchedTags = [];
  },
  setSearchedTags(state, tags) {
    state.searchedTags = tags;
  },
  addSearchedTag(state, tag) {
    state.searchedTags.push(tag);
  },
  deleteSearchedTag(state, tag) {
    state.searchedTags.splice(state.searchedTags.indexOf(tag), 1);
  }
};

export const searchObject = {
  namespaced: true,
  state,
  mutations,
  actions
};