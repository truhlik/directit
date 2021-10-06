<template>
	<img :src="logoWhite" class="white-logo">
</template>

<script>
	import logoWhite from '~/assets/images/logo/logo_white.png'

	export default {
		data: () => ({
			logoWhite: logoWhite
		})
	}
</script>