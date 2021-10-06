<template>
    <div class="referential-projects-box-component">
        <div class="mt-3" v-if="projects">
            <b-card-group deck>
                <!--<b-card bg-variant="light" :header="project.title" class="card-shadow-primary card-border mb-3 profile-responsive card"
                        v-for="project in projects">
                    <b-card-text>

                        <pre>
                            {{project}}
                        </pre>
                    </b-card-text>
                </b-card>-->
                <div class="card-shadow-primary card-border mb-3 card" v-for="project in projects" :key="project.id" 
                    > <!-- :class="{'d-none': !isClient && !project.can_edit}"  -->
                    <div class="card-header d-flex justify-content-between bg-blue-icon ref-project-card-header py-1">
                        <span class="text-white">
                            {{project.solver_obj.name}}
                        </span>
                      <span v-if="project.category" class="ml-2 btn btn-light" v-on:click="searchCategory(project.category_obj.name)">
                                   <font-awesome-icon class="ml-1" icon="layer-group"/>
                                  {{ project.category_obj.name }}
                              </span>
                    </div>
                    <div class="dropdown-menu-header">
                        <!--<div class="dropdown-menu-header-inner bg-primary">
                            <div class="menu-header-image"></div>
                            <div class="menu-header-content">
                                <div class="avatar-icon-wrapper avatar-icon-lg">
                                </div>
                                <div><h5 class="menu-header-title">{{project.title}}</h5></div>
                            </div>
                        </div>-->
                        <div class="dropdown-menu-header-inner">
                            <div class="menu-header-content">
                                <!--<div class="avatar-icon-wrapper btn-hover-shine mb-2 avatar-icon-xl">
                                    <div class="avatar-icon rounded"></div>
                                </div>-->
                                <div>
                                    <h5 class="menu-header-title text-black-50">
                                        <nuxt-link class="text-black-50"
                                                   :to="localePath({ name: 'referencni-projekty-id-detail', params: { id: project.id } })">
                                            {{ project.title }}
                                            <font-awesome-icon class="ml-1" icon="edit" v-if="project.can_edit"/>
                                            <font-awesome-icon class="ml-1" icon="info" v-if="!project.can_edit"/>
                                        </nuxt-link>
                                    </h5>
<!--                                    <h6 class="menu-header-subtitle text-black-50">
                                        {{project.solver_obj.email}} &nbsp | &nbsp {{project.solver_obj.phone}}
                                    </h6>-->
                                    {{project.client_name}}
                                </div>
                                <!--<div class="menu-header-btn-pane pt-2">
                                    <div role="group" class="btn-group text-center">
                                        <div class="nav">
                                            <a href="" class="btn btn-dark mr-1">Send</a>
                                            <a href="" class="btn btn-dark">Receive</a>
                                        </div>
                                    </div>
                                </div>-->
                            </div>
                        </div>
                    </div>
                    <div class="dropdown-menu-header">
                        <div class="no-gutters row" v-if="project.problem_text || project.solution_text || project.benefits_text">
                            <div class="col-sm-4 p-3 border border-light text-center text-dark">
                                <b-row>
                                    <b-col sm="12">
                                        <span class="title-texts">
                                            <font-awesome-icon class="mx-1" icon="puzzle-piece"/>
                                            {{$t('form.problem_text')}}
                                        </span>
                                    </b-col>
                                    <b-col md="12">
                                        {{project.problem_text | trimText(100)}}
                                    </b-col>
                                </b-row>
                            </div>
                            <div class="col-sm-4 p-3 border border-light text-center text-dark">
                                <b-row>
                                    <b-col sm="12">
                                        <span class="title-texts">
                                            <font-awesome-icon class="mx-1" icon="project-diagram"/>
                                            {{$t('form.solution_text')}}
                                        </span>
                                    </b-col>
                                    <b-col md="12">
                                        {{project.solution_text | trimText(100)}}
                                    </b-col>
                                </b-row>
                            </div>
                            <div class="col-sm-4 p-3 border border-light text-center text-dark">
                                <b-row>
                                    <b-col sm="12">
                                        <span class="title-texts">
                                            <font-awesome-icon class="mx-1" icon="money-bill"/>
                                            {{$t('form.benefits_text')}}
                                        </span>
                                    </b-col>
                                    <b-col md="12">
                                        {{project.benefits_text | trimText(100)}}
                                    </b-col>
                                </b-row>
                            </div>
                        </div>
                        <div class="no-gutters row">
                            <div class="col-12 my-2 p-2" v-if="project.products_obj.length">
                                <h6 class="text-muted text-uppercase font-size-md opacity-5 font-weight-normal d-block">{{$t('technology.applied_technologies')}}</h6>
                                <div class="accessories-tags-wrap">
                                    <button class="mb-2 mr-2 btn btn-outline-info tag"
                                            v-for="(product, index) in project.products_obj"
                                            :key="'product-'+index" @click="toggleProduct(product)" @hover="toggleProduct(product)">
                                        {{ product.name }}
                                        <span class="badge badge-info badge-dot badge-dot-lg"> </span>
                                        <transition name="slideDown">
                                            <p v-if="openedProduct == product.id" class="text-dark">
                                                {{product.description}} 
                                            </p>
                                        </transition>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!--<div class="text-center d-block card-footer">
                    </div>-->
                </div>
            </b-card-group>
        </div>
        <div class="d-flex justify-content-center mb-5 mt-5">
            <b-button v-if="pagination.next" class="btn-transition btn-hover-shine custom-lg"
                      variant="primary"
                      @click="loadMore">
                {{ $t('company.loadMore') }}
            </b-button>
        </div>
    </div>
</template>

<script>
import {mapActions, mapGetters, mapMutations, mapState} from 'vuex';
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {faPuzzlePiece, faProjectDiagram, faMoneyBill, faLayerGroup, faEdit, faInfo} from '@fortawesome/free-solid-svg-icons'

    library.add(
        faPuzzlePiece, faProjectDiagram, faMoneyBill, faLayerGroup, faEdit, faInfo,
    );

    export default {
        name: "BoxComponent",
        computed: {
            ...mapState({
                projects: state => state.projects.refProjectsList,
                pagination: state => state.projects.refProjectsPagination,
            }),
            ...mapGetters({
                isClient: 'user/isClient',
                isSupplier: 'user/isSupplier',
                isConsultant: 'user/isConsultant',
            }),
        },
        props: {
            mineOnly: {
                type: Boolean,
                default: false,
            },
        },
        components: {},
        data: () => ({
            openedProduct: null,
        }),
        methods: {
            ...mapActions('projects', {
                findProjects: 'findRefProjects',
            }),
            ...mapMutations({
                clearProjects: 'companies/clearRefProjects',
                addSearchedItems: 'searchObject/addSearchedTag',
                clearSearchedItems: 'searchObject/clearSeachedTags',
            }),
            async loadMore() {
                const nextpage = this.pagination.page + 1;
                const query = {...this.$route.query, ...{page: nextpage}};
                this.$router.push({
                    path: this.$route.path,
                    query: query
                });

                const data = {
                    page: nextpage,
                    add: true,
                    searchedString: query?.search ? query.search : ''
                };

                this.findProjects(data);
            },
            async filterByTag(role, search) {
                this.addSearchedItems(search)
            },
            toggleProduct(product) {
                //console.log('toggleProduct', id)
                if(!product.description?.length) return;
                this.openedProduct = this.openedProduct == product.id ? null : product.id;
            },
            searchCategory(string) {
                this.clearSearchedItems()
                this.addSearchedItems(string)
            }
        },
    }
</script>

<style scoped lang="scss">
    .referential-projects-box-component {
        .card {
            min-width: 500px;
            max-width: 800px;

            .ref-project-card-header {
                height: auto;
                min-height: 56px;
            }
        }
        .accessories-tags-wrap {
            .tag {
                max-width: 300px;
            }
        }
        .title-texts {
            color: #1e6294;
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
            text-transform: capitalize;
        }
    }
</style>