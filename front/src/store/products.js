export const state = function(){
    return {
        loadedProducts: [],
        accessoriesProducts: [],
    }
};

export const actions = {

    async getProducts({ commit }, data={}){
        const url = `${data.accessoriesType }/`;
        const params = {
            q: data.q ? data.q : ''
        };

        await this.$axios.$get(url, { params: params }).then(
            response => {
                commit('setLoadedProducts', response.results)
            }
        )
    },

    async addProductToProducts({ commit }, data={}){
        const url = `${data.modelType}/${data.idModel}/${data.accessoriesType}/`;

        await this.$axios.$post(url, data.dataSend).then(
            response => {
                $nuxt.$toast.success($nuxt.$t('form.actions.added'));
                commit('setAccessoriesProducts', response.products);
            }
        )
    },

    async deleteProductFromProducts({ commit }, data) {
        const url = `${data.modelType}/${data.idModel}/${data.accessoriesType}/`;
        const config = {
            data: data.dataSend
        };

        await this.$axios.delete(url, config).then(
            response => {
                commit('setAccessoriesProducts', response.data.products);
                $nuxt.$toast.success($nuxt.$t('form.actions.deleted'));
            }
        )
    },

    getProductsId(){
        let productsId = [];
        for(const item in this.state.products.accessoriesProducts){
            productsId.push(this.state.products.accessoriesProducts[item].id);
        }
        return productsId;
    },

    clearProductStates({ commit }){
        commit('clearAccessoriesProducts');
        commit('clearloadedProducts');
    }
};

export const mutations = {
    clearLoadedProducts(state) {
        state.loadedProducts = [];
    },
    setLoadedProducts(state, products) {
        state.loadedProducts = products;
    },
    clearAccessoriesProducts(state) {
        state.accessoriesProducts = [];
    },
    clearloadedProducts(state) {
        state.loadedProducts = [];
    },
    setAccessoriesProducts(state, products) {
        state.accessoriesProducts = products;
    },
    addAccessoriesProducts(state, products) {
        state.accessoriesProducts.push(products);
    },
    deleteProductFromAccessories(state, product) {
        state.accessoriesProducts.splice(state.accessoriesProducts.indexOf(product), 1);
    },
    deleteFromLoadedProducts(state, category) {
        state.loadedProducts.splice(state.loadedProducts.indexOf(category), 1);
    }
};

export const products = {
    namespaced: true,
    state,
    mutations,
    actions
};