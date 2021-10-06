import Vue from 'vue'

export const state = function () {
    return {
        project: {
            step1: 0,
            step2: 0,
            step3: 0,
            step4: 0,
            step5: 0,
            step6: 0,
        },
        projectList: [],
        projectPagination: {},
        projectsMessages: {},
        //projectsMessagesTree: {},
        projectsMessagesPagesLoaded: {},
        projectsMessagesLoading: {},
        referenceProjects: {},
        refProjectsSuggestions: [],
        refProjectsPagination: [],
        refsLoading: false,
        refProjectsList: {},
        refProject: {},
    }
};

export const actions = {

    async createProject({commit}, data) {
        let url = 'projects/';
        await this.$axios.$post(url, data).then(
            response => {
                $nuxt.$toast.success($nuxt.$t('form.actions.created'));
                $nuxt.$router.replace({path: '/projekty/seznam/'});
            },
            error => {
                // handled by api.js
            }
        );
    },

    async createRefProject({commit}, data) {
        let url = 'references/';
        await this.$axios.$post(url, data).then(
            response => {
                $nuxt.$toast.success($nuxt.$t('form.actions.created'));
                $nuxt.$router.replace({path: '/subjekty/referencni-projekty/'});
                commit('clearRefProject');
            },
            error => {
                // handled by api.js
            }
        );
    },

    async updateProject({commit}, data) {
        const url = `projects/${data.id}/`;

        await this.$axios.$patch(url, data).then(
            response => {
                $nuxt.$toast.success($nuxt.$t('form.actions.saved'));
            },
            error => {
                // handled by api.js
            }
        )
    },

    async updateRefProject({commit}, data) {
        const url = `references/${data.id}/`;

        await this.$axios.$patch(url, data).then(
            response => {
                $nuxt.$toast.success($nuxt.$t('form.actions.saved'));
                commit('setRefProject', data);
            },
            error => {
                // handled by api.js
            }
        )
    },

    async getProjectDetail({commit, redirect}, id) {
        //console.log('getProjectDetail', id);
        const url = `projects/${id}/`;

        await this.$axios.$get(url).then(
            response => {
                commit('setProject', response);
            },
            error => {
                $nuxt.$router.push({name: 'projekty-seznam___cs'});
            }
        )
    },

    async getRefProjectDetail({commit, redirect}, id) {
        //console.log('getProjectDetail', id);
        const url = `references/${id}/`;

        await this.$axios.$get(url).then(
            response => {
                commit('setRefProject', response);
            },
            error => {
                $nuxt.$router.push({name: 'subjekty-referencni-projekty___cs'});
            }
        )
    },

    async getDefaultProject({commit}, data = {}) {
        const url = `projects/default/?project_id=${data.id}`;
        await this.$axios.$get(url).then(
            response => {
                commit('setProject', response);
                commit('categories/setAccessoriesCategories', response.categories, {root: true});
            },
            error => {
                // handled by api.js
            }
        );
    },

    async getMyProjects({commit}, data) {
        const url = 'projects/';
        const params = {
            page: data.page || 1
        };

        await this.$axios.$get(url, {params: params}).then(
            response => {
                commit('setProjectPagination', response.pagination);
                commit('setProjectList', response.results);
                //console.log(response)
            },
            error => {
                // handled by api.js
            }
        )
    },

    async getProjectMessages({commit, state}, data) {
        //console.log('getProjectMessages', data)
        const PAGE_SIZE = 5
        const {parent, id/*, page, size*/, reload} = data
        if (state.projectsMessagesLoading[id] && state.projectsMessagesLoading[id][parent] == true) return   //these messages are already being loaded
        commit('setProjectMessagesLoading', {id, isLoading: true, parent})
        reload ? null : commit('increaseProjectMessagesLoaded', {id, parent})
        const page = state.projectsMessagesPagesLoaded[id][parent]
        const params = {
            thread__object_id: id,
            parent: parent == 'root' ? null : parent,
            page: reload ? 1 : page,
            page_size: reload ? PAGE_SIZE * page : PAGE_SIZE,//size
        };
        const url = `messages/`;
        const response = await this.$axios.$get(url, {params})
        //console.log('getProjectMessages response', response, parent)
        page == 1 || reload ? commit('setProjectMessages', {id, response, parent}) : commit('addProjectMessages', {id, response, parent})
        commit('setProjectMessagesLoading', {id, parent, isLoading: false})
    },

    async submitMessage({commit, dispatch}, data) {
        const {parent, text, threadId} = data;
        //console.log('submitMessage', parent, text, threadId);
        const url = `messages/`;
        const params = {
            thread_ct_id: threadId,
            text: text,
            parent: parent,
        };
        await this.$axios.$post(url, params)
        /*.then(
                    response => {
                        //console.log('response', response);
                        //commit('addProjectMessage', response, parent);
                        this.actions.getProjectMessages()
                    },
                    error => {
                        // handled by api.js
                    }
                );*/
        //console.log('message response', message);
        dispatch('getProjectMessages', {
            id: threadId,
            parent: parent,
            reload: true,
        });
    },

    clearProjects({commit}) {
        commit('clearProject');
        commit('clearProjectList');
        commit('clearProjectPagination');
    },


    async getRefProjectsSuggestions({ commit }, data){
        let url = `references/suggestion/${data.thisOwner ? '?owner=true' : ''}`;

        let params = {
            q: data.searchedString ? data.searchedString : ''
        };

        await this.$axios.$get( url , {params: params}).then(
            response => {
                if(response.results.length){
                    commit('setRefProjectsSuggestions', response.results);
                }else{
                    commit('clearRefProjectsSuggestions');
                }
            }
        )
    },

    async findRefProjects({ commit }, data = {}){
        const url = `references/${data.thisOwner ? '?owner=true' : ''}`;
        const params = {
            q: data.searchedString ? data.searchedString : '',
            page: data.page ? data.page : 1,
        };

        commit('setRefsLoading', true);
        await this.$axios.$get( url, { params: params } ).then(
            response => {
                //console.log('findRefProjects', response);
                commit('addToRefProjects', response.results);
                commit('setRefsPagination', response.pagination);
                commit('setRefsLoading', false);
            }
        )
    },

    clearRefProjects({ commit }){
        commit('clearRefProjects');
    }
};

export const mutations = {
    addToProject(state, data) {
        state.project = {...state.project, ...data};
    },
    addToRefProject(state, data) {
        state.refProject = {...state.refProject, ...data};
    },
    clearProject(state) {
        state.project = {
            step1: 0,
            step2: 0,
            step3: 0,
            step4: 0,
            step5: 0,
            step6: 0,
        }
    },
    clearProjectList(state) {
        state.projectList = [];

    },
    clearProjectPagination(state) {
        state.projectPagination = {};

    },
    setProject(state, project) {
        state.project = project;
    },
    setRefProject(state, project) {
        //console.log('setRefProject', project)
        state.refProject = project;
    },
    setProjectPagination(state, pagination) {
        state.projectPagination = {...state.projectPagination, ...pagination};
    },
    setProjectList(state, projects) {
        state.projectList = projects;
    },
    setProjectMessages(state, data) {
        const {response, parent, id} = data;
        //console.log('setProjectMessages',response, parent, id);
        state.projectsMessages[id] ? null : Vue.set(state.projectsMessages, id, {});
        Vue.set(state.projectsMessages[id], parent ?? 'root', response);
    },
    addProjectMessages(state, data) {
        const {response, parent, id} = data;
        //console.log('addProjectMessage', data)
        const threadKey = parent ?? 'root'
        state.projectsMessages[id][threadKey].results.push(...response.results.filter(Object))
        state.projectsMessages[id][threadKey].pagination = response.pagination
    },
    increaseProjectMessagesLoaded(state, data) {
        const {id, parent} = data
        //console.log('increaseProjectMessagesLoaded', data);
        state.projectsMessagesPagesLoaded[id] ? null : Vue.set(state.projectsMessagesPagesLoaded, id, {})
        //console.log('state.projectsMessagesPagesLoaded[id]', state.projectsMessagesPagesLoaded[id])
        state.projectsMessagesPagesLoaded[id][parent] ? state.projectsMessagesPagesLoaded[id][parent]++ : Vue.set(state.projectsMessagesPagesLoaded[id], parent, 1)
    },
    setProjectMessagesLoading(state, data) {
        const {isLoading, parent, id} = data;
        Vue.set(state.projectsMessagesLoading, id, {});
        Vue.set(state.projectsMessagesLoading[id], parent, isLoading);
    },
    setRefProjectsSuggestions(state, suggestions){
        state.refProjectsSuggestions = suggestions;
    },
    clearRefProjectsSuggestions(state){
        state.refProjectsSuggestions = [];
    },
    setRefsLoading(state, loading){
        state.refsLoading = loading;
    },
    addToRefProjects(state, data){
        state.refProjectsList = [ ...state.refProjectsList, ...data ];
    },
    setRefsPagination(state, pagination){
        //console.log('setRefsPagination', pagination, { ...state.refProjectsPagination, ...pagination});
        state.refProjectsPagination = { ...state.refProjectsPagination, ...pagination};
    },
    clearRefProjects(state){
        state.refProjectsList = [];
    },
    clearRefProject(state){
        state.refProject = {};
    },
};

export const projects = {
    namespaced: true,
    state,
    actions,
    mutations
};