export const state = function () {
  return {
    software: {},
    softwarePagination: {},
    softwareList: {}
  }
};

export const actions = {
  async createSoftware({ commit }, data={}) {
    const url = 'software/';
    let softData = { ...data };
    const requiredBoolean = ['need_customization', 'need_extension', 'need_upgrade', 'watch_expiration'];

    // kontrola jestli data obsahují povinná pole, pokud ne, přiřadím je s hodnotou false
    for(let value in requiredBoolean){
      if(!(requiredBoolean[value] in softData)){
        softData[requiredBoolean[value]] = false;
      }
    }

    await this.$axios.$post(url, softData).then(
      response => {
        $nuxt.$toast.success('Technologie vytvořena');
        commit('clearSoftware');
        commit('categories/clearAccessoriesCategories', null, { root: true });
        $nuxt.$router.push('/technologie/seznam/');
      }
     );
  },

  async getSoftwareList({ commit }, data={}){
    const url = 'software/';
    const params = {
      page: data.page ? data.page : 1
    };

    await this.$axios.$get(url, { params: params }).then (
      response => {
        commit('setSoftwarePagination', response.pagination);
        commit('setSoftwareList', response.results);
      }
    );
  },

  async getSoftwareDetail({ commit }, id){
    const url = `software/${id}/`;

    await this.$axios.$get(url).then(
      response => {
        commit('setSoftware', response);
      }
    )

  },

  async updateSoftware({ commit }, data){
    const url = `software/${data.id}/`;

    await this.$axios.$patch(url, data).then(
      response => {
        $nuxt.$toast.success('Uloženo');
        $nuxt.$router.push('/technologie/seznam/');
      }
    )

  },

  async deleteSoftware({commit}, id) {
    const url = `software/${id}/`;

    await this.$axios.$delete(url).then(
      response => {
        $nuxt.$toast.success($nuxt.$t('form.actions.deleted'));
        $nuxt.$router.push('/technologie/seznam/');
      }
    )
  },

  clearSoftwareAction({ commit }){
    commit('clearSoftware');
  },
};

export const mutations = {
  addToSoftware(state, data) {
    state.software = { ...state.software, ...data};
  },
  clearSoftware(state) {
    state.software = {}
  },
  setSoftware(state, software){
    state.software = software;
  },
  setSoftwareList(state, data) {
    state.softwareList = data;
  },
  setSoftwarePagination(state, pagination){
    state.softwarePagination = { ...state.softwarePagination, ...pagination};
  }
};

export const software = {
  namespaced: true,
  state,
  actions,
  mutations
};

