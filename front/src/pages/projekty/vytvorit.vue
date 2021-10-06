<template>
	<div>
    <page-title :heading=heading
                :subheading="subheading"
                :icon=icon
                v-if="heading"
                :pathUrl="pathUrl"
                :pathName="$t('menu.projects_list')"
                :pathIcon="pathIcon">
    </page-title>

		<ProjectForm></ProjectForm>
	</div>
</template>

<script>
	import PageTitle from "~/components/partials/PageTitle.vue";
	import ProjectForm from "~/components/projects/ProjectForm.vue";

	export default {
	  name: 'project-create',
		async fetch({ store, query }){
	    if(query.project_id){
	      await store.dispatch('projects/getDefaultProject', { id: query.project_id });
	    }
		},
		components:{
	    PageTitle,
			ProjectForm
    },
		data: () => ({
	    heading: $nuxt.$t('projects.title_create'),
			subheading: $nuxt.$t('subheadings.project_create'),
		  icon: 'pe-7s-vector',
			pathUrl: '/projekty/seznam/',
			pathIcon: 'list',
			update: false
		}),
	}
</script>