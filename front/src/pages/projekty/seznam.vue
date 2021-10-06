<template>
	<div class="list-projects">
    <page-title :heading=heading
                :subheading="subheading"
                :icon=icon
                v-if="heading"
                :pathUrl="pathUrl"
                :pathName="$t('menu.project_create')"
                :pathIcon="pathIcon">
    </page-title>
	    <b-card class="main-card mb-4">
        <b-table :hover="hover"
                 :striped="striped"
                 :items="items"
                 :fields="fields"
                 :current-page="projectPagination.page">
	        <template v-slot:cell(categories)="data">
		        <div class="list-tags-cell">
		          <span v-for="(value, index) in data.item.categories" :key="value.id">{{ value.name }}<span v-if="index+1 != data.item.categories.length">, </span>
		          </span>
		        </div>
	        </template>
	        <template v-slot:cell(status)="data">
		        <div class="list-tags-cell">
		          <span>{{ projectType[data.item.status] }}</span>
		        </div>
	        </template>
	        <template v-slot:cell(detail)="row">
		        <nuxt-link :to="localePath({ name: 'projekty-id-upravit', params: { id: row.item.id } })">
                    <b-button size="sm" class="mr-2 mb-1"
                    variant="primary">
                                <span>{{ $t('form.button.details') }}</span>
                                <!--<span v-if="isClient">{{ $t('form.button.update') }}</span>
                                <span v-else>{{ $t('form.button.detail') }}</span>-->
                    </b-button>
			    </nuxt-link>
                <nuxt-link v-if="!isClient" :to="localePath({ name: 'subjekt-referencni-projekt', query: {
                    title: row.item.name,
                    category: JSON.stringify(row.item.categories[0]),
                } })">
                <b-button size="sm" class="mr-2 mb-1"
                            variant="primary">
                    <span>{{ $t('form.button.add_as_ref_project') }}</span>
                </b-button>
                </nuxt-link>
	        </template>
        </b-table>
      <b-row>
        <b-col md="6" class="my-1">
          <b-pagination-nav :total-rows="projectPagination.count"
                            :value="projectPagination.page"
                            :per-page="projectPagination.page_size"
                            :number-of-pages="projectPagination.num_pages"
                            :link-gen="pageGen"
                            use-router
                            class="my-0" />
        </b-col>
      </b-row>
    </b-card>
	</div>
</template>

<script>
	import { mapState, mapGetters } from 'vuex'
	import PageTitle from "~/components/partials/PageTitle.vue";
	import { PROJECT_STATUS_TYPES } from '~/helpers/constants'

	export default {
	  name: 'project-list',
		async fetch({ store, query }){
	    await store.dispatch('projects/getMyProjects', { page: query.page ? query.page : 1 });
		},
		components: {
	    PageTitle
		},
		data: () => ({
			fields: [
			  {
          key: 'name',
				  label: 'Název'
				},
			  {
          key: 'categories',
				  label: 'Kategorie'
				},
			  {
          key: 'description',
				  label: 'Popis'
				},
			  {
          key: 'due_date',
				  label: 'Plánované dokončení'
				},
			  {
          key: 'consultant.name',
				  label: 'Konzultant'
				},
			  {
          key: 'status',
				  label: 'Status'
				},
			  {
          key: 'detail',
				  label: ''
				},
			],
			heading: $nuxt.$t('projects.title_plural'),
      hover: true,
			icon: 'pe-7s-vector icon-gradient bg-blue-icon',
			pathIcon: 'plus',
			projectType: PROJECT_STATUS_TYPES,
			subheading: $nuxt.$t('subheadings.project_list'),
			striped: true,
		}),
		computed: {
		  ...mapState({
			  projectPagination: state => state.projects.projectPagination,
			  items: state => state.projects.projectList,
		  }),
			...mapGetters({
				isClient: 'user/isClient'
			}),
			pathUrl() {
		  	if(this.isClient)
		  		return '/projekty/vytvorit/'
				return null
			}
		},
		methods: {
      pageGen(pageNum) {
        return pageNum === 1 ? '?' : `?page=${pageNum}`
      }
		},
    watchQuery: ['page']
	}
</script>