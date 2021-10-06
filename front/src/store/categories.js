export const state = function(){
  return {
    loadedCategories: [],
    accessoriesCategories: [],
  }
};

export const actions = {

  async getCategories({ commit }, data={}){
    const url = `${data.accessoriesType}/`;
    const params = {
      q: data.q ? data.q : '',
        page_size: 9999,
    };

    await this.$axios.$get(url, { params: params }).then(
      response => {
        commit('setLoadedCategories', response.results)
      }
    )
  },

  async addTagToCategories({ commit }, data={}){
    const url = `${data.modelType}/${data.idModel}/${data.accessoriesType}/`;
    //console.log('addTagToCategories', url, data)

    await this.$axios.$post(url, data.dataSend).then(
      response => {
        $nuxt.$toast.success($nuxt.$t('form.actions.added'));
        commit('setAccessoriesCategories', response.categories || [response.category_obj]);
      }
    )
  },

  /*async setTagAsCategory({ commit }, data={}){
    const url = `${data.modelType}/${data.idModel}/${data.accessoriesType}/`;

    await this.$axios.$post(url, data.dataSend).then(
      response => {
        $nuxt.$toast.success($nuxt.$t('form.actions.added'));
        commit('setAccessoriesCategories', response.categories);
      }
    )
  },*/

  async deleteTagFromCategories({ commit }, data) {
    const url = `${data.modelType}/${data.idModel}/${data.accessoriesType}/`;
    const config = {
      data: data.dataSend
    };

    await this.$axios.delete(url, config).then(
      response => {
        commit('setAccessoriesCategories', response.data.categories);
        $nuxt.$toast.success($nuxt.$t('form.actions.deleted'));
      }
    )
  },

  getCategoriesId({ commit }, objectArray){
    let CategoriesId = [];
    for(const item in objectArray){
      CategoriesId.push(objectArray[item].id);
    }
    return CategoriesId;
  },

  clearCategoriesState ({ commit }){
    commit('clearAccessoriesCategories');
    commit('clearloadedCategories');
  },

  setAccessoriesCategories({commit}, categories) {
    commit('setAccessoriesCategories', categories);
  },
};

export const mutations = {
  clearLoadedCategories(state) {
    state.loadedCategories = [];
  },
  clearAccessoriesCategories(state) {
    state.accessoriesCategories = [];
  },
  clearloadedCategories(state) {
    state.loadedCategories = [];
  },
  setLoadedCategories(state, categories) {
    state.loadedCategories = categories;
  },
  setAccessoriesCategories(state, categories) {
    state.accessoriesCategories = categories;
  },
  addAccessoriesCategories(state, category) {
    state.accessoriesCategories = state.accessoriesCategories.concat(category);
  },
  setAccessoriesCategory(state, category) {
    state.accessoriesCategories = [category];
  },
  deleteTagFromAccessCategories(state, category) {
    state.accessoriesCategories.splice(state.accessoriesCategories.indexOf(category), 1);
  },
  deleteFromLoadedCategories(state, category) {
    state.loadedCategories.splice(state.loadedCategories.indexOf(category), 1);
  }
};

export const categories = {
  namespaced: true,
  state,
  mutations,
  actions
};