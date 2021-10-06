<template>
	<div class="loader-overlay" v-if="showLoader">
		<b-spinner variant="primary"></b-spinner>
	</div>
</template>

<script>
export default {
  props: ['showLoader']
}
</script>