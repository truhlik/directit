<template>
    <!--search temporarily hidden-->
    <div class="suggestion-wrap" v-if="false">
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
				<span v-if="!showSpinner && !isLoading">
                    {{ $t('technology.found') }}:
                    <span>{{categories.length}}</span> {{ $t('technology.found_categories') }},
                    <span>{{foundStats.subcategories}}</span> {{ $t('technology.found_subcategories') }} a
                    <span>{{foundStats.products}}</span> {{ $t('technology.found_products') }}.
				</span>
                <b-spinner v-else variant="success" label="Spinning"></b-spinner>
            </b-col>
        </b-row>
    </div>
</template>
<script>
    import {mapActions, mapMutations, mapState} from 'vuex'

    export default {
        name: 'technologies-searcher-component',
        props: {},
        data: () => ({
            showSuggestionsBool: false,
            showSpinner: false,
            searchInput: '',
            suggestionActive: -1
        }),
        computed: {
            ...mapState({
                suggestions: state => state.technologies.suggestions,
                isLoading: state => state.technologies.isLoading,
                searchedItems: state => state.searchObject.searchedTags,
                categories: state => state.technologies.categories,
            }),
            foundStats: function () {
                let result = {subcategories: 0, products: 0};
                this.categories?.forEach(category => {
                    result.subcategories += category.subcategories.length
                    result.products += category.subcategories.map(s => s.products_count).reduce((a, b) => a + b, 0)
                });
                return result;
            }
        },
        methods: {
            ...mapActions('technologies', {
                getCategories: 'getCategories',
                getCategory: 'getCategory',
                getApiSuggestions: 'getSuggestions',
                getProductDetail: 'getProductDetail'
            }),
            ...mapMutations({
                clearSuggestions: 'technologies/clearSuggestions',
                setCategories: 'technologies/setCategories',
                clearCategories: 'technologies/clearCategories',
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
                    companyType: this.companyType
                };
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
            async filterCategories(searchedValue) {
                this.showSpinner = true
                const query = {...this.$route.query, ...{search: searchedValue}};
                this.$router.push({
                    path: this.$route.path,
                    query: query
                });
                const data = {
                    searchedString: searchedValue,
                };
                this.clearCategories()
                await this.getCategories(data)
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
            async searchCategories() {
                let value = this.searchedItems.join(',')
                await this.filterCategories(value)
            }
        },
        created() {
            this.clearSearchedItems()
            this.createTags(this.$route.query?.search)
            this.handleFormSearch()
        },
        watch: {
            'searchedItems': function () {
                this.searchCategories()
            }
        }
    }

</script>
