export const state = function () {
    return {
        user: {},
        callback: {
            callback_type: 'OTHER'
        },
        assistant: {
            assistant_type: 'OTHER'
        },
        myCallbacks: {
            pagination: {
                count: 0
            },
            results: []
        },
        myConsierges: {
            pagination: {
                count: 0
            },
            results: []
        },
        myAssistant: {
            pagination: {
                count: 0
            },
            results: []
        },
        mySoftware: {
            pagination: {
                count: 0
            },
            results: []
        }
    }
};

export const getters = {
    isClient(state) {
        return state.user?.role === 'CLIENT';
    },
    isConsultant(state) {
        return state.user?.role === 'CONSULTANT';
    },
    isSupplier(state) {
        return state.user?.role === 'SUPPLIER';
    },
    hasFreePlan(state) {
        return state.user?.plan === 'FREE';
    },
    hasBasicPlan(state) {
        return state.user?.plan === 'BASIC';
    },
}

export const mutations = {
    addToCallback(state, data) {
        state.callback = {...state.callback, ...data};
    },
    addToAssistant(state, data) {
        state.assistant = {...state.assistant, ...data};
    },
    setCallback(state, callback) {
        state.callback = callback;
    },
    setAssistant(state, assistant) {
        state.assistant = assistant;
    },
    setMyCallbacks(state, callbacks) {
        state.myCallbacks = callbacks;
    },
    setMyConsierges(state, consierges) {
        state.myConsierges = consierges;
    },
    setMyAssistant(state, assistant) {
        state.myAssistant = assistant;
    },
    setMySoftware(state, software) {
        state.mySoftware = software;
    },
    clearCallback(state) {
        state.callback = {callback_type: 'OTHER'};
    },
    clearAssistant(state) {
        state.assistant = {assistant_type: 'OTHER'};
    },
    addToUser(state, data) {
        state.user = {...state.user, ...data};
    },
    setUser(state, user) {
        state.user = user;
    },
    clearUser(state) {
        state.user = {}
    }
};

export const actions = {
    async deleteCallback({commit}, id) {
        const url = `callbacks/${id}/`;

        await this.$axios.$delete(url).then(
            response => {
                $nuxt.$toast.success('Smazáno');
            }
        )
    },

    async getUser({commit}) {
        const url = 'users/self/';

        await this.$axios.$get(url).then(
            response => {
                commit('setUser', response);
            }
        )
    },

    async updateUserRequest({commit}, data) {
        const url = 'users/self/';

        for (let item in data.userData) {
            if (data.userData.hasOwnProperty(item) && (data.userData[item] === '' || data.userData[item] === null)) {
                delete data.userData[item];
            }
        }

        await this.$axios.$patch(url, data.userData).then(
            response => {
                commit('setUser', response);
                this.$toast.success('Uloženo');
            },
            error => {
                // handled in api.js
            }
        )
    },

    async getOwnCompany({commit}) {
        const url = 'companies/primary/';

        await this.$axios.$get(url).then(
            response => {
                let empty = true;
                for (let i in response) {
                    empty = false;
                }
                if (!empty) this.$router.push({name: 'subjekt-id-upravit___cs', params: {id: response.id}});

            },
            error => {
                // handled in api.js
            }
        )
    },
    getMyCallbacks({commit}) {
        this.$axios.$get('callbacks/').then(
            response => {
                commit('setMyCallbacks', response);
            }
        );
    },
    getMyConsierges({commit}) {
        this.$axios.$get('consierge/').then(
            response => {
                commit('setMyConsierges', response);
            }
        );
    },
    getMyAssistant({commit}) {
        this.$axios.$get('assistant/').then(
            response => {
                commit('setMyAssistant', response);
            }
        );
    },
    getMySoftware({commit}) {
        this.$axios.$get('software/').then(
            response => {
                commit('setMySoftware', response);
            }
        );
    },
};

export const user = {
    namespaced: true,
    state,
    mutations,
    actions
};
