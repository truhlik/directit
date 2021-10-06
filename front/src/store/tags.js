export const state = function(){
  return {
    loadedTags: [],
    accessoriesTags: [],
  }
};

export const actions = {

  async getTags({ commit }, data={}){
    const url = `${data.accessoriesType }/`;
    const params = {
      q: data.q ? data.q : ''
    };

    await this.$axios.$get(url, { params: params }).then(
      response => {
        commit('setLoadedTags', response.results)
      }
    )
  },

  async addTagToTags({ commit }, data={}){
    const url = `${data.modelType}/${data.idModel}/${data.accessoriesType}/`;

    await this.$axios.$post(url, data.dataSend).then(
      response => {
        $nuxt.$toast.success($nuxt.$t('form.actions.added'));
        commit('setAccessoriesTags', response.tags);
      }
    )
  },

  async deleteTagFromTags({ commit }, data) {
    const url = `${data.modelType}/${data.idModel}/${data.accessoriesType}/`;
    const config = {
      data: data.dataSend
    };

    await this.$axios.delete(url, config).then(
      response => {
        commit('setAccessoriesTags', response.data.tags);
        $nuxt.$toast.success($nuxt.$t('form.actions.deleted'));
      }
    )
  },

  getTagsId(){
    let tagsId = [];
    for(const item in this.state.tags.accessoriesTags){
      tagsId.push(this.state.tags.accessoriesTags[item].id);
    }
    return tagsId;
  },

  clearTagStates({ commit }){
    commit('clearAccessoriesTags');
    commit('clearloadedTags');
  }
};

export const mutations = {
  clearLoadedTags(state) {
    state.loadedTags = [];
  },
  setLoadedTags(state, tags) {
    state.loadedTags = tags;
  },
  clearAccessoriesTags(state) {
    state.accessoriesTags = [];
  },
  clearloadedTags(state) {
    state.loadedTags = [];
  },
  setAccessoriesTags(state, tags) {
    state.accessoriesTags = tags;
  },
  addAccessoriesTags(state, tags) {
    state.accessoriesTags.push(tags);
  },
  deleteTagFromAccessories(state, tag) {
    state.accessoriesTags.splice(state.accessoriesTags.indexOf(tag), 1);
  },
  deleteFromLoadedTags(state, category) {
    state.loadedTags.splice(state.loadedTags.indexOf(category), 1);
  }
};

export const tags = {
  namespaced: true,
  state,
  mutations,
  actions
};