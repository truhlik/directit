import Vue from 'vue'

export const state = function () {
    return {
        all: [],
        analyzes: [],
        services: [],
        consultants: [],
    }
}

export const actions = {
    async getAll({commit}, data = {}) {
        let url = 'services/';
        const params = {
            page: data.page ? data.page : 1,
        };
        await this.$axios.$get(url, { params: params }).then(
            response => {
                console.log('axios all services', response);
                if (response?.results.length) {
                    commit('setAll', response);
                } else {
                    commit('clearAll');
                }
            }
        )
    },

    async getAnalyzes({commit}, data = {}) {
        let url = 'services/';
        const params = {
            category: 'ANALYZE',
            page: data.page ? data.page : 1,
        };
        await this.$axios.$get(url, { params: params }).then(
            response => {
                console.log('axios analyzes', response);
                if (response?.results.length) {
                    commit('setAnalyzes', response);
                } else {
                    commit('clearAnalyzes');
                }
            }
        )
    },
    async getServices({commit}, data = {}) {
        let url = 'services/';
        const params = {
            category: 'SERVICE',
            page: data.page ? data.page : 1,
        };
        await this.$axios.$get(url, { params: params }).then(
            response => {
                console.log('axios Services', response);
                if (response?.results.length) {
                    commit('setServices', response);
                } else {
                    commit('clearServices');
                }
            }
        )
    },
    async getConsultants({commit}, data = {}) {
        let url = 'services/';
        const params = {
            category: 'CONSULTANT',
            page: data.page ? data.page : 1,
        };
        await this.$axios.$get(url, { params: params }).then(
            response => {
                console.log('axios Consultants', response);
                if (response?.results.length) {
                    commit('setConsultants', response);
                } else {
                    commit('clearConsultants');
                }
            }
        )
    },
}

export const mutations = {
    setAll(state, all) {
        //console.log('setAll', all);
        state.all = all;
    },
    clearAll(state) {
        state.all = [];
    },
    setAnalyzes(state, analyzes) {
        //console.log('setAnalyzes', analyzes);
        state.analyzes = analyzes;
    },
    clearAnalyzes(state) {
        state.analyzes = [];
    },
    setServices(state, services) {
        //console.log('setServices', services);
        state.services = services;
    },
    clearServices(state) {
        state.services = [];
    },
    setConsultants(state, consultants) {
        //console.log('setConsultants', consultants);
        state.consultants = consultants;
    },
    clearConsultants(state) {
        state.consultants = [];
    },
}
export const services = {
    namespaced: true,
    state,
    //getters,
    mutations,
    actions
};