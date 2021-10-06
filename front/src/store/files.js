export const state = function () {
  return {
    file: {}
  }
}

export const getters = {

}

export const mutations = {
  addToFile(state, data){
    state.file = { ...state.file, ...data};
  },
  setFile(state, file){
    state.file = file;
  },
}

export const actions = {
  async updateFile({ commit }, data){
    if(data.hasOwnProperty('file'))
      delete data.file

    const url = `files/${data.id}/`;
    await this.$axios.$patch(url, data).then(
      response => {
        $nuxt.$toast.success($nuxt.$t('form.actions.saved'));
      },
      error => {
        // handled by api.js
      }
    );
  },
  async deleteFile({ commit }, data){
    const url = `files/${data.id}/`;
    await this.$axios.$delete(url, data).then(
      response => {
        console.log(response)
        $nuxt.$toast.success($nuxt.$t('form.actions.deleted'));
      },
      error => {
        // handled by api.js
      }
    );
  },
}

export const files = {
  namespaced: true,
  state,
  getters,
  mutations,
  files
}
