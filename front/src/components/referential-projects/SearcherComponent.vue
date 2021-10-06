<template>
    <div class="suggestion-wrap">
        <b-row>
            <form @submit.prevent="handleFormSearch">
                <div class="box-tags">
						<span v-for="sItem in searchedItems"
                              @click="removeSearchedItems(sItem)"
                              class="mb-2 mr-2 btn btn-info">{{ sItem }}</span>
                </div>
                <b-col sm="12" class="search-form-wrap">
                    <b-form-group id="id_group_suggestion" class="suggestion-group" label-for="id_suggestion">
                        <b-form-input ref="searchInput"
                                      id="id_suggestion"
                                      autocomplete="off"
                                      type="text"
                                      v-model="searchInput"
                                      v-bind:placeholder="$t('form.search_in_input')"
                                      @input="getSuggestions"
                                      @blur="hideSuggestions"
                                      @click="showSuggestions"
                                      @keyup="handleKeyUP"
                        >
                        </b-form-input>
                        <div class="suggestion-result-wrap"
                             v-if="showSuggestionsBool">
						<span @click="handleSugestionSelect(value)"
                              v-for="(value, index) in suggestions"
                              :key="index"
                              :ref="`suggestion_${index}`"
                              :class="suggestionActive === index ? 'active' : ''"
                              data-test="test"
                        >
							{{ value }}
						</span>
                        </div>
                    </b-form-group>
                    <b-form-group class="searcher-btn-group d-flex align-items-end">
                        <button type="submit" class="btn-hover-shine btn btn-primary btn-lg">
                            <i class="pe-7s-search font-weight-bold"></i> <span class="desktop-only">{{ $t('form.button.search') }}</span>
                        </button>
                    </b-form-group>
                </b-col>
            </form>
            <b-col sm="12" class="text-center search-result">
				<span>Nalezeno výsledků: <span v-if="!showSpinner && !isLoading">{{ referenceProjectsPagination.count }}</span>
					<b-spinner v-else variant="success" label="Spinning"></b-spinner>
				</span>
            </b-col>
        </b-row>
    </div>
</template>

<script>
    import {mapActions, mapMutations, mapState} from 'vuex'

    export default {
        name: 'searcher-component',
        props: {
            mineOnly: {
                type: Boolean,
                default: false,
            },
        },
        data: () => ({
            showSuggestionsBool: false,
            showSpinner: false,
            searchInput: '',
            suggestionActive: -1
        }),
        computed: {
            ...mapState({
                suggestions: state => state.projects.refProjectsSuggestions,
                referenceProjectsPagination: state => state.projects.refProjectsPagination,
                isLoading: state => state.projects.isLoading,
                searchedItems: state => state.searchObject.searchedTags
            })
        },
        methods: {
            ...mapActions('projects', {
                getApiSuggestions: 'getRefProjectsSuggestions',
                findProjects: 'findRefProjects'
            }),
            ...mapMutations({
                clearSuggestions: 'projects/clearRefProjectsSuggestions',
                clearProjects: 'projects/clearRefProjects',
                clearSearchedItems: 'searchObject/clearSeachedTags',
                addSearchedItems: 'searchObject/addSearchedTag',
                deleteSearchedItems: 'searchObject/deleteSearchedTag',
                setSearchedItems: 'searchObject/setSearchedTags',
            }),
            addToSearchItems(value) {
                this.addSearchedItems(value)
                this.clearInput()
                this.$refs['searchInput'].focus()
            },
            clearInput() {
                this.searchInput = ''
            },
            createTags(stringItems) {
                if (!stringItems) return
                this.setSearchedItems(stringItems.split(','))
            },
            getSuggestions() {
                if (this.searchInput.length < 3) {
                    this.handleClearSuggestions()
                    return
                }
                this.showSuggestions();
                const data = {
                    searchedString: this.searchInput,
                };
                if(this.mineOnly) data.thisOwner = true;
                this.getApiSuggestions(data);
            },
            removeSearchedItems(item) {
                this.deleteSearchedItems(item)
            },
            showSuggestions() {
                this.showSuggestionsBool = true;
            },
            handleClearSuggestions() {
                this.clearSuggestions()
                this.suggestionActive = -1
            },
            handleKeyUP(event) {
                if (event.code === 'Comma') {
                    let value = this.searchInput.replace(',', '')
                    value = value.trim()
                    this.addToSearchItems(value)
                }

                if (event.code === 'ArrowDown') {
                    this.handleArrowDown()
                }

                if (event.code === 'ArrowUp') {
                    this.handleArrowUp()
                }
            },
            handleArrowUp() {
                if (this.suggestionActive >= 0)
                    this.suggestionActive--

            },
            handleArrowDown() {
                if (this.suggestionActive < this.suggestions.length)
                    this.suggestionActive++
            },
            hideSuggestions() {
                setTimeout(() => {
                    this.showSuggestionsBool = false;
                }, 500);
                this.suggestionActive = -1
            },
            handleSugestionSelect(value) {
                this.addToSearchItems(value)
            },
            async filterProjects(searchedValue) {
                this.showSpinner = true
                const query = {...this.$route.query, ...{search: searchedValue, page: 1}};
                this.$router.push({
                    path: this.$route.path,
                    query: query
                });
                const data = {
                    searchedString: searchedValue,
                };
                if(this.mineOnly) data.thisOwner = true;
                this.clearProjects()
                await this.findProjects(data)
                this.handleClearSuggestions()

                this.showSpinner = false
                this.clearInput()
            },
            async handleFormSearch() {

                if (this.suggestionActive in this.suggestions)
                    this.searchInput = this.suggestions[this.suggestionActive]

                if (this.searchInput.length >= 3) {
                    this.addToSearchItems(this.searchInput)
                }
            },
            async searchProjects() {
                let value = this.searchedItems.join(',')
                await this.filterProjects(value)
            }
        },
        created() {
            this.clearSearchedItems()
            this.createTags(this.$route.query?.search)
            this.handleFormSearch()
        },
        watch: {
            'searchedItems': function (val, oldVal) {
                this.searchProjects()
            }
        }

    }

</script>

<style scoped>

</style>