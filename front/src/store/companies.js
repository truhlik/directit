export const state = function() {
  return {
    company: {
      'role': 'CONSULTANT'
    },
    myCompanies: [],
    companiesList: [],
    companyPagination: {},
    suggestions: [],
    mapMarkers: [], 
    aresData: {},
    enumType: {
      'SUPPLIER': 'Dodavatel',
      'CLIENT': 'Klient',
      'CONSULTANT': 'Konzultant'
    },
    isLoading: false
  }
};

export const getters = {
  getMyCompanies(state) {
    return state.myCompanies;
  },
  isConsultant(state) {
    return state.company.role === 'CONSULTANT';
  },
  isClient(state) {
    return state.company.role === 'CLIENT';
  },
  isSupplier(state) {
    return state.company.role === 'SUPPLIER';
  },
};

export const actions = {
  async getCompanyByICO({ commit }, valueICO){
    const params = {
      reg_number: valueICO
    };
    const url = 'ares/company/';
    await this.$axios.$get(url, { params: params }).then(
      response => {
        commit('addToCompany', response);
        $nuxt.$toast.success($nuxt.$t('form.actions.loaded'));
      },
      error => {
        //nothing to do
      }
    )
  },
  async createCompany({ commit }, newCompany){
    const url = 'companies/';
    await this.$axios.$post(url, newCompany).then(
      response => {
        commit('clearCompany');
        $nuxt.$toast.success('Úspěšně vytvořeno');
        $nuxt.$router.replace({ name: 'subjekt-id-upravit___cs', params: { id: response.id } })
      }
  )},

  async updateCompany({ commit }, company){
    // definování array, kde jsou povoleny attributy pro update
    const allowedToUpdate= ['name', 'phone', 'city', 'description', 'email', 'street', 'street_number', 'web', 'zip', 'vat_number', 'reg_number'];
    if(!company.id){
      $nuxt.$toast.error('Podle údajů není možné specifikovat objekt.');
      return;
    }

    // vytvoření nového objektu s povolenými attributy
    let updateCompany = {};
    for(const key in company){
      if(allowedToUpdate.includes(key)){
        updateCompany[key] = company[key];
      }
    }

    const url = `companies/${company.id }/`;
    await this.$axios.$patch(url, updateCompany).then(
      response =>  {
        $nuxt.$toast.success('Změny byly uloženy.');
        $nuxt.$router.replace({ name: 'subjekt-id-upravit___cs', params : { id: company.id } })
      }
    );
  },

  async getMyCompanies({commit}, page){
    const url = 'companies/';
    const params = {
      page: page
    };
    commit('setLoading', true);

    await this.$axios.$get(url, { params: params }).then(
      response => {
        commit('setCompanyPagination', response.pagination);
        commit('setMyCompanies', response.results);
        commit('setLoading', false);
      }
    )
  },

  async getCompanyDetail({commit}, data){
    const url = `${data.companyType ? data.companyType : 'companies'}/${data.id}/`;
    await this.$axios.$get(url).then(
      response => {
        commit('setCompany', response);
      },
      error => {
        $nuxt.$router.replace({ name: 'index___cs' })
      }
    )
  },

  async getLimitedCompanies({commit}, data = {}){
    const companyType = data.companyType ? data.companyType : 'suppliers';
    const url = `${companyType}/`;
    const params = {
      page: data.page ? data.page : 1
    };

    commit('setLoading', true);
    await this.$axios.$get(url, { params: params }).then(
      response => {
        commit('setCompanies', response.results);
        commit('setCompanyPagination', response.pagination);
        commit('setLoading', false);
      }
    )
  },

  async getAllCompaniesMarkers({ commit }, data = {}){
    const companyType = data.companyType ? data.companyType : 'suppliers';
    const url = `${companyType}/`;
    const params = {
      fields: 'name,gps_lat,gps_lng',
      page_size: 999999999,
      q: data.searchedString ? data.searchedString : ''
    };

    await this.$axios.$get(url, { params: params }).then(
      response => {
        if(data.add){
          commit('addMapMarkers', response.results);
        }else{
          commit('setMapMarkers', response.results);
        }
      }
    )
  },

  async getSuggestions({ commit }, data){
    const companyType = data.companyType ? data.companyType : 'suppliers';
    let url = `${companyType}/suggestion/`;

    let params = {
      q: data.searchedString ? data.searchedString : ''
    };

    await this.$axios.$get( url , {params: params}).then(
      response => {
        if(response.results.length){
          commit('setSuggestions', response.results);
        }else{
          commit('clearSuggestions');
        }
      }
    )
  },

  async findCompanies({ commit }, data = {}){
    const companyType = data.companyType ? data.companyType : 'suppliers';
    const url = `${companyType}/`;
    const params = {
      q: data.searchedString ? data.searchedString : '',
      page: data.page ? data.page : 1,
    };

    commit('setLoading', true);
    await this.$axios.$get( url, { params: params } ).then(
      response => {
        console.log('findCompanies', response);
        commit('addToCompanies', response.results);
        commit('setCompanyPagination', response.pagination);
        commit('setLoading', false);
      }
    )
  },

  async uploadCompanyImage({ commit }, data){
    const url = `companies/${data.companyId}/image/`;
    const config = {
      headers: {
        'content-type': 'multipart/form-data'
      }
    };
    await this.$axios.$post(url, data.formData, config).then(
      response => {
        commit('addToCompany', response);
      }
    )
  },

  clearAllCompanyState({ commit }){
    commit('clearCompany');
    commit('clearCompanies');
    commit('clearSuggestions');
  },

  clearCompanies({ commit }){
    commit('clearCompanies');
  }
};


export const mutations = {
  addToCompany(state, data){
      console.log('addToCompany', data)
      state.company = { ...state.company, ...data };
  },
  addToCompanies(state, data){
    state.companiesList = [ ...state.companiesList, ...data ];
  },
  addMapMarkers(state, data){
    state.mapMarkers = [ ...state.mapMarkers, ...data ];
  },
  clearCompany(state){
    state.company = {};
  },
  clearCompanies(state){
    state.companiesList = [];
  },
  clearSuggestions(state){
    state.suggestions = [];
  },
  setCompany(state, company){
    state.company = company;
  },
  setCompanies(state, companies){
    state.companiesList = companies;
  },
  setCompanyPagination(state, pagination){
    state.companyPagination = { ...state.companyPagination, ...pagination};
  },
  setSuggestions(state, suggestions){
    state.suggestions = suggestions;
  },
  setMyCompanies(state, companies){
    state.myCompanies = companies;
  },
  setMapMarkers(state, markers){
    state.mapMarkers = markers;
  },
  setLoading(state, loading){
    state.isLoading = loading;
  }
};

export const companies = {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
};