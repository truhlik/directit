import Vue from 'vue'

export const state = function () {
    return {
        isLoading: false,
        categories: [],
        groupProducts: {},
        suggestions: [],
        productDetails: []
    }
}


export const actions = {

    async getCategories({commit}, data = {}) {
        let url = 'categories/group/';
        const params = {
            q: data.searchedString ? data.searchedString : '',
        };
        commit('setLoading', true);

        await this.$axios.$get(url, { params: params }).then(
            response => {
                //console.log('axios categories', response);
                if (response?.length) {
                    commit('setCategories', response);
                } else {
                    commit('clearCategories');
                }
                commit('setLoading', false);
            }
        )
    },

    async getCategoryProducts({commit}, categoryId) {
        //console.log('getCategoryProducts', categoryId);
        let url = 'products/';
        const params = {
            categories: categoryId,
            page_size: 99999
        };

        await this.$axios.$get(url, {params: params}).then(
            response => {
                //console.log('axios getCategoryProducts', response.results);
                if (response.results?.length) {
                    commit('addGroupProducts', {categoryId, products: response.results});
                }
            }
        )
    },

    async getSuggestions({commit}, data) {
        let url = `products/suggestion/`;

        let params = {
            q: data.searchedString ? data.searchedString : ''
        };

        await this.$axios.$get(url, {params: params}).then(
            response => {
                if (response.results?.length) {
                    commit('setSuggestions', response.results);
                } else {
                    commit('clearSuggestions');
                }
            }
        )
    },

    async getProductDetail({commit}, productId) {
        let url = `products/${productId}`;

        await this.$axios.$get(url, {params: params}).then(
            response => {
                if (response.results?.length) {
                    commit('addProductDetail', productId, response.results);
                }
            }
        )
    },
}


export const mutations = {
    setCategories(state, categories) {
        //console.log('setCategories', categories);
        state.categories = categories;
    },
    clearCategories(state) {
        state.categories = [];
    },
    clearSuggestions(state) {
        state.suggestions = [];
    },
    addGroupProducts(state, result) {
        //console.log('addGroupProducts', result);
        //state.groupProducts[result.categoryId] = result.products;
        Vue.set(state.groupProducts, result.categoryId, result.products);
        //console.log('state.groupProducts', state.groupProducts);
    },
    setSuggestions(state, suggestions) {
        state.suggestions = suggestions;
    },
    addProductDetail(state, productId, product) {
        state.productDetails[productId] = product;
    },
    setLoading(state, loading){
        state.isLoading = loading;
    },
}

export const technologies = {
    namespaced: true,
    state,
    //getters,
    mutations,
    actions
};