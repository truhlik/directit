<template>
  <div class="app-container app-theme-white">
    <Nuxt/>
  </div>
</template>

<script>

  export default {
    name: 'app',
	  middleware: [
	    'routing'
	  ],
    components: {
    },
    data() {
      return {
      }
    },
    methods:{

    },
    // middleware: 'notAuthenticated'
  }
</script>

<style>
  .app-login-box img.logo {
    display: block;
    margin: 10px auto;
    width: 80%;
  }
</style>
