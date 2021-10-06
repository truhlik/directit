<template>
	<div class="callback-wrap">
    <page-title :heading=heading
                :icon=icon
                v-if="heading">
    </page-title>
		<CallbackForm></CallbackForm>
	</div>
</template>

<script>
	import PageTitle from "~/components/partials/PageTitle.vue";
	import CallbackForm from "~/components/user/CallbackForm";
	
	export default {
	  name: 'callback',
	  components: {
	    PageTitle,
		  CallbackForm
	  },
		data: () => ({
			heading: $nuxt.$t('menu.callback'),
			icon: 'pe-7s-bell icon-gradient bg-blue-icon'
		})
	}
</script>